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
---

# LNK-015: Workshop Odd Even Grouping Stable

## 📋 Problem Summary

You are given a linked list. You need to reorder it such that:
1. All nodes with **odd values** appear first.
2. All nodes with **even values** appear second.
3. The relative order of nodes within the odd group and within the even group must remain unchanged (stable).

## 🌍 Real-World Scenario

**Scenario Title:** The Workshop Team Split

A workshop facilitator wants to split participants into two large teams for a debate: "Team Odd" and "Team Even" based on the number on their badge.
- Participants are currently standing in a single line.
- The facilitator asks all "Odds" to step to the left and all "Evens" to step to the right.
- Then, the "Odd" line is placed in front of the "Even" line to enter the hall.
- Crucially, if Alice (Odd) was standing before Bob (Odd) in the original line, she must still be before him in the new team line.

**Why This Problem Matters:**

- **Data Partitioning:** Separating data into two categories (e.g., active vs. inactive users) for batch processing.
- **Radix Sort:** This is a single pass of a binary Radix Sort (sorting by the least significant bit).
- **Network Traffic:** Prioritizing certain packets (Odds) over others (Evens) while maintaining sequence order.

![Real-World Application](../images/LNK-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Partitioning

List: `2 -> 5 -> 4 -> 7`

1. **Initialize:** `OddHead`, `EvenHead`.
2. **Process 2 (Even):** Add to Even. `E: 2`
3. **Process 5 (Odd):** Add to Odd. `O: 5`
4. **Process 4 (Even):** Add to Even. `E: 2 -> 4`
5. **Process 7 (Odd):** Add to Odd. `O: 5 -> 7`

**Concatenate:**
`Odd` -> `Even`
`5 -> 7` -> `2 -> 4`

Result: `5 -> 7 -> 2 -> 4`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Parity of Value:** We are checking `val % 2`, NOT the index (odd/even positions).
- **Stability:** Order must be preserved.
- **Empty Groups:** If there are no odd numbers, the list starts with evens.

Common interpretation mistake:

- ❌ **Wrong:** Odd/Even *indices* (LeetCode "Odd Even Linked List").
- ✅ **Correct:** Odd/Even *values*.

### Core Concept: Two Dummy Heads

Using `oddDummy` and `evenDummy` eliminates the need to handle the "first node" logic separately. We just append to the respective tails.

## Naive Approach

### Intuition

Create two ArrayLists. Iterate list. Add values to lists. Rebuild list.

### Algorithm

1. `odds = []`, `evens = []`
2. Loop through list:
   - If `val % 2 != 0`: `odds.add(val)`
   - Else: `evens.add(val)`
3. Create new nodes from `odds` then `evens`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Re-link existing nodes in a single pass.

### Algorithm

1. `oddDummy`, `evenDummy`.
2. `oddTail = oddDummy`, `evenTail = evenDummy`.
3. Iterate `curr` through list:
   - If `curr.val % 2 != 0`:
     - `oddTail.next = curr`
     - `oddTail = curr`
   - Else:
     - `evenTail.next = curr`
     - `evenTail = curr`
4. **Terminate:** `evenTail.next = null` (Important! Prevents cycles).
5. **Connect:** `oddTail.next = evenDummy.next`.
6. Return `oddDummy.next`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-015/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-015/algorithm-steps.png)

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
    public ListNode groupOddEvenStable(ListNode head) {
        ListNode oddDummy = new ListNode(0);
        ListNode evenDummy = new ListNode(0);
        ListNode oddTail = oddDummy;
        ListNode evenTail = evenDummy;

        ListNode curr = head;
        while (curr != null) {
            if (curr.val % 2 != 0) {
                oddTail.next = curr;
                oddTail = oddTail.next;
            } else {
                evenTail.next = curr;
                evenTail = evenTail.next;
            }
            curr = curr.next;
        }

        evenTail.next = null; // Terminate even list
        oddTail.next = evenDummy.next; // Connect odd to even

        return oddDummy.next;
    }
}

public class Main {
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
        ListNode res = solution.groupOddEvenStable(dummy.next);
        
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
        self.val = val
        self.next = None

def group_odd_even_stable(head: ListNode) -> ListNode:
    odd_dummy = ListNode(0)
    even_dummy = ListNode(0)
    odd_tail = odd_dummy
    even_tail = even_dummy
    
    curr = head
    while curr:
        if curr.val % 2 != 0:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        else:
            even_tail.next = curr
            even_tail = even_tail.next
        curr = curr.next
        
    even_tail.next = None
    odd_tail.next = even_dummy.next
    
    return odd_dummy.next

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
            
        head = group_odd_even_stable(dummy.next)
        
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
    ListNode* groupOddEvenStable(ListNode* head) {
        ListNode oddDummy(0);
        ListNode evenDummy(0);
        ListNode* oddTail = &oddDummy;
        ListNode* evenTail = &evenDummy;

        ListNode* curr = head;
        while (curr) {
            if (curr->val % 2 != 0) {
                oddTail->next = curr;
                oddTail = oddTail->next;
            } else {
                evenTail->next = curr;
                evenTail = evenTail->next;
            }
            curr = curr->next;
        }

        evenTail->next = nullptr;
        oddTail->next = evenDummy.next;

        return oddDummy.next;
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

function groupOddEvenStable(head) {
  const oddDummy = new ListNode(0);
  const evenDummy = new ListNode(0);
  let oddTail = oddDummy;
  let evenTail = evenDummy;

  let curr = head;
  while (curr) {
    if (curr.val % 2 !== 0) {
      oddTail.next = curr;
      oddTail = oddTail.next;
    } else {
      evenTail.next = curr;
      evenTail = evenTail.next;
    }
    curr = curr.next;
  }

  evenTail.next = null;
  oddTail.next = evenDummy.next;

  return oddDummy.next;
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
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `2 5 4 7`

**Initialization:**
- `oddDummy`, `evenDummy` empty.

**Iteration:**
1. `2` (Even): `evenTail` -> 2.
2. `5` (Odd): `oddTail` -> 5.
3. `4` (Even): `evenTail` -> 4.
4. `7` (Odd): `oddTail` -> 7.

**Connection:**
- `evenTail.next = null` (4 -> null).
- `oddTail.next = evenDummy.next` (7 -> 2).

**Result:** `5 -> 7 -> 2 -> 4`.

![Example Visualization](../images/LNK-015/example-1.png)

## ✅ Proof of Correctness

### Invariant
`oddTail` points to the last processed odd node, `evenTail` points to the last processed even node. Order is preserved because we append to tail.

### Why the approach is correct
- We process sequentially.
- We separate into two disjoint sets.
- We concatenate them in the correct order (Odd then Even).

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Group by index parity (Odd positions then Even positions).
  - *Hint:* Standard LeetCode problem.
- **Extension 2:** Sort 0s, 1s, 2s.
  - *Hint:* 3 dummy heads.
- **Extension 3:** Partition around pivot X.
  - *Hint:* Same logic, condition `val < X`.

### C++ommon Mistakes to Avoid

1. **Cycle Creation**
   - ❌ Wrong: Forgetting `evenTail.next = null`. The last even node might point to an odd node from the original list, creating a cycle.
   - ✅ Correct: Always terminate the second list.

2. **Connecting Lists**
   - ❌ Wrong: `oddTail.next = evenTail`.
   - ✅ Correct: `oddTail.next = evenDummy.next`.

## Related Concepts

- **Stable Partition:** The general form of this problem.
- **Dummy Node:** Simplifies list construction.
