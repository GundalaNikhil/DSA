---
problem_id: ARR_WEIGHTED_BAL__7746
display_id: ARR-005
slug: weighted-balance-point
title: "Weighted Balance Point"
difficulty: Medium
difficulty_score: 55
topics:
  - Array
  - Prefix Sum
  - Balance Point
  - Mathematical
tags:
  - arrays
  - prefix-sum
  - equilibrium
  - medium
premium: true
subscription_tier: pro
time_limit: 2000
memory_limit: 256
---

# Weighted Balance Point

## Problem Statement

Find the smallest index `i` where `sum(left) * L == sum(right) * R` for given weights `L` and `R`; left excludes `i`, right excludes `i`. If none exists, return -1.

![Problem Illustration](../images/ARR-005/problem-illustration.png)

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5) - size of array
- Second line: `n` space-separated integers representing the array
- Third line: Two integers `L` and `R` (1 ≤ L, R ≤ 10^6) - the weights

## Output Format

Print the smallest index satisfying the weighted balance condition, or -1 if none exists.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- -10^9 ≤ a[i] ≤ 10^9
- 1 ≤ L, R ≤ 10^6
- Integer overflow possible, use long

## Examples

### Example 1

**Input:**

```
5
2 3 -1 3 2
2 1
```

**Output:**

```
1
```

**Explanation:**

At each index i, we check if `sum(elements before i) × L == sum(elements after i) × R`:

- **Index 0**: left=[] (sum=0), right=[3,-1,3,2] (sum=7)
  - Check: 0×2 == 7×1? → 0 == 7? **No** ✗
- **Index 1**: left=[2] (sum=2), right=[-1,3,2] (sum=4)
  - Check: 2×2 == 4×1? → 4 == 4? **Yes!** ✓
- **Index 2**: left=[2,3] (sum=5), right=[3,2] (sum=5)
  - Check: 5×2 == 5×1? → 10 == 5? **No** ✗
- **Index 3**: left=[2,3,-1] (sum=4), right=[2] (sum=2)
  - Check: 4×2 == 2×1? → 8 == 2? **No** ✗
- **Index 4**: left=[2,3,-1,3] (sum=7), right=[] (sum=0)
  - Check: 7×2 == 0×1? → 14 == 0? **No** ✗

The first (smallest) index satisfying the condition is **index 1**.

![Example 1 Visualization](../images/ARR-005/example-1.png)

### Example 2

**Input:**

```
4
1 2 3 4
1 1
```

**Output:**

```
-1
```

**Explanation:**

- No index satisfies the weighted balance condition when L=R=1 (standard equilibrium)

## Notes

- Precompute total sum; iterate maintaining left sum
- Use long data type to avoid overflow during multiplication

## Related Topics

Array, Prefix Sum, Balance Point, Mathematical

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int findWeightedBalancePoint(int[] arr, int L, int R) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int L = sc.nextInt();
        int R = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.findWeightedBalancePoint(arr, L, R);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def find_weighted_balance_point(arr: List[int], L: int, R: int) -> int:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    L, R = map(int, input().split())
    result = find_weighted_balance_point(arr, L, R)
    print(result)

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
    int findWeightedBalancePoint(vector<int>& arr, int L, int R) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int L, R;
    cin >> L >> R;

    Solution solution;
    int result = solution.findWeightedBalancePoint(arr, L, R);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findWeightedBalancePoint(arr, L, R) {
    // Your implementation here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
  if (lines.length === 3) {
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);
    const [L, R] = lines[2].split(" ").map(Number);

    const solution = new Solution();
    const result = solution.findWeightedBalancePoint(arr, L, R);

    console.log(result);
    rl.close();
  }
});
```
