---
problem_id: LNK_ROBOTICS_CHUNK_REVERSE_OFFSET_COUNT__6837
display_id: LNK-009
slug: robotics-chunk-reverse-offset-count
title: "Robotics Chunk Reverse with Offset and Reversal Count"
difficulty: Medium
difficulty_score: 55
topics:
  - Linked List
  - Reversal
  - Simulation
tags:
  - linked-list
  - reversal
  - counting
  - medium
premium: true
subscription_tier: basic
---

# LNK-009: Robotics Chunk Reverse with Offset and Reversal Count

## 📋 Problem Summary

You are given a linked list. Starting from a 1-based index `s`, you need to reverse nodes in groups of size `k`.
- Nodes before `s` are untouched.
- From `s`, reverse every full group of `k`.
- If a group has fewer than `k` nodes (at the end), leave it as is.
- Return the modified list, the count of groups reversed, and the sum of values of all nodes that were moved/reversed.

## 🌍 Real-World Scenario

**Scenario Title:** The Assembly Line Flipper

A robotic arm is installed on a factory conveyor belt. Its job is to flip batches of products for quality inspection (checking the bottom side).
- The arm is positioned at station `s`. Products before this station pass through normally.
- The arm grabs `k` products at a time and flips their order.
- If fewer than `k` products arrive at the end of the shift, the arm doesn't have enough grip to flip them, so they pass through unflipped.
- The system needs to track how many batches were flipped and the total value of inventory processed by the flipper.

**Why This Problem Matters:**

- **Batch Processing:** Handling data in fixed-size chunks (transactions, logs) starting from a specific offset.
- **Memory Paging:** Reordering pages or blocks in memory management systems.
- **Stream Processing:** Applying transformations to windows of data in a continuous stream.

![Real-World Application](../images/LNK-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Chunk Reversal

List: `1 -> 2 -> 3 -> 4 -> 5`
`k=2`, `s=3`

1. **Skip to Offset:**
   Skip `1 -> 2`. Pointer arrives at 2 (before 3).

2. **Check Group 1:**
   Next nodes: `3, 4`. Count = 2. `2 >= k`.
   **Reverse:** `3 -> 4` becomes `4 -> 3`.
   List: `1 -> 2 -> 4 -> 3 -> 5`
   Stats: `reversed_groups = 1`, `sum = 3 + 4 = 7`.

3. **Check Group 2:**
   Next nodes: `5`. Count = 1. `1 < k`.
   **Skip:** Leave `5` alone.

Final: `1 -> 2 -> 4 -> 3 -> 5`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **1-based Indexing:** `s=1` means start at the head.
- **Full Groups Only:** Unlike some variations where the tail is reversed, here the problem says "reverse each full group... leftover tail... stays as-is".
- **Sum Calculation:** Sum the values of nodes *inside* the reversed groups. Do not include nodes before `s` or in the unreversed tail.

Common interpretation mistake:

- ❌ **Wrong:** Reversing the tail even if length < k.
- ✅ **Correct:** Only reverse if you confirm `k` nodes exist.

### Core Concept: Lookahead

Before reversing, you must traverse `k` nodes ahead to ensure the group is complete. If you hit `null`, stop.

## Naive Approach

### Intuition

Convert list to array. Perform operations on array. Convert back.

### Algorithm

1. List -> Array.
2. Iterate `i` from `s-1` to `n` with step `k`.
3. If `i + k <= n`:
   - Reverse subarray `[i, i+k-1]`.
   - Add values to sum.
   - Increment count.
4. Array -> List.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

In-place reversal with a "probe" pointer to check for existence of `k` nodes.

### Algorithm

1. Use `dummy` node. Move `prev` to `s-1`.
2. Loop:
   - **Probe:** Send a pointer `probe` forward `k` steps.
   - If `probe` hits `null`: break loop (tail too short).
   - **Reverse:**
     - Standard reversal of `k` nodes starting at `prev.next`.
     - Accumulate values during reversal.
     - Update `reversedGroups`.
     - Link `prev` to new head, new tail to rest.
     - Move `prev` to new tail.

### Time Complexity

- **O(N)**. Each node is visited at most twice (once by probe, once by reverse).

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-009/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-009/algorithm-steps.png)

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
    int reversedGroups;
    long sum;
    Result(ListNode head, int reversedGroups, long sum) {
        this.head = head;
        this.reversedGroups = reversedGroups;
        this.sum = sum;
    }
}

class Solution {
    public Result reverseFromOffset(ListNode head, int k, int s) {
        if (head == null || k <= 1) return new Result(head, 0, 0L);

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        // Move to s-1
        for (int i = 0; i < s - 1; i++) {
            if (prev.next == null) return new Result(head, 0, 0L);
            prev = prev.next;
        }

        int groups = 0;
        long totalSum = 0;

        while (true) {
            // Probe k steps
            ListNode probe = prev;
            for (int i = 0; i < k; i++) {
                probe = probe.next;
                if (probe == null) return new Result(dummy.next, groups, totalSum);
            }

            // Reverse k nodes
            ListNode tail = prev.next;
            ListNode curr = tail.next;
            long groupSum = tail.val;
            
            for (int i = 1; i < k; i++) {
                groupSum += curr.val;
                ListNode temp = curr.next;
                curr.next = prev.next;
                prev.next = curr;
                tail.next = temp;
                curr = temp;
            }
            
            groups++;
            totalSum += groupSum;
            prev = tail; // Move prev to end of reversed group
        }
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
        
        int k = sc.nextInt();
        int s = sc.nextInt();

        Solution solution = new Solution();
        Result res = solution.reverseFromOffset(dummy.next, k, s);
        
        ListNode out = res.head;
        boolean first = true;
        while (out != null) {
            if (!first) System.out.print(" ");
            System.out.print(out.val);
            first = false;
            out = out.next;
        }
        System.out.println();
        System.out.println(res.reversedGroups);
        System.out.println(res.sum);
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

def reverse_from_offset(head: ListNode, k: int, s: int):
    if not head or k <= 1:
        return head, 0, 0
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to s-1
    for _ in range(s - 1):
        if not prev.next:
            return head, 0, 0
        prev = prev.next
        
    groups = 0
    total_sum = 0
    
    while True:
        # Probe
        probe = prev
        for _ in range(k):
            probe = probe.next
            if not probe:
                return dummy.next, groups, total_sum
        
        # Reverse
        tail = prev.next
        curr = tail.next
        group_sum = tail.val
        
        for _ in range(k - 1):
            group_sum += curr.val
            temp = curr.next
            curr.next = prev.next
            prev.next = curr
            tail.next = temp
            curr = temp
            
        groups += 1
        total_sum += group_sum
        prev = tail
        
    return dummy.next, groups, total_sum

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
            
        k = int(next(iterator))
        s = int(next(iterator))
        
        head, groups, total_sum = reverse_from_offset(dummy.next, k, s)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
        print(groups)
        print(total_sum)
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

struct Result {
    ListNode* head;
    int reversedGroups;
    long long sum;
};

class Solution {
public:
    Result reverseFromOffset(ListNode* head, int k, int s) {
        if (!head || k <= 1) return {head, 0, 0};

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        // Move to s-1
        for (int i = 0; i < s - 1; i++) {
            if (!prev->next) return {head, 0, 0};
            prev = prev->next;
        }

        int groups = 0;
        long long totalSum = 0;

        while (true) {
            // Probe
            ListNode* probe = prev;
            for (int i = 0; i < k; i++) {
                probe = probe->next;
                if (!probe) return {dummy.next, groups, totalSum};
            }

            // Reverse
            ListNode* tail = prev->next;
            ListNode* curr = tail->next;
            long long groupSum = tail->val;

            for (int i = 1; i < k; i++) {
                groupSum += curr->val;
                ListNode* temp = curr->next;
                curr->next = prev->next;
                prev->next = curr;
                tail->next = temp;
                curr = temp;
            }

            groups++;
            totalSum += groupSum;
            prev = tail;
        }
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
    
    int k, s;
    cin >> k >> s;

    Solution solution;
    Result res = solution.reverseFromOffset(dummy.next, k, s);
    
    ListNode* out = res.head;
    bool first = true;
    while (out) {
        if (!first) cout << " ";
        cout << out->val;
        first = false;
        out = out->next;
    }
    cout << "\n" << res.reversedGroups << "\n" << res.sum << "\n";
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

function reverseFromOffset(head, k, s) {
  if (!head || k <= 1) return [head, 0, 0];

  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;

  // Move to s-1
  for (let i = 0; i < s - 1; i++) {
    if (!prev.next) return [head, 0, 0];
    prev = prev.next;
  }

  let groups = 0;
  let totalSum = 0;

  while (true) {
    // Probe
    let probe = prev;
    for (let i = 0; i < k; i++) {
      probe = probe.next;
      if (!probe) return [dummy.next, groups, totalSum];
    }

    // Reverse
    let tail = prev.next;
    let curr = tail.next;
    let groupSum = tail.val;

    for (let i = 1; i < k; i++) {
      groupSum += curr.val;
      let temp = curr.next;
      curr.next = prev.next;
      prev.next = curr;
      tail.next = temp;
      curr = temp;
    }

    groups++;
    totalSum += groupSum;
    prev = tail;
  }
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
      const k = parseInt(data[idx++], 10);
      const s = parseInt(data[idx++], 10);

      const result = reverseFromOffset(dummy.next, k, s);
      let head = result[0];
      const groups = result[1];
      const sum = result[2];
      
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
      console.log(groups);
      console.log(sum);
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 2 3 4 5`, `k=2`, `s=3`

**Initialization:**
- `dummy -> 1 -> 2 -> 3 -> 4 -> 5`
- Move `prev` to node 2 (index 2, just before s=3).

**Iteration 1:**
- Probe: 2 steps from `prev`.
  - Step 1: Node 3.
  - Step 2: Node 4.
  - Exists!
- Reverse `3, 4`.
  - `tail` = 3. `curr` = 4.
  - `groupSum` = 3 + 4 = 7.
  - List: `1 -> 2 -> 4 -> 3 -> 5`.
- `groups` = 1. `totalSum` = 7.
- `prev` moves to 3.

**Iteration 2:**
- Probe: 2 steps from `prev` (3).
  - Step 1: Node 5.
  - Step 2: `null`.
  - Probe failed. Return.

**Result:**
- List: `1 2 4 3 5`
- Groups: 1
- Sum: 7

![Example Visualization](../images/LNK-009/example-1.png)

## ✅ Proof of Correctness

### Invariant
`prev` always points to the node immediately preceding the next potential group to be reversed. The list structure before `prev` is final.

### Why the approach is correct
- **Probe:** Ensures we never start reversing a partial group, satisfying the requirement.
- **Offset:** The initial loop correctly positions `prev` to respect `s`.
- **Reversal:** Standard pointer manipulation preserves connectivity.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Reverse Nodes in k-Group (Standard).
  - *Diff:* `s=1` always.
- **Extension 2:** Reverse alternate groups.
  - *Hint:* Add a `skip` step after each reverse.
- **Extension 3:** Maximize sum of reversed nodes by choosing optimal `s`.
  - *Hint:* Sliding window of size `k`.

### Common Mistakes to Avoid

1. **Probe Logic**
   - ❌ Wrong: Reversing and then checking length.
   - ✅ Correct: Check length first (probe), then reverse.

2. **Summing Unreversed Nodes**
   - ❌ Wrong: Adding values of the tail group.
   - ✅ Correct: Only add values inside the `reverse` block.

3. **Index math**
   - ❌ Wrong: `s` is 0-based.
   - ✅ Correct: `s` is 1-based. Loop `s-1` times.

## Related Concepts

- **Lookahead:** Checking conditions before modifying structure.
- **In-place Reversal:** Key linked list technique.
