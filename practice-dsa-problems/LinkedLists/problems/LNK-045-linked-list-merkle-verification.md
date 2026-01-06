---
problem_id: LNK_LINKED_LIST_MERKLE_VERIFICATION__9668
display_id: NTB-LNK-9668
slug: linked-list-merkle-verification
title: "Linked List with Merkle Verification"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-merkle-verification
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Merkle Verification

## Problem Statement

The list is divided into segments of equal size `K` (last segment may be smaller). For each segment, you are given a claimed hash value. The hash is defined as:

```
hash = (sum of values in segment) mod 1,000,000,007
```

Verify each segment and report the first invalid segment index, or `0` if all are valid.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers: list values
- Third line: `ceil(n / K)` integers: claimed hashes

## Output Format

- Single integer: index of first invalid segment (1-based), or `0`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- Values are 32-bit signed integers

## Clarifying Notes

- Use modulo `1,000,000,007` with non-negative result.

## Example Input

```
5 2
1 2 3 4 5
3 7 5
```

## Example Output

```
0
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public int verifyMerkle(int n, int K, int[] values, long[] claimedHashes) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def verifyMerkle(self, n: int, K: int, values: list[int], claimed_hashes: list[int]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int verifyMerkle(int n, int K, vector<int>& values, vector<long long>& claimedHashes) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} K
   * @param {number[]} values
   * @param {number[]} claimedHashes
   * @returns {number}
   */
  verifyMerkle(n, K, values, claimedHashes) {
    // Your code here
    return 0;
  }
}
```
