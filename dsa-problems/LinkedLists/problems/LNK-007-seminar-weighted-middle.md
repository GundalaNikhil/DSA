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

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public int weightedMiddleValue(ListNode head) {
        //Implement here
        return 0;
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

        Solution solution = new Solution();
        System.out.println(solution.weightedMiddleValue(dummy.next));
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

def weighted_middle_value(head: ListNode) -> int:
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
            
        print(weighted_middle_value(dummy.next))
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

class Solution {
public:
    int weightedMiddleValue(ListNode* head) {
        //Implement here
        return 0;
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

    Solution solution;
    cout << solution.weightedMiddleValue(dummy.next) << "\n";
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

function weightedMiddleValue(head) {
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

  console.log(weightedMiddleValue(dummy.next));
});
```

