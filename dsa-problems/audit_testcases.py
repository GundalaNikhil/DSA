#!/usr/bin/env python3
"""
Comprehensive Test Case Audit Script
Checks:
1. Which folders have testcases
2. Format consistency
3. Problem ID matching
4. Identifies issues by priority
"""

import os
import yaml
import re
from collections import defaultdict

# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def find_topic_folders():
    """Find all topic folders."""
    topics = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and item[0].isupper() and item not in ['libs']:
            topics.append(item)
    return sorted(topics)

def check_testcases_exist(topic):
    """Check if testcases directory exists and has files."""
    testcases_dir = os.path.join(topic, 'testcases')
    if not os.path.exists(testcases_dir):
        return False, 0, []
    
    yaml_files = [f for f in os.listdir(testcases_dir) if f.endswith('.yaml')]
    return True, len(yaml_files), yaml_files

def validate_yaml_format(filepath):
    """Validate YAML format and structure."""
    issues = []
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Check if file is empty
        if not content.strip():
            issues.append("Empty file")
            return issues
            
        # Try to parse YAML
        try:
            data = yaml.safe_load(content)
        except yaml.YAMLError as e:
            issues.append(f"YAML parse error: {str(e)}")
            return issues
        
        # Check required fields
        if not isinstance(data, dict):
            issues.append("Root is not a dictionary")
            return issues
            
        if 'problem_id' not in data:
            issues.append("Missing 'problem_id' field")
        
        # Check sections
        has_samples = 'samples' in data and isinstance(data.get('samples'), list)
        has_public = 'public' in data and isinstance(data.get('public'), list)
        has_hidden = 'hidden' in data and isinstance(data.get('hidden'), list)
        
        if not (has_samples or has_public or has_hidden):
            issues.append("No test case sections (samples/public/hidden)")
        
        # Check format of test cases
        for section in ['samples', 'public', 'hidden']:
            if section in data and isinstance(data[section], list):
                for idx, case in enumerate(data[section]):
                    if not isinstance(case, dict):
                        issues.append(f"{section}[{idx}]: Not a dictionary")
                        continue
                    if 'input' not in case:
                        issues.append(f"{section}[{idx}]: Missing 'input'")
                    if 'output' not in case:
                        issues.append(f"{section}[{idx}]: Missing 'output'")
                    
                    # Check if output is empty
                    if 'output' in case and not str(case['output']).strip():
                        issues.append(f"{section}[{idx}]: Empty output")
        
        # Check for proper |- format in content
        if '|-' not in content and (has_samples or has_public or has_hidden):
            issues.append("Missing '|-' multiline syntax")
            
    except Exception as e:
        issues.append(f"Exception: {str(e)}")
    
    return issues

def extract_problem_id_from_filename(filename):
    """Extract problem ID from filename."""
    # Format: XXX-NNN-slug-name.yaml
    match = re.match(r'^([A-Z]{3,4}-\d{3})-', filename)
    return match.group(1) if match else None

def check_problem_id_match(filepath):
    """Check if problem_id in file matches filename."""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        
        if not data or 'problem_id' not in data:
            return False, "No problem_id in file"
        
        file_problem_id = extract_problem_id_from_filename(os.path.basename(filepath))
        yaml_problem_id = data['problem_id']
        
        if not file_problem_id:
            return False, "Cannot extract ID from filename"
        
        # Normalize comparison (remove hyphens)
        file_id_norm = file_problem_id.replace('-', '')
        yaml_id_norm = str(yaml_problem_id).replace('-', '').replace('_', '')
        
        if file_id_norm.upper() != yaml_id_norm.upper()[:len(file_id_norm)]:
            return False, f"Mismatch: file={file_problem_id}, yaml={yaml_problem_id}"
        
        return True, "Match"
    except Exception as e:
        return False, f"Error: {str(e)}"

def count_test_cases(filepath):
    """Count test cases in file."""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        
        if not data:
            return 0, 0, 0
        
        samples = len(data.get('samples', []))
        public = len(data.get('public', []))
        hidden = len(data.get('hidden', []))
        
        return samples, public, hidden
    except:
        return 0, 0, 0

def main():
    print("=" * 80)
    print("COMPREHENSIVE TEST CASE AUDIT")
    print("=" * 80)
    print()
    
    topics = find_topic_folders()
    
    # Summary data
    summary = {
        'has_testcases': [],
        'no_testcases': [],
        'total_files': 0,
        'issues_by_severity': defaultdict(list)
    }
    
    detailed_issues = []
    
    for topic in topics:
        has_testcases, count, files = check_testcases_exist(topic)
        
        if has_testcases and count > 0:
            summary['has_testcases'].append((topic, count))
            summary['total_files'] += count
            
            print(f"{GREEN}✓{RESET} {topic:20s} → {count:3d} test files")
            
            # Check each file
            topic_issues = []
            for yaml_file in sorted(files):
                filepath = os.path.join(topic, 'testcases', yaml_file)
                
                # Validate format
                format_issues = validate_yaml_format(filepath)
                
                # Check problem ID
                id_match, id_msg = check_problem_id_match(filepath)
                
                # Count tests
                samples, public, hidden = count_test_cases(filepath)
                total_tests = samples + public + hidden
                
                # Categorize issues
                severity = 0
                file_issues = []
                
                if format_issues:
                    severity = max(severity, 3)
                    file_issues.extend(format_issues)
                
                if not id_match:
                    severity = max(severity, 2)
                    file_issues.append(f"ID issue: {id_msg}")
                
                if total_tests == 0:
                    severity = max(severity, 3)
                    file_issues.append("No test cases")
                elif total_tests < 10:
                    severity = max(severity, 1)
                    file_issues.append(f"Only {total_tests} tests (expected ~38)")
                
                if file_issues:
                    topic_issues.append({
                        'file': yaml_file,
                        'severity': severity,
                        'issues': file_issues,
                        'test_count': total_tests
                    })
            
            if topic_issues:
                detailed_issues.append({
                    'topic': topic,
                    'issues': topic_issues,
                    'max_severity': max(i['severity'] for i in topic_issues)
                })
        else:
            summary['no_testcases'].append(topic)
            print(f"{RED}✗{RESET} {topic:20s} → No testcases")
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nTopics with testcases: {len(summary['has_testcases'])}")
    print(f"Topics without testcases: {len(summary['no_testcases'])}")
    print(f"Total test files: {summary['total_files']}")
    
    if summary['no_testcases']:
        print(f"\n{YELLOW}Topics needing testcases:{RESET}")
        for topic in summary['no_testcases']:
            print(f"  - {topic}")
    
    # Report issues by severity
    print()
    print("=" * 80)
    print("ISSUES BY SEVERITY (Priority Order)")
    print("=" * 80)
    
    # Sort by severity
    detailed_issues.sort(key=lambda x: x['max_severity'], reverse=True)
    
    if not detailed_issues:
        print(f"\n{GREEN}✓ No issues found! All test cases are properly formatted.{RESET}")
    else:
        severity_names = {3: "CRITICAL", 2: "HIGH", 1: "LOW"}
        
        for topic_data in detailed_issues:
            topic = topic_data['topic']
            max_sev = topic_data['max_severity']
            
            print(f"\n{RED if max_sev == 3 else YELLOW if max_sev == 2 else BLUE}▶ {topic} (Max Severity: {severity_names.get(max_sev, 'UNKNOWN')}){RESET}")
            
            # Sort files by severity
            sorted_files = sorted(topic_data['issues'], key=lambda x: x['severity'], reverse=True)
            
            for file_info in sorted_files[:5]:  # Show top 5 issues per topic
                severity = file_info['severity']
                sev_color = RED if severity == 3 else YELLOW if severity == 2 else BLUE
                print(f"  {sev_color}[{severity_names.get(severity, '?')}]{RESET} {file_info['file']}")
                print(f"       Tests: {file_info['test_count']}")
                for issue in file_info['issues'][:3]:
                    print(f"       - {issue}")
            
            if len(sorted_files) > 5:
                print(f"  ... and {len(sorted_files) - 5} more files with issues")
    
    # Priority recommendations
    print()
    print("=" * 80)
    print("PRIORITY RECOMMENDATIONS")
    print("=" * 80)
    
    if detailed_issues:
        critical_topics = [d for d in detailed_issues if d['max_severity'] == 3]
        high_topics = [d for d in detailed_issues if d['max_severity'] == 2]
        
        if critical_topics:
            print(f"\n{RED}PRIORITY 1 - CRITICAL:{RESET}")
            print("These topics have empty files, parse errors, or no test cases:")
            for d in critical_topics[:5]:
                count = len([i for i in d['issues'] if i['severity'] == 3])
                print(f"  1. {d['topic']} ({count} files)")
        
        if high_topics:
            print(f"\n{YELLOW}PRIORITY 2 - HIGH:{RESET}")
            print("These topics have ID mismatches or format issues:")
            for d in high_topics[:5]:
                count = len([i for i in d['issues'] if i['severity'] == 2])
                print(f"  2. {d['topic']} ({count} files)")
        
        low_topics = [d for d in detailed_issues if d['max_severity'] == 1]
        if low_topics:
            print(f"\n{BLUE}PRIORITY 3 - LOW:{RESET}")
            print("These topics have minor issues (low test counts):")
            for d in low_topics[:5]:
                count = len([i for i in d['issues'] if i['severity'] == 1])
                print(f"  3. {d['topic']} ({count} files)")
    
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()
