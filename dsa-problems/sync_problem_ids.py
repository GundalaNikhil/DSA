#!/usr/bin/env python3
"""
Synchronize problem_id fields across test cases, problems, and editorials.
Ensures consistency between YAML test files and markdown problem/editorial files.
"""

import os
import re
import yaml
from pathlib import Path

BASE_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"

def extract_problem_id_from_markdown(md_filepath):
    """Extract problem_id from a problem or editorial markdown file."""
    if not os.path.exists(md_filepath):
        return None
    
    try:
        with open(md_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for problem_id in YAML frontmatter
        # Format: problem_id: XXX_PROBLEM_NAME__1234
        match = re.search(r'^problem_id:\s*(.+?)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception as e:
        print(f"  ⚠️ Error reading {md_filepath}: {e}")
    
    return None

def get_problem_id_from_testcase(yaml_filepath):
    """Get current problem_id from test case YAML file."""
    try:
        with open(yaml_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'^problem_id:\s*(.+?)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception as e:
        print(f"  ⚠️ Error reading {yaml_filepath}: {e}")
    
    return None

def update_testcase_problem_id(yaml_filepath, new_problem_id):
    """Update problem_id in test case YAML file."""
    try:
        with open(yaml_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if problem_id exists
        if re.search(r'^problem_id:', content, re.MULTILINE):
            # Replace existing problem_id
            new_content = re.sub(
                r'^problem_id:.*$',
                f'problem_id: {new_problem_id}',
                content,
                flags=re.MULTILINE
            )
        else:
            # Add problem_id at the beginning
            new_content = f"problem_id: {new_problem_id}\n{content}"
        
        with open(yaml_filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"  ❌ Error updating {yaml_filepath}: {e}")
        return False

def sync_topic(topic_name):
    """Synchronize problem_id fields for all files in a topic."""
    topic_dir = os.path.join(BASE_DIR, topic_name)
    testcases_dir = os.path.join(topic_dir, 'testcases')
    problems_dir = os.path.join(topic_dir, 'problems')
    editorials_dir = os.path.join(topic_dir, 'editorials')
    
    if not os.path.exists(testcases_dir):
        return 0, 0, 0, 0
    
    yaml_files = sorted([f for f in os.listdir(testcases_dir) if f.endswith('.yaml')])
    
    print(f"\n{'='*80}")
    print(f"📁 {topic_name} ({len(yaml_files)} test files)")
    print(f"{'='*80}")
    
    synced = 0
    already_correct = 0
    missing_source = 0
    errors = 0
    
    for yaml_file in yaml_files:
        base_name = yaml_file.replace('.yaml', '')
        yaml_path = os.path.join(testcases_dir, yaml_file)
        
        # Try to find corresponding markdown files
        problem_path = os.path.join(problems_dir, f'{base_name}.md')
        editorial_path = os.path.join(editorials_dir, f'{base_name}.md')
        
        # Extract problem_id from markdown (prefer problem file)
        source_id = extract_problem_id_from_markdown(problem_path)
        if not source_id:
            source_id = extract_problem_id_from_markdown(editorial_path)
        
        if not source_id:
            print(f"⚠️  {yaml_file}: No problem_id found in markdown files")
            missing_source += 1
            continue
        
        # Get current problem_id from test case
        current_id = get_problem_id_from_testcase(yaml_path)
        
        if current_id == source_id:
            print(f"✅ {yaml_file}: Already correct ({source_id})")
            already_correct += 1
        else:
            # Update the test case
            if update_testcase_problem_id(yaml_path, source_id):
                if current_id:
                    print(f"🔄 {yaml_file}: Updated {current_id} → {source_id}")
                else:
                    print(f"➕ {yaml_file}: Added {source_id}")
                synced += 1
            else:
                print(f"❌ {yaml_file}: Failed to update")
                errors += 1
    
    return synced, already_correct, missing_source, errors

def main():
    print("="*80)
    print("SYNCHRONIZE PROBLEM_IDs ACROSS ALL TEST CASES")
    print("="*80)
    print("Ensures test case problem_ids match problem/editorial markdown files")
    print("="*80)
    
    # Get all topic directories
    topics = []
    for item in sorted(os.listdir(BASE_DIR)):
        topic_path = os.path.join(BASE_DIR, item)
        if os.path.isdir(topic_path) and not item.startswith('.'):
            testcases_path = os.path.join(topic_path, 'testcases')
            if os.path.exists(testcases_path):
                topics.append(item)
    
    print(f"\nFound {len(topics)} topics with testcases directories\n")
    
    total_synced = 0
    total_correct = 0
    total_missing = 0
    total_errors = 0
    
    for topic in topics:
        synced, correct, missing, errors = sync_topic(topic)
        total_synced += synced
        total_correct += correct
        total_missing += missing
        total_errors += errors
    
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Already correct:        {total_correct} files")
    print(f"🔄 Synchronized:           {total_synced} files")
    print(f"⚠️  Missing source:         {total_missing} files")
    print(f"❌ Errors:                 {total_errors} files")
    print(f"{'='*80}")
    print(f"📊 Total processed:        {total_synced + total_correct + total_missing + total_errors} files")
    print(f"{'='*80}")
    
    if total_synced > 0:
        print(f"\n🎉 Successfully synchronized {total_synced} problem_id fields!")
    if total_missing > 0:
        print(f"\n⚠️  {total_missing} files are missing problem_id in markdown - may need manual review")
    if total_errors > 0:
        print(f"\n❌ {total_errors} files had errors - please check manually")

if __name__ == "__main__":
    main()
