---
problem_id: ARR_CIRCULAR_ARRAY_ENERGY_DRAIN__7366
display_id: NTB-ARR-7366
slug: circular-array-energy-drain
title: "Circular Array Energy Drain"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - circular-array-energy-drain
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

# Circular Array Energy Drain

## Problem Statement

You are given two arrays `fuel1..fueln` and `drain1..drainn` representing a circular route with `n` stations. Starting at some station `i` with energy 0:

- You gain `fuel_i` energy at station `i`.
- To move from station `i` to `i+1` (circular), you must spend `drain_i + B` energy, where `B` is a fixed base drain.

Find the smallest starting index (1-based) from which you can complete exactly one full loop and return to the start without energy dropping below 0. If impossible, output `-1`.

## Input Format

- First line: integers `n` and `B`
- Second line: `n` integers `fuel1 fuel2 ... fueln`
- Third line: `n` integers `drain1 drain2 ... drainn`

## Output Format

- Single integer: smallest feasible starting index, or `-1`

## Constraints

- `1 <= n <= 200000`
- `0 <= fuel_i, drain_i, B <= 10^9`

## Clarifying Notes

- The route is circular: station `n` connects to station `1`.
- If multiple starts are feasible, output the smallest index.

## Example Input

```
4 1
4 1 2 3
2 1 1 2
```

## Example Output

```
1
```

## Solution Stub

### Java

```java
class Solution {
    public int smallestStartStation(int n, int b, int[] fuel, int[] drain) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def smallestStartStation(self, n: int, b: int, fuel: list[int], drain: list[int]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    int smallestStartStation(int n, int b, vector<int>& fuel, vector<int>& drain) {
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
   * @param {number} b
   * @param {number[]} fuel
   * @param {number[]} drain
   * @return {number}
   */
  smallestStartStation(n, b, fuel, drain) {
    // Implement here
    return -1;
  }
}
```
