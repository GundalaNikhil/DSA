---
problem_id: REC_RECURSIVE_CODE_GENERATION__7635
display_id: NTB-REC-7635
slug: recursive-code-generation
title: "Recursive Code Generation"
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
  - recursive-code-generation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursive Code Generation

## Problem Statement

You are given a set of macros that generate a sequence of instructions by recursive expansion. Each instruction updates an accumulator `A`.

Instructions are:

- `ADD x`: `A = A + x`
- `MUL x`: `A = A * x`
- `CALL j`: expand macro `j` recursively

The expansion is depth-limited. If `depth == 0`, any `CALL` is skipped (no effect). Expansion starts from macro `1` with depth `D` and initial accumulator `A0`.

Compute the final accumulator value modulo `1,000,000,007`.

## Input Format

- First line: integers `m` and `D`
- Second line: integer `A0`
- Next `m` lines:
  - `len` followed by `len` tokens
  - Each token is one of:
    - `ADD x`
    - `MUL x`
    - `CALL j`

## Output Format

- Single integer: final accumulator value modulo `1,000,000,007`

## Constraints

- `1 <= m <= 200000`
- `0 <= D <= 50`
- `0 <= A0 <= 10^9`
- Total number of tokens across all macros <= 300000
- `0 <= x <= 10^9`

## Clarifying Notes

- Macro expansion order is left to right within each macro.
- Depth decreases only when entering a `CALL`.
- This problem requires composing transformations without fully expanding the code.

## Example Input

```
2 2
3
3 ADD 2 CALL 2 MUL 2
1 ADD 5
```

## Example Output

```
17
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long evaluateCodeGeneration(int m, int D, int A0, List<String> macros) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def evaluateCodeGeneration(self, m: int, D: int, A0: int, macros: list[str]) -> int:
        # Your code here
        return 0
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int evaluateCodeGeneration(int m, int D, int A0, vector<string>& macros) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} m
   * @param {number} D
   * @param {number} A0
   * @param {string[]} macros
   * @returns {number}
   */
  evaluateCodeGeneration(m, D, A0, macros) {
    // Your code here
    return 0;
  }
}
```
