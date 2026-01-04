---
problem_id: LNK_LAB_LOOP_DETECTOR_ENTRY_LENGTH__8412
display_id: LNK-006
slug: lab-loop-detector-entry-length
title: "Lab Loop Detector with Entry Index and Cycle Length"
difficulty: Medium
difficulty_score: 56
topics:
  - Linked List
  - Cycle Detection
  - Two Pointers
tags:
  - linked-list
  - cycle
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-006: Lab Loop Detector with Entry Index and Cycle Length

## Problem Statement

Detect whether a singly linked list has a cycle. If a cycle exists, return:

- `entry_index`: 0-based index of the cycle entry node
- `cycle_length`: number of nodes in the cycle
- `max_value_in_cycle`: maximum node value within the cycle

If no cycle exists, return `-1 0 0`.

![Problem Illustration](../images/LNK-006/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `pos` (0-based index where the tail connects, or `-1` for no cycle)

## Output Format

- Three integers: `entry_index cycle_length max_value_in_cycle`

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integer
- `-1 <= pos < n`

## Example

**Input:**

```
4
1 2 3 4
1
```

**Output:**

```
1 3 4
```

**Explanation:**

The tail connects to index 1 (value 2). The cycle is 2 -> 3 -> 4 -> back to 2.

- entry_index = 1
- cycle_length = 3
- max_value_in_cycle = 4

![Example Visualization](../images/LNK-006/example-1.png)

## Notes

- Use Floyd's cycle detection to find a meeting point
- After detection, find the entry index by moving pointers
- Traverse the cycle once to compute length and maximum value
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Cycle Detection, Floyd's Algorithm

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Result {
    int entryIndex;
    int cycleLength;
    int maxValueInCycle;
    Result(int entryIndex, int cycleLength, int maxValueInCycle) {
        this.entryIndex = entryIndex;
        this.cycleLength = cycleLength;
        this.maxValueInCycle = maxValueInCycle;
    }
}

class Solution {
    public Result detectCycle(ListNode head) {
        // Implement here
        return new Result(-1, 0, 0);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        ListNode[] nodes = new ListNode[n];
        if (n > 0) {
            String[] vals = br.readLine().trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                nodes[i] = new ListNode(Integer.parseInt(vals[i]));
                if (i > 0) nodes[i-1].next = nodes[i];
            }
        } else {
            br.readLine();
        }

        int pos = Integer.parseInt(br.readLine().trim());
        if (pos != -1 && n > 0) {
            nodes[n-1].next = nodes[pos];
        }

        Solution sol = new Solution();
        Result res = sol.detectCycle(n > 0 ? nodes[0] : null);
        System.out.println(res.entryIndex + " " + res.cycleLength + " " + res.maxValueInCycle);
    }
}
```

### Python

```python
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detect_cycle(self, head):
        # Implement here
        return -1, 0, 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    nodes = []
    for i in range(1, n + 1):
        nodes.append(ListNode(int(input_data[i])))

    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]

    pos = int(input_data[n + 1])
    if pos != -1 and n > 0:
        nodes[n - 1].next = nodes[pos]

    sol = Solution()
    entry_index, cycle_length, max_val = sol.detect_cycle(nodes[0] if n > 0 else None)
    print(f"{entry_index} {cycle_length} {max_val}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

struct Result {
    int entryIndex;
    int cycleLength;
    int maxValueInCycle;
};

class Solution {
public:
    Result detectCycle(ListNode* head) {
        // Implement here
        return {-1, 0, 0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<ListNode*> nodes(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        nodes[i] = new ListNode(val);
        if (i > 0) nodes[i-1]->next = nodes[i];
    }

    int pos;
    cin >> pos;
    if (pos != -1 && n > 0) {
        nodes[n-1]->next = nodes[pos];
    }

    Solution sol;
    Result res = sol.detectCycle(n > 0 ? nodes[0] : NULL);
    cout << res.entryIndex << " " << res.cycleLength << " " << res.maxValueInCycle << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class ListNode {
  constructor(x) {
    this.val = x;
    this.next = null;
  }
}

class Solution {
  detectCycle(head) {
    // Implement here
    return { entryIndex: -1, cycleLength: 0, maxValueInCycle: 0 };
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const nodes = [];
  for (let i = 0; i < n; i++) {
    nodes.push(new ListNode(parseInt(input[idx++])));
    if (i > 0) nodes[i - 1].next = nodes[i];
  }

  const pos = parseInt(input[idx++]);
  if (pos !== -1 && n > 0) {
    nodes[n - 1].next = nodes[pos];
  }

  const sol = new Solution();
  const res = sol.detectCycle(n > 0 ? nodes[0] : null);
  console.log(`${res.entryIndex} ${res.cycleLength} ${res.maxValueInCycle}`);
}

solve();
```
