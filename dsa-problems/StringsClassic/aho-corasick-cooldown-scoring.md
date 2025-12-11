---
unique_problem_id: stringalgo_015
display_id: STRINGALGO-015
slug: aho-corasick-cooldown-scoring
version: 1.0.0
difficulty: Medium
topic_tags:
  - String Algorithms
  - Problem Solving
---

# Aho-Corasick With Cooldown Scoring

## Problem Description

Each pattern `p_i` has a score `w_i`. When you scan text `T`, you may choose a subset of matched occurrences so that after choosing a match ending at position `r`, you must skip the next `G` characters (no chosen match may start in `(r, r+G]`). Find the maximum total score you can collect.

## Examples

- Input: patterns `[("ab",5),("b",2)]`, `G=1`, text `"abb"`
  - Occurrences: "ab" at [1,2] score 5; "b" at [2,2] score 2; "b" at [3,3] score 2.
  - Output: `5` (take "ab"; cooldown blocks starting at 3, so best total is 5)

## Constraints

`1 <= |T| <= 2 * 10^5`; total pattern length <= `2 * 10^5`; `0 <= w_i <= 10^6`; `0 <= G <= 1000`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] ahoCorasickCooldownScoring(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def ahoCorasickCooldownScoring(arr: List[int]) -> List[int]:
    """
    Solve the problem.

    Args:
        arr: Input array

    Returns:
        Result array
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<int> ahoCorasickCooldownScoring(vector<int>& arr) {
        // Implementation here
        return {};
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer n (size of array)
- Second line: n space-separated integers representing the array

### Sample Input
```
5
1 2 3 4 5
```

## Hints

Use Aho-Corasick to list all occurrences (end index, length, weight). Then sort by end position and run DP with binary search over the next allowed start (`r+G+1`) to pick non-overlapping matches respecting the cooldown.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Aho-Corasick With Cooldown Scoring'?**

A) O(1)
B) O(n)
C) O(n log n)
D) O(n^2)

**Correct Answer:** B

**Explanation:** The solution requires additional space proportional to the input size for preprocessing or storage.

### Question 2
**What technique is most applicable to solve this problem efficiently?**

A) Two pointers
B) Divide and conquer
C) Dynamic programming
D) Greedy approach

**Correct Answer:** A

**Explanation:** The problem can be efficiently solved using the two-pointer technique.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) String Algorithms
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of String Algorithms techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
