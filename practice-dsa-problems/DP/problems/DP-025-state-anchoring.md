---
problem_id: DP_STATE_ANCHORING__4387
display_id: NTB-DP-4387
slug: state-anchoring
title: "DP with State Anchoring"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - state-anchoring
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with State Anchoring

## Problem Statement

You have `n` steps and `s` states. Some states are anchors. You must not go more than `L` steps without visiting an anchor. Each step in state `j` yields reward `R[j]`.

Maximize total reward over `n` steps.

## Input Format

- First line: integers `n`, `s`, `L`
- Second line: `s` integers: rewards `R[1..s]`
- Third line: integer `a` (number of anchors)
- Fourth line: `a` integers: anchor state ids

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `1 <= s <= 20`
- `1 <= L <= n`

## Clarifying Notes

- State can change freely each step.
- Counter resets to 0 when an anchor is visited.

## Example Input

```
3 3 2
5 2 1
1
1
```

## Example Output

```
15
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int s, int l, int[] r, int[] anchors) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, s: int, l: int, r: list[int], anchors: list[int]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int s, int l, vector<int>& r, vector<int>& anchors) {
        // Implement here
        return -1;
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} s
   * @param {number} l
   * @param {number[]} r
   * @param {number[]} anchors
   * @return {number}
   */
  maxReward(n, s, l, r, anchors) {
    // Implement here
    return -1;
  }
}
```
