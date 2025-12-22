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

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public int[] cycleInfo(ListNode head) {
        // Your implementation here
        return new int[]{-1, 0, 0};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        ListNode[] nodes = new ListNode[n];
        for (int i = 0; i < n; i++) {
            cur.next = new ListNode(sc.nextInt());
            cur = cur.next;
            nodes[i] = cur;
        }
        int pos = sc.nextInt();
        if (pos >= 0 && n > 0) {
            cur.next = nodes[pos];
        }

        Solution solution = new Solution();
        int[] res = solution.cycleInfo(dummy.next);
        System.out.println(res[0] + " " + res[1] + " " + res[2]);
        sc.close();
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def cycle_info(head: ListNode):
    # Your implementation here
    return (-1, 0, 0)

def main():
    n = int(input())
    values = list(map(int, input().split())) if n > 0 else []
    pos = int(input())

    dummy = ListNode()
    cur = dummy
    nodes = []
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
        nodes.append(cur)
    if pos >= 0 and n > 0:
        cur.next = nodes[pos]

    entry, length, max_val = cycle_info(dummy.next)
    print(entry, length, max_val)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    vector<int> cycleInfo(ListNode* head) {
        // Your implementation here
        return {-1, 0, 0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    ListNode dummy(0);
    ListNode* cur = &dummy;
    vector<ListNode*> nodes;
    nodes.reserve(n);
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        cur->next = new ListNode(v);
        cur = cur->next;
        nodes.push_back(cur);
    }
    int pos;
    cin >> pos;
    if (pos >= 0 && n > 0) {
        cur->next = nodes[pos];
    }

    Solution solution;
    vector<int> res = solution.cycleInfo(dummy.next);
    cout << res[0] << " " << res[1] << " " << res[2] << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function cycleInfo(head) {
  // Your implementation here
  return [-1, 0, 0];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const dummy = new ListNode(0);
  let cur = dummy;
  const nodes = [];
  for (let i = 0; i < n; i++) {
    const node = new ListNode(parseInt(data[idx++], 10));
    cur.next = node;
    cur = cur.next;
    nodes.push(node);
  }
  const pos = parseInt(data[idx++], 10);
  if (pos >= 0 && n > 0) {
    cur.next = nodes[pos];
  }

  const res = cycleInfo(dummy.next);
  console.log(res[0] + " " + res[1] + " " + res[2]);
});
```
