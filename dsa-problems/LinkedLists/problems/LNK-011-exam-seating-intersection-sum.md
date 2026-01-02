---
problem_id: LNK_EXAM_SEATING_INTERSECTION_SUM__5629
display_id: LNK-011
slug: exam-seating-intersection-sum
title: "Exam Seating Intersection Sum"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Intersection
  - Two Pointers
tags:
  - linked-list
  - intersection
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-011: Exam Seating Intersection Sum

## Problem Statement

Two singly linked lists may intersect (share nodes). Return the sum of values in the shared suffix. If there is no intersection, return `0`.

![Problem Illustration](../images/LNK-011/problem-illustration.png)

## Input Format

- First line: two integers `n` and `m` (lengths of list A and list B)
- Second line: `n` space-separated integers (list A values)
- Third line: `m` space-separated integers (list B values)
- Fourth line: two integers `ia` and `ib`

If `ia` and `ib` are both `-1`, the lists do not intersect. Otherwise, the node at index `ib` of list B is connected to the node at index `ia` of list A (0-based). Any nodes after index `ib` in list B are ignored after the connection.

## Output Format

- Single integer: sum of values in the shared suffix

## Constraints

- `0 <= n, m <= 100000`
- Node values fit in 32-bit signed integer
- `-1 <= ia < n`, `-1 <= ib < m`

## Example

**Input:**

```
4 3
1 2 3 4
9 3 4
2 1
```

**Output:**

```
7
```

**Explanation:**

List A: 1 -> 2 -> 3 -> 4

List B starts as 9 -> 3 -> 4, but index 1 in B connects to index 2 in A.

Shared suffix is 3 -> 4, sum = 7.

![Example Visualization](../images/LNK-011/example-1.png)

## Notes

- You can find the intersection using length alignment or hashing
- Once the intersection node is found, sum to the end
- Time complexity: O(n + m)
- Space complexity: O(1)

## Related Topics

Linked Lists, Intersection, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long intersectionSum(ListNode headA, ListNode headB) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        ListNode dummyA = new ListNode(0);
        ListNode curA = dummyA;
        ListNode[] nodesA = new ListNode[n];
        for (int i = 0; i < n; i++) {
            curA.next = new ListNode(sc.nextInt());
            curA = curA.next;
            nodesA[i] = curA;
        }
        
        ListNode dummyB = new ListNode(0);
        ListNode curB = dummyB;
        ListNode[] nodesB = new ListNode[m];
        for (int i = 0; i < m; i++) {
            curB.next = new ListNode(sc.nextInt());
            curB = curB.next;
            nodesB[i] = curB;
        }
        
        int ia = sc.nextInt();
        int ib = sc.nextInt();
        if (ia >= 0 && ib >= 0 && n > 0 && m > 0) {
            nodesB[ib].next = nodesA[ia];
        }

        Solution solution = new Solution();
        System.out.println(solution.intersectionSum(dummyA.next, dummyB.next));
        sc.close();
    }
}
```

### Python

```python
import sys

def get_length(head):
    # Implementation here
    return None

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        dummyA = ListNode()
        curA = dummyA
        nodesA = []
        for _ in range(n):
            node = ListNode(int(next(iterator)))
            curA.next = node
            curA = curA.next
            nodesA.append(node)
            
        dummyB = ListNode()
        curB = dummyB
        nodesB = []
        for _ in range(m):
            node = ListNode(int(next(iterator)))
            curB.next = node
            curB = curB.next
            nodesB.append(node)
            
        ia = int(next(iterator))
        ib = int(next(iterator))
        
        if ia >= 0 and ib >= 0 and n > 0 and m > 0:
            nodesB[ib].next = nodesA[ia]
            
        print(intersection_sum(dummyA.next, dummyB.next))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long intersectionSum(ListNode* headA, ListNode* headB) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    ListNode dummyA(0);
    ListNode* curA = &dummyA;
    vector<ListNode*> nodesA;
    nodesA.reserve(n);
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        curA->next = new ListNode(v);
        curA = curA->next;
        nodesA.push_back(curA);
    }
    
    ListNode dummyB(0);
    ListNode* curB = &dummyB;
    vector<ListNode*> nodesB;
    nodesB.reserve(m);
    for (int i = 0; i < m; i++) {
        int v;
        cin >> v;
        curB->next = new ListNode(v);
        curB = curB->next;
        nodesB.push_back(curB);
    }
    
    int ia, ib;
    cin >> ia >> ib;
    if (ia >= 0 && ib >= 0 && n > 0 && m > 0) {
        nodesB[ib]->next = nodesA[ia];
    }

    Solution solution;
    cout << solution.intersectionSum(dummyA.next, dummyB.next) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  getLength(head) {
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

function new Solution().getLength(head) {
  let len = 0;
  while (head) {
    len++;
    head = head.next;
  }
  return len;
}

function intersectionSum(headA, headB) {
  let lenA = new Solution().getLength(headA);
  let lenB = new Solution().getLength(headB);

  let ptrA = headA;
  let ptrB = headB;

  while (lenA > lenB) {
    ptrA = ptrA.next;
    lenA--;
  }
  while (lenB > lenA) {
    ptrB = ptrB.next;
    lenB--;
  }

  while (ptrA !== ptrB) {
    ptrA = ptrA.next;
    ptrB = ptrB.next;
  }

  if (!ptrA) return 0;

  let sum = 0;
  while (ptrA) {
    sum += ptrA.val;
    ptrA = ptrA.next;
  }
  return sum;
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
  const m = parseInt(data[idx++], 10);
  
  const dummyA = new ListNode(0);
  let curA = dummyA;
  const nodesA = [];
  for (let i = 0; i < n; i++) {
    const node = new ListNode(parseInt(data[idx++], 10));
    curA.next = node;
    curA = curA.next;
    nodesA.push(node);
  }
  
  const dummyB = new ListNode(0);
  let curB = dummyB;
  const nodesB = [];
  for (let i = 0; i < m; i++) {
    const node = new ListNode(parseInt(data[idx++], 10));
    curB.next = node;
    curB = curB.next;
    nodesB.push(node);
  }
  
  const ia = parseInt(data[idx++], 10);
  const ib = parseInt(data[idx++], 10);
  if (ia >= 0 && ib >= 0 && n > 0 && m > 0) {
    nodesB[ib].next = nodesA[ia];
  }

  console.log(intersectionSum(dummyA.next, dummyB.next));
});
```
