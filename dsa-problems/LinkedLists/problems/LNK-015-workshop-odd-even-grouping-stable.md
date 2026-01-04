---
problem_id: LNK_WORKSHOP_ODD_EVEN_GROUPING_STABLE__5392
display_id: LNK-015
slug: workshop-odd-even-grouping-stable
title: "Workshop Odd Even Grouping Stable"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Partitioning
  - Stable Ordering
tags:
  - linked-list
  - partition
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-015: Workshop Odd Even Grouping Stable

## Problem Statement

Reorder the list so that nodes with odd values appear first, followed by nodes with even values, preserving the original order within each group.

![Problem Illustration](../images/LNK-015/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)

## Output Format

- Single line: list values after grouping

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
4
2 5 4 7
```

**Output:**

```
5 7 2 4
```

**Explanation:**

Odd values in order: 5, 7

Even values in order: 2, 4

![Example Visualization](../images/LNK-015/example-1.png)

## Notes

- Build two chains (odd and even) and concatenate
- Preserve relative order within each chain
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Stable Partitioning, Parity

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
    public ListNode groupOddEven(ListNode head) {
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
        }

        Solution sol = new Solution();
        ListNode res = sol.groupOddEven(dummy.next);

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
    def group_odd_even(self, head):
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

    sol = Solution()
    res = sol.group_odd_even(dummy.next)

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
    ListNode* groupOddEven(ListNode* head) {
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

    Solution sol;
    ListNode* res = sol.groupOddEven(dummy->next);

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
  groupOddEven(head) {
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

  const sol = new Solution();
  let res = sol.groupOddEven(dummy.next);

  const output = [];
  while (res) {
    output.push(res.val);
    res = res.next;
  }
  console.log(output.join(" "));
}

solve();
```
