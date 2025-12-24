#!/usr/bin/env python3
"""
Add missing problem_id fields to test case YAML files.
Extracts problem_id from the corresponding problem markdown file.
Targets: ProbabilisticDS, Queues, SegmentTree (48 files total)
"""

import os
import re
import yaml

def extract_problem_id_from_markdown(md_filepath):
    """Extract problem_id from a problem or editorial markdown file."""
    if not os.path.exists(md_filepath):
        return None
    
    with open(md_filepath, 'r') as f:
        content = f.read()
    
    # Look for problem_id in YAML frontmatter
    # Format: problem_id: XXX_PROBLEM_NAME__1234
    match = re.search(r'^problem_id:\s*(.+?)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    
    return None

def add_problem_id_to_file(filepath, topic_dir):
    """Add problem_id field to a YAML file if missing."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if problem_id already exists
    if re.search(r'^problem_id:', content, re.MULTILINE):
        return False, "Already has problem_id"
    
    # Extract base filename without extension
    filename = os.path.basename(filepath)
    base_name = filename.replace('.yaml', '')
    
    # Try to find the corresponding problem markdown file
    problem_file = os.path.join(topic_dir, 'problems', f'{base_name}.md')
    editorial_file = os.path.join(topic_dir, 'editorials', f'{base_name}.md')
    
    # Try problem file first, then editorial
    problem_id = extract_problem_id_from_markdown(problem_file)
    if not problem_id:
        problem_id = extract_problem_id_from_markdown(editorial_file)
    
    if not problem_id:
        # Fallback: use filename-based ID
        match = re.match(r'^([A-Z]+-\d+)-', filename)
        if match:
            problem_id = match.group(1)
            return False, f"⚠️ No problem_id in markdown, would use: {problem_id}"
        return False, f"Cannot extract problem_id from markdown or filename"
    
    # Add problem_id at the beginning
    new_content = f"problem_id: {problem_id}\n{content}"
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True, f"Added problem_id: {problem_id}"

def process_topic(topic_name):
    """Process all test case files in a topic directory."""
    base_dir = f"/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/{topic_name}"
    testcases_dir = os.path.join(base_dir, "testcases")
    
    if not os.path.exists(testcases_dir):
        print(f"⚠️ Directory not found: {testcases_dir}")
        return 0, 0
    
    files = sorted([f for f in os.listdir(testcases_dir) if f.endswith('.yaml')])
    
    print(f"\n{'='*80}")
    print(f"Processing {topic_name} ({len(files)} files)")
    print(f"{'='*80}")
    
    added_count = 0
    skipped_count = 0
    
    for filename in files:
        filepath = os.path.join(testcases_dir, filename)
        success, message = add_problem_id_to_file(filepath, base_dir)
        
        if success:
            print(f"✅ {filename}: {message}")
            added_count += 1
        else:
            print(f"⏭️  {filename}: {message}")
            skipped_count += 1
    
    return added_count, skipped_count

def main():
    print("="*80)
    print("ADD MISSING PROBLEM_ID FIELDS TO TEST CASES")
    print("="*80)
    
    topics = [
        "ProbabilisticDS",
        "Queues",
        "SegmentTree"
    ]
    
    total_added = 0
    total_skipped = 0
    
    for topic in topics:
        added, skipped = process_topic(topic)
        total_added += added
        total_skipped += skipped
    
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Added problem_id: {total_added} files")
    print(f"⏭️  Skipped: {total_skipped} files")
    print(f"📊 Total processed: {total_added + total_skipped} files")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
