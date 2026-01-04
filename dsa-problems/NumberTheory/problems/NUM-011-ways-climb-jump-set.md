---
problem_id: NUM_WAYS_CLIMB_JUMP_SET__7681
display_id: NUM-011
slug: ways-climb-jump-set
title: "Ways to Climb With Jumps Set"
difficulty: Medium
difficulty_score: 48
topics:
  - Number Theory
  - Dynamic Programming
  - Combinatorics
tags:
  - number-theory
  - dp
  - combinatorics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-011: Ways to Climb With Jumps Set

## Problem Statement

You are climbing `n` stairs. You may take jumps only from a given set `J`. Count the number of distinct ways to reach exactly stair `n`, modulo `1000000007`.

![Problem Illustration](../images/NUM-011/problem-illustration.png)

## Input Format

- First line: integers `n` and `m` (size of set J)
- Second line: `m` integers (the jump sizes)

## Output Format

- Single integer: number of ways modulo `1000000007`

## Constraints

- `1 <= n <= 100000`
- `1 <= m <= 20`
- `1 <= J[i] <= 100000`

## Example

**Input:**

```
4 2
1 3
```

**Output:**

```
3
```

**Explanation:**

Ways: 1+1+1+1, 1+3, 3+1.

![Example Visualization](../images/NUM-011/example-1.png)

## Notes

- DP: dp[i] = sum(dp[i-j]) for j in J and i >= j
- Base: dp[0] = 1
- Time complexity: O(n \* m)
- Space complexity: O(n)

## Related Topics

Dynamic Programming, Modular Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countWays(int n, int m, int[] j) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] j = new int[m];
        for (int i = 0; i < m; i++) j[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countWays(n, m, j));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_ways(self, n, m, j):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    j = [int(x) for x in input_data[2:2+m]]
    sol = Solution()
    print(sol.count_ways(n, m, j))

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
    int countWays(int n, int m, const vector<int>& j) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<int> j(m);
    for (int i = 0; i < m; i++) cin >> j[i];
    Solution sol;
    cout << sol.countWays(n, m, j) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countWays(n, m, j) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const m = parseInt(input[1]);
  const j = [];
  for (let i = 0; i < m; i++) j.push(parseInt(input[2 + i]));
  const sol = new Solution();
  console.log(sol.countWays(n, m, j).toString());
}

solve();
```
