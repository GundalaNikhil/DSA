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

![Problem Illustration](../images/DP-016/problem-illustration.png)

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

class Solution {
    static class Exam {
        long s, e, w;
        Exam(long s, long e, long w) { this.s = s; this.e = e; this.w = w; }
    }

    public long maxScore(List<Exam> exams, long g) {
        exams.sort(Comparator.comparingLong(x -> x.e));
        int n = exams.size();
        long[] ends = new long[n];
        for (int i = 0; i < n; i++) ends[i] = exams.get(i).e;
        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            Exam ex = exams.get(i - 1);
            long target = ex.s - g;
            int j = upperBound(ends, target);
            dp[i] = Math.max(dp[i - 1], dp[j] + ex.w);
        }
        return dp[n];
    }

    private int upperBound(long[] arr, long x) {
        int l = 0, r = arr.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (arr[m] <= x) l = m + 1;
            else r = m;
        }
        return l;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long g = sc.nextLong();
        List<Solution.Exam> exams = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            long s = sc.nextLong(), e = sc.nextLong(), w = sc.nextLong();
            exams.add(new Solution.Exam(s, e, w));
        }
        Solution sol = new Solution();
        System.out.println(sol.maxScore(exams, g));
        sc.close();
    }
}
```

### Python

```python
from bisect import bisect_right
from typing import List, Tuple
import sys

def max_score(exams: List[Tuple[int, int, int]], g: int) -> int:
    exams = sorted(exams, key=lambda x: x[1])  # sort by end
    ends = [e for _, e, _ in exams]
    n = len(exams)
    dp = [0] * (n + 1)
    for i, (s, e, w) in enumerate(exams, start=1):
        j = bisect_right(ends, s - g)
        dp[i] = max(dp[i - 1], dp[j] + w)
    return dp[n]

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); g = int(next(it))
    exams = []
    for _ in range(n):
        s = int(next(it)); e = int(next(it)); w = int(next(it))
        exams.append((s, e, w))
    print(max_score(exams, g))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Exam { long long s, e, w; };

long long maxScore(vector<Exam>& exams, long long g) {
    sort(exams.begin(), exams.end(), [](const Exam& a, const Exam& b){ return a.e < b.e; });
    int n = exams.size();
    vector<long long> ends(n);
    for (int i = 0; i < n; ++i) ends[i] = exams[i].e;
    vector<long long> dp(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        const auto& ex = exams[i - 1];
        long long target = ex.s - g;
        int j = upper_bound(ends.begin(), ends.end(), target) - ends.begin();
        dp[i] = max(dp[i - 1], dp[j] + ex.w);
    }
    return dp[n];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; long long g;
    if (!(cin >> n >> g)) return 0;
    vector<Exam> exams(n);
    for (int i = 0; i < n; ++i) cin >> exams[i].s >> exams[i].e >> exams[i].w;
    cout << maxScore(exams, g) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function maxScore(exams, g) {
  exams.sort((a, b) => a[1] - b[1]);
  const ends = exams.map(e => e[1]);
  const n = exams.length;
  const dp = Array(n + 1).fill(0n);
  for (let i = 1; i <= n; i++) {
    const [s, e, w] = exams[i - 1];
    const target = s - g;
    let l = 0, r = ends.length;
    while (l < r) {
      const m = (l + r) >> 1;
      if (ends[m] <= target) l = m + 1; else r = m;
    }
    const j = l;
    const take = dp[j] + BigInt(w);
    const skip = dp[i - 1];
    dp[i] = take > skip ? take : skip;
  }
  return Number(dp[n]);
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const n = data[idx++], g = data[idx++];
  const exams = [];
  for (let i = 0; i < n; i++) {
    const s = data[idx++], e = data[idx++], w = data[idx++];
    exams.push([s, e, w]);
  }
  console.log(maxScore(exams, g));
}

main();
```
