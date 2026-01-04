---
problem_id: LNK_LECTURE_NOTES_SUBTRACT_FORWARD_FREQ__9284
display_id: LNK-016
slug: lecture-notes-subtract-forward-freq
title: "Lecture Notes Subtract Two Numbers with Digit Frequency Analysis"
difficulty: Medium
difficulty_score: 60
topics:
  - Linked List
  - Arithmetic
  - Stacks
tags:
  - linked-list
  - subtraction
  - digits
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-016: Lecture Notes Subtract Two Numbers with Digit Frequency Analysis

## Problem Statement

Two linked lists represent non-negative integers in forward order (most significant digit first). Subtract the smaller number from the larger number, and return:

- `sign`: 1 if the result is positive, 0 if the result is zero
- The resulting number as a linked list in forward order
- An array of length 10 with the frequency of each digit (0-9) in the result

Do not use big integers for arithmetic.

![Problem Illustration](../images/LNK-016/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first number)
- Second line: `n` digits (0-9) in forward order
- Third line: integer `m` (length of second number)
- Fourth line: `m` digits (0-9) in forward order

## Output Format

- First line: integer `sign` (1 for positive result, 0 for zero)
- Second line: digits of the result in forward order, space-separated
- Third line: 10 integers for digit frequencies from 0 to 9

## Constraints

- `1 <= n, m <= 100000`
- Digits are in [0, 9]
- No leading zeros except the number zero itself

## Example

**Input:**

```
3
7 1 6
3
2 9 5
```

**Output:**

```
1
4 2 1
0 1 1 0 1 0 0 0 0 0
```

**Explanation:**

716 - 295 = 421. Digit frequencies: one 1, one 2, one 4.

![Example Visualization](../images/LNK-016/example-1.png)

## Notes

- Compare lengths and lexicographic order to choose the minuend
- Use stacks to subtract from least significant digit with borrow
- Remove leading zeros from the result; if empty, result is 0
- Time complexity: O(n + m)
- Space complexity: O(n + m)

## Related Topics

Linked Lists, Big Integer Arithmetic, Stacks

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
    int sign;
    ListNode head;
    int[] frequencies;
    Result(int sign, ListNode head, int[] frequencies) {
        this.sign = sign;
        this.head = head;
        this.frequencies = frequencies;
    }
}

class Solution {
    public Result subtractLists(ListNode head1, ListNode head2) {
        // Implement here
        return new Result(0, null, new int[10]);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line1Len = br.readLine();
        if (line1Len == null) return;
        int n = Integer.parseInt(line1Len.trim());
        ListNode dummy1 = new ListNode(0);
        ListNode curr1 = dummy1;
        if (n > 0) {
            String[] vals1 = br.readLine().trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                curr1.next = new ListNode(Integer.parseInt(vals1[i]));
                curr1 = curr1.next;
            }
        }

        String line2Len = br.readLine();
        if (line2Len == null) return;
        int m = Integer.parseInt(line2Len.trim());
        ListNode dummy2 = new ListNode(0);
        ListNode curr2 = dummy2;
        if (m > 0) {
            String[] vals2 = br.readLine().trim().split("\\s+");
            for (int i = 0; i < m; i++) {
                curr2.next = new ListNode(Integer.parseInt(vals2[i]));
                curr2 = curr2.next;
            }
        }

        Solution sol = new Solution();
        Result res = sol.subtractLists(dummy1.next, dummy2.next);

        PrintWriter out = new PrintWriter(System.out);
        out.println(res.sign);
        ListNode node = res.head;
        if (node == null) {
            out.println("0");
        } else {
            while (node != null) {
                out.print(node.val + (node.next == null ? "" : " "));
                node = node.next;
            }
            out.println();
        }
        for (int i = 0; i < 10; i++) {
            out.print(res.frequencies[i] + (i == 9 ? "" : " "));
        }
        out.println();
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
    def subtract_lists(self, head1, head2):
        # Implement here
        return 0, None, [0]*10

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx])
    idx += 1
    dummy1 = ListNode(0)
    curr1 = dummy1
    for _ in range(n):
        curr1.next = ListNode(int(input_data[idx]))
        idx += 1
        curr1 = curr1.next

    m = int(input_data[idx])
    idx += 1
    dummy2 = ListNode(0)
    curr2 = dummy2
    for _ in range(m):
        curr2.next = ListNode(int(input_data[idx]))
        idx += 1
        curr2 = curr2.next

    sol = Solution()
    sign, res_head, freqs = sol.subtract_lists(dummy1.next, dummy2.next)

    print(sign)
    output = []
    if not res_head:
        print(0)
    else:
        while res_head:
            output.append(str(res_head.val))
            res_head = res_head.next
        print(" ".join(output))
    print(" ".join(map(str, freqs)))

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
    int sign;
    ListNode* head;
    vector<int> frequencies;
};

class Solution {
public:
    Result subtractLists(ListNode* head1, ListNode* head2) {
        // Implement here
        return {0, NULL, vector<int>(10, 0)};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    ListNode* dummy1 = new ListNode(0);
    ListNode* dummy2 = new ListNode(0);
    ListNode* curr1 = dummy1;
    ListNode* curr2 = dummy2;

    if (cin >> n) {
        for (int i = 0; i < n; i++) {
            int val;
            cin >> val;
            curr1->next = new ListNode(val);
            curr1 = curr1->next;
        }
    }

    if (cin >> m) {
        for (int i = 0; i < m; i++) {
            int val;
            cin >> val;
            curr2->next = new ListNode(val);
            curr2 = curr2->next;
        }
    }

    Solution sol;
    Result res = sol.subtractLists(dummy1->next, dummy2->next);

    cout << res.sign << "\n";
    if (!res.head) {
        cout << "0\n";
    } else {
        ListNode* node = res.head;
        while (node) {
            cout << node->val << (node->next ? " " : "");
            node = node->next;
        }
        cout << "\n";
    }
    for (int i = 0; i < 10; i++) {
        cout << res.frequencies[i] << (i == 9 ? "" : " ");
    }
    cout << endl;

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
  subtractLists(head1, head2) {
    // Implement here
    return { sign: 0, head: null, frequencies: new Array(10).fill(0) };
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const dummy1 = new ListNode(0);
  let curr1 = dummy1;
  for (let i = 0; i < n; i++) {
    curr1.next = new ListNode(parseInt(input[idx++]));
    curr1 = curr1.next;
  }

  const m = parseInt(input[idx++]);
  const dummy2 = new ListNode(0);
  let curr2 = dummy2;
  for (let i = 0; i < m; i++) {
    curr2.next = new ListNode(parseInt(input[idx++]));
    curr2 = curr2.next;
  }

  const sol = new Solution();
  const res = sol.subtractLists(dummy1.next, dummy2.next);

  process.stdout.write(res.sign + "\n");
  if (!res.head) {
    process.stdout.write("0\n");
  } else {
    const digits = [];
    let node = res.head;
    while (node) {
      digits.push(node.val);
      node = node.next;
    }
    process.stdout.write(digits.join(" ") + "\n");
  }
  process.stdout.write(res.frequencies.join(" ") + "\n");
}

solve();
```
