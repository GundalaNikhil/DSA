---
problem_id: GRD_ROBOTICS_MEDIAN_BATCHES_STALE__4276
display_id: GRD-015
slug: robotics-median-after-batches-stale
title: "Robotics Median After Batches with Stale Filter"
difficulty: Medium
difficulty_score: 60
topics:
  - Heap
  - Two Heaps
  - Median Finding
  - Data Structures
tags:
  - heap
  - two-heaps
  - median
  - data-structures
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-015: Robotics Median After Batches with Stale Filter

## Problem Statement

Numbers arrive in batches from robot sensors. A value becomes **"stale"** once it has appeared more than `t` times in total across all batches seen so far. Stale values must be excluded from median calculations.

After processing each batch, report the median of all **non-stale** values seen so far. If all values are stale (or no values exist), output `"NA"`.

**Median definition**:

- If count is odd: middle element
- If count is even: average of two middle elements (round down)

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-015.jpg)

## Input Format

- First line: two integers `k t` (number of batches and staleness threshold)
- Next `k` lines: each line starts with integer `m` (batch size), followed by `m` integers

## Output Format

- `k` space-separated outputs: median after each batch (or "NA" if no valid values)

## Constraints

- `1 <= k <= 1000`
- `1 <= t <= 10^5`
- Total numbers across all batches `<= 2*10^5`
- Values are integers in range `[-10^9, 10^9]`

## Example

**Input:**

```
3 2
3 5 5 1
2 5 3
2 8 9
```

**Output:**

```
5 3 6
```

**Explanation:**

Threshold t = 2 (values appearing > 2 times become stale)

**After Batch 1: [5, 5, 1]**

- Frequency: {5:2, 1:1}
- Non-stale values: [5, 5, 1] (none exceed threshold)
- Sorted: [1, 5, 5]
- Median: 5

**After Batch 2: [5, 5, 1] + [5, 3]**

- Frequency: {5:3, 1:1, 3:1}
- Value 5 appears 3 times > t=2, so it's stale
- Non-stale values: [1, 3]
- Sorted: [1, 3]
- For even count, we take the upper median: 3

**After Batch 3: [1, 3] + [8, 9]** (excluding stale 5)

- Frequency: {5:3 (stale), 1:1, 3:1, 8:1, 9:1}
- Non-stale values: [1, 3, 8, 9]
- Sorted: [1, 3, 8, 9]
- For even count (4 values), median is the average of the two middle values (3 and 8): (3+8)/2 = 5.5, rounded down = 5

The median calculation uses the upper median for pairs and rounds down for averages.

![Example Visualization](../images/GRD-015/example-1.png)

## Notes

- Use two heaps (max-heap for lower half, min-heap for upper half) to maintain median
- Track frequency map to identify stale values
- Use lazy deletion: when a value becomes stale, remove it from heaps
- After each batch, rebalance heaps and compute median
- Time complexity: O(N log N) where N is total numbers

## Related Topics

Two Heaps, Median Finding, Lazy Deletion, Frequency Map, Data Structures

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<String> processBatches(int k, int t, List<List<Integer>> batches) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ktLine = br.readLine();
        if (ktLine == null) return;
        String[] kt = ktLine.trim().split("\\s+");
        int k = Integer.parseInt(kt[0]);
        int t = Integer.parseInt(kt[1]);

        List<List<Integer>> batches = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            String[] line = br.readLine().trim().split("\\s+");
            int m = Integer.parseInt(line[0]);
            List<Integer> batch = new ArrayList<>();
            for (int j = 1; j <= m; j++) batch.add(Integer.parseInt(line[j]));
            batches.add(batch);
        }

        Solution sol = new Solution();
        List<String> results = sol.processBatches(k, t, batches);
        System.out.println(String.join(" ", results));
    }
}
```

### Python

```python
import sys

class Solution:
    def process_batches(self, k, t, batches):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    kt = input_data[0].split()
    k = int(kt[0])
    t = int(kt[1])

    batches = []
    for i in range(1, k + 1):
        line = list(map(int, input_data[i].split()))
        batches.append(line[1:])

    sol = Solution()
    results = sol.process_batches(k, t, batches)
    print(" ".join(results))

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
    vector<string> processBatches(int k, int t, vector<vector<int>>& batches) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int k, t;
    if (!(cin >> k >> t)) return 0;

    vector<vector<int>> batches(k);
    for (int i = 0; i < k; i++) {
        int m;
        cin >> m;
        batches[i].resize(m);
        for (int j = 0; j < m; j++) cin >> batches[i][j];
    }

    Solution sol;
    vector<string> results = sol.processBatches(k, t, batches);
    for (int i = 0; i < results.size(); i++) {
        cout << results[i] << (i == results.size() - 1 ? "" : " ");
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
  processBatches(k, t, batches) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const kt = input[0].trim().split(/\s+/);
  const k = parseInt(kt[0]);
  const t = parseInt(kt[1]);

  const batches = [];
  for (let i = 1; i <= k; i++) {
    const line = input[i].trim().split(/\s+/).map(Number);
    batches.push(line.slice(1));
  }

  const sol = new Solution();
  const results = sol.processBatches(k, t, batches);
  console.log(results.join(" "));
}

solve();
```
