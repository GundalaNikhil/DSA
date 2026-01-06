---
problem_id: REC_RECURSIVE_STRATEGY_SYNTHESIS__2947
display_id: NTB-REC-2947
slug: recursive-strategy-synthesis
title: "Recursive Strategy Synthesis"
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
  - recursive-strategy-synthesis
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Strategy Synthesis

## Problem Statement

You are given a game tree. Each node is controlled by Player A or Player B, and leaves are labeled as winning (`1`) or losing (`0`) for Player A.

Define recursive outcomes:

- At a Player A node, A may choose any child. The node is winning if any child is winning.
- At a Player B node, B chooses a child. The node is winning only if all children are winning.

If the root is winning, output one winning strategy for Player A as a sequence of chosen child indices (1-based) along the path taken by A at each of its turns. If multiple strategies exist, choose the lexicographically smallest sequence.

If the root is losing, output `LOSE`.

## Input Format

- First line: integer `n`
- Next `n` lines: `type value parent`
  - `type` is `A`, `B`, or `L` (leaf)
  - For leaves, `value` is `0` or `1`; otherwise `value` is ignored

## Output Format

- If losing: print `LOSE`
- If winning: print `WIN` on the first line, and the strategy sequence on the second line (space-separated indices, or empty if no A moves)

## Constraints

- `1 <= n <= 200000`
- Each internal node has at least one child

## Clarifying Notes

- Child indices are based on the order of input.
- The strategy sequence only records choices at Player A nodes.

## Example Input

```
5
A 0 0
B 0 1
L 1 2
L 0 2
L 1 1
```

## Example Output

```
WIN
2
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class Result {
        public String status;
        public List<Integer> strategy;
        public Result(String status, List<Integer> strategy) {
            this.status = status;
            this.strategy = strategy;
        }
    }

    public Result findWinningStrategy(int n, List<String[]> nodeInfo) {
        // Your code here
        return null;
    }
}
```

```python
class Solution:
    def findWinningStrategy(self, n: int, node_info: list[list[str]]) -> tuple[str, list[int]]:
        # Your code here
        return "", []
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct Result {
    string status;
    vector<int> strategy;
};

class Solution {
public:
    Result findWinningStrategy(int n, vector<vector<string>>& nodeInfo) {
        // Your code here
        return {"", {}};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {string[][]} nodeInfo
   * @returns {{status: string, strategy: number[]}}
   */
  findWinningStrategy(n, nodeInfo) {
    // Your code here
    return { status: "", strategy: [] };
  }
}
```
