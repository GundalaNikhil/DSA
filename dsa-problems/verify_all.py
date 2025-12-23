
import os
import re
import yaml
import sys

# List of topics to verify
# Excluding 'Bitwise' as it's already verified (though running again is fine)
# Excluding metadata/script files
TOPICS = [
    "AdvancedGraphs", "Arrays", "Bitwise", "Concurrency", 
    "DP", "GameTheory", "Geometry", "Graphs", "GraphsBasics", 
    "Greedy", "Hashing", "Heaps", "LinkedLists", "MathAdvanced", 
    "NumberTheory", "Probabilistic", "ProbabilisticDS", "Queues", 
    "Recursion", "SegmentTree", "Sorting", "Stacks", "Strings", 
    "StringsClassic", "Trees", "TreesDP", "Tries"
]

BASE_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"

BANNED_PHRASES = [
    r"\bmaybe\b",
    r"\bwait\b",
    r"\blet me\b",
    r"\bi think\b",
    r"\blet's check\b",
    r"\bactually,\b",
    r"\bnote to self\b",
    r"\bshould be\b",
    r"\bprobably\b",
    r"\bgive me a sec\b"
]

def parse_frontmatter(content):
    if content.startswith("---"):
        try:
            parts = content.split("---", 2)
            if len(parts) >= 3:
                return yaml.safe_load(parts[1])
        except Exception:
            return None
    return None

def extract_section(content, section_name):
    escaped_name = re.escape(section_name)
    pattern = re.compile(r"##\s*[^#\n]*?" + escaped_name + r".*?\n(.*?)(?=\n##\s|\Z)", re.DOTALL | re.IGNORECASE)
    match = pattern.search(content)
    if match:
        return match.group(1).strip()
    return ""

def check_file(problem_path, editorial_path, display_id):
    report = []
    
    try:
        with open(problem_path, "r", encoding="utf-8") as f:
            p_content = f.read()
        with open(editorial_path, "r", encoding="utf-8") as f:
            e_content = f.read()
    except Exception as e:
        return [f"FAIL: Could not open files for {display_id}: {e}"]

    # 1. Frontmatter Check
    p_fm = parse_frontmatter(p_content)
    # Editorial might not have frontmatter or might act differently, but we expect it to match
    e_fm = parse_frontmatter(e_content)
    
    if p_fm and e_fm:
        if p_fm.get("problem_id") != e_fm.get("problem_id"):
            report.append(f"MISMATCH: problem_id {p_fm.get('problem_id')} vs {e_fm.get('problem_id')}")
        if p_fm.get("slug") != e_fm.get("slug"):
            report.append(f"MISMATCH: slug {p_fm.get('slug')} vs {e_fm.get('slug')}")
        if p_fm.get("title") != e_fm.get("title"):
             report.append(f"WARN: Title mismatch '{p_fm.get('title')}' vs '{e_fm.get('title')}'")

    # 2. Constraints Check
    p_constraints = extract_section(p_content, "Constraints")
    e_constraints = extract_section(e_content, "Constraints")

    if not p_constraints:
        report.append("MISSING: '## Constraints' in Problem file")
    
    # Extract numbers > 100 for comparison
    p_nums = sorted(re.findall(r'\b\d+\b', p_constraints))
    e_nums = sorted(re.findall(r'\b\d+\b', e_constraints))
    
    p_big = set([n for n in p_nums if int(n) > 100])
    e_big = set([n for n in e_nums if int(n) > 100])
    
    # If editorial has NO constraints/clarifications section, e_big is empty.
    # Usually editorial repeats constraints or simplifies them.
    # We flag if Problem has big constraints but Editorial has DIFFERENT big constraints (indicating copy-paste error).
    # If Editorial has NO big constraints, it might be acceptable (implicit).
    if e_big and p_big != e_big:
        report.append(f"CONSTRAINT MISMATCH: Problem has {p_big}, Editorial has {e_big}")

    # 3. Example Input Check
    p_input_match = re.search(r"## Example.*?Input:.*?\n(.*?)\n\*\*Output", p_content, re.DOTALL | re.IGNORECASE)
    if p_input_match:
        p_input_text = p_input_match.group(1).replace("```", "").strip()
        p_input_tokens = re.findall(r'\b\d+\b', p_input_text)
        
        e_dry_run = extract_section(e_content, "Test Case Walkthrough (Dry Run)")
        if not e_dry_run:
             e_dry_run = extract_section(e_content, "Test Case Walkthrough")
        
        if e_dry_run:
            e_tokens = re.findall(r'\b\d+\b', e_dry_run)
            if p_input_tokens:
                first_token = p_input_tokens[0]
                if first_token not in e_tokens:
                     report.append(f"EXAMPLE MISMATCH: Problem input starts with {first_token}, not found in Editorial Dry Run.")
        else:
            report.append("MISSING: Test Case Walkthrough in Editorial")

    # 4. AI Artifacts
    for phrase in BANNED_PHRASES:
        match = re.search(phrase, e_content, re.IGNORECASE)
        if match:
            idx = match.start()
            context = e_content[max(0, idx-20):idx+50].replace("\n", " ")
            report.append(f"ARTIFACT: Found '{phrase}' in Editorial: ...{context}...")

    # 5. Real World Scenario
    if "## Real-World Scenario" not in e_content and "## 🌍 Real-World Scenario" not in e_content:
         report.append("MISSING: Real-World Scenario in Editorial")

    return report

def main():
    print("Starting Deep Verification for ALL topics...")
    total_issues = 0
    
    for topic in TOPICS:
        topic_prob_dir = os.path.join(BASE_DIR, topic, "problems")
        topic_edit_dir = os.path.join(BASE_DIR, topic, "editorials")
        
        if not os.path.exists(topic_prob_dir):
            # Maybe flat structure? Or missing 'problems' subdir?
            # Some topics might be structure differently or empty.
            continue
            
        files = sorted(os.listdir(topic_prob_dir))
        
        print(f"Checking {topic}...")
        
        for f in files:
            if not f.endswith(".md"): continue
            
            display_id = f.split('.')[0] 
            # If formatted like BIT-001-slug.md, we take BIT-001
            parts = f.split('-')
            if len(parts) >= 2 and parts[1].isdigit():
                display_id = f"{parts[0]}-{parts[1]}"
            else:
                 # Fallback
                 display_id = f[:7]

            problem_path = os.path.join(topic_prob_dir, f)
            editorial_path = os.path.join(topic_edit_dir, f)
            
            if not os.path.exists(editorial_path):
                 print(f"  FAIL: Editorial not found for {f}")
                 total_issues += 1
                 continue
                 
            errors = check_file(problem_path, editorial_path, display_id)
            if errors:
                print(f"  Issues in {display_id} ({f}):")
                for e in errors:
                    print(f"    - {e}")
                    total_issues += 1
    
    print(f"\nVerification Complete. Total issues found: {total_issues}")

if __name__ == "__main__":
    main()
