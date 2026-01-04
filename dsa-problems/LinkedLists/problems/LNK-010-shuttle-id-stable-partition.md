---
problem_id: LNK_SHUTTLE_ID_STABLE_PARTITION__7184
display_id: LNK-010
slug: shuttle-id-stable-partition
title: "Shuttle ID Stable Partition"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Partitioning
  - Stable Ordering
tags:
  - linked-list
  - partition
  - stable
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-010: Shuttle ID Stable Partition

## Problem Statement

Stable-partition the list so that nodes with value less than `x` come first, then nodes equal to `x`, then nodes greater than `x`. Preserve the original relative order within each group.

![Problem Illustration](../images/LNK-010/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `x`

## Output Format

- Single line: list values after stable partition

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
5
5 1 4 2 5
4
```

**Output:**

```
1 2 4 5 5
```

**Explanation:**

Values less than 4: 1, 2

Values equal to 4: 4

Values greater than 4: 5, 5

![Example Visualization](../images/LNK-010/example-1.png)

## Notes

- Build three lists: less, equal, greater
- Concatenate in order while keeping internal stability
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Stable Partitioning

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

class Solution {
    public ListNode stablePartition(ListNode head, int x) {
        // Implement here
        return head;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        if (n > 0) {
            String[] vals = br.readLine().trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                curr.next = new ListNode(Integer.parseInt(vals[i]));
                curr = curr.next;
            }
        } else {
            br.readLine();
        }

        int x = Integer.parseInt(br.readLine().trim());

        Solution sol = new Solution();
        ListNode res = sol.stablePartition(dummy.next, x);

        PrintWriter out = new PrintWriter(System.out);
        while (res != null) {
            out.print(res.val + (res.next == null ? "" : " "));
            res = res.next;
        }
        out.println();
        out.flush();
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
    def stable_partition(self, head, x):
        # Implement here
        return head

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    dummy = ListNode(0)
    curr = dummy
    for i in range(1, n + 1):
        curr.next = ListNode(int(input_data[i]))
        curr = curr.next

    x = int(input_data[n + 1])

    sol = Solution()
    res = sol.stable_partition(dummy.next, x)

    output = []
    while res:
        output.append(str(res.val))
        res = res.next
    print(" ".join(output))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* stablePartition(ListNode* head, int x) {
        // Implement here
        return head;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    ListNode* dummy = new ListNode(0);
    ListNode* curr = dummy;
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        curr->next = new ListNode(val);
        curr = curr->next;
    }

    int x;
    cin >> x;

    Solution sol;
    ListNode* res = sol.stablePartition(dummy->next, x);

    while (res) {
        cout << res->val << (res->next ? " " : "");
        res = res->next;
    }
    cout << endl;

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
  stablePartition(head, x) {
    // Implement here
    return head;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const dummy = new ListNode(0);
  let curr = dummy;
  for (let i = 0; i < n; i++) {
    curr.next = new ListNode(parseInt(input[idx++]));
    curr = curr.next;
  }

  const x = parseInt(input[idx++]);

  const sol = new Solution();
  let res = sol.stablePartition(dummy.next, x);

  const output = [];
  while (res) {
    output.push(res.val);
    res = res.next;
  }
  console.log(output.join(" "));
}

solve();
```
