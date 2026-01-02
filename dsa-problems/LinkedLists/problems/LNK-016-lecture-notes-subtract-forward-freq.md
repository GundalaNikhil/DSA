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

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Result {
    int sign;
    ListNode head;
    int[] freq;
    Result(int sign, ListNode head, int[] freq) {
        this.sign = sign;
        this.head = head;
        this.freq = freq;
    }
}

class Solution {
    public Result subtractWithFreq(ListNode a, ListNode b) {
        return 0;
    }

    private int getLength(ListNode head) {
        int len = 0;
        while (head != null) { len++; head = head.next; }
        return len;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        ListNode dummyA = new ListNode(0);
        ListNode curA = dummyA;
        for (int i = 0; i < n; i++) {
            curA.next = new ListNode(sc.nextInt());
            curA = curA.next;
        }
        int m = sc.nextInt();
        ListNode dummyB = new ListNode(0);
        ListNode curB = dummyB;
        for (int i = 0; i < m; i++) {
            curB.next = new ListNode(sc.nextInt());
            curB = curB.next;
        }

        Solution solution = new Solution();
        Result res = solution.subtractWithFreq(dummyA.next, dummyB.next);
        System.out.println(res.sign);
        ListNode out = res.head;
        boolean first = true;
        while (out != null) {
            if (!first) System.out.print(" ");
            System.out.print(out.val);
            first = false;
            out = out.next;
        }
        System.out.println();
        for (int i = 0; i < 10; i++) {
            System.out.print(res.freq[i] + (i < 9 ? " " : ""));
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
import sys

class ListNode:
    def __init__(self, val=0):
        return 0
def get_length(head):
    return 0
def subtract_with_freq(a: ListNode, b: ListNode):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        dummy_a = ListNode()
        cur = dummy_a
        for _ in range(n):
            cur.next = ListNode(int(next(iterator)))
            cur = cur.next
            
        m = int(next(iterator))
        dummy_b = ListNode()
        cur = dummy_b
        for _ in range(m):
            cur.next = ListNode(int(next(iterator)))
            cur = cur.next
            
        sign, head, freq = subtract_with_freq(dummy_a.next, dummy_b.next)
        print(sign)
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
        print(" ".join(str(x) for x in freq))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

struct Result {
    int sign;
    ListNode* head;
    vector<int> freq;
};

class Solution {
public:
    Result subtractWithFreq(ListNode* a, ListNode* b) {
        return 0;
    }

private:
    int getLength(ListNode* head) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    ListNode dummyA(0);
    ListNode* curA = &dummyA;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        curA->next = new ListNode(v);
        curA = curA->next;
    }
    int m;
    cin >> m;
    ListNode dummyB(0);
    ListNode* curB = &dummyB;
    for (int i = 0; i < m; i++) {
        int v;
        cin >> v;
        curB->next = new ListNode(v);
        curB = curB->next;
    }

    Solution solution;
    Result res = solution.subtractWithFreq(dummyA.next, dummyB.next);
    cout << res.sign << "\n";
    ListNode* out = res.head;
    bool first = true;
    while (out) {
        if (!first) cout << " ";
        cout << out->val;
        first = false;
        out = out->next;
    }
    cout << "\n";
    for (int i = 0; i < 10; i++) {
        cout << res.freq[i] << (i < 9 ? " " : "");
    }
    cout << "\n";
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

function getLength(head) {
    return 0;
  }

function subtractWithFreq(a, b) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const p of parts) {
    if (p !== "") data.push(p);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  
  const dummyA = new ListNode(0);
  let curA = dummyA;
  for (let i = 0; i < n; i++) {
    curA.next = new ListNode(parseInt(data[idx++], 10));
    curA = curA.next;
  }
  
  const m = parseInt(data[idx++], 10);
  const dummyB = new ListNode(0);
  let curB = dummyB;
  for (let i = 0; i < m; i++) {
    curB.next = new ListNode(parseInt(data[idx++], 10));
    curB = curB.next;
  }

  const result = subtractWithFreq(dummyA.next, dummyB.next);
  console.log(result[0]);
  
  let head = result[1];
  const out = [];
  while (head) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
  console.log(result[2].join(" "));
});
```

