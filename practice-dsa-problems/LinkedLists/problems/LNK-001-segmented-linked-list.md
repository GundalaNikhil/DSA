---
problem_id: LNK_SEGMENTED_LINKED_LIST__8030
display_id: NTB-LNK-8030
slug: segmented-linked-list
title: "Segmented Linked List"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linkedlists
  - memory-management
  - pointers
  - segmented-linked-list
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Segmented Linked List

## Problem Statement

You are given a singly linked list of `n` nodes. Each node belongs to a fixed segment `seg_id` (1-based). Nodes of the same segment are contiguous in the list. You must process operations that modify the list, but **no operation may move a node across a segment boundary**.

Operations:

- `MOVE u v`: move node `u` to immediately after node `v`.
- `DEL u`: delete node `u`.
- `INS v x s`: insert a new node with value `x` and segment `s` immediately after node `v`.
- `PRINT s`: print values of all nodes in segment `s` in order.

An operation is **invalid** if it would cause any node to leave its segment or enter a different segment. Invalid operations are ignored.

## Input Format

- First line: integer `n`
- Second line: `n` integers: node values in list order
- Third line: `n` integers: segment ids in list order
- Fourth line: integer `q`
- Next `q` lines: operations as described

## Output Format

- For each `PRINT` operation, output the segment values on one line separated by spaces (empty line if segment has no nodes)

## Constraints

- `1 <= n <= 200000`
- `1 <= seg_id <= n`
- `1 <= q <= 200000`
- Total number of nodes after all inserts <= 300000
- Values are 32-bit signed integers

## Clarifying Notes

- Segment boundaries are defined by `seg_id` and cannot change.
- `MOVE` is valid only if `u` and `v` are in the same segment.
- `INS` is valid only if `s` equals the segment id of node `v`.

## Example Input

```
5
1 2 3 4 5
1 1 2 2 2
4
MOVE 3 4
INS 2 9 1
PRINT 1
PRINT 2
```

## Example Output

```
1 2 9
3 4 5
```

## Solution Stub

### Java

```java
class Solution {
    public List<String> processSegmentedList(int n, int[] values, int[] segments, String[] operations) {
        // Implement here
        return new ArrayList<>();
    }
}
```

### Python

```python
def solve(n, values, segments, operations):
    # Implement here
    return []
```

### C++

```cpp
class Solution {
public:
    vector<string> processSegmentedList(int n, vector<int>& values, vector<int>& segments, vector<string>& operations) {
        // Implement here
        return {};
    }
};
```

### JavaScript

```javascript
function solve(n, values, segments, operations) {
  // Implement here
  return [];
}
```
