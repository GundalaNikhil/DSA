---
problem_id: ARR_ARRAY_STATE_MACHINE_SIMULATION__7643
display_id: NTB-ARR-7643
slug: array-state-machine-simulation
title: "Array State Machine Simulation"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - array-state-machine-simulation
  - arrays
  - coding-interviews
  - data-structures
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Array State Machine Simulation

## Problem Statement

You are given a deterministic state machine with `S` states labeled `0..S-1` and a base `B`. A transition table `T` is provided where `T[s][b]` gives the next state from state `s` when the input bucket is `b`.

Given an array `a1..an`, process it left to right. For each element:

```
b = ((a_i % B) + B) % B
state = T[state][b]
```

You start in state `0`. Count how many times each state is visited (including the initial state before any elements). Output the visit counts for states `0..S-1`.

## Input Format

- First line: integers `n`, `S`, and `B`
- Second line: `n` integers `a1 a2 ... an`
- Next `S` lines: `B` integers each, the transition table `T`

## Output Format

- `S` integers: visit counts for states `0..S-1`

## Constraints

- `1 <= n <= 200000`
- `1 <= S <= 2000`
- `1 <= B <= 2000`
- `-10^9 <= a_i <= 10^9`
- `0 <= T[s][b] <= S-1`

## Clarifying Notes

- The initial state `0` counts as one visit before processing the array.
- The process is fully deterministic given the inputs.

## Example Input

```
5 3 2
1 2 3 4 5
1 2
2 0
0 1
```

## Example Output

```
2 2 2
```

## Solution Stub

### Java

```java
class Solution {
    public int[] simulateStateMachine(int n, int s, int b, int[] a, int[][] transitions) {
        // Implement here
        return new int[0];
    }
}
```

### Python

```python
class Solution:
    def simulateStateMachine(self, n: int, s: int, base: int, a: list[int], transitions: list[list[int]]) -> list[int]:
        # Implement here
        return []
```

### C++

```cpp
class Solution {
public:
    vector<int> simulateStateMachine(int n, int s, int b, vector<int>& a, vector<vector<int>>& transitions) {
        // Implement here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} s
   * @param {number} b
   * @param {number[]} a
   * @param {number[][]} transitions
   * @return {number[]}
   */
  simulateStateMachine(n, s, b, a, transitions) {
    // Implement here
    return [];
  }
}
```
