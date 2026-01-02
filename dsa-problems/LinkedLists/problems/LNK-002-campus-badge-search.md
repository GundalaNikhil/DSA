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

class Solution {
    public int findFirstIndex(ListNode head, int target) {
        // Implementation here
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
        
        int target = sc.nextInt();
        Solution solution = new Solution();
        System.out.println(solution.findFirstIndex(dummy.next, target));
        sc.close();
    }
}
```

### Python

```python
import sys

def find_first_index(head: ListNode, target: int) -> int:
    # Implementation here
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
            val = int(next(iterator))
            cur.next = ListNode(val)
            cur = cur.next
        
        target = int(next(iterator))
        print(find_first_index(dummy.next, target))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    int findFirstIndex(ListNode* head, int target) {
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
    
    int target;
    cin >> target;

    Solution solution;
    cout << solution.findFirstIndex(dummy.next, target) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findFirstIndex(head, target) {
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

function new Solution().findFirstIndex(head, target) {
  let current = head;
  let index = 0;
  while (current !== null) {
    if (current.val === target) {
      return index;
    }
    current = current.next;
    index++;
  }
  return -1;
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
      const target = parseInt(data[idx++], 10);
      console.log(new Solution().findFirstIndex(dummy.next, target));
  }
});
```
