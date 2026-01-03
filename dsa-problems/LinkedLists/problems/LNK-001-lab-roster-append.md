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

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public void pushBack(int value) {
        //Implement here
    }

    public int[] toArray() {
        //Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        sc.nextLine();

        Solution solution = new Solution();
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine().trim();
            if (line.startsWith("push_back")) {
                String[] parts = line.split(" ");
                int value = Integer.parseInt(parts[1]);
                solution.pushBack(value);
            } else {
                int[] arr = solution.toArray();
                for (int j = 0; j < arr.length; j++) {
                    System.out.print(arr[j]);
                    if (j + 1 < arr.length) System.out.print(" ");
                }
                System.out.println();
            }
        }
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

class Solution:
    def push_back(self, value: int) -> None:
        # //Implement here
        pass
    def to_array(self):
        # //Implement here
        return []

def main():
    input = sys.stdin.read
    data = input().splitlines()
    if not data:
        return

    n = int(data[0])
    sol = Solution()

    for i in range(1, n + 1):
        line = data[i].strip()
        if line.startswith("push_back"):
            _, v = line.split()
            sol.push_back(int(v))
        else:
            arr = sol.to_array()
            print(" ".join(str(x) for x in arr))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    void pushBack(int value) {
        //Implement here
    }

    vector<int> toArray() {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    string dummy;
    getline(cin, dummy);

    Solution solution;
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        if (line.rfind("push_back", 0) == 0) {
            stringstream ss(line);
            string op;
            int value;
            ss >> op >> value;
            solution.pushBack(value);
        } else {
            vector<int> arr = solution.toArray();
            for (int j = 0; j < (int)arr.size(); j++) {
                if (j) cout << " ";
                cout << arr[j];
            }
            cout << "\n";
        }
    }
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

class Solution {
  pushBack(value) {
    //Implement here
  }

  toArray() {
    //Implement here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  if (lines.length === 0) return;
  const n = parseInt(lines[0], 10);
  const sol = new Solution();
  for (let i = 1; i <= n; i++) {
    const line = lines[i];
    if (line.startsWith("push_back")) {
      const parts = line.split(" ");
      sol.pushBack(parseInt(parts[1], 10));
    } else {
      const arr = sol.toArray();
      console.log(arr.join(" "));
    }
  }
});
```
