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

class Solution {
    public ListNode mergeByParity(ListNode l1, ListNode l2) {
        // Implementation here
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
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

def merge_by_parity(l1: ListNode, l2: ListNode) -> ListNode:
    # Implementation here
    return []

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        d1 = ListNode()
        c1 = d1
        for _ in range(n):
            c1.next = ListNode(int(next(iterator)))
            c1 = c1.next
            
        m = int(next(iterator))
        d2 = ListNode()
        c2 = d2
        for _ in range(m):
            c2.next = ListNode(int(next(iterator)))
            c2 = c2.next
            
        head = merge_by_parity(d1.next, d2.next)
        
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

class Solution {
public:
    public:
    ListNode* mergeByParity(ListNode* l1, ListNode* l2) {
        // Implementation here
        return {};
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

class Solution {
  mergeByParity(l1, l2) {
    // Implementation here
    return null;
  }
}

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function new Solution().mergeByParity(l1, l2) {
  const evenDummy = new ListNode(0);
  const oddDummy = new ListNode(0);
  let evenTail = evenDummy;
  let oddTail = oddDummy;

  let curr = l1;
  while (curr) {
    if (curr.val % 2 === 0) {
      evenTail.next = curr;
      evenTail = evenTail.next;
    } else {
      oddTail.next = curr;
      oddTail = oddTail.next;
    }
    curr = curr.next;
  }

  curr = l2;
  while (curr) {
    if (curr.val % 2 === 0) {
      evenTail.next = curr;
      evenTail = evenTail.next;
    } else {
      oddTail.next = curr;
      oddTail = oddTail.next;
    }
    curr = curr.next;
  }

  oddTail.next = null;
  evenTail.next = oddDummy.next;

  return evenDummy.next;
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

  let head = new Solution().mergeByParity(d1.next, d2.next);
  const out = [];
  while (head) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
});
```
