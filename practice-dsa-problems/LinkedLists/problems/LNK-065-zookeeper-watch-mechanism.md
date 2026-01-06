---
problem_id: LNK_ZOOKEEPER_WATCH_MECHANISM__8910
display_id: NTB-LNK-8910
slug: zookeeper-watch-mechanism
title: "ZooKeeper Watch Mechanism"
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
  - technical-interview-prep
  - zookeeper-watch-mechanism
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ZooKeeper Watch Mechanism

## Problem Statement

Nodes can be watched. A watch triggers when the node is modified, and then is removed.

Operations:

- `WATCH id pos`: register watch `id` on position `pos`
- `SET pos x`: set value at `pos`
- `GET pos`: output value or `-1`

For each `SET`, output the watch ids triggered in increasing order, or `0` if none.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `SET`, output triggered watch ids or `0`
- For each `GET`, output the value

## Constraints

- `1 <= n, q <= 200000`
- Watch ids are unique

## Clarifying Notes

- Watches are one-time triggers.

## Example Input

```
2
1 2
4
WATCH 5 2
SET 2 9
GET 2
SET 1 3
```

## Example Output

```
5
9
0
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<String> processZookeeperWatch(int n, int[] initialList, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processZookeeperWatch(self, n: int, initial_list: list[int], operations: list[str]) -> list[str]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> processZookeeperWatch(int n, vector<int>& initialList, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} initialList
   * @param {string[]} operations
   * @returns {string[]}
   */
  processZookeeperWatch(n, initialList, operations) {
    // Your code here
    return [];
  }
}
```
