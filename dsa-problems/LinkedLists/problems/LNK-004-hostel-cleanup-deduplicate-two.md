---
problem_id: LNK_HOSTEL_CLEANUP_DEDUPLICATE_TWO__6294
display_id: LNK-004
slug: hostel-cleanup-deduplicate-two
title: "Hostel Cleanup Deduplicate (At Most Two)"
difficulty: Medium
difficulty_score: 45
topics:
  - Linked List
  - Two Pointers
  - Deduplication
tags:
  - linked-list
  - duplicates
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-004: Hostel Cleanup Deduplicate (At Most Two)

## Problem Statement

Given a sorted singly linked list, remove extra duplicates so that each distinct value appears at most twice. Return the head of the modified list.

![Problem Illustration](../images/LNK-004/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers in non-decreasing order

## Output Format

- Single line: list values after cleanup, space-separated
- If the list is empty, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
6
1 1 1 2 2 3
```

**Output:**

```
1 1 2 2 3
```

**Explanation:**

Only two occurrences of each value are kept.

![Example Visualization](../images/LNK-004/example-1.png)

## Notes

- Track the count of the current value as you traverse
- Unlink nodes beyond the second occurrence
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Deduplication, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public ListNode deduplicateAtMostTwo(ListNode head) {
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

        Solution solution = new Solution();
        ListNode res = solution.deduplicateAtMostTwo(dummy.next);
        
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

def deduplicate_at_most_two(head: ListNode) -> ListNode:
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
            
        head = deduplicate_at_most_two(dummy.next)
        
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
    ListNode* deduplicateAtMostTwo(ListNode* head) {
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

    Solution solution;
    ListNode* res = solution.deduplicateAtMostTwo(dummy.next);
    
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
  deduplicateAtMostTwo(head) {
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

function new Solution().deduplicateAtMostTwo(head) {
  if (!head || !head.next) return head;

  let prev = head;
  let current = head.next;
  let count = 1;

  while (current !== null) {
    if (current.val === prev.val) {
      count++;
      if (count > 2) {
        // Remove current
        prev.next = current.next;
        current = current.next;
      } else {
        prev = current;
        current = current.next;
      }
    } else {
      count = 1;
      prev = current;
      current = current.next;
    }
  }
  return head;
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

  let head = new Solution().deduplicateAtMostTwo(dummy.next);
  const out = [];
  while (head) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
});
```
