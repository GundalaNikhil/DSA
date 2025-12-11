---
unique_problem_id: bitwise_014
display_id: BITWISE-014
slug: bitwise-palindromes-balanced-ones
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - Digit DP
  - Palindrome
  - Popcount
  - Enumeration
---

# Bitwise Palindromes With Balanced Ones

## Problem Description

Count numbers in the range `[L, R]` whose binary representation is a palindrome AND whose number of set bits (1s) is even.

## Examples

- Example 1:
  - Input: `L = 5`, `R = 12`
  - Output: `2`
  - Explanation: Numbers with palindrome binary and even popcount:
    - 5 = 101 (palindrome, 2 ones = even) ✓
    - 6 = 110 (not palindrome)
    - 7 = 111 (palindrome, 3 ones = odd) ✗
    - 8 = 1000 (not palindrome)
    - 9 = 1001 (palindrome, 2 ones = even) ✓
    - 10 = 1010 (not palindrome)
    - 11 = 1011 (not palindrome)
    - 12 = 1100 (not palindrome)
    Count = 2 (5 and 9).

- Example 2:
  - Input: `L = 1`, `R = 3`
  - Output: `1`
  - Explanation: 1=1 (palindrome, 1 bit = odd), 2=10 (not palindrome), 3=11 (palindrome, 2 bits = even). Count = 1.

- Example 3:
  - Input: `L = 0`, `R = 0`
  - Output: `1`
  - Explanation: 0 = empty/0 (palindrome, 0 ones = even). Count = 1.

## Constraints

- `0 <= L <= R <= 10^12`

## Function Signatures

### Java
```java
class Solution {
    public long bitwisePalindromeBalancedOnes(long L, long R) {
        // Implementation here
        return 0;
    }
}
```

### Python
```python
def bitwise_palindrome_balanced_ones(L: int, R: int) -> int:
    """
    Count numbers in [L,R] with palindromic binary and even popcount.
    
    Args:
        L: Lower bound (inclusive)
        R: Upper bound (inclusive)
    
    Returns:
        Count of valid numbers
    """
    pass
```

### C++
```cpp
class Solution {
public:
    long long bitwisePalindromeBalancedOnes(long long L, long long R) {
        // Implementation here
        return 0;
    }
};
```

## Input Format

The input will be provided as:
- Single line: Two integers `L` and `R`

### Sample Input
```
5 12
```

## Hints

Generate binary palindromes by constructing the first half and mirroring. Track popcount during generation to filter even-weight numbers.

## Quiz

### Question 1
How do we generate binary palindromes efficiently?

A) Check every number  
B) Construct the first half and mirror it  
C) Use dynamic programming  
D) Binary search

**Correct Answer:** B

**Explanation:** We build the first half of bits, then mirror to create the second half. This generates all palindromes without checking each number.

### Question 2
For a k-bit binary palindrome, how many free bits do we choose?

A) k  
B) k/2  
C) ceil(k/2)  
D) k-1

**Correct Answer:** C

**Explanation:** We freely choose the first ceil(k/2) bits; the rest are determined by mirroring.

### Question 3
Why check popcount parity during generation?

A) To avoid overflow  
B) To filter results efficiently without post-processing  
C) To determine palindrome structure  
D) To sort the results

**Correct Answer:** B

**Explanation:** Tracking popcount while generating lets us immediately discard odd-popcount palindromes.

### Question 4
Is 0 considered a binary palindrome with even popcount?

A) Yes (empty or "0" is palindrome, popcount=0 is even)  
B) No, 0 is not a valid number  
C) Only if L=0  
D) It's undefined

**Correct Answer:** A

**Explanation:** 0's binary representation (empty or single 0) is a palindrome, and popcount(0)=0 is even.
