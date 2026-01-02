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

class Solution {
    public boolean canBePalindrome(ListNode head) {
        // Implementation here
        return false;
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
        System.out.println(solution.canBePalindrome(dummy.next) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys

def is_palindrome(vals, left, right):
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
            
        print("true" if can_be_palindrome(dummy.next) else "false")
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
    bool canBePalindrome(ListNode* head) {
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

    Solution solution;
    cout << (solution.canBePalindrome(dummy.next) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  isPalindrome(vals, left, right) {
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

function new Solution().isPalindrome(vals, left, right) {
  while (left < right) {
    if (vals[left] !== vals[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}

function canBePalindrome(head) {
  const vals = [];
  let curr = head;
  while (curr) {
    vals.push(curr.val);
    curr = curr.next;
  }

  let left = 0;
  let right = vals.length - 1;

  while (left < right) {
    if (vals[left] !== vals[right]) {
      return new Solution().isPalindrome(vals, left + 1, right) || 
             new Solution().isPalindrome(vals, left, right - 1);
    }
    left++;
    right--;
  }
  return true;
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

  console.log(canBePalindrome(dummy.next) ? "true" : "false");
});
```
