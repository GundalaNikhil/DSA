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

![Problem Illustration](../images/DP-003/problem-illustration.png)

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

class Solution {
    public long maxValueWithRequiredWeight(int n, int W, int R, int[] w, long[] v) {
        // Your implementation here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int W = sc.nextInt();
        int R = sc.nextInt();
        int[] w = new int[n];
        long[] v = new long[n];
        for (int i = 0; i < n; i++) {
            w[i] = sc.nextInt();
            v[i] = sc.nextLong();
        }
        System.out.println(new Solution().maxValueWithRequiredWeight(n, W, R, w, v));
        sc.close();
    }
}
```

### Python

```python
def max_value_required_weight(n: int, W: int, R: int, items: list[tuple[int, int]]) -> int:
    # Your implementation here
    return -1

def main():
    n, W, R = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    print(max_value_required_weight(n, W, R, items))

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
    long long maxValueWithRequiredWeight(int n, int W, int R,
                                         const vector<int>& w,
                                         const vector<long long>& v) {
        // Your implementation here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W, R;
    cin >> n >> W >> R;
    vector<int> w(n);
    vector<long long> v(n);
    for (int i = 0; i < n; i++) cin >> w[i] >> v[i];

    Solution sol;
    cout << sol.maxValueWithRequiredWeight(n, W, R, w, v) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxValueWithRequiredWeight(n, W, R, w, v) {
    // Your implementation here
    return -1;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [nStr, WStr, RStr] = lines[idx++].split(" ");
  const n = Number(nStr), W = Number(WStr), R = Number(RStr);
  const w = new Array(n);
  const v = new Array(n);
  for (let i = 0; i < n; i++) {
    const [wi, vi] = lines[idx++].split(" ").map(Number);
    w[i] = wi; v[i] = vi;
  }
  const sol = new Solution();
  console.log(sol.maxValueWithRequiredWeight(n, W, R, w, v));
});
```

