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
    public long maxScore(List<Exam> exams, long g) {
        // Implementation here
        return 0;
    }
}

class Main {
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

def max_score(exams: List[Tuple[int, int, int]], g: int) -> int:
    # Implementation here
    return 0

def main():
    n, g = map(int, input().split())
    exams = []
    for _ in range(n):
        s, e, w = map(int, input().split())
        exams.append((s, e, w))
    print(max_score(exams, g))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>

using namespace std;

class Solution {
public:
    long long maxScore(vector<Exam>& exams, long long g) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; long long g;
    if (!(cin >> n >> g)) return 0;
    vector<Exam> exams(n);
    for (int i = 0; i < n; ++i) cin >> exams[i].s >> exams[i].e >> exams[i].w;
    cout << maxScore(exams, g) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxScore(exams, g) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  let ptr = 0;
  const parts = data[ptr++].split(/\s+/).map(Number);
  const n = parts[0];
  const g = parts[1];
  const exams = [];
  for (let i = 0; i < n; i++) {
    const exam = data[ptr++].split(/\s+/).map(Number);
    exams.push(exam);
  }

  console.log(new Solution().maxScore(exams, g));
});
```
