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
time_limit: 2000
memory_limit: 256
---

# LNK-008: Lab Playlist Merge by Parity

## Problem Statement

Merge two sorted linked lists into one list. In the output, all even-valued nodes must appear before all odd-valued nodes, while preserving the relative order among evens and among odds.

![Problem Illustration](../images/LNK-008/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first list)
- Second line: `n` space-separated integers (first list values)
- Third line: integer `m` (length of second list)
- Fourth line: `m` space-separated integers (second list values)

## Output Format

- Single line: merged list values with evens first, space-separated
- If the result is empty, print an empty line

## Constraints

- `0 <= n, m <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
3
1 4 7
3
2 3 10
```

**Output:**

```
4 2 10 1 7 3
```

**Explanation:**

Evens in order: 4 (list1), 2 (list2), 10 (list2)

Odds in order: 1 (list1), 7 (list1), 3 (list2)

![Example Visualization](../images/LNK-008/example-1.png)

## Notes

- A stable merge by parity keeps original order within even and odd groups
- You can build two chains (evens and odds) and concatenate
- Time complexity: O(n + m)
- Space complexity: O(1)

## Related Topics

Linked Lists, Stable Merge, Partitioning

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
    public ListNode mergeByParity(ListNode head1, ListNode head2) {
        // Implement here
        return null;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ListNode dummy1 = new ListNode(0);
        ListNode curr1 = dummy1;
        String line1 = br.readLine();
        if (line1 != null) {
            int n = Integer.parseInt(line1.trim());
            if (n > 0) {
                String[] vals1 = br.readLine().trim().split("\\s+");
                for (int i = 0; i < n; i++) {
                    curr1.next = new ListNode(Integer.parseInt(vals1[i]));
                    curr1 = curr1.next;
                }
            } else {
                br.readLine();
            }
        }

        ListNode dummy2 = new ListNode(0);
        ListNode curr2 = dummy2;
        String line2 = br.readLine();
        if (line2 != null) {
            int m = Integer.parseInt(line2.trim());
            if (m > 0) {
                String[] vals2 = br.readLine().trim().split("\\s+");
                for (int i = 0; i < m; i++) {
                    curr2.next = new ListNode(Integer.parseInt(vals2[i]));
                    curr2 = curr2.next;
                }
            } else {
                br.readLine();
            }
        }

        Solution sol = new Solution();
        ListNode res = sol.mergeByParity(dummy1.next, dummy2.next);

        PrintWriter out = new PrintWriter(System.out);
        while (res != null) {
            out.print(res.val + (res.next == null ? "" : " "));
            res = res.next;
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
    def merge_by_parity(self, head1, head2):
        # Implement here
        return None

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx++])
    dummy1 = ListNode(0)
    curr1 = dummy1
    for i in range(n):
        curr1.next = ListNode(int(input_data[idx++]))
        curr1 = curr1.next

    m = int(input_data[idx++])
    dummy2 = ListNode(0)
    curr2 = dummy2
    for i in range(m):
        curr2.next = ListNode(int(input_data[idx++]))
        curr2 = curr2.next

    sol = Solution()
    res = sol.merge_by_parity(dummy1.next, dummy2.next)

    output = []
    while res:
        output.append(str(res.val))
        res = res.next
    print(" ".join(output))

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
    ListNode* mergeByParity(ListNode* head1, ListNode* head2) {
        // Implement here
        return NULL;
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
    ListNode* res = sol.mergeByParity(dummy1->next, dummy2->next);

    while (res) {
        cout << res->val << (res->next ? " " : "");
        res = res->next;
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
  mergeByParity(head1, head2) {
    // Implement here
    return null;
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
  let res = sol.mergeByParity(dummy1.next, dummy2.next);

  const output = [];
  while (res) {
    output.push(res.val);
    res = res.next;
  }
  console.log(output.join(" "));
}

solve();
```
