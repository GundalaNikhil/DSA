---
problem_id: REC_EXAM_SEATING_BACKTRACK__6392
display_id: REC-004
slug: exam-seating-backtrack
title: "Exam Seating Backtrack"
difficulty: Medium
difficulty_score: 44
topics:
  - Recursion
  - Backtracking
  - Combinatorics
tags:
  - recursion
  - backtracking
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-004: Exam Seating Backtrack

## Problem Statement

An exam hall has `n` seats in a single row, indexed `0` to `n-1`. You must place exactly `k` students so that any two students have at least `d` empty seats between them.

Count how many valid arrangements are possible.

![Problem Illustration](../images/REC-004/problem-illustration.png)

## Input Format

- First line: three integers `n`, `k`, and `d`

## Output Format

- Single integer: number of valid arrangements

## Constraints

- `1 <= n <= 15`
- `0 <= k <= n`
- `0 <= d <= n`

## Example

**Input:**

```
5 2 2
```

**Output:**

```
3
```

**Explanation:**

With at least 2 empty seats between students, valid pairs are (0,3), (0,4), (1,4).

![Example Visualization](../images/REC-004/example-1.png)

## Notes

- If positions are `i < j`, then `j - i - 1 >= d`
- Use recursion to choose the next valid seat index
- Prune when remaining seats are insufficient
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinatorics, Recursion

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countArrangements(int n, int k, int d) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int d = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countArrangements(n, k, d));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_arrangements(self, n, k, d):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    d = int(input_data[2])
    sol = Solution()
    print(sol.count_arrangements(n, k, d))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    long long countArrangements(int n, int k, int d) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k, d;
    if (!(cin >> n >> k >> d)) return 0;
    Solution sol;
    cout << sol.countArrangements(n, k, d) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countArrangements(n, k, d) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const d = parseInt(input[2]);
  const sol = new Solution();
  console.log(sol.countArrangements(n, k, d).toString());
}

solve();
```
