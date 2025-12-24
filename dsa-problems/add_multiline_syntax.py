#!/usr/bin/env python3
"""
Add missing |- multiline syntax to test case YAML files.
Targets files that are missing proper multiline syntax for input/output.
"""

import os
import re
import yaml

def needs_multiline_fix(filepath):
    """Check if file needs |- multiline syntax added."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if |- is already present
    if '|-' in content:
        return False
    
    # Check if there are multiline inputs/outputs that need it
    # Look for patterns like: input: 'text\ntext' or input: "text\ntext"
    if re.search(r"(input|output):\s*['\"].*\\n", content):
        return True
    
    # Check for raw YAML that should have |-
    if re.search(r"(input|output):\s*'[^']*\n\s+[^-]", content):
        return True
    
    return False

def fix_multiline_syntax(filepath):
    """Add |- multiline syntax to a YAML file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Try to parse as YAML first
    try:
        data = yaml.safe_load(content)
    except:
        return False, "YAML parse error"
    
    if not isinstance(data, dict):
        return False, "Invalid YAML structure"
    
    # Rebuild YAML with proper |- syntax
    lines = []
    
    # Add problem_id if present
    if 'problem_id' in data:
        lines.append(f"problem_id: {data['problem_id']}")
    
    # Process each section
    for section in ['samples', 'public', 'hidden']:
        if section not in data or not data[section]:
            continue
        
        lines.append(f"{section}:")
        
        for case in data[section]:
            if not isinstance(case, dict):
                continue
            
            # Input
            if 'input' in case:
                input_str = str(case['input']).strip()
                if '\n' in input_str or len(input_str) > 50:
                    lines.append("- input: |-")
                    for line in input_str.split('\n'):
                        lines.append(f"    {line}")
                else:
                    lines.append(f"- input: {input_str}")
            
            # Output
            if 'output' in case:
                output_str = str(case['output']).strip()
                if '\n' in output_str or len(output_str) > 50:
                    lines.append("  output: |-")
                    for line in output_str.split('\n'):
                        lines.append(f"    {line}")
                else:
                    lines.append(f"  output: {output_str}")
    
    new_content = '\n'.join(lines) + '\n'
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True, "Added |- syntax"

def process_topic(topic_name):
    """Process all test case files in a topic directory."""
    testcases_dir = f"/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/{topic_name}/testcases"
    
    if not os.path.exists(testcases_dir):
        print(f"⚠️ Directory not found: {testcases_dir}")
        return 0, 0, 0
    
    files = sorted([f for f in os.listdir(testcases_dir) if f.endswith('.yaml')])
    
    print(f"\n{'='*80}")
    print(f"Processing {topic_name} ({len(files)} files)")
    print(f"{'='*80}")
    
    fixed_count = 0
    skipped_count = 0
    error_count = 0
    
    for filename in files:
        filepath = os.path.join(testcases_dir, filename)
        
        if not needs_multiline_fix(filepath):
            print(f"⏭️  {filename}: Already has |- syntax")
            skipped_count += 1
            continue
        
        success, message = fix_multiline_syntax(filepath)
        
        if success:
            print(f"✅ {filename}: {message}")
            fixed_count += 1
        else:
            print(f"❌ {filename}: {message}")
            error_count += 1
    
    return fixed_count, skipped_count, error_count

def main():
    print("="*80)
    print("ADD MISSING |- MULTILINE SYNTAX TO TEST CASES")
    print("="*80)
    
    # Topics that need fixing based on audit
    topics = [
        "Bitwise",
        "GraphsBasics",
        # Add more as needed
    ]
    
    total_fixed = 0
    total_skipped = 0
    total_errors = 0
    
    for topic in topics:
        fixed, skipped, errors = process_topic(topic)
        total_fixed += fixed
        total_skipped += skipped
        total_errors += errors
    
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Fixed: {total_fixed} files")
    print(f"⏭️  Skipped (already OK): {total_skipped} files")
    print(f"❌ Errors: {total_errors} files")
    print(f"📊 Total processed: {total_fixed + total_skipped + total_errors} files")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
