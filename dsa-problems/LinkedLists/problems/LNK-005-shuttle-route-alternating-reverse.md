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

class Solution {
    public ListNode alternatingReverse(ListNode head, int l, int k) {
        // Implementation here
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
        
        int l = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.alternatingReverse(dummy.next, l, k);
        
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

def alternating_reverse(head: ListNode, l: int, k: int) -> ListNode:
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
        dummy = ListNode()
        cur = dummy
        for _ in range(n):
            cur.next = ListNode(int(next(iterator)))
            cur = cur.next
            
        l = int(next(iterator))
        k = int(next(iterator))
        
        head = alternating_reverse(dummy.next, l, k)
        
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
    ListNode* alternatingReverse(ListNode* head, int l, int k) {
        // Implementation here
        return {};
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
    
    int l, k;
    cin >> l >> k;

    Solution solution;
    ListNode* res = solution.alternatingReverse(dummy.next, l, k);
    
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
  alternatingReverse(head, l, k) {
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

function new Solution().alternatingReverse(head, l, k) {
  if (!head || k <= 1) return head;

  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;

  // Move to l-1
  for (let i = 0; i < l - 1; i++) {
    if (!prev.next) return head;
    prev = prev.next;
  }

  let reverse = true;
  while (prev.next) {
    if (reverse) {
      let tail = prev.next;
      let curr = tail.next;
      let count = 1;
      while (curr && count < k) {
        let temp = curr.next;
        curr.next = prev.next;
        prev.next = curr;
        tail.next = temp;
        curr = temp;
        count++;
      }
      prev = tail;
    } else {
      let count = 0;
      while (prev.next && count < k) {
        prev = prev.next;
        count++;
      }
    }
    reverse = !reverse;
  }
  return dummy.next;
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
      const l = parseInt(data[idx++], 10);
      const k = parseInt(data[idx++], 10);

      let head = new Solution().alternatingReverse(dummy.next, l, k);
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
  }
});
```
