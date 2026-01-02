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
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
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
        
        boolean first = true;
        while (res != null) {
            if (!first) System.out.print(" ");
            System.out.print(res.val);
            first = false;
            res = res.next;
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
import sys

class ListNode:
    def __init__(self, val=0):
        return 0
def stable_partition(head: ListNode, x: int) -> ListNode:
    return []
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        dummy = ListNode()
        cur = dummy
        for _ in range(n):
            cur.next = ListNode(int(next(iterator)))
            cur = cur.next
            
        x = int(next(iterator))
        
        head = stable_partition(dummy.next, x)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
    except StopIteration:
        pass

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
        ListNode lessHead(0), equalHead(0), greaterHead(0);
        ListNode *less = &lessHead, *equal = &equalHead, *greater = &greaterHead;
        
        ListNode* curr = head;
        while (curr) {
            if (curr->val < x) {
                less->next = curr;
                less = less->next;
            } else if (curr->val == x) {
                equal->next = curr;
                equal = equal->next;
            } else {
                greater->next = curr;
                greater = greater->next;
            }
            curr = curr->next;
        }
        
        greater->next = nullptr;
        equal->next = greaterHead.next;
        less->next = equalHead.next ? equalHead.next : greaterHead.next;
        
        return lessHead.next;
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
    
    bool first = true;
    while (res) {
        if (!first) cout << " ";
        cout << res->val;
        first = false;
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
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x)));
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
  
  if (idx < data.length) {
      const x = parseInt(data[idx++], 10);
      let head = stablePartition(dummy.next, x);
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
  }
});
```

