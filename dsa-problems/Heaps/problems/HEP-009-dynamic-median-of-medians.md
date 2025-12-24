---
problem_id: HEP_DYNAMIC_MEDIAN_OF_MEDIANS__7312
display_id: HEP-009
slug: dynamic-median-of-medians
title: "Dynamic Median of Medians"
difficulty: Medium
difficulty_score: 60
topics:
  - Heaps
  - Medians
  - Union-Find
tags:
  - heaps
  - median
  - union-find
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-009: Dynamic Median of Medians

## Problem Statement

Maintain multiple groups of numbers. Each group has its own median (lower middle if even). You must support the following operations:

- `NEW id m` followed by `m` integers: create a new group
- `ADD id x`: insert `x` into group `id`
- `MERGE id1 id2`: merge group `id2` into `id1`
- `QUERY`: output the median of the current group medians

If no groups contain elements, output `EMPTY`.

![Problem Illustration](../images/HEP-009/problem-illustration.png)

## Input Format

- First line: integer `q` (number of operations)
- Next operations:
  - `NEW id m` then a line with `m` integers
  - `ADD id x`
  - `MERGE id1 id2`
  - `QUERY`

## Output Format

- For each `QUERY`, output one line with the median of medians or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= id <= 100000`
- Total elements across all groups `<= 100000`
- `-10^9 <= value <= 10^9`

## Example

**Input:**

```
4
NEW 1 2
1 3
NEW 2 1
2
MERGE 1 2
QUERY
```

**Output:**

```
2
```

**Explanation:**

After merging, group 1 contains [1, 2, 3]. Its median is 2, which is also the median of all group medians.

![Example Visualization](../images/HEP-009/example-1.png)

## Notes

- Maintain two heaps for each group to track its median
- Track medians globally using another pair of heaps
- Merge smaller group into larger group for efficiency
- Time complexity: O((n + q) log n)
- Space complexity: O(n)

## Related Topics

Heaps, Median Maintenance, Union-Find, Merging

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
            if (op.equals("NEW")) {
                String id = sc.next();
                int m = sc.nextInt();
                String[] line = new String[2 + m];
                line[0] = op;
                line[1] = id;
                for (int j = 0; j < m; j++) {
                    line[2 + j] = sc.next();
                }
                operations.add(line);
            } else if (op.equals("ADD")) {
                String id = sc.next();
                String x = sc.next();
                operations.add(new String[]{op, id, x});
            } else if (op.equals("MERGE")) {
                String id1 = sc.next();
                String id2 = sc.next();
                operations.add(new String[]{op, id1, id2});
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
        if op == "NEW":
            gid = next(it)
            m = int(next(it))
            values = [next(it) for _ in range(m)]
            operations.append([op, gid] + values)
        elif op == "ADD":
            gid = next(it)
            x = next(it)
            operations.append([op, gid, x])
        elif op == "MERGE":
            gid1 = next(it)
            gid2 = next(it)
            operations.append([op, gid1, gid2])
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
        if (op == "NEW") {
            string gid;
            int m;
            cin >> gid >> m;
            vector<string> line;
            line.push_back(op);
            line.push_back(gid);
            for (int j = 0; j < m; j++) {
                string x;
                cin >> x;
                line.push_back(x);
            }
            operations.push_back(line);
        } else if (op == "ADD") {
            string gid, x;
            cin >> gid >> x;
            operations.push_back({op, gid, x});
        } else if (op == "MERGE") {
            string gid1, gid2;
            cin >> gid1 >> gid2;
            operations.push_back({op, gid1, gid2});
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
    if (op === "NEW") {
      const gid = data[idx++];
      const m = parseInt(data[idx++], 10);
      const values = [];
      for (let j = 0; j < m; j++) {
        values.push(data[idx++]);
      }
      operations.push([op, gid, ...values]);
    } else if (op === "ADD") {
      const gid = data[idx++];
      const x = data[idx++];
      operations.push([op, gid, x]);
    } else if (op === "MERGE") {
      const gid1 = data[idx++];
      const gid2 = data[idx++];
      operations.push([op, gid1, gid2]);
    } else {
      operations.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processOperations(operations);
  console.log(result.join("\n"));
});
```
