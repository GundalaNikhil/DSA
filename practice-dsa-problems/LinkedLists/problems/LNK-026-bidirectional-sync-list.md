---
problem_id: LNK_BIDIRECTIONAL_SYNC_LIST__4877
display_id: NTB-LNK-4877
slug: bidirectional-sync-list
title: "Bidirectional Sync List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - bidirectional-sync-list
  - coding-interviews
  - data-structures
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Bidirectional Sync List

## Problem Statement

Two linked lists `A` and `B` must remain synchronized. A fixed offset `D` defines the transformation between values:

```
value_in_B = value_in_A + D
```

Operations on one list must be mirrored on the other at the same position using this rule.

Operations:

- `INS A pos x`
- `INS B pos y`
- `DEL A pos`
- `DEL B pos`
- `GET A pos` / `GET B pos`

For `INS B pos y`, the inserted value in `A` is `y - D`.

## Input Format

- First line: integers `n` and `D`
- Second line: `n` integers: initial list `A`
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output the value at the position in the requested list, or `-1` if out of range

## Constraints

- `1 <= n, q <= 200000`
- Values are 32-bit signed integers

## Clarifying Notes

- All operations are valid if the position exists in the target list at the time of operation.
- The two lists always have the same length.

## Example Input

```
3 5
1 2 3
4
GET B 2
INS A 2 10
GET B 2
DEL B 3
```

## Example Output

```
7
15
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> processSyncList(int n, int D, int[] initialA, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processSyncList(self, n: int, D: int, initial_a: list[int], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> processSyncList(int n, int D, vector<int>& initialA, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} D
   * @param {number[]} initialA
   * @param {string[]} operations
   * @returns {number[]}
   */
  processSyncList(n, D, initialA, operations) {
    // Your code here
    return [];
  }
}
```
