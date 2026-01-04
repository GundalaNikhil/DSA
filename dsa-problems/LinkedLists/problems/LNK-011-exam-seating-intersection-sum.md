---
problem_id: LNK_EXAM_SEATING_INTERSECTION_SUM__5629
display_id: LNK-011
slug: exam-seating-intersection-sum
title: "Exam Seating Intersection Sum"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked List
  - Intersection
  - Two Pointers
tags:
  - linked-list
  - intersection
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-011: Exam Seating Intersection Sum

## Problem Statement

Two singly linked lists may intersect (share nodes). Return the sum of values in the shared suffix. If there is no intersection, return `0`.

![Problem Illustration](../images/LNK-011/problem-illustration.png)

## Input Format

- First line: two integers `n` and `m` (lengths of list A and list B)
- Second line: `n` space-separated integers (list A values)
- Third line: `m` space-separated integers (list B values)
- Fourth line: two integers `ia` and `ib`

If `ia` and `ib` are both `-1`, the lists do not intersect. Otherwise, the node at index `ib` of list B is connected to the node at index `ia` of list A (0-based). Any nodes after index `ib` in list B are ignored after the connection.

## Output Format

- Single integer: sum of values in the shared suffix

## Constraints

- `0 <= n, m <= 100000`
- Node values fit in 32-bit signed integer
- `-1 <= ia < n`, `-1 <= ib < m`

## Example

**Input:**

```
4 3
1 2 3 4
9 3 4
2 1
```

**Output:**

```
7
```

**Explanation:**

List A: 1 -> 2 -> 3 -> 4

List B starts as 9 -> 3 -> 4, but index 1 in B connects to index 2 in A.

Shared suffix is 3 -> 4, sum = 7.

![Example Visualization](../images/LNK-011/example-1.png)

## Notes

- You can find the intersection using length alignment or hashing
- Once the intersection node is found, sum to the end
- Time complexity: O(n + m)
- Space complexity: O(1)

## Related Topics

Linked Lists, Intersection, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class ListNode {
    long val;
    ListNode next;
    ListNode(long x) { val = x; }
}

class Solution {
    public long getIntersectionSum(ListNode headA, ListNode headB) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] lens = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(lens[0]);
        int m = Integer.parseInt(lens[1]);

        ListNode[] nodesA = new ListNode[n];
        if (n > 0) {
            String[] valsA = br.readLine().trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                nodesA[i] = new ListNode(Long.parseLong(valsA[i]));
                if (i > 0) nodesA[i-1].next = nodesA[i];
            }
        } else {
            br.readLine();
        }

        ListNode[] nodesB = new ListNode[m];
        if (m > 0) {
            String[] valsB = br.readLine().trim().split("\\s+");
            for (int i = 0; i < m; i++) {
                nodesB[i] = new ListNode(Long.parseLong(valsB[i]));
                if (i > 0) nodesB[i-1].next = nodesB[i];
            }
        } else {
            br.readLine();
        }

        String[] conn = br.readLine().trim().split("\\s+");
        int ia = Integer.parseInt(conn[0]);
        int ib = Integer.parseInt(conn[1]);
        if (ia != -1 && ib != -1 && n > 0 && m > 0) {
            nodesB[ib].next = nodesA[ia];
        }

        Solution sol = new Solution();
        System.out.println(sol.getIntersectionSum(n > 0 ? nodesA[0] : null, m > 0 ? nodesB[0] : null));
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
    def get_intersection_sum(self, head_a, head_b):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx++])
    m = int(input_data[idx++])

    nodes_a = []
    for i in range(n):
        nodes_a.append(ListNode(int(input_data[idx++])))
    for i in range(n - 1):
        nodes_a[i].next = nodes_a[i + 1]

    nodes_b = []
    for i in range(m):
        nodes_b.append(ListNode(int(input_data[idx++])))
    for i in range(m - 1):
        nodes_b[i].next = nodes_b[i + 1]

    ia = int(input_data[idx++])
    ib = int(input_data[idx++])

    if ia != -1 and ib != -1 and n > 0 and m > 0:
        nodes_b[ib].next = nodes_a[ia]

    sol = Solution()
    print(sol.get_intersection_sum(nodes_a[0] if n > 0 else None, nodes_b[0] if m > 0 else None))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    long long val;
    ListNode *next;
    ListNode(long long x) : val(x), next(NULL) {}
};

class Solution {
public:
    long long getIntersectionSum(ListNode* headA, ListNode* headB) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<ListNode*> nodesA(n);
    for (int i = 0; i < n; i++) {
        long long val;
        cin >> val;
        nodesA[i] = new ListNode(val);
        if (i > 0) nodesA[i-1]->next = nodesA[i];
    }

    vector<ListNode*> nodesB(m);
    for (int i = 0; i < m; i++) {
        long long val;
        cin >> val;
        nodesB[i] = new ListNode(val);
        if (i > 0) nodesB[i-1]->next = nodesB[i];
    }

    int ia, ib;
    cin >> ia >> ib;
    if (ia != -1 && ib != -1 && n > 0 && m > 0) {
        nodesB[ib]->next = nodesA[ia];
    }

    Solution sol;
    cout << sol.getIntersectionSum(n > 0 ? nodesA[0] : NULL, m > 0 ? nodesB[0] : NULL) << endl;

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
  getIntersectionSum(headA, headB) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const nodesA = [];
  for (let i = 0; i < n; i++) {
    nodesA.push(new ListNode(BigInt(input[idx++])));
    if (i > 0) nodesA[i - 1].next = nodesA[i];
  }

  const nodesB = [];
  for (let i = 0; i < m; i++) {
    nodesB.push(new ListNode(BigInt(input[idx++])));
    if (i > 0) nodesB[i - 1].next = nodesB[i];
  }

  const ia = parseInt(input[idx++]);
  const ib = parseInt(input[idx++]);

  if (ia !== -1 && ib !== -1 && n > 0 && m > 0) {
    nodesB[ib].next = nodesA[ia];
  }

  const sol = new Solution();
  console.log(
    sol
      .getIntersectionSum(n > 0 ? nodesA[0] : null, m > 0 ? nodesB[0] : null)
      .toString()
  );
}

solve();
```
