---
problem_id: DP_EXAMS_COOLDOWN_GAP__7731
display_id: DP-016
slug: exams-with-cooldown-gap
title: "Exams With Cooldown Gap"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Scheduling
  - Binary Search
tags:
  - dp
  - intervals
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-016: Exams With Cooldown Gap

## Problem Statement

You are given `n` exams, each with start time `start[i]`, end time `end[i]`, and score `score[i]`. If you take two exams `A` then `B`, you must leave at least `g` units of time between them: `start[B] >= end[A] + g`.

Select a subset of exams maximizing total score while respecting the cooldown gap.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513335/dsa/dp/x206bmrngmovr8lpjaem.jpg)

## Input Format

- First line: two integers `n` and `g`
- Next `n` lines: three integers `start`, `end`, `score` for each exam

## Output Format

- Single integer: maximum achievable total score.

## Constraints

- `1 <= n <= 100000`
- `0 <= g <= 10^9`
- `0 <= start[i] < end[i] <= 10^9`
- `0 <= score[i] <= 10^9`
- Use 64-bit integers for all sums.

## Example

**Input:**

```
3 1
1 3 5
4 6 6
6 10 5
```

**Output:**

```
11
```

**Explanation:**

Take exams 1 and 2 (score 5 + 6 = 11). Exam 3 starts at 6, but with `g = 1` you need `start >= 7` after exam 2, so you cannot add it.

![Example Visualization](../images/DP-016/example-1.png)

## Notes

- If `g = 0`, this reduces to classic weighted interval scheduling.
- Sorting by end time and binary searching the latest compatible exam yields an efficient solution.
- Overlapping exams are allowed in input; you choose a non-conflicting subset.

## Related Topics

Dynamic Programming, Binary Search, Scheduling

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Exam {
    long start, end, score;
    Exam(long s, long e, long sc) {
        this.start = s;
        this.end = e;
        this.score = sc;
    }
}

class Solution {
    public long maxScore(int n, long g, List<Exam> exams) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ngLine = br.readLine();
        if (ngLine == null) return;
        String[] ngParts = ngLine.trim().split("\\s+");
        int n = Integer.parseInt(ngParts[0]);
        long g = Long.parseLong(ngParts[1]);

        List<Exam> exams = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            if (line == null) break;
            String[] eParts = line.trim().split("\\s+");
            exams.add(new Exam(Long.parseLong(eParts[0]), Long.parseLong(eParts[1]), Long.parseLong(eParts[2])));
        }

        Solution sol = new Solution();
        System.out.println(sol.maxScore(n, g, exams));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_score(self, n, g, exams):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    g = int(input_data[1])
    idx = 2
    exams = []
    for _ in range(n):
        exams.append([int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])])
        idx += 3

    sol = Solution()
    print(sol.max_score(n, g, exams))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Exam {
    long long start, end, score;
};

class Solution {
public:
    long long maxScore(int n, long long g, vector<Exam>& exams) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long g;
    if (!(cin >> n >> g)) return 0;

    vector<Exam> exams(n);
    for (int i = 0; i < n; i++) {
        cin >> exams[i].start >> exams[i].end >> exams[i].score;
    }

    Solution sol;
    cout << sol.maxScore(n, g, exams) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxScore(n, g, exams) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const g = BigInt(input[idx++]);
  const exams = [];
  for (let i = 0; i < n; i++) {
    exams.push({
      start: BigInt(input[idx++]),
      end: BigInt(input[idx++]),
      score: BigInt(input[idx++]),
    });
  }

  const sol = new Solution();
  const res = sol.maxScore(n, g, exams);
  console.log(res === null || res === undefined ? 0 : res.toString());
}

solve();
```
