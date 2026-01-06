---
problem_id: DP_PACKET_SCHEDULING__6866
display_id: NTB-DP-6866
slug: packet-scheduling
title: "Network Packet Scheduling DP"
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
  - packet-scheduling
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Network Packet Scheduling DP

## Problem Statement

You have `n` packets, each with deadline `d_i` and value `v_i`. Each packet takes 1 time unit and must be scheduled before or at its deadline. At most one packet can be sent per time unit.

Maximize total value.

## Input Format

- First line: integer `n`
- Next `n` lines: `d_i v_i`

## Output Format

- Single integer: maximum total value

## Constraints

- `1 <= n <= 2000`
- `1 <= d_i <= 2000`
- `0 <= v_i <= 10^9`

## Clarifying Notes

- This is a DP over time and packets.

## Example Input

```
3
1 5
2 6
2 4
```

## Example Output

```
11
```

## Solution Stub

```java
public class Solution {
    public long maxTotalValue(int n, int[][] packets) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def maxTotalValue(self, n: int, packets: list[list[int]]) -> int:
        # Your code here
        return 0
```

```cpp
class Solution {
public:
    long long maxTotalValue(int n, vector<vector<int>>& packets) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  maxTotalValue(n, packets) {
    // Your code here
    return 0;
  }
}
```
