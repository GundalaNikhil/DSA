#!/usr/bin/env python3
"""
Comprehensive Verification Script for StringsClassic Topic (STC-001 to STC-016)
Verifies all 608 test cases against editorial solutions.
"""

import yaml
import os
import sys
import random

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# ============================================================================
# Editorial Solutions - MATCHING GENERATION SCRIPT
# ============================================================================

def compute_prefix_function(s):
    """Compute KMP prefix function."""
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def solve_stc001(input_lines):
    """STC-001: KMP Prefix Function"""
    s = input_lines[0].strip()
    pi = compute_prefix_function(s)
    return ' '.join(map(str, pi))

def kmp_search(text, pattern):
    """Find all occurrences of pattern in text using KMP."""
    if not pattern or not text:
        return []
    
    pi = compute_prefix_function(pattern)
    matches = []
    j = 0
    
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - len(pattern) + 1)
            j = pi[j - 1]
    
    return matches

def solve_stc002(input_lines):
    """STC-002: Pattern Search KMP"""
    text = input_lines[0].strip()
    pattern = input_lines[1].strip()
    matches = kmp_search(text, pattern)
    return ' '.join(map(str, matches)) if matches else "-1"

def compute_z_function(s):
    """Compute Z-function."""
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def solve_stc003(input_lines):
    """STC-003: Z Function"""
    s = input_lines[0].strip()
    z = compute_z_function(s)
    return ' '.join(map(str, z))

def z_search(text, pattern):
    """Find all occurrences using Z-function."""
    combined = pattern + "$" + text
    z = compute_z_function(combined)
    m = len(pattern)
    matches = []
    
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            matches.append(i - m - 1)
    
    return matches

def solve_stc004(input_lines):
    """STC-004: Pattern Search Z"""
    text = input_lines[0].strip()
    pattern = input_lines[1].strip()
    matches = z_search(text, pattern)
    return ' '.join(map(str, matches)) if matches else "-1"

def build_suffix_array(s):
    """Build suffix array using doubling algorithm."""
    n = len(s)
    suffixes = list(range(n))
    rank = [ord(c) for c in s]
    temp_rank = [0] * n
    k = 1
    
    while k < n:
        suffixes.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        
        temp_rank[suffixes[0]] = 0
        for i in range(1, n):
            prev = suffixes[i - 1]
            curr = suffixes[i]
            if (rank[curr], rank[curr + k] if curr + k < n else -1) == \
               (rank[prev], rank[prev + k] if prev + k < n else -1):
                temp_rank[curr] = temp_rank[prev]
            else:
                temp_rank[curr] = temp_rank[prev] + 1
        
        rank = temp_rank[:]
        k *= 2
    
    return suffixes

def solve_stc005(input_lines):
    """STC-005: Suffix Array Doubling"""
    s = input_lines[0].strip()
    sa = build_suffix_array(s)
    return ' '.join(map(str, sa))

def kasai_lcp(s, sa):
    """Compute LCP array using Kasai's algorithm."""
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    
    lcp = [0] * n
    h = 0
    
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    
    return lcp

def solve_stc006(input_lines):
    """STC-006: LCP Array Kasai"""
    s = input_lines[0].strip()
    sa = build_suffix_array(s)
    lcp = kasai_lcp(s, sa)
    return ' '.join(map(str, lcp))

def longest_repeated_substring(s):
    """Find longest repeated substring using suffix array."""
    if len(s) <= 1:
        return 0
    
    sa = build_suffix_array(s)
    lcp = kasai_lcp(s, sa)
    
    return max(lcp) if lcp else 0

def solve_stc007(input_lines):
    """STC-007: Longest Repeated Substring SA"""
    s = input_lines[0].strip()
    result = longest_repeated_substring(s)
    return str(result)

def count_distinct_substrings(s):
    """Count distinct substrings using suffix array."""
    n = len(s)
    if n == 0:
        return 0
    
    sa = build_suffix_array(s)
    lcp = kasai_lcp(s, sa)
    
    total = n * (n + 1) // 2
    duplicates = sum(lcp)
    
    return total - duplicates

def solve_stc008(input_lines):
    """STC-008: Distinct Substrings SA"""
    s = input_lines[0].strip()
    result = count_distinct_substrings(s)
    return str(result)

def minimal_rotation(s):
    """Find lexicographically minimal rotation."""
    doubled = s + s
    n = len(s)
    sa = build_suffix_array(doubled)
    
    for idx in sa:
        if idx < n:
            return idx
    
    return 0

def solve_stc009(input_lines):
    """STC-009: Minimal Rotation SA"""
    s = input_lines[0].strip()
    result = minimal_rotation(s)
    return str(result)

def lcp_two_suffixes(s, i, j):
    """Compute LCP of two suffixes."""
    n = len(s)
    lcp_len = 0
    while i + lcp_len < n and j + lcp_len < n and s[i + lcp_len] == s[j + lcp_len]:
        lcp_len += 1
    return lcp_len

def solve_stc010(input_lines):
    """STC-010: LCP Two Suffixes"""
    s = input_lines[0].strip()
    i, j = map(int, input_lines[1].split())
    result = lcp_two_suffixes(s, i, j)
    return str(result)

def lcs_two_strings(s1, s2):
    """Find longest common substring using suffix array."""
    if not s1 or not s2:
        return 0
    
    combined = s1 + "#" + s2
    n1, n2 = len(s1), len(s2)
    sa = build_suffix_array(combined)
    lcp = kasai_lcp(combined, sa)
    
    max_lcp = 0
    for i in range(1, len(sa)):
        if (sa[i] < n1) != (sa[i-1] < n1):
            max_lcp = max(max_lcp, lcp[i])
    
    return max_lcp

def solve_stc011(input_lines):
    """STC-011: LCS Two Strings SA"""
    s1 = input_lines[0].strip()
    s2 = input_lines[1].strip()
    result = lcs_two_strings(s1, s2)
    return str(result)

def diff_substrings_two_strings(s1, s2):
    """Count substrings in s1 not in s2."""
    total_s1 = count_distinct_substrings(s1)
    
    all_substrings_s2 = set()
    for i in range(len(s2)):
        for j in range(i + 1, len(s2) + 1):
            all_substrings_s2.add(s2[i:j])
    
    common_distinct = len(set(s1[i:j] for i in range(len(s1)) for j in range(i+1, len(s1)+1)) & all_substrings_s2)
    
    return total_s1 - common_distinct

def solve_stc012(input_lines):
    """STC-012: Diff Substrings Two Strings"""
    s1 = input_lines[0].strip()
    s2 = input_lines[1].strip()
    result = diff_substrings_two_strings(s1, s2)
    return str(result)

def count_distinct_palindromes(s):
    """Count distinct palindromic substrings."""
    n = len(s)
    palindromes = set()
    
    # Odd-length palindromes
    for center in range(n):
        left = right = center
        while left >= 0 and right < n and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
    
    # Even-length palindromes
    for center in range(n - 1):
        left = center
        right = center + 1
        while left >= 0 and right < n and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
    
    return len(palindromes)

def solve_stc013(input_lines):
    """STC-013: Palindromic Tree (Eertree)"""
    s = input_lines[0].strip()
    result = count_distinct_palindromes(s)
    return str(result)

def longest_palindrome_one_wildcard(s):
    """Find longest palindrome with at most one wildcard change."""
    n = len(s)
    max_len = 1
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            mismatches = 0
            left, right = 0, len(substr) - 1
            
            while left < right:
                if substr[left] != substr[right]:
                    mismatches += 1
                left += 1
                right -= 1
            
            if mismatches <= 1:
                max_len = max(max_len, len(substr))
    
    return max_len

def solve_stc014(input_lines):
    """STC-014: Longest Palindrome One Wildcard"""
    s = input_lines[0].strip()
    result = longest_palindrome_one_wildcard(s)
    return str(result)

def aho_corasick_count(text, patterns):
    """Count total pattern matches using simple approach."""
    total = 0
    for pattern in patterns:
        i = 0
        while i <= len(text) - len(pattern):
            if text[i:i+len(pattern)] == pattern:
                total += 1
                i += len(pattern)
            else:
                i += 1
    return total

def solve_stc015(input_lines):
    """STC-015: Aho-Corasick Cooldown Scoring"""
    text = input_lines[0].strip()
    k = int(input_lines[1])
    patterns = [input_lines[i+2].strip() for i in range(k)]
    result = aho_corasick_count(text, patterns)
    return str(result)

def suffix_automaton_queries(s, queries):
    """Check if each query is a substring."""
    results = []
    for query in queries:
        results.append("YES" if query in s else "NO")
    return results

def solve_stc016(input_lines):
    """STC-016: Suffix Automaton Queries"""
    s = input_lines[0].strip()
    q = int(input_lines[1])
    queries = [input_lines[i+2].strip() for i in range(q)]
    results = suffix_automaton_queries(s, queries)
    return '\n'.join(results)

# ============================================================================
# Test Case Verification
# ============================================================================

def parse_yaml_file(filepath):
    """Parse YAML test case file."""
    with open(filepath, 'r') as f:
        content = f.read()
    return yaml.safe_load(content)

def verify_problem(problem_id, testcases):
    """Verify all test cases for a problem."""
    stats = {'total': 0, 'passed': 0, 'failed': 0, 'errors': []}
    
    solver_map = {
        'STC-001': solve_stc001,
        'STC-002': solve_stc002,
        'STC-003': solve_stc003,
        'STC-004': solve_stc004,
        'STC-005': solve_stc005,
        'STC-006': solve_stc006,
        'STC-007': solve_stc007,
        'STC-008': solve_stc008,
        'STC-009': solve_stc009,
        'STC-010': solve_stc010,
        'STC-011': solve_stc011,
        'STC-012': solve_stc012,
        'STC-013': solve_stc013,
        'STC-014': solve_stc014,
        'STC-015': solve_stc015,
        'STC-016': solve_stc016
    }
    
    solve_func = solver_map.get(problem_id)
    if not solve_func:
        return stats
    
    for section in ['samples', 'public', 'hidden']:
        if section not in testcases:
            continue
        
        for idx, case in enumerate(testcases[section]):
            stats['total'] += 1
            input_lines = case['input'].strip().split('\n')
            expected_output = case['output'].strip()
            
            try:
                actual = solve_func(input_lines).strip()
                
                if actual == expected_output:
                    stats['passed'] += 1
                else:
                    stats['failed'] += 1
                    stats['errors'].append({
                        'section': section,
                        'index': idx,
                        'expected': expected_output,
                        'actual': actual
                    })
            
            except Exception as e:
                stats['failed'] += 1
                stats['errors'].append({
                    'section': section,
                    'index': idx,
                    'error': str(e)
                })
    
    return stats

def main():
    """Main verification function."""
    print("=" * 80)
    print("STRINGSCLASSIC TEST CASE VERIFICATION - ALL PROBLEMS")
    print("=" * 80)
    print()
    
    testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/StringsClassic/testcases"
    
    problems = [
        ('STC-001', 'kmp-prefix-function'),
        ('STC-002', 'pattern-search-kmp'),
        ('STC-003', 'z-function'),
        ('STC-004', 'pattern-search-z'),
        ('STC-005', 'suffix-array-doubling'),
        ('STC-006', 'lcp-array-kasai'),
        ('STC-007', 'longest-repeated-substring-sa'),
        ('STC-008', 'distinct-substrings-sa'),
        ('STC-009', 'minimal-rotation-sa'),
        ('STC-010', 'lcp-two-suffixes'),
        ('STC-011', 'lcs-two-strings-sa'),
        ('STC-012', 'diff-substrings-two-strings'),
        ('STC-013', 'palindromic-tree-eertree'),
        ('STC-014', 'longest-palindrome-one-wildcard'),
        ('STC-015', 'aho-corasick-cooldown-scoring'),
        ('STC-016', 'suffix-automaton-queries')
    ]
    
    total_stats = {'total': 0, 'passed': 0, 'failed': 0}
    problem_results = []
    
    for problem_id, problem_name in problems:
        filepath = os.path.join(testcases_dir, f"{problem_id}-{problem_name}.yaml")
        
        if not os.path.exists(filepath):
            print(f"{RED}✗ {problem_id}: File not found{RESET}")
            continue
        
        testcases = parse_yaml_file(filepath)
        stats = verify_problem(problem_id, testcases)
        
        total_stats['total'] += stats['total']
        total_stats['passed'] += stats['passed']
        total_stats['failed'] += stats['failed']
        
        pass_rate = (stats['passed'] / stats['total'] * 100) if stats['total'] > 0 else 0
        
        status = GREEN + '✓' if stats['failed'] == 0 else RED + '✗'
        print(f"{status} {problem_id}: {stats['passed']}/{stats['total']} passed ({pass_rate:.1f}%){RESET}")
        
        problem_results.append({
            'id': problem_id,
            'stats': stats,
            'pass_rate': pass_rate
        })
        
        if stats['errors'] and len(stats['errors']) <= 3:
            for err in stats['errors'][:3]:
                print(f"  {YELLOW}Error in {err.get('section', 'unknown')}[{err.get('index', '?')}]{RESET}")
                if 'error' in err:
                    print(f"    Exception: {err['error']}")
    
    print()
    print("=" * 80)
    overall_rate = (total_stats['passed'] / total_stats['total'] * 100) if total_stats['total'] > 0 else 0
    
    if total_stats['failed'] == 0:
        print(f"{GREEN}✅ ALL TESTS PASSED: {total_stats['passed']}/{total_stats['total']} ({overall_rate:.1f}%){RESET}")
    else:
        print(f"{YELLOW}RESULTS: {total_stats['passed']}/{total_stats['total']} passed ({overall_rate:.1f}%){RESET}")
        print(f"{RED}Failed: {total_stats['failed']} test cases{RESET}")
    
    print("=" * 80)
    
    return total_stats['failed'] == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
