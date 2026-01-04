---
problem_id: DP_REQ_WEIGHT_KNAP__6427
display_id: DP-003
slug: required-weight-knapsack
title: "Required Weight Knapsack"
difficulty: Medium
difficulty_score: 54
topics:
  - Dynamic Programming
  - Knapsack
  - Optimization
tags:
  - dp
  - knapsack
  - 0-1-knapsack
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-003: Required Weight Knapsack

## Problem Statement

You are given `n` items. Item `i` has weight `w[i]` and value `v[i]`. You also have a knapsack with maximum capacity `W`.

Unlike classic knapsack, you must select items such that the **total weight is at least `R`** (required minimum weight) and **at most `W`**.

Your task is to maximize the total value under these constraints.

If it is impossible to reach total weight ≥ `R` without exceeding `W`, print `-1`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513326/dsa/dp/pi8avepmznqnbxzcmeou.jpg)

## Input Format

- First line: three integers `n`, `W`, `R`
- Next `n` lines: two integers `w[i]` and `v[i]`

## Output Format

Print a single integer:

- maximum achievable value with `R <= totalWeight <= W`, or
- `-1` if no valid selection exists

## Constraints

- `1 <= n <= 200`
- `1 <= W <= 5000`
- `0 <= R <= W`
- `1 <= w[i] <= W`
- `0 <= v[i] <= 10^9`

## Example

**Input:**

```
3 6 5
2 4
3 5
4 6
```

**Output:**

```
10
```

**Explanation:**

Valid selections must have total weight between 5 and 6:

- Pick items with weights `2 + 3 = 5` ⇒ value `4 + 5 = 9`
- Pick items with weights `2 + 4 = 6` ⇒ value `4 + 6 = 10` ✅ best

So the answer is `10`.

![Example Visualization](../images/DP-003/example-1.png)

## Notes

- This is a **0/1 knapsack**: each item can be taken at most once.
- The “required minimum weight” constraint is handled by taking the best value among weights `R..W`.
- Use 64-bit integers for value sums.

## Related Topics

Dynamic Programming, 0/1 Knapsack, Optimization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maximizeValue(int n, int W, int R, long[][] items) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int W = Integer.parseInt(parts[1]);
        int R = Integer.parseInt(parts[2]);

        long[][] items = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] itemParts = br.readLine().trim().split("\\s+");
            items[i][0] = Long.parseLong(itemParts[0]); // weight
            items[i][1] = Long.parseLong(itemParts[1]); // value
        }

        Solution sol = new Solution();
        System.out.println(sol.maximizeValue(n, W, R, items));
    }
}
```

### Python

```python
import sys

class Solution:
    def maximize_value(self, n, W, R, items):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n, W, R = map(int, input_data[:3])
    idx = 3
    items = []
    for _ in range(n):
        items.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.maximize_value(n, W, R, items))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maximizeValue(int n, int W, int R, const vector<pair<long long, long long>>& items) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, W, R;
    if (!(cin >> n >> W >> R)) return 0;

    vector<pair<long long, long long>> items(n);
    for (int i = 0; i < n; i++) {
        cin >> items[i].first >> items[i].second;
    }

    Solution sol;
    cout << sol.maximizeValue(n, W, R, items) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maximizeValue(n, W, R, items) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const W = parseInt(input[idx++]);
  const R = parseInt(input[idx++]);
  const items = [];
  for (let i = 0; i < n; i++) {
    items.push([BigInt(input[idx++]), BigInt(input[idx++])]);
  }

  const sol = new Solution();
  const res = sol.maximizeValue(n, W, R, items);
  console.log(res === null || res === undefined ? -1 : res.toString());
}

solve();
```
