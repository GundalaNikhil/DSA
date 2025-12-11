---
unique_problem_id: hashing_016
display_id: HASHING-016
slug: hash-near-anagram-indexing
version: 1.0.0
difficulty: Medium
topic_tags:
  - Hashing
  - Problem Solving
---

# Hash-Based Near-Anagram Indexing

## Problem Description

Group words where two words belong together if they become anagrams after deleting exactly one character from each (choose any one char to drop). Return number of such groups.

## Examples

- Input: ["abcd","abdc","abc","abd"]
  - Output: 2 (group1: "abcd","abdc","abc"; group2: "abd")

## Constraints

`1 <= n <= 10^5`, word length <= 30`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] hashNearAnagramIndexing(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def hashNearAnagramIndexing(arr: List[int]) -> List[int]:
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
    vector<int> hashNearAnagramIndexing(vector<int>& arr) {
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

For each word, generate signatures of length-1 deletions (sorted multiset hash) and union groups sharing a signature.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Hash-Based Near-Anagram Indexing'?**

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

A) Hashing
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Hashing techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
