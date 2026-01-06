---
problem_id: REC_RECURSIVE_LAYER_VALIDATION__7230
display_id: NTB-REC-7230
slug: recursive-layer-validation
title: "Recursive Layer Validation"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursive-layer-validation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Layer Validation

## Problem Statement

You are given a rooted tree and a list of layer rules. At depth `d` (root at depth 0), the sum of node values at that depth must satisfy:

```
sum_d % K_d == 0
```

All depth rules must hold. Determine if the tree is valid.

## Input Format

- First line: integers `n` and `H`
- Next `n` lines: `value parent` (parent is 0 for root)
- Next line: `H+1` integers `K_0..K_H`

`H` is the maximum depth to validate; depths greater than `H` are ignored.

## Output Format

- `YES` if all rules pass, otherwise `NO`

## Constraints

- `1 <= n <= 200000`
- `0 <= H <= 200000`
- `1 <= K_d <= 10^9`

## Clarifying Notes

- If a depth `d` has no nodes, its sum is 0.

## Example Input

```
4 1
3 0
2 1
1 1
4 2
3 5
```

## Example Output

```
YES
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public String validateLayers(int n, int H, int[][] nodes, long[] K) {
        // Your code here
        return "";
    }
}
```

```python
class Solution:
    def validateLayers(self, n: int, H: int, nodes: list[list[int]], K: list[int]) -> str:
        # Your code here
        return ""
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string validateLayers(int n, int H, vector<vector<int>>& nodes, vector<long long>& K) {
        // Your code here
        return "";
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} H
   * @param {number[][]} nodes
   * @param {number[]} K
   * @returns {string}
   */
  validateLayers(n, H, nodes, K) {
    // Your code here
    return "";
  }
}
```
