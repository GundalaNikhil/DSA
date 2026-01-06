---
problem_id: LNK_LINKED_LIST_REVERSIBLE_SECTIONS__8058
display_id: NTB-LNK-8058
slug: linked-list-reversible-sections
title: "Linked List with Reversible Sections"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-reversible-sections
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Reversible Sections

## Problem Statement

Each node is marked reversible (1) or immutable (0). You must process range-reversal operations that are allowed only if **all nodes in the range are reversible**.

Operations:

- `REV l r`: reverse the sublist from position `l` to `r`

Invalid operations are ignored. Output the final list and the count of invalid operations.

## Input Format

- First line: integer `n`
- Second line: `n` integers: node values
- Third line: `n` integers: flags (1 reversible, 0 immutable)
- Fourth line: integer `q`
- Next `q` lines: operations

## Output Format

- First line: invalid operation count
- Second line: final list values

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- Positions are 1-based in the current list state.

## Example Input

```
4
1 2 3 4
1 0 1 1
2
REV 1 3
REV 2 4
```

## Example Output

```
1
1 2 4 3
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    static class Result {
        int invalidCount;
        List<Integer> finalValues;
        Result(int invalidCount, List<Integer> finalValues) {
            this.invalidCount = invalidCount;
            this.finalValues = finalValues;
        }
    }

    public Result processReversibleSections(int n, int[] values, int[] flags, String[] operations) {
        // Your code here
        return null;
    }
}
```

```python
class Result:
    def __init__(self, invalid_count, final_values):
        self.invalid_count = invalid_count
        self.final_values = final_values

class Solution:
    def processReversibleSections(self, n: int, values: list[int], flags: list[int], operations: list[str]) -> Result:
        # Your code here
        return None
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct Result {
    int invalidCount;
    vector<int> finalValues;
};

class Solution {
public:
    Result processReversibleSections(int n, vector<int>& values, vector<int>& flags, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Result {
  constructor(invalidCount, finalValues) {
    this.invalidCount = invalidCount;
    this.finalValues = finalValues;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number[]} values
   * @param {number[]} flags
   * @param {string[]} operations
   * @returns {Result}
   */
  processReversibleSections(n, values, flags, operations) {
    // Your code here
    return null;
  }
}
```
