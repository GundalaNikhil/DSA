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

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode rotateBlocks(ListNode head, int b, int k) {
        // Your implementation here
        return head;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int i = 0; i < n; i++) {
            cur.next = new ListNode(sc.nextInt());
            cur = cur.next;
        }
        int b = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.rotateBlocks(dummy.next, b, k);
        while (res != null) {
            System.out.print(res.val + (res.next != null ? " " : ""));
            res = res.next;
        }
        System.out.println();
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

def rotate_blocks(head: ListNode, b: int, k: int) -> ListNode:
    # Your implementation here
    return head

def main():
    n = int(input())
    values = list(map(int, input().split())) if n > 0 else []
    b, k = map(int, input().split())

    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next

    head = rotate_blocks(dummy.next, b, k)
    out = []
    while head:
        out.append(str(head.val))
        head = head.next
    print(" ".join(out))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* rotateBlocks(ListNode* head, int b, int k) {
        // Your implementation here
        return head;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    ListNode dummy(0);
    ListNode* cur = &dummy;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    int b, k;
    cin >> b >> k;

    Solution solution;
    ListNode* res = solution.rotateBlocks(dummy.next, b, k);
    while (res) {
        cout << res->val << (res->next ? " " : "");
        res = res->next;
    }
    cout << "\n";
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

function rotateBlocks(head, b, k) {
  // Your implementation here
  return head;
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
  for (let i = 0; i < n; i++) {
    cur.next = new ListNode(parseInt(data[idx++], 10));
    cur = cur.next;
  }
  const b = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);

  let head = rotateBlocks(dummy.next, b, k);
  const out = [];
  while (head) {
    out.push(head.val.toString());
    head = head.next;
  }
  console.log(out.join(" "));
});
```
