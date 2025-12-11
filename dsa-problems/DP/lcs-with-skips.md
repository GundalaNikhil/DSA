# Longest Common Subsequence With Skips

## Problem Metadata
- **unique_problem_id**: `dp_010`
- **display_id**: `DP-010`
- **slug**: `lcs-with-skips`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "String", "Longest Common Subsequence"]`

## Problem Title
Longest Common Subsequence With Skips

## Problem Description
Given two strings `a` and `b`, and an integer `s`, find the longest common subsequence (LCS) between them with a twist: you may skip up to `s` characters from string `a` for free.

Skipping a character means removing it from consideration without breaking the order of remaining characters. This gives you more flexibility in finding common subsequences.

Return the length of the longest common subsequence achievable.

## Examples

### Example 1
**Input:**
```
a = "abcde"
b = "ace"
s = 1
```

**Output:**
```
3
```

**Explanation:**
- Standard LCS("abcde", "ace") = "ace" with length 3
- We don't even need to use the skip allowance
- Result: 3

### Example 2
**Input:**
```
a = "abcxdef"
b = "abef"
s = 2
```

**Output:**
```
4
```

**Explanation:**
- Skip 'c' and 'x' from a (uses 2 skips) → "abdef"
- Skip 'd' from result → "abef"
- Common with b = "abef" has length 4

### Example 3
**Input:**
```
a = "programming"
b = "gaming"
s = 5
```

**Output:**
```
6
```

**Explanation:**
- Skip "progr" from a → "amming"
- LCS of "amming" and "gaming" = "aming" with length 5... wait let me recalculate
- "gaming" vs "programming": common letters: g,a,m,i,n,g
- If we skip "pro" from start and some middle chars, we can match "gaming"
- Actually the LCS is "gaming" itself if we skip appropriately
- Length = 6

## Constraints
- `0 <= |a|, |b| <= 2000`
- `0 <= s <= |a|`

## Function Signatures

### Java
```java
class Solution {
    public int lcsWithSkips(String a, String b, int s) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def lcsWithSkips(self, a: str, b: str, s: int) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int lcsWithSkips(string a, string b, int s) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: String a
Line 2: String b
Line 3: Integer s (skip allowance)
```

### Sample Input
```
abcde
ace
1
```

## Hints
- Extend standard LCS DP to track skip usage
- State: dp[i][j][k] = max LCS length using first i chars of a, first j chars of b, with k skips used
- Transitions:
  - If a[i] == b[j]: dp[i+1][j+1][k] = dp[i][j][k] + 1 (match, no skip)
  - Skip from a (if k < s): dp[i+1][j][k+1] = dp[i][j][k] (skip a[i])
  - Skip from b: dp[i][j+1][k] = dp[i][j][k] (move in b without match)
- Base case: dp[0][0][0] = 0
- Answer: max(dp[|a|][|b|][k]) for all k ≤ s

## Related Topics Quiz

### Question 1
How does this problem differ from standard LCS?
- A) It uses three strings
- B) It allows skipping characters from the first string
- C) It finds the shortest sequence
- D) It requires exact matches

**Answer:** B) It allows skipping characters from the first string - We can skip up to s characters from string a.

### Question 2
What is the time complexity of the DP solution?
- A) O(|a| × |b|)
- B) O(|a| × |b| × s)
- C) O(|a| + |b| + s)
- D) O(|a|² × |b|²)

**Answer:** B) O(|a| × |b| × s) - Three dimensions: positions in both strings and skips used.

### Question 3
What is the maximum possible LCS length with unlimited skips (s = |a|)?
- A) |a|
- B) |b|
- C) min(|a|, |b|)
- D) |a| + |b|

**Answer:** B) |b| - With unlimited skips, we can skip all characters in a that don't match b, so at most |b| length.

### Question 4
If s = 0, what problem does this reduce to?
- A) Edit Distance
- B) Standard LCS
- C) Longest Palindrome
- D) Substring matching

**Answer:** B) Standard LCS - No skips allowed means standard Longest Common Subsequence.

### Question 5
Why do we skip from string a and not string b?
- A) String a is always longer
- B) The problem definition allows skips only from a
- C) It's more efficient
- D) We actually skip from both

**Answer:** B) The problem definition allows skips only from a - The asymmetry is part of the problem constraint.
