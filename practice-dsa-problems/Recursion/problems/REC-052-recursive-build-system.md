---
problem_id: REC_RECURSIVE_BUILD_SYSTEM__4761
display_id: NTB-REC-4761
slug: recursive-build-system
title: "Recursive Build System"
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
  - recursive-build-system
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Build System

## Problem Statement

You are given a dependency graph of build targets. Each target has a build time cost and a last built timestamp. Source files are modeled as targets with no dependencies.

A target must be rebuilt if any dependency's current timestamp is greater than its own timestamp. When rebuilt, its new timestamp becomes `max(dep timestamps) + 1` and its cost is added to the total build time.

Compute the total build time required to update the target `S` and return its final timestamp.

## Input Format

- First line: integers `n`, `m`, and `S`
- Next `n` lines: `cost time`
- Next `m` lines: directed edges `u v` meaning `u` depends on `v`

## Output Format

- Two integers: `total_cost` and `final_timestamp` for `S`

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `0 <= cost <= 10^9`
- `0 <= time <= 10^9`

## Clarifying Notes

- Dependencies are evaluated recursively; each target is considered once.
- Cycles do not occur in the dependency graph.

## Example Input

```
3 2 1
5 10
3 12
2 9
1 2
1 3
```

## Example Output

```
5 13
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class BuildResult {
        public long totalCost;
        public long finalTimestamp;
        public BuildResult(long totalCost, long finalTimestamp) {
            this.totalCost = totalCost;
            this.finalTimestamp = finalTimestamp;
        }
    }

    public BuildResult computeBuildTime(int n, int m, int S, long[][] targetInfo, int[][] edges) {
        // Your code here
        return null;
    }
}
```

```python
class Solution:
    def computeBuildTime(self, n: int, m: int, S: int, target_info: list[list[int]], edges: list[list[int]]) -> tuple[int, int]:
        # Your code here
        return 0, 0
```

```cpp
#include <vector>

using namespace std;

struct BuildResult {
    long long totalCost;
    long long finalTimestamp;
};

class Solution {
public:
    BuildResult computeBuildTime(int n, int m, int S, vector<vector<long long>>& targetInfo, vector<vector<int>>& edges) {
        // Your code here
        return {0, 0};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} S
   * @param {number[][]} targetInfo
   * @param {number[][]} edges
   * @returns {{totalCost: number, finalTimestamp: number}}
   */
  computeBuildTime(n, m, S, targetInfo, edges) {
    // Your code here
    return { totalCost: 0, finalTimestamp: 0 };
  }
}
```
