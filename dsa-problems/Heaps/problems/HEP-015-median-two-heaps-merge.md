---
problem_id: HEP_MEDIAN_TWO_HEAPS_MERGE__4476
display_id: HEP-015
slug: median-two-heaps-merge
title: "Median of Two Heaps After Merge"
difficulty: Medium
difficulty_score: 50
topics:
  - Heaps
  - Median
  - Data Structures
tags:
  - heaps
  - median
  - merge
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-015: Median of Two Heaps After Merge

## Problem Statement

You are given the contents of a max-heap and a min-heap (as arrays). Treat them as two multisets. Compute the median of all elements after merging both sets.

If the total number of elements is odd, the median is the middle element. If it is even, the median is the average of the two middle elements.

![Problem Illustration](../images/HEP-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers (max-heap contents)
- Third line: `m` integers (min-heap contents)

## Output Format

- Single number: the median (use `.5` if needed)

## Constraints

- `0 <= n, m <= 200000`
- `-10^9 <= value <= 10^9`

## Example

**Input:**

```
2 2
1 3
2 4
```

**Output:**

```
2.5
```

**Explanation:**

Merged values are [1,2,3,4]. Median is (2 + 3) / 2 = 2.5.

![Example Visualization](../images/HEP-015/example-1.png)

## Notes

- Use two heaps to balance all elements
- Keep size difference at most 1
- Time complexity: O((n+m) log(n+m))
- Space complexity: O(n+m)

## Related Topics

Heaps, Median Maintenance, Data Structures

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public double findMedianAfterMerge(int n, int m, int[] heap1, int[] heap2) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);

        int[] heap1 = new int[n];
        if (n > 0) {
            String[] v1 = br.readLine().trim().split("\\s+");
            for (int i = 0; i < n; i++) heap1[i] = Integer.parseInt(v1[i]);
        }

        int[] heap2 = new int[m];
        if (m > 0) {
            String[] v2 = br.readLine().trim().split("\\s+");
            for (int i = 0; i < m; i++) heap2[i] = Integer.parseInt(v2[i]);
        }

        Solution sol = new Solution();
        double res = sol.findMedianAfterMerge(n, m, heap1, heap2);
        if (res == (long) res) System.out.println((long) res);
        else System.out.println(res);
    }
}
```

### Python

```python
import sys

class Solution:
    def find_median_after_merge(self, n, m, heap1, heap2):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    heap1 = list(map(int, input_data[2:2+n]))
    heap2 = list(map(int, input_data[2+n:2+n+m]))

    sol = Solution()
    res = sol.find_median_after_merge(n, m, heap1, heap2)
    if res == int(res):
        print(int(res))
    else:
        print(res)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double findMedianAfterMerge(int n, int m, vector<int>& heap1, vector<int>& heap2) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> heap1(n), heap2(m);
    for (int i = 0; i < n; i++) cin >> heap1[i];
    for (int i = 0; i < m; i++) cin >> heap2[i];

    Solution sol;
    double res = sol.findMedianAfterMerge(n, m, heap1, heap2);

    if (res == (long long)res) cout << (long long)res << endl;
    else cout << fixed << setprecision(1) << res << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findMedianAfterMerge(n, m, heap1, heap2) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);

  const heap1 = [];
  for (let i = 0; i < n; i++) heap1.push(parseInt(input[idx++]));
  const heap2 = [];
  for (let i = 0; i < m; i++) heap2.push(parseInt(input[idx++]));

  const sol = new Solution();
  const res = sol.findMedianAfterMerge(n, m, heap1, heap2);
  console.log(res);
}

solve();
```
