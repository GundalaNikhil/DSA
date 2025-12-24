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

class Solution {
    public int[][] mergeIntervals(int[][] intervals) {
        // Your implementation here
        return new int[0][0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] intervals = new int[n][3];
        for (int i = 0; i < n; i++) {
            intervals[i][0] = sc.nextInt();
            intervals[i][1] = sc.nextInt();
            intervals[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[][] result = solution.mergeIntervals(intervals);
        System.out.println(result.length);
        for (int[] row : result) {
            System.out.println(row[0] + " " + row[1] + " " + row[2]);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    # Your implementation here
    return []

def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        start, end, payload = map(int, input().split())
        intervals.append([start, end, payload])

    result = merge_intervals(intervals)
    print(len(result))
    for start, end, payload in result:
        print(start, end, payload)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> mergeIntervals(const vector<vector<int>>& intervals) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> intervals(n, vector<int>(3));
    for (int i = 0; i < n; i++) {
        cin >> intervals[i][0] >> intervals[i][1] >> intervals[i][2];
    }

    Solution solution;
    vector<vector<int>> result = solution.mergeIntervals(intervals);
    cout << result.size() << "\n";
    for (const auto& row : result) {
        cout << row[0] << " " << row[1] << " " << row[2] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mergeIntervals(intervals) {
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
  const n = parseInt(data[idx++], 10);
  const intervals = [];
  for (let i = 0; i < n; i++) {
    const start = parseInt(data[idx++], 10);
    const end = parseInt(data[idx++], 10);
    const payload = parseInt(data[idx++], 10);
    intervals.push([start, end, payload]);
  }

  const solution = new Solution();
  const result = solution.mergeIntervals(intervals);
  console.log(result.length);
  for (const row of result) {
    console.log(row[0] + " " + row[1] + " " + row[2]);
  }
});
```
