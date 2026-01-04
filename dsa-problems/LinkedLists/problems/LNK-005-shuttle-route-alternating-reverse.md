---
problem_id: LNK_SHUTTLE_ROUTE_ALTERNATING_REVERSE__5831
display_id: LNK-005
slug: shuttle-route-alternating-reverse
title: "Shuttle Route Alternating Reverse"
difficulty: Medium
difficulty_score: 55
topics:
  - Linked List
  - Reversal
  - Simulation
tags:
  - linked-list
  - reversal
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-005: Shuttle Route Alternating Reverse

## Problem Statement

Starting at position `l` (1-indexed), reverse every other contiguous block of length `k` in the list. The pattern is:

- Reverse `k` nodes
- Skip `k` nodes
- Reverse `k` nodes
- ...

If the final block has fewer than `k` nodes and it is a reverse turn, reverse that smaller block. Nodes before position `l` remain unchanged.

![Problem Illustration](../images/LNK-005/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: two integers `l` and `k`

## Output Format

- Single line: list values after alternating reversals

## Constraints

- `1 <= l <= n <= 100000`
- `1 <= k <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
7
1 2 3 4 5 6 7
2 2
```

**Output:**

```
1 3 2 4 5 7 6
```

**Explanation:**

Start at position 2:

- Reverse nodes [2,3] -> 3,2
- Skip nodes [4,5]
- Reverse nodes [6,7] -> 7,6

Final list: 1 -> 3 -> 2 -> 4 -> 5 -> 7 -> 6

![Example Visualization](../images/LNK-005/example-1.png)

## Notes

- Move a pointer to position `l` before processing blocks
- Toggle between reverse and skip blocks of size `k`
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Block Reversal, Simulation

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
    public ListNode alternatingReverse(ListNode head, int l, int k) {
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

        String[] params = br.readLine().trim().split("\\s+");
        int l = Integer.parseInt(params[0]);
        int k = Integer.parseInt(params[1]);

        Solution sol = new Solution();
        ListNode res = sol.alternatingReverse(dummy.next, l, k);

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
    def alternating_reverse(self, head, l, k):
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

    l = int(input_data[n + 1])
    k = int(input_data[n + 2])

    sol = Solution()
    res = sol.alternating_reverse(dummy.next, l, k)

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
    ListNode* alternatingReverse(ListNode* head, int l, int k) {
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

    int l, k;
    cin >> l >> k;

    Solution sol;
    ListNode* res = sol.alternatingReverse(dummy->next, l, k);

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
  alternatingReverse(head, l, k) {
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

  const l = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);

  const sol = new Solution();
  let res = sol.alternatingReverse(dummy.next, l, k);

  const output = [];
  while (res) {
    output.push(res.val);
    res = res.next;
  }
  console.log(output.join(" "));
}

solve();
```
