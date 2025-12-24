---
problem_id: HEP_K_CLOSEST_STREAM_WEIGHT__4950
display_id: HEP-011
slug: k-closest-stream-weight
title: "K Closest Points to Origin (Stream) with Weight"
difficulty: Medium
difficulty_score: 53
topics:
  - Heaps
  - Streaming
  - Geometry
tags:
  - heaps
  - streaming
  - geometry
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-011: K Closest Points to Origin (Stream) with Weight

## Problem Statement

You receive a stream of points. Each point `(x, y)` has a positive weight `w`. The weighted distance is:

```
(x^2 + y^2) / w
```

Maintain the `k` points with the smallest weighted distance. Each `ADD` assigns an increasing id starting from 1. For each `QUERY`, output the ids of the current `k` closest points in ascending order of weighted distance (break ties by smaller id). If fewer than `k` points exist, output all. If no points exist, output `EMPTY`.

![Problem Illustration](../images/HEP-011/problem-illustration.png)

## Input Format

- First line: integers `q` and `k`
- Next `q` lines:
  - `ADD x y w`
  - `QUERY`

## Output Format

- For each `QUERY`, output one line with ids separated by spaces, or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= k <= 100000`
- `-10^6 <= x, y <= 10^6`
- `1 <= w <= 10^6`

## Example

**Input:**

```
3 1
ADD 1 1 1
ADD 2 2 1
QUERY
```

**Output:**

```
1
```

**Explanation:**

Distances:

- id 1: (1^2 + 1^2) / 1 = 2
- id 2: (2^2 + 2^2) / 1 = 8

The closest point is id 1.

![Example Visualization](../images/HEP-011/example-1.png)

## Notes

- Use a max-heap of size k to keep the closest points
- Compare distances by cross-multiplying to avoid floating errors
- Time complexity: O(q log k)
- Space complexity: O(k)

## Related Topics

Heaps, Streaming, Geometry, Top K

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<String> processOperations(int k, List<String[]> operations) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        int k = sc.nextInt();
        List<String[]> operations = new ArrayList<>();

        for (int i = 0; i < q; i++) {
            String op = sc.next();
            if (op.equals("ADD")) {
                String x = sc.next();
                String y = sc.next();
                String w = sc.next();
                operations.add(new String[]{op, x, y, w});
            } else {
                operations.add(new String[]{op});
            }
        }

        Solution solution = new Solution();
        List<String> result = solution.processOperations(k, operations);
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

def process_operations(k: int, operations: List[List[str]]) -> List[str]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    k = int(next(it))
    operations = []
    for _ in range(q):
        op = next(it)
        if op == "ADD":
            x = next(it)
            y = next(it)
            w = next(it)
            operations.append([op, x, y, w])
        else:
            operations.append([op])

    result = process_operations(k, operations)
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
    vector<string> processOperations(int k, const vector<vector<string>>& operations) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q, k;
    if (!(cin >> q >> k)) return 0;
    vector<vector<string>> operations;
    operations.reserve(q);

    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        if (op == "ADD") {
            string x, y, w;
            cin >> x >> y >> w;
            operations.push_back({op, x, y, w});
        } else {
            operations.push_back({op});
        }
    }

    Solution solution;
    vector<string> result = solution.processOperations(k, operations);
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
  processOperations(k, operations) {
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
  const k = parseInt(data[idx++], 10);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "ADD") {
      const x = data[idx++];
      const y = data[idx++];
      const w = data[idx++];
      operations.push([op, x, y, w]);
    } else {
      operations.push([op]);
    }
  }

  const solution = new Solution();
  const result = solution.processOperations(k, operations);
  console.log(result.join("\n"));
});
```
