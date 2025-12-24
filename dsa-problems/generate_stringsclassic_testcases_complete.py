#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for StringsClassic Topic (STC-001 to STC-016)
Following the Universal Test Case Generation Prompt.
Target: 30-40 test cases per problem with proper YAML format.
"""

import random
import string
from collections import defaultdict

def format_testcase_yaml(data):
    """Format test cases in proper YAML with |- syntax."""
    lines = []
    lines.append(f"problem_id: {data['problem_id']}")
    
    for section_name in ['samples', 'public', 'hidden']:
        if section_name not in data or not data[section_name]:
            continue
        lines.append(f"{section_name}:")
        for case in data[section_name]:
            lines.append("- input: |-")
            for line in case['input'].strip().split('\n'):
                lines.append(f"    {line}")
            lines.append("  output: |-")
            for line in case['output'].strip().split('\n'):
                lines.append(f"    {line}")
    
    return '\n'.join(lines)


# ============================================================================
# STC-001: KMP Prefix Function
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

def generate_stc001_cases():
    cases = {'problem_id': 'STC-001', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["ababa", "aaaa", "abcabc"]
    for s in sample_strings:
        pi = compute_prefix_function(s)
        cases['samples'].append({
            'input': s,
            'output': ' '.join(map(str, pi))
        })
    
    # Public + Hidden
    random.seed(42)
    test_patterns = [
        lambda n: 'a' * n,  # All same
        lambda n: ''.join(chr(ord('a') + i % 3) for i in range(n)),  # Pattern
        lambda n: ''.join(random.choice('abc') for _ in range(n)),  # Random
        lambda n: 'ab' * (n // 2) + 'a' * (n % 2),  # Repeating
        lambda n: ''.join(chr(ord('a') + i % 5) for i in range(n)),  # 5-pattern
    ]
    
    for idx in range(35):
        n = random.randint(5, 50)
        pattern_func = random.choice(test_patterns)
        s = pattern_func(n)
        pi = compute_prefix_function(s)
        
        test_case = {
            'input': s,
            'output': ' '.join(map(str, pi))
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-002: Pattern Search KMP
# ============================================================================

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

def generate_stc002_cases():
    cases = {'problem_id': 'STC-002', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ("abababa", "aba"),
        ("aaaa", "aa"),
        ("abcdefg", "xyz")
    ]
    
    for text, pattern in sample_data:
        matches = kmp_search(text, pattern)
        cases['samples'].append({
            'input': f"{text}\n{pattern}",
            'output': ' '.join(map(str, matches)) if matches else "-1"
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(10, 60)
        m = random.randint(2, min(10, n))
        
        # Generate text and pattern
        text = ''.join(random.choice('abc') for _ in range(n))
        pattern = ''.join(random.choice('abc') for _ in range(m))
        
        matches = kmp_search(text, pattern)
        
        test_case = {
            'input': f"{text}\n{pattern}",
            'output': ' '.join(map(str, matches)) if matches else "-1"
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-003: Z Function
# ============================================================================

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

def generate_stc003_cases():
    cases = {'problem_id': 'STC-003', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["abacaba", "aaaa", "abcabc"]
    for s in sample_strings:
        z = compute_z_function(s)
        cases['samples'].append({
            'input': s,
            'output': ' '.join(map(str, z))
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(5, 50)
        s = ''.join(random.choice('abc') for _ in range(n))
        z = compute_z_function(s)
        
        test_case = {
            'input': s,
            'output': ' '.join(map(str, z))
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-004: Pattern Search Z
# ============================================================================

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

def generate_stc004_cases():
    cases = {'problem_id': 'STC-004', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ("abababa", "aba"),
        ("aaaa", "aa"),
        ("abcdefg", "xyz")
    ]
    
    for text, pattern in sample_data:
        matches = z_search(text, pattern)
        cases['samples'].append({
            'input': f"{text}\n{pattern}",
            'output': ' '.join(map(str, matches)) if matches else "-1"
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(10, 60)
        m = random.randint(2, min(10, n))
        text = ''.join(random.choice('abc') for _ in range(n))
        pattern = ''.join(random.choice('abc') for _ in range(m))
        
        matches = z_search(text, pattern)
        
        test_case = {
            'input': f"{text}\n{pattern}",
            'output': ' '.join(map(str, matches)) if matches else "-1"
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-005: Suffix Array Doubling
# ============================================================================

def build_suffix_array(s):
    """Build suffix array using doubling algorithm."""
    n = len(s)
    suffixes = list(range(n))
    rank = [ord(c) for c in s]
    temp_rank = [0] * n
    k = 1
    
    while k < n:
        # Sort by (rank[i], rank[i+k])
        suffixes.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        
        # Update ranks
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

def generate_stc005_cases():
    cases = {'problem_id': 'STC-005', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["cababa", "banana", "abc"]
    for s in sample_strings:
        sa = build_suffix_array(s)
        cases['samples'].append({
            'input': s,
            'output': ' '.join(map(str, sa))
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(5, 30)
        s = ''.join(random.choice('abc') for _ in range(n))
        sa = build_suffix_array(s)
        
        test_case = {
            'input': s,
            'output': ' '.join(map(str, sa))
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-006: LCP Array Kasai
# ============================================================================

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

def generate_stc006_cases():
    cases = {'problem_id': 'STC-006', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["banana", "ababa", "aaa"]
    for s in sample_strings:
        sa = build_suffix_array(s)
        lcp = kasai_lcp(s, sa)
        cases['samples'].append({
            'input': s,
            'output': ' '.join(map(str, lcp))
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(5, 30)
        s = ''.join(random.choice('abc') for _ in range(n))
        sa = build_suffix_array(s)
        lcp = kasai_lcp(s, sa)
        
        test_case = {
            'input': s,
            'output': ' '.join(map(str, lcp))
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-007: Longest Repeated Substring SA
# ============================================================================

def longest_repeated_substring(s):
    """Find longest repeated substring using suffix array."""
    if len(s) <= 1:
        return 0
    
    sa = build_suffix_array(s)
    lcp = kasai_lcp(s, sa)
    
    return max(lcp) if lcp else 0

def generate_stc007_cases():
    cases = {'problem_id': 'STC-007', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["banana", "abcabc", "abc"]
    for s in sample_strings:
        result = longest_repeated_substring(s)
        cases['samples'].append({
            'input': s,
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(5, 30)
        s = ''.join(random.choice('abc') for _ in range(n))
        result = longest_repeated_substring(s)
        
        test_case = {
            'input': s,
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-008: Distinct Substrings SA
# ============================================================================

def count_distinct_substrings(s):
    """Count distinct substrings using suffix array."""
    n = len(s)
    if n == 0:
        return 0
    
    sa = build_suffix_array(s)
    lcp = kasai_lcp(s, sa)
    
    # Total substrings - duplicates
    total = n * (n + 1) // 2
    duplicates = sum(lcp)
    
    return total - duplicates

def generate_stc008_cases():
    cases = {'problem_id': 'STC-008', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["abc", "aaa", "ababa"]
    for s in sample_strings:
        result = count_distinct_substrings(s)
        cases['samples'].append({
            'input': s,
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(3, 25)
        s = ''.join(random.choice('abc') for _ in range(n))
        result = count_distinct_substrings(s)
        
        test_case = {
            'input': s,
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-009: Minimal Rotation SA
# ============================================================================

def minimal_rotation(s):
    """Find lexicographically minimal rotation."""
    doubled = s + s
    n = len(s)
    sa = build_suffix_array(doubled)
    
    # Find first suffix that starts within original string
    for idx in sa:
        if idx < n:
            return idx
    
    return 0

def generate_stc009_cases():
    cases = {'problem_id': 'STC-009', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["bca", "aaa", "dcba"]
    for s in sample_strings:
        result = minimal_rotation(s)
        cases['samples'].append({
            'input': s,
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(3, 25)
        s = ''.join(random.choice('abc') for _ in range(n))
        result = minimal_rotation(s)
        
        test_case = {
            'input': s,
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-010: LCP Two Suffixes
# ============================================================================

def lcp_two_suffixes(s, i, j):
    """Compute LCP of two suffixes."""
    n = len(s)
    lcp_len = 0
    while i + lcp_len < n and j + lcp_len < n and s[i + lcp_len] == s[j + lcp_len]:
        lcp_len += 1
    return lcp_len

def generate_stc010_cases():
    cases = {'problem_id': 'STC-010', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ("banana", 1, 3),
        ("abcabc", 0, 3),
        ("aaa", 0, 2)
    ]
    
    for s, i, j in sample_data:
        result = lcp_two_suffixes(s, i, j)
        cases['samples'].append({
            'input': f"{s}\n{i} {j}",
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(5, 30)
        s = ''.join(random.choice('abc') for _ in range(n))
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        result = lcp_two_suffixes(s, i, j)
        
        test_case = {
            'input': f"{s}\n{i} {j}",
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-011: LCS Two Strings SA
# ============================================================================

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
        # Check if suffixes are from different strings
        if (sa[i] < n1) != (sa[i-1] < n1):
            max_lcp = max(max_lcp, lcp[i])
    
    return max_lcp

def generate_stc011_cases():
    cases = {'problem_id': 'STC-011', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ("abcde", "xabcy"),
        ("aaa", "aaa"),
        ("abc", "xyz")
    ]
    
    for s1, s2 in sample_data:
        result = lcs_two_strings(s1, s2)
        cases['samples'].append({
            'input': f"{s1}\n{s2}",
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n1 = random.randint(5, 20)
        n2 = random.randint(5, 20)
        s1 = ''.join(random.choice('abc') for _ in range(n1))
        s2 = ''.join(random.choice('abc') for _ in range(n2))
        result = lcs_two_strings(s1, s2)
        
        test_case = {
            'input': f"{s1}\n{s2}",
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-012: Diff Substrings Two Strings
# ============================================================================

def diff_substrings_two_strings(s1, s2):
    """Count substrings in s1 not in s2."""
    total_s1 = count_distinct_substrings(s1)
    
    # Count common substrings (simplified approach)
    all_substrings_s2 = set()
    for i in range(len(s2)):
        for j in range(i + 1, len(s2) + 1):
            all_substrings_s2.add(s2[i:j])
    
    common = 0
    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            if s1[i:j] in all_substrings_s2:
                common += 1
    
    # Count distinct common
    common_distinct = len(set(s1[i:j] for i in range(len(s1)) for j in range(i+1, len(s1)+1)) & all_substrings_s2)
    
    return total_s1 - common_distinct

def generate_stc012_cases():
    cases = {'problem_id': 'STC-012', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ("abc", "ab"),
        ("aaa", "aa"),
        ("xyz", "abc")
    ]
    
    for s1, s2 in sample_data:
        result = diff_substrings_two_strings(s1, s2)
        cases['samples'].append({
            'input': f"{s1}\n{s2}",
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n1 = random.randint(3, 15)
        n2 = random.randint(3, 15)
        s1 = ''.join(random.choice('abc') for _ in range(n1))
        s2 = ''.join(random.choice('abc') for _ in range(n2))
        result = diff_substrings_two_strings(s1, s2)
        
        test_case = {
            'input': f"{s1}\n{s2}",
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-013: Palindromic Tree (Eertree)
# ============================================================================

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

def generate_stc013_cases():
    cases = {'problem_id': 'STC-013', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["aba", "aaa", "abc"]
    for s in sample_strings:
        result = count_distinct_palindromes(s)
        cases['samples'].append({
            'input': s,
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(3, 25)
        s = ''.join(random.choice('abc') for _ in range(n))
        result = count_distinct_palindromes(s)
        
        test_case = {
            'input': s,
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-014: Longest Palindrome One Wildcard
# ============================================================================

def longest_palindrome_one_wildcard(s):
    """Find longest palindrome with at most one wildcard change."""
    n = len(s)
    max_len = 1
    
    # Check all substrings
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

def generate_stc014_cases():
    cases = {'problem_id': 'STC-014', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_strings = ["abca", "racecar", "abc"]
    for s in sample_strings:
        result = longest_palindrome_one_wildcard(s)
        cases['samples'].append({
            'input': s,
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(3, 20)
        s = ''.join(random.choice('abc') for _ in range(n))
        result = longest_palindrome_one_wildcard(s)
        
        test_case = {
            'input': s,
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-015: Aho-Corasick Cooldown Scoring
# ============================================================================

def aho_corasick_count(text, patterns):
    """Count total pattern matches using simple approach."""
    total = 0
    for pattern in patterns:
        i = 0
        while i <= len(text) - len(pattern):
            if text[i:i+len(pattern)] == pattern:
                total += 1
                i += len(pattern)  # Move past this match
            else:
                i += 1
    return total

def generate_stc015_cases():
    cases = {'problem_id': 'STC-015', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ("ababab", ["ab", "ba"]),
        ("aaaa", ["aa"]),
        ("abcdef", ["xyz", "abc"])
    ]
    
    for text, patterns in sample_data:
        result = aho_corasick_count(text, patterns)
        inp = f"{text}\n{len(patterns)}\n" + '\n'.join(patterns)
        cases['samples'].append({
            'input': inp,
            'output': str(result)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(10, 40)
        text = ''.join(random.choice('abc') for _ in range(n))
        k = random.randint(2, 5)
        patterns = [''.join(random.choice('abc') for _ in range(random.randint(2, 4))) for _ in range(k)]
        
        result = aho_corasick_count(text, patterns)
        inp = f"{text}\n{k}\n" + '\n'.join(patterns)
        
        test_case = {
            'input': inp,
            'output': str(result)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# STC-016: Suffix Automaton Queries
# ============================================================================

def suffix_automaton_queries(s, queries):
    """Check if each query is a substring."""
    results = []
    for query in queries:
        results.append("YES" if query in s else "NO")
    return results

def generate_stc016_cases():
    cases = {'problem_id': 'STC-016', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ("banana", ["an", "xyz", "ana"]),
        ("abcabc", ["abc", "cab", "xyz"]),
        ("aaa", ["aa", "aaaa", "a"])
    ]
    
    for s, queries in sample_data:
        results = suffix_automaton_queries(s, queries)
        inp = f"{s}\n{len(queries)}\n" + '\n'.join(queries)
        cases['samples'].append({
            'input': inp,
            'output': '\n'.join(results)
        })
    
    # Public + Hidden
    random.seed(42)
    for idx in range(35):
        n = random.randint(10, 30)
        s = ''.join(random.choice('abc') for _ in range(n))
        q = random.randint(2, 5)
        queries = []
        for _ in range(q):
            if random.random() < 0.5 and n > 2:
                # Create substring
                start = random.randint(0, n - 2)
                end = random.randint(start + 1, min(start + 5, n))
                queries.append(s[start:end])
            else:
                # Random string
                queries.append(''.join(random.choice('abc') for _ in range(random.randint(2, 4))))
        
        results = suffix_automaton_queries(s, queries)
        inp = f"{s}\n{q}\n" + '\n'.join(queries)
        
        test_case = {
            'input': inp,
            'output': '\n'.join(results)
        }
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# Main Generation
# ============================================================================

def main():
    """Generate test cases for all StringsClassic problems."""
    print("=" * 80)
    print("STRINGSCLASSIC TEST CASE GENERATION - ALL PROBLEMS (STC-001 to STC-016)")
    print("=" * 80)
    
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/StringsClassic/testcases"
    
    problems = [
        ("STC-001", "kmp-prefix-function", generate_stc001_cases),
        ("STC-002", "pattern-search-kmp", generate_stc002_cases),
        ("STC-003", "z-function", generate_stc003_cases),
        ("STC-004", "pattern-search-z", generate_stc004_cases),
        ("STC-005", "suffix-array-doubling", generate_stc005_cases),
        ("STC-006", "lcp-array-kasai", generate_stc006_cases),
        ("STC-007", "longest-repeated-substring-sa", generate_stc007_cases),
        ("STC-008", "distinct-substrings-sa", generate_stc008_cases),
        ("STC-009", "minimal-rotation-sa", generate_stc009_cases),
        ("STC-010", "lcp-two-suffixes", generate_stc010_cases),
        ("STC-011", "lcs-two-strings-sa", generate_stc011_cases),
        ("STC-012", "diff-substrings-two-strings", generate_stc012_cases),
        ("STC-013", "palindromic-tree-eertree", generate_stc013_cases),
        ("STC-014", "longest-palindrome-one-wildcard", generate_stc014_cases),
        ("STC-015", "aho-corasick-cooldown-scoring", generate_stc015_cases),
        ("STC-016", "suffix-automaton-queries", generate_stc016_cases),
    ]
    
    total_cases = 0
    
    for prob_id, slug, generator_func in problems:
        print(f"\n[{prob_id}] Generating {slug}...")
        cases = generator_func()
        yaml_content = format_testcase_yaml(cases)
        
        output_path = f"{base_path}/{prob_id}-{slug}.yaml"
        with open(output_path, 'w') as f:
            f.write(yaml_content)
        
        count = len(cases['samples']) + len(cases['public']) + len(cases['hidden'])
        total_cases += count
        print(f"✅ {prob_id}: {count} test cases")
        print(f"   Samples: {len(cases['samples'])}, Public: {len(cases['public'])}, Hidden: {len(cases['hidden'])}")
    
    print("\n" + "=" * 80)
    print(f"✅ ALL STRINGSCLASSIC TESTS COMPLETE: {total_cases} test cases generated")
    print("=" * 80)


if __name__ == "__main__":
    main()
