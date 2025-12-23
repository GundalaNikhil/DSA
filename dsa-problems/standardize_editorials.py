import os
import re
import sys

def get_file_content(filepath):
    """Reads file content."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file_content(filepath, content):
    """Writes content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_constraints(content):
    """Extracts the Constraints section from the problem statement."""
    # Look for ## Constraints or # Constraints
    pattern = re.compile(r"^(#+)\s*Constraints\s*(.*?)(?=\n#+ |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(content)
    if match:
        header_level = match.group(1)
        body = match.group(2).strip()
        return body
    return None

def has_constraints_section(content):
    """Checks if the editorial already has a Constraints section."""
    return re.search(r"^#+\s*Constraints", content, re.MULTILINE) is not None

def insert_constraints(editorial_content, constraints_body):
    """Inserts the constraints section into the editorial."""
    # We want to insert it after the "Problem Summary" section or "Real-World Scenario".
    # A safe place is usually after the first few sections (Summary) but before "Approaches" or "solution-template".
    
    # Let's target insertion after "## Problem Summary" section.
    # Find the end of Problem Summary.
    
    summary_pattern = re.compile(r"^(#+\s*Problem Summary\s*.*?)(?=\n#+ |\Z)", re.MULTILINE | re.DOTALL)
    match = summary_pattern.search(editorial_content)
    
    new_section = f"\n\n## Constraints\n\n{constraints_body}"
    
    if match:
        # Insert after Problem Summary
        end_idx = match.end()
        new_content = editorial_content[:end_idx] + new_section + editorial_content[end_idx:]
        return new_content
    
    # Fallback: Insert before "## Approaches" or similar
    approaches_match = re.search(r"^#+\s*Approaches", editorial_content, re.MULTILINE)
    if approaches_match:
        start_idx = approaches_match.start()
        new_content = editorial_content[:start_idx] + new_section + "\n\n" + editorial_content[start_idx:]
        return new_content

    # Fallback: Append to end (unlikely to be ideal but safe)
    return editorial_content + new_section

def standardize_topic(base_path, topic):
    """Standardizes all editorials in a topic."""
    problems_dir = os.path.join(base_path, topic, "problems")
    editorials_dir = os.path.join(base_path, topic, "editorials")
    
    if not os.path.exists(problems_dir) or not os.path.exists(editorials_dir):
        print(f"Skipping {topic}: directories not found.")
        return

    files = sorted([f for f in os.listdir(problems_dir) if f.endswith(".md")])
    
    count_updated = 0
    
    for filename in files:
        prob_path = os.path.join(problems_dir, filename)
        edit_path = os.path.join(editorials_dir, filename)
        
        prob_content = get_file_content(prob_path)
        edit_content = get_file_content(edit_path)
        
        if not prob_content or not edit_content:
            continue
            
        # 1. Check if editorial already has constraints
        if has_constraints_section(edit_content):
            print(f"[{filename}] Already has constraints. Skipping.")
            continue
            
        # 2. Extract constraints from problem
        constraints = extract_constraints(prob_content)
        if not constraints:
            print(f"[{filename}] No constraints found in problem statement. Skipping.")
            continue
            
        # 3. Insert into editorial
        new_content = insert_constraints(edit_content, constraints)
        
        # 4. Write back
        if new_content != edit_content:
            write_file_content(edit_path, new_content)
            print(f"[{filename}] Updated with constraints.")
            count_updated += 1
            
    print(f"Topic {topic}: Updated {count_updated} editorials.")

if __name__ == "__main__":
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"
    
    if len(sys.argv) < 2:
        print("Usage: python standardize_editorials.py <Topic1> [Topic2 ...]")
        sys.exit(1)
        
    topics = sys.argv[1:]
    for t in topics:
        standardize_topic(base_path, t)
