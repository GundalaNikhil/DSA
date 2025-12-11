---
unique_problem_id: gametheory_010
display_id: GAMETHEORY-010
slug: removal-game-strings
version: 1.0.0
difficulty: Medium
topic_tags:
  - Game Theory
  - String Manipulation
  - Sprague-Grundy
  - Interval DP
  - Palindrome
---

# Removal Game on Strings

## Problem Description

Given string `s`. Move: remove any palindrome substring of length >=2. Remaining parts concatenate. Player unable to move loses. Determine winner for |s|<=200 via Grundy with memo.

## Examples

- Example 1:
  - Input: s = "aba"
  - Output: `First`
  - Explanation: Remove "aba" (entire palindrome). String becomes empty. Second player has no moves.

- Example 2:
  - Input: s = "ab"
  - Output: `Second`
  - Explanation: No palindrome of length >= 2 exists. First player cannot move.

- Example 3:
  - Input: s = "aa"
  - Output: `First`
  - Explanation: Remove "aa" (palindrome). Empty string. Second loses.

## Constraints

- |s| <= 200

## Function Signatures

### Java
```java
class Solution {
    public String removalGameStrings(String s) {
        // Implementation here
    }
}
```

### Python
```python
def removal_game_strings(s: str) -> str:
    """
    Determine winner of palindrome removal game.
    
    Args:
        s: Input string
    
    Returns:
        "First" or "Second" indicating winner
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string removalGameStrings(string s) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Single line: string s

### Sample Input
```
aba
```

## Hints

Use interval DP. For substring s[i..j], compute Grundy by trying all palindrome removals. Removing substring creates two independent parts whose Grundy values XOR.

## Quiz

### Question 1
Why is memoization essential here?

A) Strings can be long  
B) Many overlapping subproblems (same substrings)  
C) To track palindromes  
D) Both A and B

**Correct Answer:** D

**Explanation:** With |s|=200, there are O(n²) substrings. Many game states lead to the same substrings, making memoization critical.

### Question 2
What happens when a middle palindrome is removed?

A) Game ends  
B) Remaining parts form two independent games  
C) Parts concatenate into one string  
D) Both B and C (concatenate, but analyzed as interval)

**Correct Answer:** C

**Explanation:** After removal, remaining parts concatenate, forming a new string to analyze.

### Question 3
Is "a" (single character) a valid removal?

A) Yes  
B) No, length must be >= 2  
C) Depends on position  
D) Only at string ends

**Correct Answer:** B

**Explanation:** The problem specifies palindrome of length >= 2 is required.

### Question 4
What is time complexity with memoization?

A) O(n²)  
B) O(n³) - O(n²) states, O(n) transitions  
C) O(n⁴)  
D) O(2^n)

**Correct Answer:** B

**Explanation:** O(n²) possible substrings, each requiring O(n) palindrome checks/transitions.
