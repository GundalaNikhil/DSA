---
problem_id: LNK_LAB_SWAP_NEIGHBORS_SKIP__5817
display_id: LNK-003
slug: lab-swap-neighbors-skip-threshold
title: "Lab Swap Neighbors with Skip and Threshold"
difficulty: Medium
difficulty_score: 45
topics:
  - Linked List
  - Two Pointers
  - Simulation
tags:
  - linked-list
  - swapping
  - constraints
  - medium
premium: true
subscription_tier: basic
---

# LNK-003: Lab Swap Neighbors with Skip and Threshold

## 📋 Problem Summary

You need to swap adjacent nodes in a linked list (like `1->2` becoming `2->1`), but with two specific rules:
1. **Negative Skip:** If either node in a pair has a negative value, you cannot swap them.
2. **Swap Limit:** You can perform at most `K` swaps. Once you reach this limit, stop swapping.

Return the modified list and the total count of swaps performed.

## 🌍 Real-World Scenario

**Scenario Title:** Lab Partner Reassignment

In a chemistry lab, students are seated in a long row. The professor wants to mix things up by swapping every adjacent pair of students (Student 1 swaps with Student 2, Student 3 with Student 4, etc.).

However, there are complications:
- **Stubborn Students (Negative Values):** Some students (represented by negative IDs) refuse to move. If a pair involves a stubborn student, they stay put.
- **Time Constraint (K Limit):** The experiment is about to start. The professor only has time to approve `K` swaps. Once `K` swaps are done, everyone else stays where they are.

**Why This Problem Matters:**

- **Conditional Processing:** Real-world data processing often involves rules where certain "bad" data points (like corrupted packets or flagged transactions) prevent standard operations.
- **Resource Constraints:** Algorithms often have to work within a budget (time, energy, or operation count), requiring early termination.
- **Linked List Manipulation:** Swapping nodes is a classic pointer manipulation test that requires careful handling of `prev`, `curr`, and `next` pointers to avoid breaking the chain.

![Real-World Application](../images/LNK-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Swapping Logic

Let's visualize swapping a pair `A -> B`. We need a pointer to the node *before* A (`prev`) to link it to B.

**Before Swap:**
```
       +---+      +---+      +---+
prev ->| A | ---> | B | ---> | C |
       +---+      +---+      +---+
```

**After Swap:**
```
       +---+      +---+      +---+
prev ->| B | ---> | A | ---> | C |
       +---+      +---+      +---+
```

**Pointer Changes:**
1. `prev.next = B`
2. `A.next = B.next` (which is C)
3. `B.next = A`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Pairs are Disjoint:** We look at (Node 1, Node 2), then (Node 3, Node 4). We do *not* look at (Node 2, Node 3).
- **K Limit:** If `K=0`, no swaps happen.
- **Negative Check:** If `Node 1` is `-5` and `Node 2` is `10`, we skip. If both are positive, we swap (if `K > 0`).
- **Return Value:** You must return the new head of the list (which might change if the first pair is swapped) and the count.

Common interpretation mistake:

- ❌ **Wrong:** Swapping values (`val`) instead of nodes.
- ✅ **Correct:** The problem usually implies pointer manipulation for linked lists, though swapping values is often accepted unless specified otherwise. However, pointer manipulation is the intended skill.
- ❌ **Wrong:** Decrementing K even if a swap was skipped due to negative values.
- ✅ **Correct:** Only decrement K if a swap *actually* happens.

## Naive Approach

### Intuition

We can iterate through the list two nodes at a time. For each pair, check the conditions. If met, swap.

### Algorithm

1. Create a `dummy` node pointing to `head`. This helps if the first pair needs swapping.
2. Initialize `prev` to `dummy`.
3. Loop while `prev.next` and `prev.next.next` exist (i.e., there is a pair):
   - Let `first = prev.next` and `second = prev.next.next`.
   - Check if `K > 0`.
   - Check if `first.val >= 0` AND `second.val >= 0`.
   - **If both true:**
     - Perform swap (adjust pointers).
     - Decrement `K`.
     - Increment `swapCount`.
     - Move `prev` to `first` (since `first` is now the second node in the pair).
   - **Else:**
     - Don't swap.
     - Move `prev` to `second` (skip this pair).

### Time Complexity

- **O(N)**. We visit each node once.

### Space Complexity

- **O(1)**. Only pointers are used.

### Why This Works

It directly simulates the requirements. The use of a `dummy` node handles the edge case where the head changes.

## Optimal Approach

The simulation approach described above is already optimal O(N) time and O(1) space. There is no faster way because we must inspect the values to decide whether to swap.

![Algorithm Visualization](../images/LNK-003/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-003/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Result {
    ListNode head;
    int swaps;
    Result(ListNode head, int swaps) {
        this.head = head;
        this.swaps = swaps;
    }
}

class Solution {
    public Result swapWithSkip(ListNode head, int K) {
        if (head == null || head.next == null) {
            return new Result(head, 0);
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        int swapCount = 0;

        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            // Check conditions
            boolean nonNegative = (first.val >= 0 && second.val >= 0);
            boolean canSwap = (K > 0);

            if (nonNegative && canSwap) {
                // Perform swap
                prev.next = second;
                first.next = second.next;
                second.next = first;

                // Update state
                K--;
                swapCount++;
                prev = first; // first is now the 2nd node in the pair
            } else {
                // Skip pair
                prev = second; // second is the 2nd node in the unswapped pair
            }
        }

        return new Result(dummy.next, swapCount);
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
        int K = sc.nextInt();

        Solution solution = new Solution();
        Result res = solution.swapWithSkip(dummy.next, K);
        ListNode out = res.head;
        while (out != null) {
            System.out.print(out.val + (out.next != null ? " " : ""));
            out = out.next;
        }
        System.out.println();
        System.out.println(res.swaps);
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

def swap_with_skip(head: ListNode, K: int):
    if not head or not head.next:
        return head, 0
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    swaps_performed = 0
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # Check conditions
        non_negative = (first.val >= 0 and second.val >= 0)
        can_swap = (K > 0)
        
        if non_negative and can_swap:
            # Swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            K -= 1
            swaps_performed += 1
            prev = first
        else:
            # Skip
            prev = second
            
    return dummy.next, swaps_performed

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
        
        K = int(next(iterator))
        
        head, swaps = swap_with_skip(dummy.next, K)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
        print(swaps)
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

struct Result {
    ListNode* head;
    int swaps;
};

class Solution {
public:
    Result swapWithSkip(ListNode* head, int K) {
        if (!head || !head->next) return {head, 0};

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        int swapCount = 0;

        while (prev->next && prev->next->next) {
            ListNode* first = prev->next;
            ListNode* second = prev->next->next;

            bool nonNegative = (first->val >= 0 && second->val >= 0);
            bool canSwap = (K > 0);

            if (nonNegative && canSwap) {
                prev->next = second;
                first->next = second->next;
                second->next = first;

                K--;
                swapCount++;
                prev = first;
            } else {
                prev = second;
            }
        }
        return {dummy.next, swapCount};
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
    
    int K;
    cin >> K;

    Solution solution;
    Result res = solution.swapWithSkip(dummy.next, K);
    
    ListNode* out = res.head;
    bool first = true;
    while (out) {
        if (!first) cout << " ";
        cout << out->val;
        first = false;
        out = out->next;
    }
    cout << "\n";
    cout << res.swaps << "\n";
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

function swapWithSkip(head, K) {
  if (!head || !head.next) return [head, 0];

  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;
  let swapCount = 0;

  while (prev.next && prev.next.next) {
    const first = prev.next;
    const second = prev.next.next;

    const nonNegative = (first.val >= 0 && second.val >= 0);
    const canSwap = (K > 0);

    if (nonNegative && canSwap) {
      prev.next = second;
      first.next = second.next;
      second.next = first;

      K--;
      swapCount++;
      prev = first;
    } else {
      prev = second;
    }
  }

  return [dummy.next, swapCount];
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
      const K = parseInt(data[idx++], 10);
      const result = swapWithSkip(dummy.next, K);
      let head = result[0];
      const swaps = result[1];
      
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
      console.log(swaps);
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 -2 3 4 5 6`, `K=1`

**Initialization:**
- `dummy -> 1 -> -2 -> 3 -> 4 -> 5 -> 6`
- `prev = dummy`
- `K = 1`

**Iteration 1:**
- Pair: `(1, -2)`
- Check: `1 >= 0` (True), `-2 >= 0` (False). Condition fails.
- Action: No swap.
- Move `prev` to `-2`.
- List: `1 -> -2 -> 3 -> 4 -> 5 -> 6`

**Iteration 2:**
- Pair: `(3, 4)`
- Check: `3 >= 0` (True), `4 >= 0` (True). `K > 0` (True).
- Action: Swap.
- Pointers: `prev(-2)` points to `4`. `4` points to `3`. `3` points to `5`.
- `K` becomes 0. `swapCount` becomes 1.
- Move `prev` to `3`.
- List: `1 -> -2 -> 4 -> 3 -> 5 -> 6`

**Iteration 3:**
- Pair: `(5, 6)`
- Check: `5 >= 0` (True), `6 >= 0` (True). `K > 0` (False).
- Action: No swap (K limit reached).
- Move `prev` to `6`.
- List: `1 -> -2 -> 4 -> 3 -> 5 -> 6`

**Result:**
- List: `1 -2 4 3 5 6`
- Swaps: `1`

![Example Visualization](../images/LNK-003/example-1.png)

## ✅ Proof of Correctness

### Invariant
After processing `i` pairs, the first `2i` nodes are in their final state relative to each other (swapped or not), and `prev` points to the `2i`-th node.

### Why the approach is correct
- We process pairs sequentially.
- The logic strictly follows the problem constraints: check negativity, check K, then swap or skip.
- Pointer manipulation for swapping is standard and correct (`prev -> second -> first -> rest`).
- The loop terminates when fewer than 2 nodes remain, which is correct for pair processing.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Swap nodes in groups of `k` (Reverse Nodes in k-Group).
- **Extension 2:** Only swap if the sum of the pair is even.
  - *Hint:* Change the condition `nonNegative` to `(first.val + second.val) % 2 == 0`.
- **Extension 3:** Recursive solution.
  - *Hint:* `swap(head)` calls `swap(head.next.next)`. Easier to write but uses O(N) stack space.

### Common Mistakes to Avoid

1. **Broken Links**
   - ❌ Wrong: `first.next = second.next; second.next = first;` without updating `prev.next`.
   - ✅ Correct: You must update the node *before* the pair (`prev`) to point to the new first node (`second`).

2. **Infinite Loop**
   - ❌ Wrong: Not advancing `prev` correctly after a swap or skip.
   - ✅ Correct: If swapped, `prev` moves to `first` (new 2nd node). If skipped, `prev` moves to `second` (existing 2nd node).

3. **Edge Cases**
   - ❌ Wrong: Crashing on empty list or single-node list.
   - ✅ Correct: Check `head == null || head.next == null` at the start.

## Related Concepts

- **Dummy Node:** Essential pattern for operations that might change the head.
- **Two Pointers:** Used here to track the pair being swapped.
- **Greedy Algorithms:** We swap whenever we can until K runs out (locally optimal choice).
