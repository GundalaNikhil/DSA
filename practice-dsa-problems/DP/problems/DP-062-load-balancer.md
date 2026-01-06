---
problem_id: DP_LOAD_BALANCER__8619
display_id: NTB-DP-8619
slug: load-balancer
title: "Load Balancer DP"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - load-balancer
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Load Balancer DP

## Problem Statement

You have `s` servers and `n` requests in order. Request `i` has size `w_i`. Server `j` has capacity `cap_j` and latency cost `lat_j`. If a request assigned to server `j` causes total assigned load to exceed `cap_j`, you pay an overload penalty `P` for that request.

Minimize total latency plus overload penalties.

## Input Format

- First line: integers `n`, `s`, `P`
- Second line: `n` integers: request sizes
- Third line: `s` integers: capacities
- Fourth line: `s` integers: latencies

## Output Format

- Single integer: minimum total cost

## Constraints

- `1 <= n <= 60`
- `1 <= s <= 4`
- `0 <= P <= 10^6`
- `0 <= sizes, capacities, latencies <= 50`

## Clarifying Notes

- Each request must be assigned to exactly one server.
- Total load per server is cumulative over all requests.

## Example Input

```
3 2 5
2 3 4
4 5
1 2
```

## Example Output

```
9
```

## Solution Stub

```java
public class Solution {
    public int minTotalCost(int n, int s, int P, int[] sizes, int[] capacities, int[] latencies) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def minTotalCost(self, n: int, s: int, P: int, sizes: list[int], capacities: list[int], latencies: list[int]) -> int:
        # Your code here
        return 0
```

```cpp
class Solution {
public:
    int minTotalCost(int n, int s, int P, vector<int>& sizes, vector<int>& capacities, vector<int>& latencies) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  minTotalCost(n, s, P, sizes, capacities, latencies) {
    // Your code here
    return 0;
  }
}
```
