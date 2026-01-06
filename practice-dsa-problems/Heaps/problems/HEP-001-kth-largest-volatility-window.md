---
problem_id: HEP_KTH_LARGEST_VOLATILITY_WINDOW__7214
display_id: NTB-HEP-7214
slug: kth-largest-volatility-window
title: "Kth Largest Element with Volatility Window"
difficulty: Medium
difficulty_score: 50
topics:
  - Heaps
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - heaps
  - kth-largest-volatility-window
  - priority-queues
  - sorting
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Kth Largest Element with Volatility Window

## Problem Statement

You are given a stream of `n` integers `a1..an`. For every index `i` (1-based), define the active window as the longest suffix ending at `i` that satisfies both rules:

1. Its length is at most `W`.
2. For every consecutive pair inside the window, the volatility condition holds:
   `|a_j - a_{j-1}| <= T`.

Equivalently, let `last_bad` be the largest index `j` (1 < j <= i) such that `|a_j - a_{j-1}| > T`. Then the active window for `i` is:

```
L = max(1, i - W + 1, last_bad + 1)
window = [L, i]
```

For each `i`, output the `K`-th largest value within its active window. If the window size is less than `K`, output `-1` for that index.

## Input Format

- First line: integers `n`, `K`, `W`, `T`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n` integers separated by spaces: the answer for each index `i` from `1` to `n`

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- `1 <= W <= n`
- `0 <= T <= 10^9`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- The active window is always a suffix ending at `i` and is contracted deterministically using `last_bad`.
- If `i = 1`, then `last_bad` is undefined and the window is `[1, 1]`.
- The `K`-th largest is defined by sorting the window values in descending order.

## Example Input

```
5 2 3 2
4 5 7 6 3
```

## Example Output

```
-1 4 5 6 -1
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long[] findKthLargest(int n, int K, int W, int T, int[] a) {
        // Your code here
        return new long[0];
    }
}
```

```python
import heapq

class Solution:
    def findKthLargest(self, n: int, K: int, W: int, T: int, a: list[int]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<long long> findKthLargest(int n, int K, int W, int T, vector<int>& a) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} K
   * @param {number} W
   * @param {number} T
   * @param {number[]} a
   * @returns {number[]}
   */
  findKthLargest(n, K, W, T, a) {
    // Your code here
    return [];
  }
}
```
