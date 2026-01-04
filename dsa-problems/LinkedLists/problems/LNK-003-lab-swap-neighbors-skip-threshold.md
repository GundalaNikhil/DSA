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
time_limit: 2000
memory_limit: 256
---

# LNK-003: Lab Swap Neighbors with Skip and Threshold

## Problem Statement

Swap nodes in pairs in a singly linked list with two constraints:

- If either node in a pair has a negative value, do not swap that pair
- You can perform at most `K` swaps total; after `K` swaps are used, all remaining pairs stay as-is

Return the new head and the number of swaps actually performed.

![Problem Illustration](../images/LNK-003/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `K` (maximum swaps)

## Output Format

- First line: space-separated list values after swaps
- Second line: integer swaps performed

## Constraints

- `0 <= n <= 100000`
- `0 <= K <= n / 2`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
6
1 -2 3 4 5 6
1
```

**Output:**

```
1 -2 4 3 5 6
1
```

**Explanation:**

Pairs are (1, -2), (3, 4), (5, 6).

- Pair (1, -2): contains negative, no swap
- Pair (3, 4): swap (K becomes 0)
- Pair (5, 6): K exhausted, no swap

![Example Visualization](../images/LNK-003/example-1.png)

## Notes

- A dummy head simplifies pair manipulation
- Track swap count and stop swapping once K is reached
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Pair Swapping, Constraints Handling

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
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
    public Result swapPairs(ListNode head, int k) {
        // Implement here
        return new Result(head, 0);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        if (n > 0) {
            String[] vals = br.readLine().trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                curr.next = new ListNode(Integer.parseInt(vals[i]));
                curr = curr.next;
            }
        } else {
            br.readLine(); // consume empty line if any
        }

        int k = Integer.parseInt(br.readLine().trim());

        Solution sol = new Solution();
        Result res = sol.swapPairs(dummy.next, k);

        PrintWriter out = new PrintWriter(System.out);
        ListNode node = res.head;
        while (node != null) {
            out.print(node.val + (node.next == null ? "" : " "));
            node = node.next;
        }
        out.println();
        out.println(res.swaps);
        out.flush();
    }
}
```

### Python

```python
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swap_pairs(self, head, k):
        # Implement here
        return head, 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    dummy = ListNode(0)
    curr = dummy
    for i in range(1, n + 1):
        curr.next = ListNode(int(input_data[i]))
        curr = curr.next

    k = int(input_data[n + 1])

    sol = Solution()
    new_head, swaps = sol.swap_pairs(dummy.next, k)

    res = []
    curr = new_head
    while curr:
        res.append(str(curr.val))
        curr = curr.next

    print(" ".join(res))
    print(swaps)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

struct Result {
    ListNode* head;
    int swaps;
};

class Solution {
public:
    Result swapPairs(ListNode* head, int k) {
        // Implement here
        return {head, 0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    ListNode* dummy = new ListNode(0);
    ListNode* curr = dummy;
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        curr->next = new ListNode(val);
        curr = curr->next;
    }

    int k;
    cin >> k;

    Solution sol;
    Result res = sol.swapPairs(dummy->next, k);

    ListNode* node = res.head;
    while (node) {
        cout << node->val << (node->next ? " " : "");
        node = node->next;
    }
    cout << "\n" << res.swaps << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class ListNode {
  constructor(x) {
    this.val = x;
    this.next = null;
  }
}

class Solution {
  swapPairs(head, k) {
    // Implement here
    return { head, swaps: 0 };
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const dummy = new ListNode(0);
  let curr = dummy;
  for (let i = 0; i < n; i++) {
    curr.next = new ListNode(parseInt(input[idx++]));
    curr = curr.next;
  }

  const k = parseInt(input[idx++]);

  const sol = new Solution();
  const res = sol.swapPairs(dummy.next, k);

  const resultArr = [];
  let node = res.head;
  while (node) {
    resultArr.push(node.val);
    node = node.next;
  }
  console.log(resultArr.join(" "));
  console.log(res.swaps);
}

solve();
```
