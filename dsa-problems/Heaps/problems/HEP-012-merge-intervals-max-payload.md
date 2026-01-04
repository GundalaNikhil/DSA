---
problem_id: HEP_MERGE_INTERVALS_MAX_PAYLOAD__6043
display_id: HEP-012
slug: merge-intervals-max-payload
title: "Merge Intervals With Max Payload"
difficulty: Medium
difficulty_score: 48
topics:
  - Heaps
  - Intervals
  - Sorting
tags:
  - heaps
  - intervals
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-012: Merge Intervals With Max Payload

## Problem Statement

You are given `n` intervals, each with a payload value. When two intervals overlap, they should be merged into a single interval `[minStart, maxEnd]`. The merged payload is the maximum payload among all intervals in that merged group.

Return the merged intervals sorted by start time.

![Problem Illustration](../images/HEP-012/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n` lines: three integers `start`, `end`, `payload`

## Output Format

- First line: integer `m` (number of merged intervals)
- Next `m` lines: `start end payload` for each merged interval

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= start <= end <= 10^9`
- `0 <= payload <= 10^9`

## Example

**Input:**

```
2
1 3 5
2 4 7
```

**Output:**

```
1
1 4 7
```

**Explanation:**

The intervals overlap, so they merge into [1,4] with payload max(5,7)=7.

![Example Visualization](../images/HEP-012/example-1.png)

## Notes

- Sort intervals by start time
- Extend the current interval while overlaps exist
- Track the maximum payload in the merged segment
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Intervals, Sorting, Sweeping, Heaps

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<int[]> mergeIntervals(int n, int[][] intervals) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        int n = Integer.parseInt(firstLine.trim());

        int[][] intervals = new int[n][3];
        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            intervals[i][0] = Integer.parseInt(parts[0]);
            intervals[i][1] = Integer.parseInt(parts[1]);
            intervals[i][2] = Integer.parseInt(parts[2]);
        }

        Solution sol = new Solution();
        List<int[]> result = sol.mergeIntervals(n, intervals);

        PrintWriter out = new PrintWriter(System.out);
        out.println(result.size());
        for (int[] interval : result) {
            out.println(interval[0] + " " + interval[1] + " " + interval[2]);
        }
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def merge_intervals(self, n, intervals):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    intervals = []
    idx = 1
    for _ in range(n):
        start = int(input_data[idx])
        end = int(input_data[idx+1])
        payload = int(input_data[idx+2])
        intervals.append([start, end, payload])
        idx += 3

    sol = Solution()
    result = sol.merge_intervals(n, intervals)
    print(len(result))
    for res in result:
        print(*(res))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> mergeIntervals(int n, vector<vector<int>>& intervals) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> intervals(n, vector<int>(3));
    for (int i = 0; i < n; i++) {
        cin >> intervals[i][0] >> intervals[i][1] >> intervals[i][2];
    }

    Solution sol;
    vector<vector<int>> result = sol.mergeIntervals(n, intervals);

    cout << result.size() << "\n";
    for (const auto& res : result) {
        cout << res[0] << " " << res[1] << " " << res[2] << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  mergeIntervals(n, intervals) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const intervals = [];
  for (let i = 0; i < n; i++) {
    const start = parseInt(input[idx++]);
    const end = parseInt(input[idx++]);
    const payload = parseInt(input[idx++]);
    intervals.push([start, end, payload]);
  }

  const sol = new Solution();
  const result = sol.mergeIntervals(n, intervals);
  process.stdout.write(result.length + "\n");
  for (const res of result) {
    process.stdout.write(res.join(" ") + "\n");
  }
}

solve();
```
