---
problem_id: LNK_ROBOTICS_PALINDROME_ONE_SKIP__6741
display_id: LNK-014
slug: robotics-palindrome-one-skip
title: "Robotics Palindrome with One Skip"
difficulty: Medium
difficulty_score: 54
topics:
  - Linked List
  - Two Pointers
  - Palindrome
tags:
  - linked-list
  - palindrome
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-014: Robotics Palindrome with One Skip

## Problem Statement

Determine whether a singly linked list can become a palindrome after deleting at most one node. Deleting zero nodes is allowed.

![Problem Illustration](../images/LNK-014/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)

## Output Format

- Print `true` if the list can be a palindrome after at most one deletion, otherwise `false`

## Constraints

- `1 <= n <= 100000`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
5
1 2 3 2 1
```

**Output:**

```
true
```

**Explanation:**

The list is already a palindrome, so zero deletions are needed.

![Example Visualization](../images/LNK-014/example-1.png)

## Notes

- You may use array conversion or reverse the second half
- Allow one mismatch and try skipping either side
- Time complexity: O(n)
- Space complexity: O(1) or O(n) depending on approach

## Related Topics

Linked Lists, Palindromes, Two Pointers

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
    public boolean canBePalindrome(ListNode head) {
        // Implement here
        return false;
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
        }

        Solution sol = new Solution();
        System.out.println(sol.canBePalindrome(dummy.next));
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
    def can_be_palindrome(self, head):
        # Implement here
        return False

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
    print(str(sol.can_be_palindrome(dummy.next)).lower())

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
    bool canBePalindrome(ListNode* head) {
        // Implement here
        return false;
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

    Solution sol;
    cout << (sol.canBePalindrome(dummy->next) ? "true" : "false") << endl;

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
  canBePalindrome(head) {
    // Implement here
    return false;
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

  const sol = new Solution();
  console.log(sol.canBePalindrome(dummy.next));
}

solve();
```
