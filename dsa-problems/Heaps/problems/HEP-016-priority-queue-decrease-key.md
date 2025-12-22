---
problem_id: HEP_PRIORITY_QUEUE_DECREASE_KEY__8091
display_id: HEP-016
slug: priority-queue-decrease-key
title: "Priority Queue with Decrease-Key"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Priority Queue
  - Data Structures
tags:
  - heaps
  - priority-queue
  - decrease-key
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-016: Priority Queue with Decrease-Key

## Problem Statement

Implement a priority queue that supports:

- `INSERT id value`
- `DECREASE id delta` (decrease the key of `id` by `delta`)
- `EXTRACT` (remove and output the minimum key)

If `EXTRACT` is called on an empty queue, output `EMPTY`. If multiple ids have the same key, return the lexicographically smallest id.

![Problem Illustration](../images/HEP-016/problem-illustration.png)

## Input Format

- First line: integer `q`
- Next `q` lines: one of the operations above

## Output Format

- For each `EXTRACT`, output `value id` or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= value, delta <= 10^9`
- `1 <= |id| <= 20` (alphanumeric)

## Example

**Input:**

```
5
INSERT id1 5
INSERT id2 3
DECREASE id1 4
EXTRACT
EXTRACT
```

**Output:**

```
1 id1
3 id2
```

**Explanation:**

- id1 decreases from 5 to 1
- Extracts return id1 (1) then id2 (3)

![Example Visualization](../images/HEP-016/example-1.png)

## Notes

- Use a binary heap with a position map
- Decrease-key can be O(log n) with index tracking
- Time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Heaps, Priority Queue, Decrease-Key, Data Structures

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<String> processOperations(List<String[]> operations) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        List<String[]> operations = new ArrayList<>();

        for (int i = 0; i < q; i++) {
            String op = sc.next();
            if (op.equals("INSERT")) {
                String id = sc.next();
                String value = sc.next();
                operations.add(new String[]{op, id, value});
            } else if (op.equals("DECREASE")) {
                String id = sc.next();
                String delta = sc.next();
                operations.add(new String[]{op, id, delta});
            } else {
                operations.add(new String[]{op});
            }
        }

        Solution solution = new Solution();
        List<String> result = solution.processOperations(operations);
        for (String line : result) {
            System.out.println(line);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def process_operations(operations: List[List[str]]) -> List[str]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    operations = []
    for _ in range(q):
        op = next(it)
        if op == "INSERT":
            gid = next(it)
            value = next(it)
            operations.append([op, gid, value])
        elif op == "DECREASE":
            gid = next(it)
            delta = next(it)
            operations.append([op, gid, delta])
        else:
            operations.append([op])

    result = process_operations(operations)
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> processOperations(const vector<vector<string>>& operations) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    vector<vector<string>> operations;
    operations.reserve(q);

    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        if (op == "INSERT") {
            string id, value;
            cin >> id >> value;
            operations.push_back({op, id, value});
        } else if (op == "DECREASE") {
            string id, delta;
            cin >> id >> delta;
            operations.push_back({op, id, delta});
        } else {
            operations.push_back({op});
        }
    }

    Solution solution;
    vector<string> result = solution.processOperations(operations);
    for (const string& line : result) {
        cout << line << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processOperations(operations) {
    // Your implementation here
    return [];
  }
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
  const q = parseInt(data[idx++], 10);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "INSERT") {
      const id = data[idx++];
      const value = data[idx++];
      operations.push([op, id, value]);
    } else if (op === "DECREASE") {
      const id = data[idx++];
      const delta = data[idx++];
      operations.push([op, id, delta]);
    } else {
      operations.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processOperations(operations);
  console.log(result.join("\n"));
});
```
