---
problem_id: GRD_LIBRARY_MERGE_QUEUES__8135
display_id: GRD-010
slug: library-merge-queues
title: "Library Merge Queues"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Heap
  - Merge K Sorted Lists
tags:
  - greedy
  - heap
  - priority-queue
  - merge
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-010: Library Merge Queues

## Problem Statement

You have `k` sorted queues of book IDs (integers). You need to merge them into a single sorted stream with a constraint: **no book ID can appear more than twice consecutively** in the output.

If a book ID would appear for the third time in a row, skip it and move to the next available different ID. Continue this process until all queues are processed.

Return the merged stream as a list.

![Problem Illustration](../images/GRD-010/problem-illustration.png)

## Input Format

- First line: integer `k` (number of queues)
- Next `k` lines: each line starts with an integer `len` (queue length), followed by `len` sorted integers

## Output Format

- Single line with space-separated integers representing the merged stream

## Constraints

- `1 <= k <= 100`
- Total elements across all queues `<= 2*10^5`
- All queues are sorted in non-decreasing order
- Book IDs are integers in range `[1, 10^9]`

## Example

**Input:**

```
3
3 1 1 1
2 1 2
1 2
```

**Output:**

```
1 1 1 2 2
```

**Explanation:**

Queues:

- Queue 0: [1, 1, 1]
- Queue 1: [1, 2]
- Queue 2: [2]

Merge process:

1. Take 1 from queue 0 → output: [1], last two: [1]
2. Take 1 from queue 0 → output: [1, 1], last two: [1, 1]
3. Cannot take another 1 (would be third consecutive). Take 2 from queue 1 → output: [1, 1, 2]
4. Take 1 from queue 0 → output: [1, 1, 2, 1]
5. Take 2 from queue 2 → output: [1, 1, 2, 1, 2]

The constraint ensures no more than 2 consecutive identical values.

![Example Visualization](../images/GRD-010/example-1.png)

## Notes

- Use a min-heap to track the minimum value across all queue fronts
- Track the last two values added to the output
- If the next minimum would create three consecutive identical values, temporarily skip it
- Pull from a different queue/value, then resume
- Time complexity: O(N log k) where N is total elements

## Related Topics

Merge K Sorted Lists, Heap, Priority Queue, Greedy Algorithms, Constraint Handling

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> mergeWithConstraint(int k, List<List<Integer>> queues) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String kLine = br.readLine();
        if (kLine == null) return;
        int k = Integer.parseInt(kLine.trim());

        List<List<Integer>> queues = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            int len = Integer.parseInt(line[0]);
            List<Integer> q = new ArrayList<>();
            for (int j = 1; j <= len; j++) q.add(Integer.parseInt(line[j]));
            queues.add(q);
        }

        Solution sol = new Solution();
        List<Integer> result = sol.mergeWithConstraint(k, queues);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < result.size(); i++) {
            out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def merge_with_constraint(self, k, queues):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    k = int(input_data[0].strip())
    queues = []
    for i in range(1, k + 1):
        line = list(map(int, input_data[i].split()))
        queues.append(line[1:])

    sol = Solution()
    result = sol.merge_with_constraint(k, queues)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> mergeWithConstraint(int k, vector<vector<int>>& queues) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int k;
    if (!(cin >> k)) return 0;

    vector<vector<int>> queues(k);
    for (int i = 0; i < k; i++) {
        int len;
        cin >> len;
        queues[i].resize(len);
        for (int j = 0; j < len; j++) cin >> queues[i][j];
    }

    Solution sol;
    vector<int> result = sol.mergeWithConstraint(k, queues);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  mergeWithConstraint(k, queues) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const k = parseInt(input[0].trim());
  const queues = [];
  for (let i = 1; i <= k; i++) {
    const line = input[i].trim().split(/\s+/).map(Number);
    queues.push(line.slice(1));
  }

  const sol = new Solution();
  const result = sol.mergeWithConstraint(k, queues);
  console.log(result.join(" "));
}

solve();
```
