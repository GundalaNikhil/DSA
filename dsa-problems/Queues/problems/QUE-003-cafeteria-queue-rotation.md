---
problem_id: QUE_CAFETERIA_QUEUE_ROTATION__9067
display_id: QUE-003
slug: cafeteria-queue-rotation
title: "Cafeteria Queue Rotation"
difficulty: Easy
difficulty_score: 20
topics:
  - Queue
  - Array Manipulation
  - Simulation
tags:
  - queue
  - rotation
  - easy
  - arrays
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-003: Cafeteria Queue Rotation

## Problem Statement

A cafeteria line is represented as a queue of student IDs. The manager rotates the line by moving the first `k` students to the back of the line in the same order.

Given the initial queue and `k`, output the resulting order after the left rotation. If `k` is larger than the queue length, use `k % n` rotations.

![Problem Illustration](../images/QUE-003/problem-illustration.png)

## Input Format

- First line: integer `n` (number of students)
- Second line: `n` space-separated integers (queue order, front to back)
- Third line: integer `k` (number of left rotations)

## Output Format

- Single line with the rotated queue values, space-separated
- If `n = 0`, print an empty line

## Constraints

- `1 <= n <= 100000`
- `0 <= k <= 10^9`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
4
4 9 1 7
3
```

**Output:**

```
7 4 9 1
```

**Explanation:**

Rotate left by `3`:

- Move 4 -> back
- Move 9 -> back
- Move 1 -> back

Queue becomes `[7, 4, 9, 1]`.

![Example Visualization](../images/QUE-003/example-1.png)

## Notes

- Normalize `k` with `k % n` to avoid extra work
- You can simulate by dequeuing and enqueuing `k` times
- Time complexity: O(n)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Rotation, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String processQueueOperations(List<String[]> operations) {
        //Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            List<String[]> operations = new ArrayList<>();

            for (int i = 0; i < m; i++) {
                String op = sc.next();
                if (op.equals("ENQUEUE")) {
                    String val = sc.next();
                    operations.add(new String[]{op, val});
                } else {
                    operations.add(new String[]{op});
                }
            }

            Solution solution = new Solution();
            String result = solution.processQueueOperations(operations);
            System.out.println(result);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
from collections import deque
import sys

def process_queue_operations(operations: List[List[str]]) -> str:
    # //Implement here
    return ""

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        m = int(next(iterator))  # number of operations
        operations = []
        for _ in range(m):
            op = next(iterator)
            if op in ("ENQUEUE",):
                val = next(iterator)
                operations.append([op, val])
            else:
                operations.append([op])

        result = process_queue_operations(operations)
        print(result)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

class Solution {
public:
    string processQueueOperations(const vector<vector<string>>& operations) {
        //Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (cin >> m) {
        vector<vector<string>> operations;
        operations.reserve(m);

        for (int i = 0; i < m; i++) {
            string op;
            cin >> op;
            if (op == "ENQUEUE") {
                string val;
                cin >> val;
                operations.push_back({op, val});
            } else {
                operations.push_back({op});
            }
        }

        Solution solution;
        string result = solution.processQueueOperations(operations);
        cout << result << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processQueueOperations(operations) {
    //Implement here
    return "";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) =>
  data.push(
    ...line
      .trim()
      .split(/\s+/)
      .filter((x) => x !== "")
  )
);
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const m = parseInt(data[idx++], 10);
  const operations = [];

  for (let i = 0; i < m; i++) {
    const op = data[idx++];
    if (op === "ENQUEUE") {
      const val = data[idx++];
      operations.push([op, val]);
    } else {
      operations.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processQueueOperations(operations);
  console.log(result);
});
```
