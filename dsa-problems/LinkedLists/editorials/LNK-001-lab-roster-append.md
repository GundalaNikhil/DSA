---
problem_id: LNK_LAB_ROSTER_APPEND__3582
display_id: LNK-001
slug: lab-roster-append
title: "Lab Roster Append"
difficulty: Easy
difficulty_score: 20
topics:
  - Linked List
  - Data Structures
  - Implementation
tags:
  - linked-list
  - implementation
  - append
  - easy
premium: true
subscription_tier: basic
---

# LNK-001: Lab Roster Append

## 📋 Problem Summary

You need to implement a basic singly linked list that supports two operations: appending a value to the end (`push_back`) and converting the current list to an array (`to_array`). The challenge is to perform the append operation efficiently, ideally in O(1) time, while maintaining the correct order of elements.

## 🌍 Real-World Scenario

**Scenario Title:** The Lab Registration Desk

Imagine you are a teaching assistant running a busy computer science lab. Students arrive one by one to register for their practical session. As each student walks in, you write their name at the bottom of the roster sheet.

Occasionally, the professor asks for the current list of registered students to check attendance or assign groups. You need to read out the names in the order they arrived.

**Why This Problem Matters:**

- **Efficient Data Logging:** In systems where data arrives continuously (like server logs or transaction streams), we need to append new entries quickly without rewriting the entire history.
- **Queue Implementation:** This is the foundational logic for queues (First-In-First-Out), used in printer spoolers, task scheduling, and breadth-first search algorithms.
- **Memory Management:** Unlike arrays which require contiguous memory and resizing (copying all elements) when full, linked lists can grow dynamically by allocating memory for just one new node at a time.

![Real-World Application](../images/LNK-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Linked List Structure

A singly linked list consists of nodes. Each node holds a `value` and a pointer (`next`) to the next node. To support O(1) append, we maintain two pointers: `head` (start) and `tail` (end).

```
Initial State (Empty):
head: null
tail: null

Operation: push_back(3)
Node created: [3 | null]
head: [3] -> null
tail: [3] -> null

Operation: push_back(7)
Node created: [7 | null]
       +---+      +---+
head ->| 3 | ---> | 7 | -> null
       +---+      +---+
                    ^
                   tail

Operation: push_back(-2)
Node created: [-2 | null]
       +---+      +---+      +----+
head ->| 3 | ---> | 7 | ---> | -2 | -> null
       +---+      +---+      +----+
                               ^
                              tail
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Empty List:** If the list is empty, `to_array` should return an empty array (or print an empty line).
- **First Element:** When appending to an empty list, both `head` and `tail` must point to the new node.
- **Subsequent Elements:** When appending to a non-empty list, the current `tail.next` should point to the new node, and then `tail` should be updated.

Common interpretation mistake:

- ❌ **Wrong:** Iterating from `head` to find the last node for every `push_back`. This makes append O(N).
- ✅ **Correct:** Keeping a `tail` pointer to access the last node instantly. This makes append O(1).

### Core Concept: The Tail Pointer

The key to efficiency here is the `tail` pointer. Without it, you'd have to traverse the entire list from the `head` every time you want to add an element, which becomes very slow as the list grows.

## Naive Approach

### Intuition

The most basic implementation might only track the `head` of the list. To add an element, we traverse from the `head` until we find a node where `next` is `null`, and attach the new node there.

### Algorithm

1. Create a new node with the given value.
2. If `head` is `null`, set `head` to the new node.
3. Else, start a temporary pointer `current` at `head`.
4. Loop while `current.next` is not `null`: move `current` to `current.next`.
5. Set `current.next` to the new node.

### Time Complexity

- **push_back:** O(N), where N is the number of elements in the list. We traverse all N nodes.
- **to_array:** O(N).

### Space Complexity

- **O(N)** to store the elements.

### Limitations

- **Too Slow:** If we perform N `push_back` operations, the total time complexity becomes O(N²). For N=100,000, this is 10 billion operations, which will exceed the time limit (usually ~10^8 operations per second).

## Optimal Approach

### Key Insight

We can avoid the traversal by remembering where the last node is. By maintaining a `tail` reference, we can jump directly to the end of the list.

### Algorithm

**push_back(value):**
1. Create a new node `newNode` with `value`.
2. If `head` is `null` (list is empty):
   - Set `head = newNode`
   - Set `tail = newNode`
3. Else (list not empty):
   - Set `tail.next = newNode`
   - Update `tail = newNode`

**to_array():**
1. Initialize an empty list/array `result`.
2. Start a pointer `current` at `head`.
3. While `current` is not `null`:
   - Add `current.val` to `result`.
   - Move `current` to `current.next`.
4. Return `result`.

### Time Complexity

- **push_back:** O(1). We perform a constant number of pointer updates regardless of list size.
- **to_array:** O(N). We must visit every node once to read the values.

### Space Complexity

- **O(N)** to store the nodes.

### Why This Is Optimal

You cannot append faster than O(1), and you cannot read all elements faster than O(N). Thus, this solution is optimal in terms of time complexity.

![Algorithm Visualization](../images/LNK-001/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-001/algorithm-steps.png)

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
    private ListNode head = null;
    private ListNode tail = null;

    public void pushBack(int value) {
        ListNode newNode = new ListNode(value);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
    }

    public int[] toArray() {
        List<Integer> list = new ArrayList<>();
        ListNode current = head;
        while (current != null) {
            list.add(current.val);
            current = current.next;
        }
        // Convert List to int[]
        int[] arr = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }
        return arr;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        sc.nextLine();

        Solution solution = new Solution();
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine().trim();
            if (line.startsWith("push_back")) {
                String[] parts = line.split(" ");
                int value = Integer.parseInt(parts[1]);
                solution.pushBack(value);
            } else {
                int[] arr = solution.toArray();
                for (int j = 0; j < arr.length; j++) {
                    System.out.print(arr[j]);
                    if (j + 1 < arr.length) System.out.print(" ");
                }
                System.out.println();
            }
        }
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

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value: int) -> None:
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

def main():
    input = sys.stdin.read
    data = input().splitlines()
    if not data:
        return
    
    n = int(data[0])
    sol = Solution()
    
    for i in range(1, n + 1):
        line = data[i].strip()
        if line.startswith("push_back"):
            _, v = line.split()
            sol.push_back(int(v))
        else:
            arr = sol.to_array()
            print(" ".join(str(x) for x in arr))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* head = nullptr;
    ListNode* tail = nullptr;

    void pushBack(int value) {
        ListNode* newNode = new ListNode(value);
        if (!head) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    vector<int> toArray() {
        vector<int> result;
        ListNode* current = head;
        while (current) {
            result.push_back(current->val);
            current = current->next;
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    string dummy;
    getline(cin, dummy);

    Solution solution;
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        if (line.rfind("push_back", 0) == 0) {
            stringstream ss(line);
            string op;
            int value;
            ss >> op >> value;
            solution.pushBack(value);
        } else {
            vector<int> arr = solution.toArray();
            for (int j = 0; j < (int)arr.size(); j++) {
                if (j) cout << " ";
                cout << arr[j];
            }
            cout << "\n";
        }
    }
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

class Solution {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  pushBack(value) {
    const newNode = new ListNode(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  toArray() {
    const result = [];
    let current = this.head;
    while (current) {
      result.push(current.val);
      current = current.next;
    }
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  if (lines.length === 0) return;
  const n = parseInt(lines[0], 10);
  const sol = new Solution();
  for (let i = 1; i <= n; i++) {
    const line = lines[i];
    if (line.startsWith("push_back")) {
      const parts = line.split(" ");
      sol.pushBack(parseInt(parts[1], 10));
    } else {
      const arr = sol.toArray();
      console.log(arr.join(" "));
    }
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Use the sample input:
```
push_back 3
push_back 7
to_array
push_back -2
to_array
```

We maintain:
- `head`: points to first node
- `tail`: points to last node

Initialize:
- `head = null`, `tail = null`

Now iterate:

| Step | Operation | Value | Explanation | List State |
| ---: | :----: | -----: | ----------- | ------ |
| 1 | push_back | 3 | List empty. `head` & `tail` -> new node(3) | `[3]` |
| 2 | push_back | 7 | List not empty. `tail.next` -> new node(7), update `tail` | `[3] -> [7]` |
| 3 | to_array | - | Traverse from `head`. Print 3, then 7. | Output: `3 7` |
| 4 | push_back | -2 | `tail` (at 7) points to -2. Update `tail` to -2. | `[3] -> [7] -> [-2]` |
| 5 | to_array | - | Traverse from `head`. Print 3, 7, -2. | Output: `3 7 -2` |

![Example Visualization](../images/LNK-001/example-1.png)

## ✅ Proof of Correctness

### Invariant
At any point, `head` points to the first node of the sequence, and `tail` points to the last node. The `next` pointer of `tail` is always `null`.

### Why the approach is correct
- **Base Case (Empty List):** When the list is empty, `push_back` correctly sets both `head` and `tail` to the new node. The invariant holds (single node is both first and last).
- **Inductive Step:** Assume the list has $k$ nodes and `tail` points to the $k$-th node. When adding the $(k+1)$-th node, we set `tail.next` to the new node, linking the list correctly. Then we update `tail` to point to the new node. The invariant is maintained: `head` is unchanged (still points to 1st), and `tail` now points to $(k+1)$-th.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Implement `push_front` (add to beginning).
  - *Hint:* Create new node, set `new.next = head`, update `head = new`. O(1).
- **Extension 2:** Implement `pop_back` (remove last element).
  - *Hint:* Requires traversing to the second-to-last node to update `tail`, making it O(N) for singly linked list. O(1) if doubly linked list.
- **Extension 3:** Reverse the linked list.
  - *Hint:* Iterate through the list, reversing the `next` pointers. Update `head` and `tail`.

### C++ommon Mistakes to Avoid

1. **Forgetting to update Tail**
   - ❌ Wrong: Only setting `tail.next = newNode` but not moving `tail`.
   - ✅ Correct: Always `tail = newNode` after linking.

2. **Null Pointer Exception on Empty List**
   - ❌ Wrong: Trying to access `tail.next` when `tail` is `null`.
   - ✅ Correct: Check `if (head == null)` or `if (tail == null)` first.

3. **Losing the Head**
   - ❌ Wrong: Using `head` to traverse the list in `to_array` (`head = head.next`).
   - ✅ Correct: Use a temporary variable `current = head` for traversal.

## Related Concepts

- **Doubly Linked List:** Nodes have `prev` and `next` pointers.
- **Queue:** FIFO structure often implemented with linked list.
- **Stack:** LIFO structure often implemented with linked list.
