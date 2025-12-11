---
unique_problem_id: trie_004
display_id: TRIE-004
slug: replace-words-shortest-rare-prefix
version: 1.0.0
difficulty: Medium
topic_tags:
  - Tries
  - Problem Solving
---

# Replace Words with Shortest Rare Prefix

## Problem Description

Given a dictionary of root words with rarity scores `r[root]` (lower is rarer) and a sentence, replace each word by the prefix among dictionary roots that is both a prefix of the word and has the smallest rarity; if multiple, pick the shortest; if none, leave word unchanged.

## Examples

- Input: dict roots `["cat","car"]` with rarity `{cat:1, car:2}`, sentence `"the cattle carried"`.
  - Output: `"the cat car"`

## Constraints

`1 <= dict size <= 10^5`, word length <= 30`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] replaceWordsShortestRarePrefix(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def replaceWordsShortestRarePrefix(arr: List[int]) -> List[int]:
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
    vector<int> replaceWordsShortestRarePrefix(vector<int>& arr) {
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

No hints available.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Replace Words with Shortest Rare Prefix'?**

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

A) Tries
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Tries techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
