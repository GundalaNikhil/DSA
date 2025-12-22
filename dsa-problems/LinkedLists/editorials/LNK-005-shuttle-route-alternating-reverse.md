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
---

# LNK-005: Shuttle Route Alternating Reverse

## 📋 Problem Summary

You are given a linked list representing a sequence of stops. Starting from a specific position `l` (1-indexed), you need to modify the list by reversing every other block of `k` nodes.

The pattern is:
1. **Reverse** the next `k` nodes.
2. **Skip** the next `k` nodes.
3. Repeat.

If the last block has fewer than `k` nodes and it falls on a "reverse" turn, reverse it.

## 🌍 Real-World Scenario

**Scenario Title:** The Shuttle Bus Re-routing

A campus shuttle bus follows a long route with many stops. To optimize fuel efficiency during rush hour, the transportation department decides to change the direction of travel for specific segments of the route.

Starting from the "Downtown Hub" (stop `l`), they want to reverse the order of stops for every `k` stops (e.g., stops 1-3 reverse, stops 4-6 stay same, stops 7-9 reverse). This creates a "zig-zag" flow that better matches passenger demand patterns.

**Why This Problem Matters:**

- **Data Transformation:** Processing streams of data where blocks need to be permuted or encrypted in alternating patterns.
- **DNA Sequencing:** In bioinformatics, certain enzymes can flip segments of DNA strands.
- **Memory Layout:** Reordering data structures to optimize cache locality for specific access patterns.

![Real-World Application](../images/LNK-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Alternating Reversal

Let `l=2`, `k=2`.
List: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`

1. **Move to `l`:** Skip node 1. Current is at 2.
2. **Reverse Block 1 (size 2):** Nodes `[2, 3]` become `[3, 2]`.
   List: `1 -> 3 -> 2 -> 4 -> 5 -> 6 -> 7`
3. **Skip Block 2 (size 2):** Skip nodes `[4, 5]`.
   List unchanged.
4. **Reverse Block 3 (size 2):** Nodes `[6, 7]` become `[7, 6]`.
   List: `1 -> 3 -> 2 -> 4 -> 5 -> 7 -> 6`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **1-based Indexing:** The `l` parameter is 1-based. If `l=1`, start processing from the head.
- **Partial Blocks:** If you have 3 nodes left and `k=5`, and it's a "reverse" turn, you reverse all 3.
- **Skip Logic:** If you have 3 nodes left and `k=5`, and it's a "skip" turn, you just skip them (do nothing).

Common interpretation mistake:

- ❌ **Wrong:** Reversing *every* block of k.
- ✅ **Correct:** Reversing *alternating* blocks. Reverse, Skip, Reverse, Skip...

### Core Concept: Block Reversal

To reverse a sublist from `start` to `end`, we need the node *before* `start` to link it to `end`, and we need to link `start` to the node *after* `end`.

## Naive Approach

### Intuition

We can extract the values into an array, perform the reversals using array indexing (which is easy), and then reconstruct the linked list.

### Algorithm

1. Traverse list, store values in `ArrayList`.
2. Iterate from index `l-1` with step `2*k`.
3. For each step, reverse the subarray from `i` to `min(i+k, n)`.
4. Rebuild linked list from the modified array.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)** to store the array. This is not ideal for linked list problems where O(1) space is expected.

## Optimal Approach

### Key Insight

Perform the reversals in-place by manipulating pointers. We need a helper function or logic to reverse `k` nodes and return the new tail of that segment.

### Algorithm

1. Create a `dummy` node pointing to `head`.
2. Move a pointer `prev` `l-1` times so it sits just before the start of the modification zone.
3. Loop while there are nodes remaining:
   - **Reverse Phase:**
     - Identify the start of the block (`cur = prev.next`).
     - Reverse `k` nodes (or fewer if end of list).
     - Connect `prev` to the new head of the reversed block.
     - Connect the new tail of the reversed block to the rest of the list.
     - Move `prev` to the new tail.
   - **Skip Phase:**
     - Move `prev` forward `k` times (or until end of list).
     - If we reach end of list, stop.

### Time Complexity

- **O(N)**. We visit each node a constant number of times.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-005/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-005/algorithm-steps.png)

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
    public ListNode alternatingReverse(ListNode head, int l, int k) {
        if (head == null || k <= 1) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        // Move to the starting position l
        for (int i = 0; i < l - 1; i++) {
            if (prev.next == null) return head;
            prev = prev.next;
        }

        boolean reverse = true;
        while (prev.next != null) {
            if (reverse) {
                // Reverse next k nodes
                ListNode tail = prev.next;
                ListNode curr = prev.next.next;
                int count = 1;
                while (curr != null && count < k) {
                    ListNode temp = curr.next;
                    curr.next = prev.next;
                    prev.next = curr;
                    tail.next = temp;
                    curr = temp;
                    count++;
                }
                prev = tail; // Move prev to the end of the reversed block
            } else {
                // Skip next k nodes
                int count = 0;
                while (prev.next != null && count < k) {
                    prev = prev.next;
                    count++;
                }
            }
            reverse = !reverse; // Toggle mode
        }

        return dummy.next;
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

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def alternating_reverse(head: ListNode, l: int, k: int) -> ListNode:
    if not head or k <= 1:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to start position l
    for _ in range(l - 1):
        if not prev.next:
            return head
        prev = prev.next
        
    reverse_turn = True
    
    while prev.next:
        if reverse_turn:
            # Reverse next k nodes
            tail = prev.next
            curr = tail.next
            count = 1
            while curr and count < k:
                temp = curr.next
                curr.next = prev.next
                prev.next = curr
                tail.next = temp
                curr = temp
                count += 1
            prev = tail # Move prev to end of reversed block
        else:
            # Skip k nodes
            count = 0
            while prev.next and count < k:
                prev = prev.next
                count += 1
        
        reverse_turn = not reverse_turn
        
    return dummy.next

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

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* alternatingReverse(ListNode* head, int l, int k) {
        if (!head || k <= 1) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        // Move to l-1
        for (int i = 0; i < l - 1; i++) {
            if (!prev->next) return head;
            prev = prev->next;
        }

        bool reverse = true;
        while (prev->next) {
            if (reverse) {
                ListNode* tail = prev->next;
                ListNode* curr = tail->next;
                int count = 1;
                while (curr && count < k) {
                    ListNode* temp = curr->next;
                    curr->next = prev->next;
                    prev->next = curr;
                    tail->next = temp;
                    curr = temp;
                    count++;
                }
                prev = tail;
            } else {
                int count = 0;
                while (prev->next && count < k) {
                    prev = prev->next;
                    count++;
                }
            }
            reverse = !reverse;
        }
        return dummy.next;
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

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function alternatingReverse(head, l, k) {
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
  
  if (idx < data.length) {
      const l = parseInt(data[idx++], 10);
      const k = parseInt(data[idx++], 10);

      let head = alternatingReverse(dummy.next, l, k);
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 2 3 4 5 6 7`, `l=2`, `k=2`

**Initialization:**
- `dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`
- Move `prev` to `l-1` (node 1).
- `reverse = true`

**Iteration 1 (Reverse):**
- `tail` = 2, `curr` = 3.
- Move 3 to front of block (after 1).
- List: `1 -> 3 -> 2 -> 4 ...`
- `count` reaches 2.
- Move `prev` to `tail` (2).
- `reverse = false`.

**Iteration 2 (Skip):**
- Skip 2 nodes (4, 5).
- `prev` moves to 5.
- `reverse = true`.

**Iteration 3 (Reverse):**
- `tail` = 6, `curr` = 7.
- Move 7 to front of block (after 5).
- List: `... 5 -> 7 -> 6`.
- `count` reaches 2.
- Move `prev` to `tail` (6).
- `reverse = false`.

**End:** `prev.next` is null. Return head.

![Example Visualization](../images/LNK-005/example-1.png)

## ✅ Proof of Correctness

### Invariant
After processing a block (reverse or skip), `prev` always points to the last node of that processed block, which serves as the anchor for the next block operation.

### Why the approach is correct
- The standard linked list reversal algorithm (`curr.next = prev.next; prev.next = curr; ...`) is used, which is O(K) for K nodes.
- By toggling the `reverse` boolean, we strictly adhere to the alternating pattern.
- The logic handles partial blocks naturally: the `while` loop condition `curr != null` ensures we stop if the list ends mid-block.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Reverse Nodes in k-Group (LeetCode Hard).
  - *Diff:* If last block < k, *don't* reverse it.
- **Extension 2:** Reverse even positions only.
  - *Hint:* Extract evens, reverse, merge back.
- **Extension 3:** Palindrome check.
  - *Hint:* Reverse second half and compare.

### C++ommon Mistakes to Avoid

1. **Lost Head**
   - ❌ Wrong: Not using a dummy node. If `l=1`, the head changes.
   - ✅ Correct: Always use `dummy` when head might change.

2. **Pointer Confusion**
   - ❌ Wrong: Losing track of the connection to the rest of the list.
   - ✅ Correct: `tail.next = temp` ensures the rest of the list stays attached.

3. **Off-by-One**
   - ❌ Wrong: Moving `prev` too far or not far enough for `l`.
   - ✅ Correct: Loop `l-1` times.

## Related Concepts

- **In-place Reversal:** A fundamental linked list skill.
- **Dummy Node:** Simplifies head operations.
- **Modular Arithmetic:** Conceptually similar to `i % 2k < k`.
