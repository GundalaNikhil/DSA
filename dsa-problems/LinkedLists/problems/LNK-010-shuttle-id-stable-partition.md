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

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode stablePartition(ListNode head, int x) {
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
        int x = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.stablePartition(dummy.next, x);
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

def stable_partition(head: ListNode, x: int) -> ListNode:
    # Your implementation here
    return head

def main():
    n = int(input())
    values = list(map(int, input().split())) if n > 0 else []
    x = int(input())

    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next

    head = stable_partition(dummy.next, x)
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
    ListNode* stablePartition(ListNode* head, int x) {
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
    int x;
    cin >> x;

    Solution solution;
    ListNode* res = solution.stablePartition(dummy.next, x);
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

function stablePartition(head, x) {
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
  const x = parseInt(data[idx++], 10);

  let head = stablePartition(dummy.next, x);
  const out = [];
  while (head) {
    out.push(head.val.toString());
    head = head.next;
  }
  console.log(out.join(" "));
});
```
