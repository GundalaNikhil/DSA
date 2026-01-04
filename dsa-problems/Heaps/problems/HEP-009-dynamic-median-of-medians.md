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
import java.io.*;

class Solution {
    public void processMedianOperations(int q, List<String> queries) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        int q = Integer.parseInt(firstLine.trim());

        List<String> queries = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            StringBuilder queryLine = new StringBuilder(br.readLine());
            if (queryLine.toString().startsWith("NEW")) {
                queryLine.append("\n").append(br.readLine());
            }
            queries.add(queryLine.toString());
        }

        Solution sol = new Solution();
        sol.processMedianOperations(q, queries);
    }
}
```

### Python

```python
import sys

class Solution:
    def process_median_operations(self, q, queries):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    q = int(input_data[0].strip())
    queries = []
    i = 1
    while len(queries) < q:
        query_line = input_data[i]
        if query_line.startswith("NEW"):
            queries.append(query_line + "\n" + input_data[i+1])
            i += 2
        else:
            queries.append(query_line)
            i += 1

    sol = Solution()
    sol.process_median_operations(q, queries)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    void processMedianOperations(int q, const vector<string>& queries) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int q;
    if (!(cin >> q)) return 0;
    cin.ignore();

    vector<string> queries;
    for (int i = 0; i < q; i++) {
        string line;
        getline(cin, line);
        if (line.substr(0, 3) == "NEW") {
            string nextLine;
            getline(cin, nextLine);
            queries.push_back(line + "\n" + nextLine);
        } else {
            queries.push_back(line);
        }
    }

    Solution sol;
    sol.processMedianOperations(q, queries);

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  processMedianOperations(q, queries) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const q = parseInt(input[0].trim());
  const queries = [];
  let i = 1;
  while (queries.length < q) {
    let queryLine = input[i];
    if (queryLine.startsWith("NEW")) {
      queries.push(queryLine + "\n" + input[i + 1]);
      i += 2;
    } else {
      queries.push(queryLine);
      i += 1;
    }
  }

  const sol = new Solution();
  sol.processMedianOperations(q, queries);
}

solve();
```
