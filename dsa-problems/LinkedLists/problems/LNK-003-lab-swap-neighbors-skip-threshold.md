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

class Solution {
    public Result swapWithSkip(ListNode head, int K) {
        // Implementation here
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
        int K = sc.nextInt();

        Solution solution = new Solution();
        Result res = solution.swapWithSkip(dummy.next, K);
        ListNode out = res.head;
        while (out != null) {
            System.out.print(out.val + (out.next != null ? " " : ""));
            out = out.next;
        }
        System.out.println();
        System.out.println(res.swaps);
        sc.close();
    }
}
```

### Python

```python
import sys

def swap_with_skip(head: ListNode, K: int):
    # Implementation here
    return None

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
        
        K = int(next(iterator))
        
        head, swaps = swap_with_skip(dummy.next, K)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
        print(swaps)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    Result swapWithSkip(ListNode* head, int K) {
        // Implementation here
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
    
    int K;
    cin >> K;

    Solution solution;
    Result res = solution.swapWithSkip(dummy.next, K);
    
    ListNode* out = res.head;
    bool first = true;
    while (out) {
        if (!first) cout << " ";
        cout << out->val;
        first = false;
        out = out->next;
    }
    cout << "\n";
    cout << res.swaps << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  swapWithSkip(head, K) {
    // Implementation here
    return null;
  }
}

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function new Solution().swapWithSkip(head, K) {
  if (!head || !head.next) return [head, 0];

  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;
  let swapCount = 0;

  while (prev.next && prev.next.next) {
    const first = prev.next;
    const second = prev.next.next;

    const nonNegative = (first.val >= 0 && second.val >= 0);
    const canSwap = (K > 0);

    if (nonNegative && canSwap) {
      prev.next = second;
      first.next = second.next;
      second.next = first;

      K--;
      swapCount++;
      prev = first;
    } else {
      prev = second;
    }
  }

  return [dummy.next, swapCount];
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
      const K = parseInt(data[idx++], 10);
      const result = new Solution().swapWithSkip(dummy.next, K);
      let head = result[0];
      const swaps = result[1];
      
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
      console.log(swaps);
  }
});
```
