---
problem_id: LNK_ROBOTICS_CHUNK_REVERSE_OFFSET_COUNT__6837
display_id: LNK-009
slug: robotics-chunk-reverse-offset-count
title: "Robotics Chunk Reverse with Offset and Reversal Count"
difficulty: Medium
difficulty_score: 55
topics:
  - Linked List
  - Reversal
  - Simulation
tags:
  - linked-list
  - reversal
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-009: Robotics Chunk Reverse with Offset and Reversal Count

## Problem Statement

Reverse nodes in groups of size `k`, but start grouping at position `s` (1-indexed). Nodes before position `s` remain unchanged. From `s` onward, reverse each full group of size `k`; any leftover tail with fewer than `k` nodes stays as-is.

Return three outputs:

- The new head of the list
- `reversal_count`: number of full groups reversed
- `sum_of_reversed_values`: sum of all node values that were part of reversed groups

![Problem Illustration](../images/LNK-009/problem-illustration.png)

## Input Format

- First line: integer `n` (number of nodes)
- Second line: `n` space-separated integers (node values)
- Third line: two integers `k` and `s`

## Output Format

- First line: list values after reversal, space-separated
- Second line: `reversal_count`
- Third line: `sum_of_reversed_values`

## Constraints

- `0 <= n <= 100000`
- `1 <= k <= max(1, n)`
- `1 <= s <= max(1, n)`
- Node values fit in 32-bit signed integer

## Example

**Input:**

```
5
1 2 3 4 5
2 3
```

**Output:**

```
1 2 4 3 5
1
7
```

**Explanation:**

Start at position 3. The group [3, 4] is reversed, yielding 4 -> 3.

- reversal_count = 1
- sum_of_reversed_values = 3 + 4 = 7

![Example Visualization](../images/LNK-009/example-1.png)

## Notes

- Only complete groups of size `k` are reversed
- Keep running sum of values inside reversed groups
- Time complexity: O(n)
- Space complexity: O(1)

## Related Topics

Linked Lists, Block Reversal, Counting

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
    int reversalCount;
    long sumOfReversedValues;
    Result(ListNode head, int reversalCount, long sumOfReversedValues) {
        this.head = head;
        this.reversalCount = reversalCount;
        this.sumOfReversedValues = sumOfReversedValues;
    }
}

class Solution {
    public Result chunkReverse(ListNode head, int k, int s) {
        // Implement here
        return new Result(head, 0, 0L);
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
            br.readLine();
        }

        String[] params = br.readLine().trim().split("\\s+");
        int k = Integer.parseInt(params[0]);
        int s = Integer.parseInt(params[1]);

        Solution sol = new Solution();
        Result res = sol.chunkReverse(dummy.next, k, s);

        PrintWriter out = new PrintWriter(System.out);
        ListNode node = res.head;
        while (node != null) {
            out.print(node.val + (node.next == null ? "" : " "));
            node = node.next;
        }
        out.println();
        out.println(res.reversalCount);
        out.println(res.sumOfReversedValues);
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
    def chunk_reverse(self, head, k, s):
        # Implement here
        return head, 0, 0

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
    s = int(input_data[n + 2])

    sol = Solution()
    new_head, reversal_count, reverse_sum = sol.chunk_reverse(dummy.next, k, s)

    output = []
    curr = new_head
    while curr:
        output.append(str(curr.val))
        curr = curr.next
    print(" ".join(output))
    print(reversal_count)
    print(reverse_sum)

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
    int reversalCount;
    long long sumOfReversedValues;
};

class Solution {
public:
    Result chunkReverse(ListNode* head, int k, int s) {
        // Implement here
        return {head, 0, 0LL};
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

    int k, s;
    cin >> k >> s;

    Solution sol;
    Result res = sol.chunkReverse(dummy->next, k, s);

    ListNode* node = res.head;
    while (node) {
        cout << node->val << (node->next ? " " : "");
        node = node->next;
    }
    cout << "\n" << res.reversalCount << "\n" << res.sumOfReversedValues << endl;

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
  chunkReverse(head, k, s) {
    // Implement here
    return { head, reversalCount: 0, sumOfReversedValues: 0 };
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
  const s = parseInt(input[idx++]);

  const sol = new Solution();
  const res = sol.chunkReverse(dummy.next, k, s);

  const resultArr = [];
  let node = res.head;
  while (node) {
    resultArr.push(node.val);
    node = node.next;
  }
  process.stdout.write(resultArr.join(" ") + "\n");
  process.stdout.write(res.reversalCount + "\n");
  process.stdout.write(res.sumOfReversedValues + "\n");
}

solve();
```
