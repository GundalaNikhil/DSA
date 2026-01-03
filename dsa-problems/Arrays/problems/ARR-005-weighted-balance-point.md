---
problem_id: ARR_WEIGHTED_BALANCE_POINT__7742
display_id: ARR-005
slug: weighted-balance-point
title: "Weighted Balance Point"
difficulty: Medium
difficulty_score: 44
topics:
  - Arrays
  - Prefix Sum
  - Math
tags:
  - arrays
  - prefix-sum
  - math
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-005: Weighted Balance Point

## Problem Statement

Find the smallest index i such that the weighted sum of elements to the left of i equals the weighted sum of elements to the right of i. The left side excludes i and is multiplied by L, the right side excludes i and is multiplied by R.

![Problem Illustration](../images/ARR-005/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: two integers L and R

## Output Format

Print the smallest index i (0-based) that satisfies the condition, or -1.

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= a[i] <= 1000000000`
- `1 <= L, R <= 1000000`

## Example

**Input:**
```
5
2 3 -1 3 2
2 1
```

**Output:**
```
2
```

**Explanation:**

At i = 2, left sum is 5 and right sum is 8. 5 * 2 == 8 * 1, so the answer is 2.

![Example Visualization](../images/ARR-005/example-1.png)

## Notes

- Use 64-bit integers to avoid overflow.
- Left and right sums exclude index i.

## Related Topics

Arrays, Prefix Sum, Math

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int weightedBalancePoint(int[] a, int L, int R) {
        //Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;

        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        int L = sc.nextInt();
        int R = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.weightedBalancePoint(a, L, R));
        sc.close();
    }
}
```

### Python

```python
import sys

def weighted_balance_point(a: list[int], L: int, R: int) -> int:
    # //Implement here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    L, R = map(int, input().split())

    result = weighted_balance_point(a, L, R)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int weightedBalancePoint(vector<int>& a, int L, int R) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int L, R;
    cin >> L >> R;

    Solution solution;
    cout << solution.weightedBalancePoint(a, L, R) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  weightedBalancePoint(a, L, R) {
    //Implement here
    return 0;
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
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const a = [];
  for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));

  const L = Number(tokens[ptr++]);
  const R = Number(tokens[ptr++]);

  const solution = new Solution();
  console.log(solution.weightedBalancePoint(a, L, R));
});
```

