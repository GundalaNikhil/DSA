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

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Result {
    ListNode head;
    int reversedGroups;
    long sum;
    Result(ListNode head, int reversedGroups, long sum) {
        this.head = head;
        this.reversedGroups = reversedGroups;
        this.sum = sum;
    }
}

class Solution {
    public Result reverseFromOffset(ListNode head, int k, int s) {
        //Implement here
        return null;
    }
}

class Main {
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
        
        int k = sc.nextInt();
        int s = sc.nextInt();

        Solution solution = new Solution();
        Result res = solution.reverseFromOffset(dummy.next, k, s);
        
        ListNode out = res.head;
        boolean first = true;
        while (out != null) {
            if (!first) System.out.print(" ");
            System.out.print(out.val);
            first = false;
            out = out.next;
        }
        System.out.println();
        System.out.println(res.reversedGroups);
        System.out.println(res.sum);
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

def reverse_from_offset(head: ListNode, k: int, s: int):
    # //Implement here
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
            
        k = int(next(iterator))
        s = int(next(iterator))
        
        head, groups, total_sum = reverse_from_offset(dummy.next, k, s)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
        print(groups)
        print(total_sum)
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

struct Result {
    ListNode* head;
    int reversedGroups;
    long long sum;
};

class Solution {
public:
    Result reverseFromOffset(ListNode* head, int k, int s) {
        //Implement here
        return {};
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
    
    int k, s;
    cin >> k >> s;

    Solution solution;
    Result res = solution.reverseFromOffset(dummy.next, k, s);
    
    ListNode* out = res.head;
    bool first = true;
    while (out) {
        if (!first) cout << " ";
        cout << out->val;
        first = false;
        out = out->next;
    }
    cout << "\n" << res.reversedGroups << "\n" << res.sum << "\n";
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

function reverseFromOffset(head, k, s) {
  //Implement here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x)));
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
  
  if (idx < data.length) {
      const k = parseInt(data[idx++], 10);
      const s = parseInt(data[idx++], 10);

      const result = reverseFromOffset(dummy.next, k, s);
      let head = result[0];
      const groups = result[1];
      const sum = result[2];
      
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
      console.log(groups);
      console.log(sum);
  }
});
```

