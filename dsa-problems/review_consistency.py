import os
import re
import sys

def get_file_content(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def extract_section(content, header_pattern):
    # Regex to find the section matching header_pattern and capture until next header
    # Headers are usually ## Header
    pattern = re.compile(f"^{header_pattern}.*?$(.*?)(^#|\\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(content)
    if match:
        return match.group(1).strip()
    return "Section not found."

def analyze_topic(base_path, topic):
    problems_dir = os.path.join(base_path, topic, "problems")
    editorials_dir = os.path.join(base_path, topic, "editorials")
    
    if not os.path.exists(problems_dir) or not os.path.exists(editorials_dir):
        print(f"Skipping {topic}: problems or editorials dir not found.")
        return

    problem_files = sorted([f for f in os.listdir(problems_dir) if f.endswith(".md")])
    
    print(f"Reviewing Topic: {topic}")
    print("=" * 60)
    
    for p_file in problem_files:
        # Match ID like AGR-001
        p_id_match = re.match(r"([A-Z]+-\d+)", p_file)
        if not p_id_match:
            continue
        p_id = p_id_match.group(1)
        
        # Find corresponding editorial
        e_files = [f for f in os.listdir(editorials_dir) if f.startswith(p_id) and f.endswith(".md")]
        if not e_files:
            print(f"MISSING EDITORIAL FOR {p_id}")
            continue
        e_file = e_files[0]
        
        p_path = os.path.join(problems_dir, p_file)
        e_path = os.path.join(editorials_dir, e_file)
        
        p_content = get_file_content(p_path)
        e_content = get_file_content(e_path)
        
        # Extract Description from Problem (usually after first header line or frontmatter)
        # Problem files usually have frontmatter, then description is the first text.
        # Often starts with description directly or '## Problem Description'
        # Let's just take the first 1000 chars of non-frontmatter content for context.

        # Helper to get text buffer
        p_text = re.sub(r"^---.*?---", "", p_content, flags=re.DOTALL).strip()
        e_text = re.sub(r"^---.*?---", "", e_content, flags=re.DOTALL).strip()

        # Extract Problem Description (heuristic)
        # Look for ## Problem Description, ## Problem Statement, or just take the first paragraph
        p_desc_match = re.search(r"^#+ (Problem Description|Problem Statement|Description)(.*?)(^#+|\Z)", p_text, re.MULTILINE | re.DOTALL)
        if p_desc_match:
            p_desc = p_desc_match.group(2).strip()
        else:
            # Fallback: take text after title until next header
            # Usually title is # Title
            p_desc = re.split(r"^#+ ", p_text, flags=re.MULTILINE)
            p_body_parts = re.split(r"^#+ .*?$", p_text, flags=re.MULTILINE)
            p_desc = p_body_parts[1].strip() if len(p_body_parts) > 1 else p_text[:500]

            
        # Extract Constraints (Problem)
        p_cons = extract_section(p_text, r"^#+ .*Constraints") # flexible #
        if p_cons == "Section not found.":
            match = re.search(r"\*\*Constraints\*\*:?(.*?)$", p_text, re.MULTILINE | re.DOTALL)
            if match:
                # Capture until next double newline or header
                 p_cons = match.group(1).split("\n\n")[0].strip()

        
        # Editorial Summary
        e_summ = extract_section(e_text, r"^#+ .*Summary")
        if e_summ == "Section not found.":
             # Fallback to Problem Statement in Editorial
             e_summ = extract_section(e_text, r"^#+ Problem Statement")
        
        # Editorial Input/Output/Constraints
        e_cons = extract_section(e_text, r"^#+ .*Clarifications")
        if e_cons == "Section not found.":
             e_cons = extract_section(e_text, r"^#+ .*Constraints")
        if e_cons == "Section not found.":
             match = re.search(r"\*\*Constraints\*\*:?(.*?)$", e_text, re.MULTILINE | re.DOTALL)
             if match:
                 e_cons = match.group(1).split("\n\n")[0].strip()

        print(f"ID: {p_id}")
        print(f"Problem File: {p_file}")
        print(f"Editorial File: {e_file}")
        print("-" * 20 + " PROBLEM DESCRIPTION " + "-" * 20)
        print(p_desc[:300].replace("\n", " ") + ("..." if len(p_desc) > 300 else ""))
        print("-" * 20 + " PROBLEM CONSTRAINTS " + "-" * 20)
        print(p_cons[:300].replace("\n", " ") + ("..." if len(p_cons) > 300 else ""))
        print("-" * 20 + " EDITORIAL SUMMARY " + "-" * 22)
        print(e_summ[:300].replace("\n", " ") + ("..." if len(e_summ) > 300 else ""))
        print("-" * 20 + " EDITORIAL CONSTRAINTS " + "-" * 18)
        print(e_cons[:300].replace("\n", " ") + ("..." if len(e_cons) > 300 else ""))
        print("=" * 60 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python review_consistency.py <Topic|all>")
        sys.exit(1)
    
    base = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"
    arg = sys.argv[1]
    
    if arg == "all":
        topics = sorted([d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)) and not d.startswith(".") and d not in ["libs"]])
        for t in topics:
            analyze_topic(base, t)
    else:
        analyze_topic(base, arg)
