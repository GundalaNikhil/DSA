---
problem_id: LNK_LAB_ROSTER_APPEND__3582
display_id: LNK-001
slug: lab-roster-append
title: "Lab Roster Append"
difficulty: Easy
difficulty_score: 20
topics:
  - Linked List
  - Data Structures
  - Implementation
tags:
  - linked-list
  - implementation
  - append
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# LNK-001: Lab Roster Append

## Problem Statement

Implement a singly linked list that supports two operations:

- `push_back value`: append `value` to the end of the list
- `to_array`: output all elements in order

For each `to_array` operation, print the current list contents.

![Problem Illustration](../images/LNK-001/problem-illustration.png)

## Input Format

- First line: integer `n` (number of operations)
- Next `n` lines: either `push_back value` or `to_array`

## Output Format

- For each `to_array`, print list values space-separated on one line
- If the list is empty, print an empty line

## Constraints

- `1 <= n <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5
push_back 3
push_back 7
to_array
push_back -2
to_array
```

**Output:**

```
3 7
3 7 -2
```

**Explanation:**

Operation sequence:

1. push_back 3 -> list: [3]
2. push_back 7 -> list: [3, 7]
3. to_array -> output: 3 7
4. push_back -2 -> list: [3, 7, -2]
5. to_array -> output: 3 7 -2

![Example Visualization](../images/LNK-001/example-1.png)

## Notes

- Track both head and tail pointers for O(1) append
- Handle empty list carefully
- Time complexity: O(1) per push_back, O(n) per to_array
- Space complexity: O(n)

## Related Topics

Linked List Implementation, Tail Pointer, Array Conversion

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
    private ListNode head, tail;

    public void pushBack(int value) {
        // Implement here
    }

    public List<Integer> toArray() {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        Solution sol = new Solution();
        PrintWriter out = new PrintWriter(System.out);

        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            if (parts[0].equals("push_back")) {
                sol.pushBack(Integer.parseInt(parts[1]));
            } else if (parts[0].equals("to_array")) {
                List<Integer> res = sol.toArray();
                for (int j = 0; j < res.size(); j++) {
                    out.print(res.get(j) + (j == res.size() - 1 ? "" : " "));
                }
                out.println();
            }
        }
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
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value):
        # Implement here
        pass

    def to_array(self):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])
    sol = Solution()

    for i in range(1, n + 1):
        parts = input_data[i].split()
        if parts[0] == "push_back":
            sol.push_back(int(parts[1]))
        elif parts[0] == "to_array":
            print(*(sol.to_array()))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
private:
    ListNode *head, *tail;
public:
    Solution() : head(NULL), tail(NULL) {}

    void pushBack(int value) {
        // Implement here
    }

    vector<int> toArray() {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    Solution sol;
    string op;
    while (n--) {
        cin >> op;
        if (op == "push_back") {
            int val;
            cin >> val;
            sol.pushBack(val);
        } else if (op == "to_array") {
            vector<int> res = sol.toArray();
            for (int i = 0; i < res.size(); i++) {
                cout << res[i] << (i == res.size() - 1 ? "" : " ");
            }
            cout << "\n";
        }
    }

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
  constructor() {
    this.head = null;
    this.tail = null;
  }

  pushBack(value) {
    // Implement here
  }

  toArray() {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length === 0) return;

  let n = parseInt(input[0]);
  const sol = new Solution();

  for (let i = 1; i <= n; i++) {
    const parts = input[i].trim().split(/\s+/);
    if (parts[0] === "push_back") {
      sol.pushBack(parseInt(parts[1]));
    } else if (parts[0] === "to_array") {
      console.log(sol.toArray().join(" "));
    }
  }
}

solve();
```
