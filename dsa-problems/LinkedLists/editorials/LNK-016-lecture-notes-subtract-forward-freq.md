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
---

# LNK-016: Lecture Notes Subtract Two Numbers with Digit Frequency Analysis

## 📋 Problem Summary

You are given two non-negative integers represented as linked lists in **forward order** (most significant digit first). You need to:
1. Subtract the smaller number from the larger number.
2. Determine the sign of the result (1 if positive, 0 if zero).
3. Return the result as a linked list (forward order).
4. Count the frequency of each digit (0-9) in the result.

## 🌍 Real-World Scenario

**Scenario Title:** The Bank Ledger Audit

A bank needs to reconcile two massive ledgers. Each ledger contains a total balance that is too large to fit in a standard 64-bit integer (e.g., a country's national debt in cents). The balances are stored as linked lists of digits.
- Ledger A: `7 -> 1 -> 6` (716)
- Ledger B: `2 -> 9 -> 5` (295)

The auditor needs to find the exact difference (`421`), determine if it's a surplus or deficit, and analyze the distribution of digits in the difference for fraud detection (Benford's Law analysis).

**Why This Problem Matters:**

- **Big Integer Arithmetic:** Implementing core math operations for cryptography libraries (RSA keys are huge integers).
- **Arbitrary Precision:** Scientific computing where standard types lose precision.
- **Data Analysis:** Frequency analysis is a common first step in statistical modeling.

![Real-World Application](../images/LNK-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Subtraction with Borrow

`716 - 295`

1. **Align & Compare:** 716 > 295. Result is positive.
2. **Reverse/Stack:** Process from right to left.
   - `6 - 5 = 1`. No borrow. Result digit: 1.
   - `1 - 9`: Need borrow. `11 - 9 = 2`. Borrow = 1. Result digit: 2.
   - `7 - 2 - 1 (borrow) = 4`. Result digit: 4.
3. **Result:** `4 -> 2 -> 1`.
4. **Frequencies:** {1:1, 2:1, 4:1, others:0}.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Forward Order:** You cannot subtract easily from head to tail. You need to process from tail to head.
- **Comparison:** You must first determine which number is larger to ensure `Larger - Smaller`.
- **Leading Zeros:** If the result is `007`, return `7`. If result is `0`, return `0` (list with one node `0`).

Common interpretation mistake:

- ❌ **Wrong:** Converting to `BigInteger` or `string`.
- ✅ **Correct:** Manipulating the linked list structure (or using stacks/recursion) is the goal.

### Core Concept: Stacks for Reversal

Since the list is singly linked and forward, we can push all nodes onto stacks. Popping from the stack gives us the digits in reverse order (LSD first), allowing easy subtraction with borrow.

## Naive Approach

### Intuition

Reverse both lists. Subtract. Reverse result.

### Algorithm

1. `revA = reverse(A)`, `revB = reverse(B)`.
2. Compare `revA` and `revB` to find larger.
3. Iterate, subtracting `valA - valB - borrow`.
4. Store result in new list.
5. Reverse result list.
6. Count frequencies.

### Time Complexity

- **O(N + M)**.

### Space Complexity

- **O(N + M)** to store the reversed/result lists.

## Optimal Approach

### Key Insight

Use Stacks to avoid modifying the input lists (non-destructive).

### Algorithm

1. **Compare:**
   - If `len(A) != len(B)`, longer is larger.
   - If lengths equal, compare node by node. First non-equal determines larger.
   - If identical, return `sign=0, head=0, freq={1 at 0}`.
2. **Push to Stacks:** Push digits of Larger to `s1`, Smaller to `s2`.
3. **Subtract:**
   - While stacks not empty:
     - `val1 = s1.pop()`, `val2 = s2.pop()` (or 0 if empty).
     - `diff = val1 - val2 - borrow`.
     - If `diff < 0`: `diff += 10`, `borrow = 1`. Else `borrow = 0`.
     - Prepend `diff` to result list (build forward).
     - Update frequency map.
4. **Clean up:** Remove leading zeros.
5. Return result.

### Time Complexity

- **O(N + M)**.

### Space Complexity

- **O(N + M)** for stacks and result.

![Algorithm Visualization](../images/LNK-016/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-016/algorithm-steps.png)

## Implementations

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
        // 1. Compare to find larger
        int lenA = getLength(a);
        int lenB = getLength(b);
        ListNode large = a, small = b;
        
        if (lenA < lenB) {
            large = b; small = a;
        } else if (lenA == lenB) {
            ListNode currA = a, currB = b;
            while (currA != null && currA.val == currB.val) {
                currA = currA.next;
                currB = currB.next;
            }
            if (currA == null) return new Result(0, new ListNode(0), new int[]{1,0,0,0,0,0,0,0,0,0}); // Equal
            if (currA.val < currB.val) {
                large = b; small = a;
            }
        }

        // 2. Use Stacks
        Deque<Integer> s1 = new ArrayDeque<>();
        Deque<Integer> s2 = new ArrayDeque<>();
        
        ListNode curr = large;
        while (curr != null) { s1.push(curr.val); curr = curr.next; }
        curr = small;
        while (curr != null) { s2.push(curr.val); curr = curr.next; }

        // 3. Subtract
        ListNode head = null;
        int borrow = 0;
        int[] freq = new int[10];

        while (!s1.isEmpty()) {
            int v1 = s1.pop();
            int v2 = s2.isEmpty() ? 0 : s2.pop();
            
            int diff = v1 - v2 - borrow;
            if (diff < 0) {
                diff += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }
            
            ListNode node = new ListNode(diff);
            node.next = head;
            head = node;
        }

        // 4. Remove leading zeros
        while (head != null && head.val == 0 && head.next != null) {
            head = head.next;
        }

        // 5. Count Freq
        curr = head;
        while (curr != null) {
            freq[curr.val]++;
            curr = curr.next;
        }

        return new Result(1, head, freq);
    }

    private int getLength(ListNode head) {
        int len = 0;
        while (head != null) { len++; head = head.next; }
        return len;
    }
}

public class Main {
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
        self.val = val
        self.next = None

def get_length(head):
    l = 0
    while head:
        l += 1
        head = head.next
    return l

def subtract_with_freq(a: ListNode, b: ListNode):
    len_a = get_length(a)
    len_b = get_length(b)
    
    large, small = a, b
    
    if len_a < len_b:
        large, small = b, a
    elif len_a == len_b:
        curr_a, curr_b = a, b
        while curr_a and curr_a.val == curr_b.val:
            curr_a = curr_a.next
            curr_b = curr_b.next
        
        if not curr_a: # Equal
            return 0, ListNode(0), [1] + [0]*9
            
        if curr_a.val < curr_b.val:
            large, small = b, a
            
    s1, s2 = [], []
    curr = large
    while curr:
        s1.append(curr.val)
        curr = curr.next
    curr = small
    while curr:
        s2.append(curr.val)
        curr = curr.next
        
    head = None
    borrow = 0
    
    while s1:
        v1 = s1.pop()
        v2 = s2.pop() if s2 else 0
        
        diff = v1 - v2 - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
            
        node = ListNode(diff)
        node.next = head
        head = node
        
    while head and head.val == 0 and head.next:
        head = head.next
        
    freq = [0] * 10
    curr = head
    while curr:
        freq[curr.val] += 1
        curr = curr.next
        
    return 1, head, freq

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
        int lenA = getLength(a);
        int lenB = getLength(b);
        ListNode *large = a, *small = b;

        if (lenA < lenB) {
            large = b; small = a;
        } else if (lenA == lenB) {
            ListNode *currA = a, *currB = b;
            while (currA && currA->val == currB->val) {
                currA = currA->next;
                currB = currB->next;
            }
            if (!currA) return {0, new ListNode(0), {1,0,0,0,0,0,0,0,0,0}};
            if (currA->val < currB->val) {
                large = b; small = a;
            }
        }

        stack<int> s1, s2;
        ListNode* curr = large;
        while (curr) { s1.push(curr->val); curr = curr->next; }
        curr = small;
        while (curr) { s2.push(curr->val); curr = curr->next; }

        ListNode* head = nullptr;
        int borrow = 0;

        while (!s1.empty()) {
            int v1 = s1.top(); s1.pop();
            int v2 = 0;
            if (!s2.empty()) { v2 = s2.top(); s2.pop(); }

            int diff = v1 - v2 - borrow;
            if (diff < 0) {
                diff += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }

            ListNode* node = new ListNode(diff);
            node->next = head;
            head = node;
        }

        while (head && head->val == 0 && head->next) {
            ListNode* temp = head;
            head = head->next;
            delete temp;
        }

        vector<int> freq(10, 0);
        curr = head;
        while (curr) {
            freq[curr->val]++;
            curr = curr->next;
        }

        return {1, head, freq};
    }

private:
    int getLength(ListNode* head) {
        int len = 0;
        while (head) { len++; head = head->next; }
        return len;
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
  let len = 0;
  while (head) {
    len++;
    head = head.next;
  }
  return len;
}

function subtractWithFreq(a, b) {
  let lenA = getLength(a);
  let lenB = getLength(b);
  let large = a, small = b;

  if (lenA < lenB) {
    large = b; small = a;
  } else if (lenA === lenB) {
    let currA = a, currB = b;
    while (currA && currA.val === currB.val) {
      currA = currA.next;
      currB = currB.next;
    }
    if (!currA) return [0, new ListNode(0), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]];
    if (currA.val < currB.val) {
      large = b; small = a;
    }
  }

  const s1 = [];
  const s2 = [];
  let curr = large;
  while (curr) { s1.push(curr.val); curr = curr.next; }
  curr = small;
  while (curr) { s2.push(curr.val); curr = curr.next; }

  let head = null;
  let borrow = 0;

  while (s1.length > 0) {
    let v1 = s1.pop();
    let v2 = s2.length > 0 ? s2.pop() : 0;

    let diff = v1 - v2 - borrow;
    if (diff < 0) {
      diff += 10;
      borrow = 1;
    } else {
      borrow = 0;
    }

    let node = new ListNode(diff);
    node.next = head;
    head = node;
  }

  while (head && head.val === 0 && head.next) {
    head = head.next;
  }

  const freq = Array(10).fill(0);
  curr = head;
  while (curr) {
    freq[curr.val]++;
    curr = curr.next;
  }

  return [1, head, freq];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
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

## 🧪 Test Case Walkthrough (Dry Run)

Input: `7 1 6` - `2 9 5`

1. **Compare:** 716 > 295. Large=`716`, Small=`295`.
2. **Stacks:** `s1=[7,1,6]`, `s2=[2,9,5]`.
3. **Pop 1:** `6 - 5 - 0 = 1`. Head=`1`.
4. **Pop 2:** `1 - 9 - 0 = -8`. Borrow=1. Diff=`2`. Head=`2->1`.
5. **Pop 3:** `7 - 2 - 1 = 4`. Head=`4->2->1`.
6. **Clean:** No leading zeros.
7. **Freq:** {1:1, 2:1, 4:1}.

Result: `1`, `4 2 1`, `0 1 1 0 1 0 0 0 0 0`.

![Example Visualization](../images/LNK-016/example-1.png)

## ✅ Proof of Correctness

### Invariant
The stacks allow processing digits from least significant to most significant, correctly propagating the borrow bit.

### Why the approach is correct
- **Comparison:** Ensures we always subtract smaller from larger, avoiding negative intermediate results (except borrow).
- **Borrow Logic:** Standard elementary subtraction algorithm.
- **Leading Zeros:** Handled as a post-processing step.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Add two numbers.
  - *Hint:* Simpler, carry instead of borrow.
- **Extension 2:** Multiply two numbers.
  - *Hint:* O(N*M), much harder.
- **Extension 3:** Negative numbers support.
  - *Hint:* Check signs first. `(-A) - B = -(A+B)`.

## Common Mistakes to Avoid

1. **Comparison Logic**
   - ❌ Wrong: Comparing only lengths.
   - ✅ Correct: If lengths equal, must compare MSB to LSB.

2. **Borrow Propagation**
   - ❌ Wrong: Forgetting to subtract borrow in the next step.
   - ✅ Correct: `v1 - v2 - borrow`.

## Related Concepts

- **BigInt Arithmetic:** How Python handles large integers internally.
- **Stacks:** Reversing order of processing.
