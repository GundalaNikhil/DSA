---
problem_id: REC_SELF_MODIFYING_RECURSION__6313
display_id: NTB-REC-6313
slug: self-modifying-recursion
title: "Self-Modifying Recursion"
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
  - self-modifying-recursion
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Self-Modifying Recursion

## Problem Statement

You are given a set of symbols. Each symbol has two possible expansion lists and a toggle flag. A recursive evaluation starts from symbol `S` with mode `0` and depth `D`.

Define `Eval(symbol, depth, mode)` as follows:

- If `depth == 0` or the chosen expansion list is empty, return `weight[symbol]`.
- Otherwise choose the expansion list based on `mode` (`list0` if mode=0, `list1` if mode=1).
- Let `next_mode = mode XOR toggle[symbol]`.
- Return the sum of `Eval(child, depth-1, next_mode)` over all children in the chosen list.

Compute `Eval(S, D, 0)` modulo `1,000,000,007`.

## Input Format

- First line: integers `n` and `D`
- Second line: integer `S` (start symbol, 1-indexed)
- Next `n` lines: `weight toggle c0 list0... c1 list1...`
  - `weight`: integer value for this symbol
  - `toggle`: `0` or `1`
  - `c0`: number of children in `list0`, followed by `c0` integers
  - `c1`: number of children in `list1`, followed by `c1` integers

## Output Format

- Single integer: value of `Eval(S, D, 0)` modulo `1,000,000,007`

## Constraints

- `1 <= n <= 200000`
- `0 <= D <= 60`
- `1 <= S <= n`
- `0 <= weight <= 10^9`
- `0 <= c0, c1 <= 3`
- Children are in the range `[1, n]`

## Clarifying Notes

- The mode changes for the entire subtree of a symbol, not just a single child.
- The chosen expansion list is determined before the mode is toggled.
- The recursion is self-modifying because the rule selection depends on prior toggles along the path.

## Example Input

```
3 2
1
5 1 2 2 3 1 2
2 0 0 1 3
4 1 0 0
```

## Example Output

```
10
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class SymbolInfo {
        public long weight;
        public int toggle;
        public List<Integer> list0;
        public List<Integer> list1;
        public SymbolInfo(long weight, int toggle, List<Integer> list0, List<Integer> list1) {
            this.weight = weight;
            this.toggle = toggle;
            this.list0 = list0;
            this.list1 = list1;
        }
    }

    public long evaluateSelfModifyingRecursion(int n, int D, int S, List<SymbolInfo> symbols) {
        // Your code here
        return 0;
    }
}
```

```python
class SymbolInfo:
    def __init__(self, weight: int, toggle: int, list0: list[int], list1: list[int]):
        self.weight = weight
        self.toggle = toggle
        self.list0 = list0
        self.list1 = list1

class Solution:
    def evaluateSelfModifyingRecursion(self, n: int, D: int, S: int, symbols: list[SymbolInfo]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>

using namespace std;

struct SymbolInfo {
    long long weight;
    int toggle;
    vector<int> list0;
    vector<int> list1;
};

class Solution {
public:
    int evaluateSelfModifyingRecursion(int n, int D, int S, vector<SymbolInfo>& symbols) {
        // Your code here
        return 0;
    }
};
```

```javascript
class SymbolInfo {
  constructor(weight, toggle, list0, list1) {
    this.weight = weight;
    this.toggle = toggle;
    this.list0 = list0;
    this.list1 = list1;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} D
   * @param {number} S
   * @param {SymbolInfo[]} symbols
   * @returns {number}
   */
  evaluateSelfModifyingRecursion(n, D, S, symbols) {
    // Your code here
    return 0;
  }
}
```
