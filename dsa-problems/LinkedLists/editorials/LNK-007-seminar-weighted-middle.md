---
problem_id: LNK_SEMINAR_WEIGHTED_MIDDLE__4729
display_id: LNK-007
slug: seminar-weighted-middle
title: "Seminar Weighted Middle Seat"
difficulty: Easy
difficulty_score: 28
topics:
  - Linked List
  - Prefix Sum
  - Weighted Median
tags:
  - linked-list
  - prefix-sum
  - easy
premium: true
subscription_tier: basic
---

# LNK-007: Seminar Weighted Middle Seat

## 📋 Problem Summary

You are given a linked list where each node has a positive weight. You need to find the "weighted middle" node. This is defined as the first node where the sum of weights from the head up to that node is at least half of the total weight of the entire list.

## 🌍 Real-World Scenario

**Scenario Title:** The Seminar Room Center

Imagine a long seminar room with a single row of tables. Different tables have different numbers of people sitting at them.
- Table 1: 2 people
- Table 2: 1 person
- Table 3: 3 people
- Table 4: 4 people

The speaker wants to stand at a position that splits the audience roughly in half, so they can be heard equally well by the "left" and "right" sides of the weighted audience. They want to find the table that represents the "median" person.

**Why This Problem Matters:**

- **Load Balancing:** Finding the server or partition that splits the total request load evenly.
- **Center of Gravity:** In physics simulations, finding the center of mass of a linear object with varying density.
- **Logistics:** Determining the optimal warehouse location along a supply chain route to minimize total transport distance (weighted median minimizes sum of absolute deviations).

![Real-World Application](../images/LNK-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Prefix Sums

List: `[2] -> [1] -> [3] -> [4]`

1. **Calculate Total Weight:**
   `2 + 1 + 3 + 4 = 10`.

2. **Calculate Target:**
   Half of 10 is 5. We need the first node where `prefix_sum >= 5`.

3. **Scan for Target:**
   - Node 1 (val 2): Sum = 2. (2 < 5, continue)
   - Node 2 (val 1): Sum = 2 + 1 = 3. (3 < 5, continue)
   - Node 3 (val 3): Sum = 3 + 3 = 6. (6 >= 5, **FOUND!**)

Result: Node with value 3.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Positive Weights:** All weights are `>= 1`.
- **Target Calculation:** If total is odd (e.g., 9), half is 4.5. The problem says use `(total + 1) / 2`, which gives 5. This is the standard integer ceiling for "at least half".
- **Return Value:** Return the **value** of the node, not the index or the node itself.

Common interpretation mistake:

- ❌ **Wrong:** Finding the middle node by count (standard middle of linked list).
- ✅ **Correct:** Finding the middle by *weight*. A single heavy node at the start could be the weighted middle even if it's the first node.

### Core Concept: Two-Pass Algorithm

Since we don't know the total weight initially, we cannot know when to stop. We must traverse the list once to get the sum, and a second time to find the split point.

## Naive Approach

### Intuition

Store all weights in an array. Compute total. Iterate array to find the answer.

### Algorithm

1. Traverse list, store values in `ArrayList`.
2. Sum all values.
3. Iterate `ArrayList`, keeping running sum.
4. Return value when `running_sum >= threshold`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)** to store the array.

## Optimal Approach

### Key Insight

We can avoid O(N) space by doing two passes over the linked list.

### Algorithm

1. **Pass 1:** Traverse the list to calculate `totalWeight`.
2. Calculate `threshold = (totalWeight + 1) / 2`.
3. **Pass 2:** Traverse the list again. Maintain `currentSum`.
   - `currentSum += node.val`
   - If `currentSum >= threshold`, return `node.val`.

### Time Complexity

- **O(N)**. We traverse the list exactly twice (2N steps).

### Space Complexity

- **O(1)**. Only a few variables are used.

![Algorithm Visualization](../images/LNK-007/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-007/algorithm-steps.png)

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
    public int weightedMiddleValue(ListNode head) {
        if (head == null) return 0;

        // Pass 1: Calculate total weight
        long totalWeight = 0;
        ListNode curr = head;
        while (curr != null) {
            totalWeight += curr.val;
            curr = curr.next;
        }

        long threshold = (totalWeight + 1) / 2;

        // Pass 2: Find the node
        long currentSum = 0;
        curr = head;
        while (curr != null) {
            currentSum += curr.val;
            if (currentSum >= threshold) {
                return curr.val;
            }
            curr = curr.next;
        }
        return 0; // Should not reach here
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
        System.out.println(solution.weightedMiddleValue(dummy.next));
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

def weighted_middle_value(head: ListNode) -> int:
    if not head:
        return 0
        
    # Pass 1: Total weight
    total_weight = 0
    curr = head
    while curr:
        total_weight += curr.val
        curr = curr.next
        
    threshold = (total_weight + 1) // 2
    
    # Pass 2: Find node
    current_sum = 0
    curr = head
    while curr:
        current_sum += curr.val
        if current_sum >= threshold:
            return curr.val
        curr = curr.next
        
    return 0

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
            
        print(weighted_middle_value(dummy.next))
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
    int weightedMiddleValue(ListNode* head) {
        if (!head) return 0;

        // Pass 1: Total weight
        long long totalWeight = 0;
        ListNode* curr = head;
        while (curr) {
            totalWeight += curr->val;
            curr = curr->next;
        }

        long long threshold = (totalWeight + 1) / 2;

        // Pass 2: Find node
        long long currentSum = 0;
        curr = head;
        while (curr) {
            currentSum += curr->val;
            if (currentSum >= threshold) {
                return curr->val;
            }
            curr = curr->next;
        }
        return 0;
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
    cout << solution.weightedMiddleValue(dummy.next) << "\n";
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

function weightedMiddleValue(head) {
  if (!head) return 0;

  // Pass 1: Total weight
  let totalWeight = 0;
  let curr = head;
  while (curr) {
    totalWeight += curr.val;
    curr = curr.next;
  }

  const threshold = Math.floor((totalWeight + 1) / 2);

  // Pass 2: Find node
  let currentSum = 0;
  curr = head;
  while (curr) {
    currentSum += curr.val;
    if (currentSum >= threshold) {
      return curr.val;
    }
    curr = curr.next;
  }
  return 0;
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

  console.log(weightedMiddleValue(dummy.next));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `2 1 3 4`

**Pass 1:**
- Node 2: sum=2
- Node 1: sum=3
- Node 3: sum=6
- Node 4: sum=10
- Total = 10.
- Threshold = (10+1)/2 = 5.

**Pass 2:**
- Node 2: currentSum=2. (2 < 5)
- Node 1: currentSum=3. (3 < 5)
- Node 3: currentSum=6. (6 >= 5) -> **Return 3**.

![Example Visualization](../images/LNK-007/example-1.png)

## ✅ Proof of Correctness

### Invariant
The cumulative sum strictly increases (since weights > 0). There is exactly one point where the sum crosses from `< threshold` to `>= threshold`.

### Why the approach is correct
- We calculate the exact total first, ensuring our threshold is correct.
- We scan sequentially, so we are guaranteed to find the *first* node meeting the condition.
- Using `long long` (in C++/Java) prevents overflow if weights are large, though problem constraints say weights fit in integer, sum might exceed 2^31-1 if N is large (10^5 * 10^9 = 10^14).

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if weights can be negative?
  - *Hint:* The concept of "cumulative weight" becomes non-monotonic. The problem definition would need to be clearer (e.g., "partition point").
- **Extension 2:** Find the "Center of Mass" index (float).
  - *Hint:* `sum (index x weight) / sum weight`.
- **Extension 3:** Dynamic updates?
  - *Hint:* If weights change, a Segment Tree or Fenwick Tree is better than a Linked List.

### Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Wrong: Using `int` for `totalWeight` when sum can exceed 2 billion.
   - ✅ Correct: Use `long` (Java) or `long long` (C++).

2. **Threshold Calculation**
   - ❌ Wrong: `total / 2` (integer division floors 4.5 to 4).
   - ✅ Correct: `(total + 1) / 2` or `Math.ceil(total / 2.0)`.

3. **Empty List**
   - ❌ Wrong: Not handling `head == null`.
   - ✅ Correct: Return 0 or handle gracefully.

## Related Concepts

- **Prefix Sum:** The running total technique.
- **Two-Pass Algorithm:** Common pattern when global info (total) is needed for local decisions.
