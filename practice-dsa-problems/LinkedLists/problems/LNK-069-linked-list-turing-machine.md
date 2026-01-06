---
problem_id: LNK_LINKED_LIST_TURING_MACHINE__9481
display_id: NTB-LNK-9481
slug: linked-list-turing-machine
title: "Linked List as Turing Machine"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-turing-machine
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List as Turing Machine

## Problem Statement

A linked list represents a tape of symbols `0` and `1`. A head points to a node. You are given a set of state transitions:

```
(state, symbol) -> (new_symbol, move, new_state)
```

where `move` is `L` or `R`. Simulate exactly `T` steps or stop early if no transition exists. Output the final tape and head position.

## Input Format

- First line: integers `n`, `S`, `T`
- Second line: string of length `n` (tape)
- Third line: integer `h` (head position, 1-based)
- Next line: integer `m` (number of transitions)
- Next `m` lines: `state symbol new_symbol move new_state`

## Output Format

- First line: final head position
- Second line: final tape string

## Constraints

- `1 <= n <= 200000`
- `1 <= S <= 20`
- `0 <= T <= 200000`

## Clarifying Notes

- Head cannot move beyond tape ends; if move would go out of bounds, halt.

## Example Input

```
3 2 2
010
2
2
0 1 1 R 1
1 0 1 L 0
```

## Example Output

```
2
110
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    static class TuringResult {
        int headPos;
        String tape;
        TuringResult(int headPos, String tape) {
            this.headPos = headPos;
            this.tape = tape;
        }
    }

    public TuringResult simulateTuring(int n, int S, int T, String initialTape, int h, String[] transitions) {
        // Your code here
        return null;
    }
}
```

```python
class TuringResult:
    def __init__(self, head_pos, tape):
        self.head_pos = head_pos
        self.tape = tape

class Solution:
    def simulateTuring(self, n: int, S: int, T: int, initial_tape: str, h: int, transitions: list[str]) -> TuringResult:
        # Your code here
        return None
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct TuringResult {
    int headPos;
    string tape;
};

class Solution {
public:
    TuringResult simulateTuring(int n, int S, int T, string initialTape, int h, vector<string>& transitions) {
        // Your code here
        return {};
    }
};
```

```javascript
class TuringResult {
  constructor(headPos, tape) {
    this.headPos = headPos;
    this.tape = tape;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} S
   * @param {number} T
   * @param {string} initialTape
   * @param {number} h
   * @param {string[]} transitions
   * @returns {TuringResult}
   */
  simulateTuring(n, S, T, initialTape, h, transitions) {
    // Your code here
    return null;
  }
}
```
