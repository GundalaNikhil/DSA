---
problem_id: DP_BRANCH_PREDICTION__3670
display_id: NTB-DP-3670
slug: branch-prediction
title: "Branch Prediction DP"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - branch-prediction
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Branch Prediction DP

## Problem Statement

You are given a sequence of branch outcomes `0/1` of length `n`. You may use one of `k` prediction strategies. Strategy `i` has a state machine with `s_i` states, a prediction for each state, and a deterministic next-state function based on the actual outcome.

You may switch strategies at any time with cost `C`. A misprediction costs 1.

Minimize total cost (mispredictions + switch costs).

## Input Format

- First line: integers `n`, `k`, `C`
- Second line: string of length `n` (branch outcomes)
- For each strategy `i`:
  - Line: integer `s_i`
  - Line: `s_i` integers: prediction for each state (0 or 1)
  - Next `s_i` lines: two integers: next state for outcome 0 and outcome 1

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= n <= 2000`
- `1 <= k <= 5`
- `1 <= s_i <= 10`
- `0 <= C <= 10^6`

## Clarifying Notes

- Each strategy starts in state 0 when first used.

## Example Input

```
3 1 0
010
2
0 1
0 1
1 0
```

## Example Output

```
1
```

## Solution Stub

```java
public class Solution {
    static class Strategy {
        int s;
        int[] predictions;
        int[][] transitions;
    }

    public long minPredictionCost(int n, int k, int C, String outcomes, Strategy[] strategies) {
        // Your code here
        return 0;
    }
}
```

```python
class Strategy:
    def __init__(self, s, predictions, transitions):
        self.s = s
        self.predictions = predictions
        self.transitions = transitions

class Solution:
    def minPredictionCost(self, n: int, k: int, C: int, outcomes: str, strategies: list[Strategy]) -> int:
        # Your code here
        return 0
```

```cpp
struct Strategy {
    int s;
    vector<int> predictions;
    vector<vector<int>> transitions;
};

class Solution {
public:
    long long minPredictionCost(int n, int k, int C, string outcomes, vector<Strategy>& strategies) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} k
   * @param {number} C
   * @param {string} outcomes
   * @param {Array<{s: number, predictions: number[], transitions: number[][]}>} strategies
   */
  minPredictionCost(n, k, C, outcomes, strategies) {
    // Your code here
    return 0;
  }
}
```
