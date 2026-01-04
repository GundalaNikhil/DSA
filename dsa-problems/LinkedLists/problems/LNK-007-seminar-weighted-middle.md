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
time_limit: 2000
memory_limit: 256
---

# LNK-007: Seminar Weighted Middle Seat

## Problem Statement

Each node contains a positive weight. Return the node value where the cumulative weight from the head first reaches at least half of the total weight (weighted median node).

If the total weight is odd, use the ceiling of half (i.e., `(total + 1) / 2`).

![Problem Illustration](../images/LNK-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` positive integers (node weights)

## Output Format

- Single integer: value of the weighted median node

## Constraints

- `1 <= n <= 100000`
- `1 <= weight <= 10^9`

## Example

**Input:**

```
4
2 1 3 4
```

**Output:**

```
3
```

**Explanation:**

Total weight = 10, half = 5. The prefix sums are 2, 3, 6, 10.

The first node reaching at least 5 has value 3.

![Example Visualization](../images/LNK-007/example-1.png)

## Notes

- Compute total weight in one pass
- Find the first node with prefix sum >= (total + 1) / 2
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Prefix Sums, Weighted Median

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
    public long findWeightedMiddle(ListNode head) {
        // Implement here
        return 0;
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
                curr.next = new ListNode(Long.parseLong(vals[i]));
                curr = curr.next;
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.findWeightedMiddle(dummy.next));
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
    def find_weighted_middle(self, head):
        # Implement here
        return 0

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

    sol = Solution()
    print(sol.find_weighted_middle(dummy.next))

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
    long long findWeightedMiddle(ListNode* head) {
        // Implement here
        return 0;
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
        long long val;
        cin >> val;
        curr->next = new ListNode(val);
        curr = curr->next;
    }

    Solution sol;
    cout << sol.findWeightedMiddle(dummy->next) << endl;

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
  findWeightedMiddle(head) {
    // Implement here
    return 0;
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
    curr.next = new ListNode(BigInt(input[idx++]));
    curr = curr.next;
  }

  const sol = new Solution();
  console.log(sol.findWeightedMiddle(dummy.next).toString());
}

solve();
```
