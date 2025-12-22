---
problem_id: LNK_LAB_LOOP_DETECTOR_ENTRY_LENGTH__8412
display_id: LNK-006
slug: lab-loop-detector-entry-length
title: "Lab Loop Detector with Entry Index and Cycle Length"
difficulty: Medium
difficulty_score: 56
topics:
  - Linked List
  - Cycle Detection
  - Two Pointers
tags:
  - linked-list
  - cycle
  - two-pointers
  - medium
premium: true
subscription_tier: basic
---

# LNK-006: Lab Loop Detector with Entry Index and Cycle Length

## 📋 Problem Summary

You are given a linked list that might contain a cycle. If a cycle exists, you need to determine:
1. The **index** where the cycle begins (0-based).
2. The **length** of the cycle (number of nodes in the loop).
3. The **maximum value** among all nodes in the cycle.

If no cycle exists, return `{-1, 0, 0}`.

## 🌍 Real-World Scenario

**Scenario Title:** The Infinite Loop Debugger

You are building a debugger for a new programming language. Sometimes, users write code that gets stuck in an infinite loop. Your debugger needs to analyze the execution trace (represented as a linked list of states) to detect if the program has entered a repeating cycle.

If it has, you want to tell the user:
- "The loop starts at step #X." (Entry Index)
- "The loop repeats every Y steps." (Cycle Length)
- "The highest memory usage seen in this loop was Z." (Max Value)

**Why This Problem Matters:**

- **Deadlock Detection:** In operating systems, resource allocation graphs are checked for cycles to detect deadlocks.
- **Network Routing:** Detecting routing loops where packets circulate indefinitely.
- **Garbage Collection:** Reference counting fails with cyclic references; mark-and-sweep algorithms need to handle graph cycles.

![Real-World Application](../images/LNK-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Floyd's Cycle Detection

We use two pointers: `slow` (moves 1 step) and `fast` (moves 2 steps).

```
List: 1 -> 2 -> 3 -> 4 -> 5
                ^         |
                |_________|
Cycle: 3 -> 4 -> 5 -> 3 ...

Step 1: Slow=1, Fast=1
Step 2: Slow=2, Fast=3
Step 3: Slow=3, Fast=5
Step 4: Slow=4, Fast=4 (MEETING POINT!)
```

Once they meet, we know a cycle exists. But the meeting point is NOT necessarily the entry point.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **0-based Indexing:** The head is at index 0.
- **No Cycle:** Return `-1 0 0`.
- **Max Value:** Only consider nodes *inside* the cycle, not the "tail" leading up to it.

Common interpretation mistake:

- ❌ **Wrong:** Assuming the meeting point is the start of the cycle.
- ✅ **Correct:** The meeting point is just *some* node inside the cycle. You need a second phase to find the entry.

### Core Concept: The Mathematics of Floyd's Algorithm

Let:
- $L$ = distance from head to cycle entry.
- $C$ = length of cycle.
- $X$ = distance from entry to meeting point.

When they meet:
- Slow has traveled $L + X$.
- Fast has traveled $L + X + nC$ (where $n$ is loops fast made).
- Fast travels twice as fast: $2(L + X) = L + X + nC$.
- Simplifying: $L + X = nC \implies L = nC - X$.

This means the distance from head to entry ($L$) is equal to the distance from meeting point to entry ($C - X$) plus some multiple of cycle lengths. So, if we move one pointer from `head` and one from `meeting point` at same speed, they will meet at the entry!

## Naive Approach

### Intuition

Use a Hash Set to store visited nodes. Traverse the list. If we see a node already in the set, that's the entry point.

### Algorithm

1. Create `visited` map: Node -> Index.
2. Traverse list with `index` counter.
3. If `curr` in `visited`:
   - Entry Index = `visited[curr]`.
   - Cycle Length = `current_index - visited[curr]`.
   - Traverse cycle again to find max value.
   - Return info.
4. Add `curr` to `visited`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**. This uses extra memory, which we want to avoid.

## Optimal Approach

### Key Insight

Use Floyd's Tortoise and Hare algorithm for O(1) space.

### Algorithm

1. **Detection:**
   - `slow = head`, `fast = head`.
   - Loop: `slow` moves 1, `fast` moves 2.
   - If `fast` reaches null, no cycle. Return `-1 0 0`.
   - If `slow == fast`, cycle detected.

2. **Find Entry:**
   - Reset `slow = head`. Keep `fast` at meeting point.
   - Move both 1 step at a time.
   - Maintain an `index` counter for `slow`.
   - When they meet, that node is the **Entry**. `entry_index` is the counter.

3. **Analyze Cycle:**
   - Start from `Entry`.
   - Traverse `next` pointers until you return to `Entry`.
   - Count nodes (`length`).
   - Track `max_val`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/LNK-006/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-006/algorithm-steps.png)

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
    public int[] cycleInfo(ListNode head) {
        if (head == null) return new int[]{-1, 0, 0};

        ListNode slow = head;
        ListNode fast = head;
        boolean hasCycle = false;

        // Phase 1: Detect Cycle
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }

        if (!hasCycle) return new int[]{-1, 0, 0};

        // Phase 2: Find Entry
        ListNode entry = head;
        int entryIndex = 0;
        while (entry != slow) {
            entry = entry.next;
            slow = slow.next;
            entryIndex++;
        }

        // Phase 3: Cycle Stats
        int length = 0;
        int maxVal = Integer.MIN_VALUE;
        ListNode curr = entry;
        do {
            length++;
            maxVal = Math.max(maxVal, curr.val);
            curr = curr.next;
        } while (curr != entry);

        return new int[]{entryIndex, length, maxVal};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        ListNode[] nodes = new ListNode[n];
        for (int i = 0; i < n; i++) {
            cur.next = new ListNode(sc.nextInt());
            cur = cur.next;
            nodes[i] = cur;
        }
        
        int pos = sc.nextInt();
        if (pos >= 0 && n > 0) {
            cur.next = nodes[pos];
        }

        Solution solution = new Solution();
        int[] res = solution.cycleInfo(dummy.next);
        System.out.println(res[0] + " " + res[1] + " " + res[2]);
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

def cycle_info(head: ListNode):
    if not head:
        return (-1, 0, 0)
    
    slow = head
    fast = head
    has_cycle = False
    
    # Phase 1: Detect
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return (-1, 0, 0)
        
    # Phase 2: Find Entry
    entry = head
    entry_index = 0
    while entry != slow:
        entry = entry.next
        slow = slow.next
        entry_index += 1
        
    # Phase 3: Stats
    length = 0
    max_val = -float('inf')
    curr = entry
    while True:
        length += 1
        max_val = max(max_val, curr.val)
        curr = curr.next
        if curr == entry:
            break
            
    return (entry_index, length, max_val)

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
        nodes = []
        for _ in range(n):
            node = ListNode(int(next(iterator)))
            cur.next = node
            cur = cur.next
            nodes.append(node)
            
        pos = int(next(iterator))
        if pos >= 0 and n > 0:
            cur.next = nodes[pos]
            
        entry, length, max_val = cycle_info(dummy.next)
        print(f"{entry} {length} {max_val}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    vector<int> cycleInfo(ListNode* head) {
        if (!head) return {-1, 0, 0};

        ListNode* slow = head;
        ListNode* fast = head;
        bool hasCycle = false;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }

        if (!hasCycle) return {-1, 0, 0};

        ListNode* entry = head;
        int entryIndex = 0;
        while (entry != slow) {
            entry = entry->next;
            slow = slow->next;
            entryIndex++;
        }

        int length = 0;
        int maxVal = INT_MIN;
        ListNode* curr = entry;
        do {
            length++;
            maxVal = max(maxVal, curr->val);
            curr = curr->next;
        } while (curr != entry);

        return {entryIndex, length, maxVal};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    ListNode dummy(0);
    ListNode* cur = &dummy;
    vector<ListNode*> nodes;
    nodes.reserve(n);
    
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        cur->next = new ListNode(v);
        cur = cur->next;
        nodes.push_back(cur);
    }
    
    int pos;
    cin >> pos;
    if (pos >= 0 && n > 0) {
        cur->next = nodes[pos];
    }

    Solution solution;
    vector<int> res = solution.cycleInfo(dummy.next);
    cout << res[0] << " " << res[1] << " " << res[2] << "\n";
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

function cycleInfo(head) {
  if (!head) return [-1, 0, 0];

  let slow = head;
  let fast = head;
  let hasCycle = false;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      hasCycle = true;
      break;
    }
  }

  if (!hasCycle) return [-1, 0, 0];

  let entry = head;
  let entryIndex = 0;
  while (entry !== slow) {
    entry = entry.next;
    slow = slow.next;
    entryIndex++;
  }

  let length = 0;
  let maxVal = -Infinity;
  let curr = entry;
  do {
    length++;
    maxVal = Math.max(maxVal, curr.val);
    curr = curr.next;
  } while (curr !== entry);

  return [entryIndex, length, maxVal];
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
  const nodes = [];
  for (let i = 0; i < n; i++) {
    const node = new ListNode(parseInt(data[idx++], 10));
    cur.next = node;
    cur = cur.next;
    nodes.push(node);
  }
  
  if (idx < data.length) {
      const pos = parseInt(data[idx++], 10);
      if (pos >= 0 && n > 0) {
        cur.next = nodes[pos];
      }
      
      const res = cycleInfo(dummy.next);
      console.log(res.join(" "));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 2 3 4`, `pos=1`
List: `1 -> 2 -> 3 -> 4 -> 2...`

**Phase 1: Detection**
- S=1, F=1
- S=2, F=3
- S=3, F=2 (wrap)
- S=4, F=4 (MEET at node 4)

**Phase 2: Entry**
- Reset `entry` to head (1). `slow` stays at 4.
- `entry` moves to 2. `slow` moves to 2.
- Meet at node 2!
- `entryIndex` = 1.

**Phase 3: Stats**
- Start at 2.
- Visit 3 (len=1, max=3)
- Visit 4 (len=2, max=4)
- Visit 2 (len=3, max=4) -> Stop.

Result: `1 3 4`.

![Example Visualization](../images/LNK-006/example-1.png)

## ✅ Proof of Correctness

### Invariant
Floyd's algorithm guarantees that if a cycle exists, `fast` will eventually lap `slow` and they will meet inside the cycle.

### Why the approach is correct
- **Detection:** Standard proof. Fast closes gap by 1 each step.
- **Entry:** Mathematical derivation $L = nC - X$ proves they meet at entry.
- **Stats:** Once entry is known, traversing until we hit entry again covers exactly one full cycle.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Brent's Algorithm.
  - *Hint:* An alternative cycle detection algorithm that is often faster on average (though same worst-case complexity).
- **Extension 2:** Find median of the cycle.
  - *Hint:* Store cycle nodes in array/list, sort/select.
- **Extension 3:** Remove the cycle.
  - *Hint:* Once you find the entry, find the node pointing to it and set `next = null`.

### Common Mistakes to Avoid

1. **Null Checks**
   - ❌ Wrong: `while (fast.next != null)` without checking `fast`.
   - ✅ Correct: `while (fast != null && fast.next != null)`.

2. **Entry Logic**
   - ❌ Wrong: Assuming meeting point is entry.
   - ✅ Correct: Must reset one pointer to head.

3. **Max Value Init**
   - ❌ Wrong: `maxVal = 0`.
   - ✅ Correct: `maxVal = Integer.MIN_VALUE` (nodes can be negative).

## Related Concepts

- **Floyd's Cycle-Finding Algorithm:** The core concept.
- **Modular Arithmetic:** Underlying the "lapping" logic.
- **Functional Programming:** Infinite streams often use lazy evaluation which can be modeled as potentially cyclic lists.
