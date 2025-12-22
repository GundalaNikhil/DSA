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
---

# LNK-011: Exam Seating Intersection Sum

## 📋 Problem Summary

You are given two singly linked lists, List A and List B. They might intersect at some node and share all subsequent nodes (forming a 'Y' shape). Your task is to:
1. Determine if they intersect.
2. If they do, calculate the sum of values of all nodes in the shared suffix (starting from the intersection node to the end).
3. If they don't intersect, return 0.

## 🌍 Real-World Scenario

**Scenario Title:** The Merging Exam Lines

Students from two different exam halls (Hall A and Hall B) are leaving the building.
- Hall A students walk down Corridor A.
- Hall B students walk down Corridor B.
- At some point, Corridor B merges into Corridor A, and from there, everyone walks down the same final path to the exit.

You want to calculate the "total age" (sum of values) of all students who are walking in the shared path after the merge point.

**Why This Problem Matters:**

- **Git Branches:** Two branches of development history merging into a common timeline.
- **River Systems:** Tributaries joining a main river; calculating water volume in the main channel.
- **Memory Sharing:** In immutable data structures (like in functional programming), two lists might share a common tail to save memory.

![Real-World Application](../images/LNK-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Intersection

List A: `1 -> 2 -> 3 -> 4`
List B: `9 -> 3 -> 4` (Connects to 3 in A)

Visualizing the 'Y' shape:
```
A: 1 -> 2
         \
          3 -> 4 -> null
         /
B:      9
```
Intersection Node: `3`.
Shared Suffix: `3 -> 4`.
Sum: `3 + 4 = 7`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Reference Equality:** Intersection is defined by reference (memory address), not value. Two nodes with value `3` are distinct unless they are literally the same object.
- **No Intersection:** If the lists never merge, return 0.
- **Suffix Sum:** Include the intersection node itself in the sum.

Common interpretation mistake:

- ❌ **Wrong:** Summing values from the start of both lists.
- ✅ **Correct:** Only summing the shared tail.

### Core Concept: Length Alignment

If List A has length 5 and List B has length 3, the intersection cannot happen at A's first 2 nodes. We can skip the first `5-3=2` nodes of A to align the starting positions.

## Naive Approach

### Intuition

For every node in List A, traverse List B to see if it matches.

### Algorithm

1. Loop `currA` through List A.
2. Inside, loop `currB` through List B.
3. If `currA == currB`, we found intersection. Calculate sum and return.

### Time Complexity

- **O(N * M)**. Too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Align the starts. Calculate length of A (`lenA`) and B (`lenB`). Advance the pointer of the longer list by `abs(lenA - lenB)`. Then move both pointers forward together. They will meet at the intersection.

### Algorithm

1. Calculate `lenA` and `lenB`.
2. Reset pointers `ptrA = headA`, `ptrB = headB`.
3. If `lenA > lenB`, advance `ptrA` by `lenA - lenB`.
4. If `lenB > lenA`, advance `ptrB` by `lenB - lenA`.
5. While `ptrA != ptrB`:
   - `ptrA = ptrA.next`
   - `ptrB = ptrB.next`
   - If either becomes null, return 0 (no intersection).
6. Now `ptrA` is the intersection node (or null).
7. Traverse from `ptrA` to end, summing values.
8. Return sum.

### Time Complexity

- **O(N + M)**. We traverse each list a constant number of times.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-011/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-011/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public long intersectionSum(ListNode headA, ListNode headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);

        ListNode ptrA = headA;
        ListNode ptrB = headB;

        // Align pointers
        while (lenA > lenB) {
            ptrA = ptrA.next;
            lenA--;
        }
        while (lenB > lenA) {
            ptrB = ptrB.next;
            lenB--;
        }

        // Find intersection
        while (ptrA != ptrB) {
            ptrA = ptrA.next;
            ptrB = ptrB.next;
        }

        // ptrA is now intersection or null
        if (ptrA == null) return 0;

        // Sum suffix
        long sum = 0;
        while (ptrA != null) {
            sum += ptrA.val;
            ptrA = ptrA.next;
        }
        return sum;
    }

    private int getLength(ListNode head) {
        int len = 0;
        while (head != null) {
            len++;
            head = head.next;
        }
        return len;
    }
}

public class Main {
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

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def intersection_sum(headA: ListNode, headB: ListNode) -> int:
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    ptrA = headA
    ptrB = headB
    
    # Align
    while lenA > lenB:
        ptrA = ptrA.next
        lenA -= 1
    while lenB > lenA:
        ptrB = ptrB.next
        lenB -= 1
        
    # Find intersection
    while ptrA != ptrB:
        ptrA = ptrA.next
        ptrB = ptrB.next
        
    if not ptrA:
        return 0
        
    # Sum suffix
    total_sum = 0
    while ptrA:
        total_sum += ptrA.val
        ptrA = ptrA.next
        
    return total_sum

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

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    long long intersectionSum(ListNode* headA, ListNode* headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);

        ListNode* ptrA = headA;
        ListNode* ptrB = headB;

        while (lenA > lenB) {
            ptrA = ptrA->next;
            lenA--;
        }
        while (lenB > lenA) {
            ptrB = ptrB->next;
            lenB--;
        }

        while (ptrA != ptrB) {
            ptrA = ptrA->next;
            ptrB = ptrB->next;
        }

        if (!ptrA) return 0;

        long long sum = 0;
        while (ptrA) {
            sum += ptrA->val;
            ptrA = ptrA->next;
        }
        return sum;
    }

private:
    int getLength(ListNode* head) {
        int len = 0;
        while (head) {
            len++;
            head = head->next;
        }
        return len;
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

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function getLength(head) {
  let len = 0;
  while (head) {
    len++;
    head = head.next;
  }
  return len;
}

function intersectionSum(headA, headB) {
  let lenA = getLength(headA);
  let lenB = getLength(headB);

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
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
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

## 🧪 Test Case Walkthrough (Dry Run)

Input: A=`1->2->3->4`, B=`9->3->4` (B connects to A's 3).
`lenA` = 4. `lenB` = 3.

**Alignment:**
- `lenA` > `lenB`. Advance `ptrA` by 1.
- `ptrA` points to 2. `ptrB` points to 9.

**Search:**
- `ptrA` (2) != `ptrB` (9). Advance both.
- `ptrA` (3) == `ptrB` (3). **Match!**

**Sum:**
- Start at 3. Sum = 3.
- Next is 4. Sum = 3 + 4 = 7.
- Next is null.

Result: 7.

![Example Visualization](../images/LNK-011/example-1.png)

## ✅ Proof of Correctness

### Invariant
After alignment, `ptrA` and `ptrB` are equidistant from the end of the list.

### Why the approach is correct
- Since they share the suffix, the distance from intersection to end is identical.
- By aligning starts, we ensure that if they meet, they meet at the *first* common node.
- If they reach null without meeting, there is no intersection.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if list has cycles?
  - *Hint:* Much harder. Need to detect cycles first, then check if cycles are same.
- **Extension 2:** Find intersection without length calculation (Two Pointers trick).
  - *Hint:* `ptrA` traverses A then B. `ptrB` traverses B then A. They meet at intersection or null.
- **Extension 3:** Minimize memory access.
  - *Hint:* Length calculation is cache-friendly (sequential access).

### Common Mistakes to Avoid

1. **Value Comparison**
   - ❌ Wrong: `ptrA.val == ptrB.val`.
   - ✅ Correct: `ptrA == ptrB` (reference check).

2. **Off-by-one**
   - ❌ Wrong: Advancing `lenA - lenB - 1`.
   - ✅ Correct: Advance exactly the difference.

3. **Null Pointer**
   - ❌ Wrong: Accessing `ptrA.next` when `ptrA` is null.
   - ✅ Correct: Loop condition `ptrA != null`.

## Related Concepts

- **Two Pointers:** Aligning start positions.
- **Reference vs Value:** Crucial in linked lists.
