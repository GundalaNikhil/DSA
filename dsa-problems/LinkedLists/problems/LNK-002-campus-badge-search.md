---
problem_id: LNK_CAMPUS_BADGE_SEARCH__7294
display_id: LNK-002
slug: campus-badge-search
title: "Campus Badge Search"
difficulty: Easy
difficulty_score: 22
topics:
  - Linked List
  - Search
  - Linear Scan
tags:
  - linked-list
  - search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-002: Campus Badge Search

## Problem Statement

Given the head of a singly linked list and a target value, return the 0-based index of the first occurrence of the target. If the target does not appear, return `-1`.

![Problem Illustration](../images/LNK-002/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: integer `target`

## Output Format

- Single integer: index of the first occurrence of `target`, or `-1`

## Constraints

- `1 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
4
5 1 5 9
9
```

**Output:**

```
3
```

**Explanation:**

List: 5 -> 1 -> 5 -> 9

The target 9 appears at index 3.

![Example Visualization](../images/LNK-002/example-1.png)

## Notes

- A single linear scan is sufficient
- Stop early once the target is found
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Linear Search

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

class Solution {
    public int search(ListNode head, int target) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        String[] vals = br.readLine().trim().split("\\s+");
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int i = 0; i < n; i++) {
            curr.next = new ListNode(Integer.parseInt(vals[i]));
            curr = curr.next;
        }

        int target = Integer.parseInt(br.readLine().trim());

        Solution sol = new Solution();
        System.out.println(sol.search(dummy.next, target));
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
    def search(self, head, target):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    dummy = ListNode(0)
    curr = dummy
    for i in range(n):
        curr.next = ListNode(int(input_data[i + 1]))
        curr = curr.next

    target = int(input_data[n + 1])

    sol = Solution()
    print(sol.search(dummy.next, target))

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

class Solution {
public:
    int search(ListNode* head, int target) {
        // Implement here
        return -1;
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

    int target;
    cin >> target;

    Solution sol;
    cout << sol.search(dummy->next, target) << endl;

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
  search(head, target) {
    // Implement here
    return -1;
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

  const target = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.search(dummy.next, target));
}

solve();
```
