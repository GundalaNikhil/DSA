---
problem_id: LNK_HOSTEL_NUMBER_REMOVE_MTH__4285
display_id: LNK-012
slug: hostel-number-remove-mth
title: "Hostel Number Remove Mth from Start"
difficulty: Medium
difficulty_score: 44
topics:
  - Linked List
  - Deletion
  - Single Pass
tags:
  - linked-list
  - deletion
  - single-pass
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-012: Hostel Number Remove Mth from Start

## Problem Statement

Remove the M-th node from the start of a singly linked list (1-indexed). If `M` is larger than the list length, return the original list.

![Problem Illustration](../images/LNK-012/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `M`

## Output Format

- Single line: list values after removal

## Constraints

- `1 <= n <= 100000`
- `1 <= M <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
4
9 8 7 6
2
```

**Output:**

```
9 7 6
```

**Explanation:**

The 2nd node (value 8) is removed.

![Example Visualization](../images/LNK-012/example-1.png)

## Notes

- Use a dummy head to handle removal of the first node
- A single pass with a counter is enough
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Deletion

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
    public ListNode removeMth(ListNode head, int M) {
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
        int M = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.removeMth(dummy.next, M);
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

def remove_mth(head: ListNode, M: int) -> ListNode:
    # Your implementation here
    return head

def main():
    n = int(input())
    values = list(map(int, input().split()))
    M = int(input())

    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next

    head = remove_mth(dummy.next, M)
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
    ListNode* removeMth(ListNode* head, int M) {
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
    int M;
    cin >> M;

    Solution solution;
    ListNode* res = solution.removeMth(dummy.next, M);
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

function removeMth(head, M) {
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
  const M = parseInt(data[idx++], 10);

  let head = removeMth(dummy.next, M);
  const out = [];
  while (head) {
    out.push(head.val.toString());
    head = head.next;
  }
  console.log(out.join(" "));
});
```
