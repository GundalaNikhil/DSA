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

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode groupOddEvenStable(ListNode head) {
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

        Solution solution = new Solution();
        ListNode res = solution.groupOddEvenStable(dummy.next);
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

def group_odd_even_stable(head: ListNode) -> ListNode:
    # Your implementation here
    return head

def main():
    n = int(input())
    values = list(map(int, input().split())) if n > 0 else []

    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next

    head = group_odd_even_stable(dummy.next)
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
    ListNode* groupOddEvenStable(ListNode* head) {
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

    Solution solution;
    ListNode* res = solution.groupOddEvenStable(dummy.next);
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

function groupOddEvenStable(head) {
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

  let head = groupOddEvenStable(dummy.next);
  const out = [];
  while (head) {
    out.push(head.val.toString());
    head = head.next;
  }
  console.log(out.join(" "));
});
```
