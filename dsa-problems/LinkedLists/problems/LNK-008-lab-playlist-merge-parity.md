---
problem_id: LNK_LAB_PLAYLIST_MERGE_PARITY__5863
display_id: LNK-008
slug: lab-playlist-merge-parity
title: "Lab Playlist Merge by Parity"
difficulty: Medium
difficulty_score: 42
topics:
  - Linked List
  - Merge
  - Stable Ordering
tags:
  - linked-list
  - merge
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-008: Lab Playlist Merge by Parity

## Problem Statement

Merge two sorted linked lists into one list. In the output, all even-valued nodes must appear before all odd-valued nodes, while preserving the relative order among evens and among odds.

![Problem Illustration](../images/LNK-008/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first list)
- Second line: `n` space-separated integers (first list values)
- Third line: integer `m` (length of second list)
- Fourth line: `m` space-separated integers (second list values)

## Output Format

- Single line: merged list values with evens first, space-separated
- If the result is empty, print an empty line

## Constraints

- `0 <= n, m <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
3
1 4 7
3
2 3 10
```

**Output:**

```
4 2 10 1 7 3
```

**Explanation:**

Evens in order: 4 (list1), 2 (list2), 10 (list2)

Odds in order: 1 (list1), 7 (list1), 3 (list2)

![Example Visualization](../images/LNK-008/example-1.png)

## Notes

- A stable merge by parity keeps original order within even and odd groups
- You can build two chains (evens and odds) and concatenate
- Time complexity: O(n + m)
- Space complexity: O(1)

## Related Topics

Linked Lists, Stable Merge, Partitioning

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
    public ListNode mergeByParity(ListNode l1, ListNode l2) {
        // Your implementation here
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ListNode d1 = new ListNode(0);
        ListNode c1 = d1;
        for (int i = 0; i < n; i++) {
            c1.next = new ListNode(sc.nextInt());
            c1 = c1.next;
        }
        int m = sc.nextInt();
        ListNode d2 = new ListNode(0);
        ListNode c2 = d2;
        for (int i = 0; i < m; i++) {
            c2.next = new ListNode(sc.nextInt());
            c2 = c2.next;
        }

        Solution solution = new Solution();
        ListNode res = solution.mergeByParity(d1.next, d2.next);
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

def merge_by_parity(l1: ListNode, l2: ListNode) -> ListNode:
    # Your implementation here
    return None

def main():
    n = int(input())
    values1 = list(map(int, input().split())) if n > 0 else []
    m = int(input())
    values2 = list(map(int, input().split())) if m > 0 else []

    d1 = ListNode()
    c1 = d1
    for v in values1:
        c1.next = ListNode(v)
        c1 = c1.next
    d2 = ListNode()
    c2 = d2
    for v in values2:
        c2.next = ListNode(v)
        c2 = c2.next

    head = merge_by_parity(d1.next, d2.next)
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
    ListNode* mergeByParity(ListNode* l1, ListNode* l2) {
        // Your implementation here
        return nullptr;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    ListNode d1(0);
    ListNode* c1 = &d1;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        c1->next = new ListNode(v);
        c1 = c1->next;
    }
    int m;
    cin >> m;
    ListNode d2(0);
    ListNode* c2 = &d2;
    for (int i = 0; i < m; i++) {
        int v;
        cin >> v;
        c2->next = new ListNode(v);
        c2 = c2->next;
    }

    Solution solution;
    ListNode* res = solution.mergeByParity(d1.next, d2.next);
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

function mergeByParity(l1, l2) {
  // Your implementation here
  return null;
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
  const d1 = new ListNode(0);
  let c1 = d1;
  for (let i = 0; i < n; i++) {
    c1.next = new ListNode(parseInt(data[idx++], 10));
    c1 = c1.next;
  }
  const m = parseInt(data[idx++], 10);
  const d2 = new ListNode(0);
  let c2 = d2;
  for (let i = 0; i < m; i++) {
    c2.next = new ListNode(parseInt(data[idx++], 10));
    c2 = c2.next;
  }

  let head = mergeByParity(d1.next, d2.next);
  const out = [];
  while (head) {
    out.push(head.val.toString());
    head = head.next;
  }
  console.log(out.join(" "));
});
```
