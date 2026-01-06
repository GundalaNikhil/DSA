---
problem_id: MAT_MATRIX_EVENT_REPLAY__9358
display_id: NTB-MAT-9358
slug: matrix-event-replay
title: "Matrix Event Replay"
difficulty: Medium
difficulty_score: 50
topics:
  - Matrix
tags:
  - 2d-arrays
  - algorithms
  - coding-interviews
  - data-structures
  - grids
  - matrix
  - matrix-event-replay
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Matrix Event Replay

## Problem Statement

You are given an initial matrix, a final matrix, and an event log. Replay the events and verify consistency.

Operations:

- `SET r c v`
- `ADD r c v`
- `SWAPROW r1 r2`
- `SWAPCOL c1 c2`

If any operation is out of bounds, it is invalid.

Output:

- The index of the first invalid operation, or
- `q + 1` if all operations are valid but the final matrix does not match, or
- `0` if the replay matches the final matrix.

## Input Format

- First line: integers `n`, `m`, `q`
- Next `n` lines: `m` integers (initial matrix)
- Next `n` lines: `m` integers (target final matrix)
- Next `q` lines: operations

## Output Format

- Single integer as described

## Constraints

- `1 <= n, m <= 200`
- `1 <= q <= 200000`
- `-10^9 <= values <= 10^9`

## Clarifying Notes

- Indices are 1-based.

## Example Input

```
2 2 2
1 2
3 4
1 2
4 3
SWAPROW 1 2
SWAPCOL 1 2
```

## Example Output

```
0
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public int verifyReplay(int n, int m, int q, int[][] initial, int[][] target, List<String> operations) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def verifyReplay(self, n: int, m: int, q: int, initial: list[list[int]], target: list[list[int]], operations: list[str]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int verifyReplay(int n, int m, int q, vector<vector<int>>& initial, vector<vector<int>>& target, vector<string>& operations) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} q
   * @param {number[][]} initial
   * @param {number[][]} target
   * @param {string[]} operations
   * @returns {number}
   */
  verifyReplay(n, m, q, initial, target, operations) {
    // Your code here
    return 0;
  }
}
```
