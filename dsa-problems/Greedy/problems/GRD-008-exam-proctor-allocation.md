---
problem_id: GRD_EXAM_PROCTOR_ALLOCATION__3517
display_id: GRD-008
slug: exam-proctor-allocation
title: "Exam Proctor Allocation"
difficulty: Medium
difficulty_score: 40
topics:
  - Greedy Algorithms
  - Sweep Line
  - Intervals
tags:
  - greedy
  - sweep-line
  - intervals
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-008: Exam Proctor Allocation

## Problem Statement

You have `n` exam sessions, where each session `i` occurs during time interval `[start[i], end[i]]`. Each proctor can supervise up to `r` simultaneously occurring exams.

Your task is to find the minimum number of proctors needed to cover all exam sessions.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-008.jpg)

## Input Format

- First line: two integers `n r` (number of exams and max exams per proctor)
- Next `n` lines: two integers `start end` representing each exam's time interval

## Output Format

- Single integer: minimum number of proctors needed

## Constraints

- `1 <= n <= 10^5`
- `1 <= r <= 10^9`
- `0 <= start < end <= 10^9`

## Example

**Input:**

```
3 2
0 10
5 7
6 9
```

**Output:**

```
2
```

**Explanation:**

Exams:

- Exam 1: [0, 10]
- Exam 2: [5, 7]
- Exam 3: [6, 9]

Each proctor can handle up to r = 2 exams simultaneously.

Timeline analysis:

- At time 5: Exams 1 and 2 are active (2 exams)
- At time 6: Exams 1, 2, and 3 are active (3 exams)
- Maximum overlap: 3 exams

Proctors needed: ceil(3 / 2) = ceil(1.5) = 2

![Example Visualization](../images/GRD-008/example-1.png)

## Notes

- Use sweep line algorithm to track overlapping intervals
- Track maximum number of simultaneously active exams
- Answer = ceil(max_overlap / r)
- Create events for exam start (+1) and exam end (-1)
- Sort events by time and process in order
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Sweep Line, Interval Scheduling, Resource Allocation

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minProctors(int n, long r, int[][] exams) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nrLine = br.readLine();
        if (nrLine == null) return;
        String[] nr = nrLine.trim().split("\\s+");
        int n = Integer.parseInt(nr[0]);
        long r = Long.parseLong(nr[1]);

        int[][] exams = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] examLine = br.readLine().trim().split("\\s+");
            exams[i][0] = Integer.parseInt(examLine[0]);
            exams[i][1] = Integer.parseInt(examLine[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minProctors(n, r, exams));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_proctors(self, n, r, exams):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    r = int(input_data[1])
    idx = 2
    exams = []
    for _ in range(n):
        exams.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.min_proctors(n, r, exams))

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
    long long minProctors(int n, long long r, vector<vector<int>>& exams) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long r;
    if (!(cin >> n >> r)) return 0;

    vector<vector<int>> exams(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> exams[i][0] >> exams[i][1];
    }

    Solution sol;
    cout << sol.minProctors(n, r, exams) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minProctors(n, r, exams) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const r = BigInt(input[idx++]);
  const exams = [];
  for (let i = 0; i < n; i++) {
    exams.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.minProctors(n, r, exams).toString());
}

solve();
```
