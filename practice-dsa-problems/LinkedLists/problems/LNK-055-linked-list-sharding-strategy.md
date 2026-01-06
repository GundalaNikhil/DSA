---
problem_id: LNK_LINKED_LIST_SHARDING_STRATEGY__3755
display_id: NTB-LNK-3755
slug: linked-list-sharding-strategy
title: "Linked List with Sharding Strategy"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-sharding-strategy
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Sharding Strategy

## Problem Statement

The list is partitioned into shards (contiguous ranges). Each shard has a maximum size `U` and minimum size `L`. After each insertion or deletion, rebalance:

- If a shard size exceeds `U`, split it into two shards as evenly as possible.
- If a shard size falls below `L`, merge it with the next shard (if any).

Report the total number of splits and merges, then output final shard sizes.

## Input Format

- First line: integers `n`, `L`, `U`
- Second line: `n` integers: initial list values
- Third line: integer `q`
- Next `q` lines: `INS pos x` or `DEL pos`

## Output Format

- First line: two integers `splits merges`
- Second line: final shard sizes in order

## Constraints

- `1 <= n, q <= 200000`
- `1 <= L <= U <= 200000`

## Clarifying Notes

- If there is no next shard during merge, do nothing.

## Example Input

```
5 2 4
1 2 3 4 5
2
INS 3 9
DEL 1
```

## Example Output

```
1 0
2 2 2
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    static class ShardResult {
        int splits, merges;
        List<Integer> shardSizes;
        ShardResult(int splits, int merges, List<Integer> shardSizes) {
            this.splits = splits;
            this.merges = merges;
            this.shardSizes = shardSizes;
        }
    }

    public ShardResult processSharding(int n, int L, int U, int[] initialList, String[] operations) {
        // Your code here
        return null;
    }
}
```

```python
class ShardResult:
    def __init__(self, splits, merges, shard_sizes):
        self.splits = splits
        self.merges = merges
        self.shard_sizes = shard_sizes

class Solution:
    def processSharding(self, n: int, L: int, U: int, initial_list: list[int], operations: list[str]) -> ShardResult:
        # Your code here
        return None
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct ShardResult {
    int splits, merges;
    vector<int> shardSizes;
};

class Solution {
public:
    ShardResult processSharding(int n, int L, int U, vector<int>& initialList, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class ShardResult {
  constructor(splits, merges, shardSizes) {
    this.splits = splits;
    this.merges = merges;
    this.shardSizes = shardSizes;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number} L
   * @param {number} U
   * @param {number[]} initialList
   * @param {string[]} operations
   * @returns {ShardResult}
   */
  processSharding(n, L, U, initialList, operations) {
    // Your code here
    return null;
  }
}
```
