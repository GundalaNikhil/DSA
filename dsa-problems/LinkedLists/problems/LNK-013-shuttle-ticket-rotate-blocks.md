---
problem_id: LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__8156
display_id: LNK-013
slug: shuttle-ticket-rotate-blocks
title: "Shuttle Ticket Rotate by Blocks"
difficulty: Medium
difficulty_score: 46
topics:
  - Linked List
  - Rotation
  - Block Processing
tags:
  - linked-list
  - rotation
  - blocks
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-013: Shuttle Ticket Rotate by Blocks

## Problem Statement

Rotate the list to the right by `k` places, but only within each block of size `b`. The list is partitioned into consecutive blocks of length `b` (the final block may be shorter). Rotate each block independently by `k % blockSize`, then concatenate the blocks in order.

![Problem Illustration](../images/LNK-013/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: two integers `b` and `k`

## Output Format

- Single line: list values after block rotations

## Constraints

- `0 <= n <= 100000`
- `1 <= b <= max(1, n)`
- `0 <= k <= 10^9`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
6
1 2 3 4 5 6
3 1
```

**Output:**

```
3 1 2 6 4 5
```

**Explanation:**

Blocks of size 3:

- [1, 2, 3] rotated right by 1 -> [3, 1, 2]
- [4, 5, 6] rotated right by 1 -> [6, 4, 5]

![Example Visualization](../images/LNK-013/example-1.png)

## Notes

- For each block, use `k % blockSize`
- The last block may be shorter but is still rotated
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Rotation, Block Processing

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
    public ListNode rotateByBlocks(ListNode head, int b, long k) {
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
        int b = Integer.parseInt(params[0]);
        long k = Long.parseLong(params[1]);

        Solution sol = new Solution();
        ListNode res = sol.rotateByBlocks(dummy.next, b, k);

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
    def rotate_by_blocks(self, head, b, k):
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

    b = int(input_data[n + 1])
    k = int(input_data[n + 2])

    sol = Solution()
    res = sol.rotate_by_blocks(dummy.next, b, k)

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
    ListNode* rotateByBlocks(ListNode* head, int b, long long k) {
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

    int b;
    long long k;
    cin >> b >> k;

    Solution sol;
    ListNode* res = sol.rotateByBlocks(dummy->next, b, k);

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
  rotateByBlocks(head, b, k) {
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

  const b = parseInt(input[idx++]);
  const k = BigInt(input[idx++]);

  const sol = new Solution();
  let res = sol.rotateByBlocks(dummy.next, b, k);

  const output = [];
  while (res) {
    output.push(res.val);
    res = res.next;
  }
  console.log(output.join(" "));
}

solve();
```
