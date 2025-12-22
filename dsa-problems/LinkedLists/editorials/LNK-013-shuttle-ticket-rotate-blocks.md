---
problem_id: LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__8156
display_id: LNK-013
slug: shuttle-ticket-rotate-blocks
title: "Shuttle Ticket Rotate by Blocks"
difficulty: Medium
difficulty_score: 46
topics:
  - Linked List
  - Rotation
  - Block Processing
tags:
  - linked-list
  - rotation
  - blocks
  - medium
premium: true
subscription_tier: basic
---

# LNK-013: Shuttle Ticket Rotate by Blocks

## 📋 Problem Summary

You are given a linked list. You need to divide it into consecutive blocks of size `b`. For each block, rotate its nodes to the right by `k` positions.
- If the last block has fewer than `b` nodes, rotate it by `k` relative to its actual size.
- Concatenate the rotated blocks to form the final list.

## 🌍 Real-World Scenario

**Scenario Title:** The Shift Scheduler

A factory has `N` workers standing in a line. They are divided into teams of size `b`. Every week, the manager rotates the roles within each team by `k` positions to ensure everyone learns every job.
- Team 1: Workers 1-3. Rotate by 1 -> Worker 3 moves to front.
- Team 2: Workers 4-6. Rotate by 1 -> Worker 6 moves to front.
- Team 3: Workers 7-8 (incomplete team). Rotate by 1 -> Worker 8 moves to front.

You need to generate the new lineup order.

**Why This Problem Matters:**

- **Cryptography:** Block ciphers often involve permuting or rotating bits within fixed-size blocks.
- **UI Carousels:** Multiple independent carousels on a page rotating their content.
- **Data Batching:** Processing batches of data where the processing order within each batch is cyclic.

![Real-World Application](../images/LNK-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Block Rotation

List: `1 -> 2 -> 3 -> 4 -> 5 -> 6`
`b = 3`, `k = 1`

**Block 1:** `1 -> 2 -> 3`
- Size = 3.
- Rotate Right by `1 % 3 = 1`.
- Result: `3 -> 1 -> 2`.

**Block 2:** `4 -> 5 -> 6`
- Size = 3.
- Rotate Right by `1 % 3 = 1`.
- Result: `6 -> 4 -> 5`.

**Concatenate:**
`3 -> 1 -> 2` -> `6 -> 4 -> 5`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Independent Rotations:** Rotating block 1 does not affect block 2.
- **Last Block:** If `N=5, b=3`, the second block has size 2. Rotate it by `k % 2`.
- **Large K:** `k` can be very large, so always use modulo arithmetic.

Common interpretation mistake:

- ❌ **Wrong:** Rotating the entire list first, then splitting.
- ✅ **Correct:** Split first, then rotate each piece.

### Core Concept: Isolate and Rotate

To solve this cleanly, write a helper function `rotate(head, length, k)` that rotates a standalone list. Then, iterate through the main list, cutting out chunks of size `b`, rotating them, and stitching them back together.

## Naive Approach

### Intuition

Convert list to array. Process chunks in array. Convert back.

### Algorithm

1. List -> ArrayList.
2. For `i = 0` to `n` step `b`:
   - Extract sublist `[i, min(i+b, n))`.
   - Rotate sublist.
   - Append to result.
3. Array -> List.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

In-place manipulation. Maintain a `tail` pointer for the *previous* block to link to the *current* rotated block.

### Algorithm

1. `dummy` points to head. `prevTail = dummy`.
2. Loop while `head` exists:
   - **Identify Block:** Traverse `b` nodes to find the end of the current block. Count actual length `len`.
   - **Detach:** Save `nextBlockHead`. Break the link after the current block.
   - **Rotate:** Perform standard linked list rotation on the current block (size `len`, shift `k`).
   - **Attach:**
     - `prevTail.next = newBlockHead`
     - `prevTail = newBlockTail`
   - **Advance:** `head = nextBlockHead`.

### Time Complexity

- **O(N)**. We visit each node a constant number of times.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-013/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-013/algorithm-steps.png)

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
    public ListNode rotateBlocks(ListNode head, int b, int k) {
        if (head == null || b <= 0) return head;

        ListNode dummy = new ListNode(0);
        ListNode prevTail = dummy;
        ListNode curr = head;

        while (curr != null) {
            // 1. Identify block start and end
            ListNode blockHead = curr;
            ListNode blockTail = curr;
            int len = 1;
            
            // Move b-1 steps to find tail of block
            for (int i = 0; i < b - 1 && blockTail.next != null; i++) {
                blockTail = blockTail.next;
                len++;
            }
            
            // 2. Detach
            ListNode nextBlockHead = blockTail.next;
            blockTail.next = null; // Cut
            
            // 3. Rotate
            ListNode[] rotated = rotateList(blockHead, len, k);
            
            // 4. Attach
            prevTail.next = rotated[0]; // New head
            prevTail = rotated[1];      // New tail
            
            // 5. Advance
            curr = nextBlockHead;
        }

        return dummy.next;
    }

    // Returns [newHead, newTail]
    private ListNode[] rotateList(ListNode head, int len, int k) {
        if (len <= 1 || k % len == 0) {
            // Find tail
            ListNode tail = head;
            while (tail.next != null) tail = tail.next;
            return new ListNode[]{head, tail};
        }

        k = k % len;
        int moves = len - k; // Moves to new tail

        ListNode newTail = head;
        for (int i = 0; i < moves - 1; i++) {
            newTail = newTail.next;
        }
        
        ListNode newHead = newTail.next;
        newTail.next = null; // Break ring
        
        // Find end of newHead to link to old head? 
        // 1->2->3, k=1. len=3. moves=2.
        // newTail = 2. newHead = 3.
        // 3->null. Need 3->1->2.
        
        ListNode temp = newHead;
        while (temp.next != null) temp = temp.next;
        temp.next = head; // Link end to start
        
        return new ListNode[]{newHead, newTail};
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
        int b = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        ListNode res = solution.rotateBlocks(dummy.next, b, k);
        
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

def rotate_list(head: ListNode, length: int, k: int):
    if length <= 1 or k % length == 0:
        tail = head
        while tail.next:
            tail = tail.next
        return head, tail
    
    k = k % length
    moves = length - k
    
    new_tail = head
    for _ in range(moves - 1):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    new_tail.next = None
    
    temp = new_head
    while temp.next:
        temp = temp.next
    temp.next = head
    
    return new_head, new_tail

def rotate_blocks(head: ListNode, b: int, k: int) -> ListNode:
    if not head or b <= 0:
        return head
        
    dummy = ListNode(0)
    prev_tail = dummy
    curr = head
    
    while curr:
        block_head = curr
        block_tail = curr
        length = 1
        
        # Find block end
        for _ in range(b - 1):
            if not block_tail.next:
                break
            block_tail = block_tail.next
            length += 1
            
        next_block_head = block_tail.next
        block_tail.next = None # Detach
        
        # Rotate
        new_head, new_tail = rotate_list(block_head, length, k)
        
        # Attach
        prev_tail.next = new_head
        prev_tail = new_tail
        
        curr = next_block_head
        
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
            
        b = int(next(iterator))
        k = int(next(iterator))
        
        head = rotate_blocks(dummy.next, b, k)
        
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
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* rotateBlocks(ListNode* head, int b, int k) {
        if (!head || b <= 0) return head;

        ListNode dummy(0);
        ListNode* prevTail = &dummy;
        ListNode* curr = head;

        while (curr) {
            ListNode* blockHead = curr;
            ListNode* blockTail = curr;
            int len = 1;

            for (int i = 0; i < b - 1 && blockTail->next; i++) {
                blockTail = blockTail->next;
                len++;
            }

            ListNode* nextBlockHead = blockTail->next;
            blockTail->next = nullptr;

            pair<ListNode*, ListNode*> rotated = rotateList(blockHead, len, k);
            
            prevTail->next = rotated.first;
            prevTail = rotated.second;

            curr = nextBlockHead;
        }

        return dummy.next;
    }

private:
    pair<ListNode*, ListNode*> rotateList(ListNode* head, int len, int k) {
        if (len <= 1 || k % len == 0) {
            ListNode* tail = head;
            while (tail->next) tail = tail->next;
            return {head, tail};
        }

        k %= len;
        int moves = len - k;

        ListNode* newTail = head;
        for (int i = 0; i < moves - 1; i++) {
            newTail = newTail->next;
        }

        ListNode* newHead = newTail->next;
        newTail->next = nullptr;

        ListNode* temp = newHead;
        while (temp->next) temp = temp->next;
        temp->next = head;

        return {newHead, newTail};
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
    int b, k;
    cin >> b >> k;

    Solution solution;
    ListNode* res = solution.rotateBlocks(dummy.next, b, k);
    
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

function rotateList(head, len, k) {
  if (len <= 1 || k % len === 0) {
    let tail = head;
    while (tail.next) tail = tail.next;
    return [head, tail];
  }

  k = k % len;
  let moves = len - k;

  let newTail = head;
  for (let i = 0; i < moves - 1; i++) {
    newTail = newTail.next;
  }

  let newHead = newTail.next;
  newTail.next = null;

  let temp = newHead;
  while (temp.next) temp = temp.next;
  temp.next = head;

  return [newHead, newTail];
}

function rotateBlocks(head, b, k) {
  if (!head || b <= 0) return head;

  const dummy = new ListNode(0);
  let prevTail = dummy;
  let curr = head;

  while (curr) {
    let blockHead = curr;
    let blockTail = curr;
    let len = 1;

    for (let i = 0; i < b - 1 && blockTail.next; i++) {
      blockTail = blockTail.next;
      len++;
    }

    let nextBlockHead = blockTail.next;
    blockTail.next = null;

    const [newHead, newTail] = rotateList(blockHead, len, k);

    prevTail.next = newHead;
    prevTail = newTail;

    curr = nextBlockHead;
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
      const b = parseInt(data[idx++], 10);
      const k = parseInt(data[idx++], 10);

      let head = rotateBlocks(dummy.next, b, k);
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

Input: `1 2 3 4 5 6`, `b=3`, `k=1`

**Block 1:**
- `curr` at 1. `blockTail` moves 2 steps to 3. `len`=3.
- `nextBlockHead` = 4. Detach 3->null.
- Rotate `1->2->3` right by 1.
  - `moves` = 3 - 1 = 2.
  - `newTail` moves 1 step to 2.
  - `newHead` = 3.
  - Link 3->1. Break 2->null.
  - Result: `3->1->2`.
- Attach to dummy: `dummy->3->1->2`. `prevTail` = 2.

**Block 2:**
- `curr` at 4. `blockTail` moves 2 steps to 6. `len`=3.
- `nextBlockHead` = null. Detach 6->null.
- Rotate `4->5->6` right by 1.
  - Result: `6->4->5`.
- Attach to `prevTail`: `2->6->4->5`. `prevTail` = 5.

**Result:** `3 1 2 6 4 5`.

![Example Visualization](../images/LNK-013/example-1.png)

## ✅ Proof of Correctness

### Invariant
The list processed so far consists of fully rotated blocks in their correct relative order. `prevTail` always points to the last node of the processed portion.

### Why the approach is correct
- **Isolation:** Detaching blocks prevents rotation logic from messing up the rest of the list.
- **Modularity:** Using a standard `rotateList` function ensures correctness for edge cases (k=0, k>len).
- **Connectivity:** We explicitly track `prevTail` to stitch the result back together.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Rotate Left instead of Right.
  - *Hint:* `Rotate Left(k)` is same as `Rotate Right(len - k)`.
- **Extension 2:** Reverse blocks instead of rotate.
  - *Hint:* This is "Reverse Nodes in k-Group".
- **Extension 3:** Variable block sizes (given as an array).
  - *Hint:* Pass `sizes[i]` to the loop instead of constant `b`.

### Common Mistakes to Avoid

1. **Tail Linking**
   - ❌ Wrong: Forgetting to link the new tail of a rotated block to the *next* block (though our loop handles this by linking `prevTail` to `newHead` in the next iteration).
   - ✅ Correct: Our approach links `prevTail.next = newHead`.

2. **Modulo Arithmetic**
   - ❌ Wrong: `k % b` (using block size constant).
   - ✅ Correct: `k % len` (using actual length, which might be smaller for the last block).

## Related Concepts

- **List Rotation:** Standard problem.
- **Block Processing:** Breaking problems into chunks.
- **In-place Manipulation:** Avoiding extra arrays.
