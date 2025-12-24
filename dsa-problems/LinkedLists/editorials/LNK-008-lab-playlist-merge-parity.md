---
problem_id: LNK_LAB_PLAYLIST_MERGE_PARITY__5863
display_id: LNK-008
slug: lab-playlist-merge-parity
title: "Lab Playlist Merge by Parity"
difficulty: Medium
difficulty_score: 42
topics:
  - Linked List
  - Merge
  - Stable Ordering
tags:
  - linked-list
  - merge
  - parity
  - medium
premium: true
subscription_tier: basic
---

# LNK-008: Lab Playlist Merge by Parity

## 📋 Problem Summary

You are given two sorted linked lists. You need to merge them into a single list such that:
1. All **even** numbers come before all **odd** numbers.
2. The relative order of even numbers is preserved (stable).
3. The relative order of odd numbers is preserved (stable).
4. You process the first list, then the second list (or merge them, but the problem implies just collecting evens then odds from the inputs).

*Correction based on Example:* The example shows `1 4 7` and `2 3 10` becoming `4 2 10 1 7 3`.
- Evens: 4 (from L1), 2 (from L2), 10 (from L2).
- Odds: 1 (from L1), 7 (from L1), 3 (from L2).
This implies we process L1 entirely, then L2 entirely (or just iterate through them in order) and bucket them into Evens and Odds.

## 🌍 Real-World Scenario

**Scenario Title:** The Party Playlist Mixer

You are the DJ for a party. You have two playlists: "Oldies" (List 1) and "New Hits" (List 2). Both are sorted by popularity.
You want to play all the **High Energy** songs (Even BPMs) first to get people dancing, followed by the **Chill** songs (Odd BPMs) for the cool-down.
However, within the "High Energy" block, you want to respect the original popularity order: play the best Oldies high-energy songs, then the best New Hits high-energy songs. Same for the Chill block.

**Why This Problem Matters:**

- **Priority Scheduling:** Executing high-priority tasks (Evens) from multiple queues before low-priority tasks (Odds).
- **Data Partitioning:** Separating data into two streams (e.g., valid vs. invalid transactions) while maintaining the original timestamp order.
- **Log Processing:** separating error logs from info logs from multiple source files.

![Real-World Application](../images/LNK-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Partitioning

List 1: `1 -> 4 -> 7`
List 2: `2 -> 3 -> 10`

We maintain two chains: `Evens` and `Odds`.

**Processing List 1:**
- Node 1 (Odd): Add to Odds. `Odds: 1`
- Node 4 (Even): Add to Evens. `Evens: 4`
- Node 7 (Odd): Add to Odds. `Odds: 1 -> 7`

**Processing List 2:**
- Node 2 (Even): Add to Evens. `Evens: 4 -> 2`
- Node 3 (Odd): Add to Odds. `Odds: 1 -> 7 -> 3`
- Node 10 (Even): Add to Evens. `Evens: 4 -> 2 -> 10`

**Final Step:**
Connect `Evens` tail to `Odds` head.
Result: `4 -> 2 -> 10 -> 1 -> 7 -> 3`

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Order of Processing:** The example suggests we process List 1 then List 2. It does *not* imply a sorted merge of values (e.g. 1 vs 2). It implies "Stable concatenation of filtered views".
- **Empty Lists:** Handle cases where one or both lists are empty.
- **All Evens/Odds:** Handle cases where one category is empty.

Common interpretation mistake:

- ❌ **Wrong:** Sorting the final list.
- ✅ **Correct:** Preserving the input order. 4 comes before 2 because 4 was in List 1 and 2 was in List 2.

### Core Concept: Dummy Heads

Use two dummy heads: `evenDummy` and `oddDummy`. This simplifies the logic because you don't have to check if `head` is null when adding the first element.

## Naive Approach

### Intuition

Create two ArrayLists, one for evens and one for odds. Iterate L1 then L2, adding values. Create a new Linked List from the arrays.

### Algorithm

1. `evens = []`, `odds = []`
2. For val in L1: if even add to `evens`, else `odds`.
3. For val in L2: if even add to `evens`, else `odds`.
4. Create new nodes for `evens`, then `odds`.

### Time Complexity

- **O(N + M)**.

### Space Complexity

- **O(N + M)** for the arrays and new nodes.

## Optimal Approach

### Key Insight

We can re-link the existing nodes instead of creating new ones. This is O(1) extra space.

### Algorithm

1. Initialize `evenHead`, `evenTail`, `oddHead`, `oddTail` using dummy nodes.
2. Helper function `process(node)`:
   - If `node.val % 2 == 0`:
     - `evenTail.next = node`
     - `evenTail = node`
   - Else:
     - `oddTail.next = node`
     - `oddTail = node`
3. Iterate L1: call `process` for each node.
4. Iterate L2: call `process` for each node.
5. **Important:** `oddTail.next = null` (terminate the list).
6. Link `evenTail.next = oddHead.next` (skip dummy).
7. Return `evenHead.next`.

### Time Complexity

- **O(N + M)**.

### Space Complexity

- **O(1)**. We reuse nodes.

![Algorithm Visualization](../images/LNK-008/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-008/algorithm-steps.png)

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
    public ListNode mergeByParity(ListNode l1, ListNode l2) {
        ListNode evenDummy = new ListNode(0);
        ListNode oddDummy = new ListNode(0);
        ListNode evenTail = evenDummy;
        ListNode oddTail = oddDummy;

        // Process List 1
        ListNode curr = l1;
        while (curr != null) {
            if (curr.val % 2 == 0) {
                evenTail.next = curr;
                evenTail = evenTail.next;
            } else {
                oddTail.next = curr;
                oddTail = oddTail.next;
            }
            curr = curr.next;
        }

        // Process List 2
        curr = l2;
        while (curr != null) {
            if (curr.val % 2 == 0) {
                evenTail.next = curr;
                evenTail = evenTail.next;
            } else {
                oddTail.next = curr;
                oddTail = oddTail.next;
            }
            curr = curr.next;
        }

        // Connect lists
        oddTail.next = null; // Terminate odd list
        evenTail.next = oddDummy.next; // Connect even tail to odd head

        return evenDummy.next;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        ListNode d1 = new ListNode(0);
        ListNode c1 = d1;
        for (int i = 0; i < n; i++) {
            c1.next = new ListNode(sc.nextInt());
            c1 = c1.next;
        }
        
        int m = sc.nextInt();
        ListNode d2 = new ListNode(0);
        ListNode c2 = d2;
        for (int i = 0; i < m; i++) {
            c2.next = new ListNode(sc.nextInt());
            c2 = c2.next;
        }

        Solution solution = new Solution();
        ListNode res = solution.mergeByParity(d1.next, d2.next);
        
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

def merge_by_parity(l1: ListNode, l2: ListNode) -> ListNode:
    even_dummy = ListNode(0)
    odd_dummy = ListNode(0)
    even_tail = even_dummy
    odd_tail = odd_dummy
    
    # Process L1
    curr = l1
    while curr:
        if curr.val % 2 == 0:
            even_tail.next = curr
            even_tail = even_tail.next
        else:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        curr = curr.next
        
    # Process L2
    curr = l2
    while curr:
        if curr.val % 2 == 0:
            even_tail.next = curr
            even_tail = even_tail.next
        else:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        curr = curr.next
        
    # Connect
    odd_tail.next = None
    even_tail.next = odd_dummy.next
    
    return even_dummy.next

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        d1 = ListNode()
        c1 = d1
        for _ in range(n):
            c1.next = ListNode(int(next(iterator)))
            c1 = c1.next
            
        m = int(next(iterator))
        d2 = ListNode()
        c2 = d2
        for _ in range(m):
            c2.next = ListNode(int(next(iterator)))
            c2 = c2.next
            
        head = merge_by_parity(d1.next, d2.next)
        
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
    ListNode* mergeByParity(ListNode* l1, ListNode* l2) {
        ListNode evenDummy(0);
        ListNode oddDummy(0);
        ListNode* evenTail = &evenDummy;
        ListNode* oddTail = &oddDummy;

        ListNode* curr = l1;
        while (curr) {
            if (curr->val % 2 == 0) {
                evenTail->next = curr;
                evenTail = evenTail->next;
            } else {
                oddTail->next = curr;
                oddTail = oddTail->next;
            }
            curr = curr->next;
        }

        curr = l2;
        while (curr) {
            if (curr->val % 2 == 0) {
                evenTail->next = curr;
                evenTail = evenTail->next;
            } else {
                oddTail->next = curr;
                oddTail = oddTail->next;
            }
            curr = curr->next;
        }

        oddTail->next = nullptr;
        evenTail->next = oddDummy.next;

        return evenDummy.next;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    ListNode d1(0);
    ListNode* c1 = &d1;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        c1->next = new ListNode(v);
        c1 = c1->next;
    }
    
    int m;
    cin >> m;
    ListNode d2(0);
    ListNode* c2 = &d2;
    for (int i = 0; i < m; i++) {
        int v;
        cin >> v;
        c2->next = new ListNode(v);
        c2 = c2->next;
    }

    Solution solution;
    ListNode* res = solution.mergeByParity(d1.next, d2.next);
    
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

function mergeByParity(l1, l2) {
  const evenDummy = new ListNode(0);
  const oddDummy = new ListNode(0);
  let evenTail = evenDummy;
  let oddTail = oddDummy;

  let curr = l1;
  while (curr) {
    if (curr.val % 2 === 0) {
      evenTail.next = curr;
      evenTail = evenTail.next;
    } else {
      oddTail.next = curr;
      oddTail = oddTail.next;
    }
    curr = curr.next;
  }

  curr = l2;
  while (curr) {
    if (curr.val % 2 === 0) {
      evenTail.next = curr;
      evenTail = evenTail.next;
    } else {
      oddTail.next = curr;
      oddTail = oddTail.next;
    }
    curr = curr.next;
  }

  oddTail.next = null;
  evenTail.next = oddDummy.next;

  return evenDummy.next;
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
  
  const d1 = new ListNode(0);
  let c1 = d1;
  for (let i = 0; i < n; i++) {
    c1.next = new ListNode(parseInt(data[idx++], 10));
    c1 = c1.next;
  }
  
  const m = parseInt(data[idx++], 10);
  const d2 = new ListNode(0);
  let c2 = d2;
  for (let i = 0; i < m; i++) {
    c2.next = new ListNode(parseInt(data[idx++], 10));
    c2 = c2.next;
  }

  let head = mergeByParity(d1.next, d2.next);
  const out = [];
  while (head) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 4 7` and `2 3 10`

**Initialization:**
- `evenDummy`, `oddDummy` empty.

**Processing L1:**
- `1` -> Odd. `oddTail` points to 1.
- `4` -> Even. `evenTail` points to 4.
- `7` -> Odd. `oddTail` points to 7.

**Processing L2:**
- `2` -> Even. `evenTail` points to 2.
- `3` -> Odd. `oddTail` points to 3.
- `10` -> Even. `evenTail` points to 10.

**Connection:**
- `oddTail.next = null` (3 -> null).
- `evenTail.next = oddDummy.next` (10 -> 1).

**Result:**
- `evenDummy.next` is 4.
- Chain: `4 -> 2 -> 10 -> 1 -> 7 -> 3`.

![Example Visualization](../images/LNK-008/example-1.png)

## ✅ Proof of Correctness

### Invariant
At any point, `evenTail` is the last processed even node, and `oddTail` is the last processed odd node. The relative order within each chain matches the input order.

### Why the approach is correct
- We iterate L1 then L2, guaranteeing L1 elements appear before L2 elements within the same parity group.
- We append to tail, maintaining stable order.
- We explicitly null-terminate the list to prevent cycles or dangling pointers.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Partition by pivot `x` (all nodes `< x` before nodes `>= x`).
  - *Hint:* Same logic, just condition changes from `val % 2` to `val < x`.
- **Extension 2:** Three-way partition (Dutch National Flag).
  - *Hint:* Three dummy heads: less, equal, greater.
- **Extension 3:** Merge K lists by parity.
  - *Hint:* Iterate all K lists sequentially.

### Common Mistakes to Avoid

1. **Cycle Creation**
   - ❌ Wrong: Forgetting `oddTail.next = null`. The last odd node might still point to something else from the original list.
   - ✅ Correct: Always terminate the last node.

2. **Connecting Lists**
   - ❌ Wrong: `evenTail.next = oddTail`.
   - ✅ Correct: `evenTail.next = oddDummy.next` (the first real odd node).

3. **Empty Input**
   - ❌ Wrong: Crashing if `l1` or `l2` is null.
   - ✅ Correct: `while(curr != null)` handles empty lists naturally.

## Related Concepts

- **Stable Partition:** The core algorithm.
- **Dummy Node:** Simplifies list construction.
- **Two-Pointer:** Used for building the two chains.
