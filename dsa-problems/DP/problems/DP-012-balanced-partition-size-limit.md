---
problem_id: DP_BAL_PART_SIZE__5120
display_id: DP-012
slug: balanced-partition-size-limit
title: "Balanced Partition With Size Limit"
difficulty: Medium
difficulty_score: 56
topics:
  - Dynamic Programming
  - Subset Sum
  - Optimization
tags:
  - dp
  - subset-sum
  - partition
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-012: Balanced Partition With Size Limit

## Problem Statement

You are given an array `a` of length `n` and an integer `D`. Partition the array into two groups (each element goes to exactly one group) such that:

- The absolute difference of the two group sums is at most `D`.
- Among all such valid partitions, minimize the size of the **larger** group.

Return the minimum possible larger-group size. If no valid partition exists, return `-1`.

![Problem Illustration](../images/DP-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `D`
- Second line: `n` integers `a[i]`

## Output Format

Print one integer: the minimum larger-group size, or `-1` if impossible.

## Constraints

- `1 <= n <= 50`
- `-500 <= a[i] <= 500`
- `0 <= D <= 5000`

## Example

**Input:**
```
4 1
3 1 4 2
```

**Output:**
```
2
```

**Explanation:**

Partition into `{3,2}` and `{1,4}`:

- sums: 5 and 5, difference = 0 ≤ 1
- group sizes: 2 and 2, larger size = 2 (minimum possible)

![Example Visualization](../images/DP-012/example-1.png)

## Notes

- Groups can be empty, but that may be suboptimal. Check constraints carefully.
- Negative values are allowed; sums can be negative.
- We minimize the larger group size, **not** the difference (difference is constrained).

## Related Topics

Dynamic Programming, Subset Sum, Partitioning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minLargerGroupSize(int[] a, int D) {
        // Your implementation here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int D = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        System.out.println(new Solution().minLargerGroupSize(a, D));
        sc.close();
    }
}
```

### Python

```python
def min_larger_group_size(a: list[int], D: int) -> int:
    # Your implementation here
    return -1

def main():
    n, D = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_larger_group_size(a, D))

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
    int minLargerGroupSize(const vector<int>& a, int D) {
        // Your implementation here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, D;
    cin >> n >> D;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution sol;
    cout << sol.minLargerGroupSize(a, D) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minLargerGroupSize(a, D) {
    // Your implementation here
    return -1;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  const [nStr, DStr] = lines[0].split(" ");
  const n = Number(nStr), D = Number(DStr);
  const a = lines[1].split(" ").map(Number);
  const sol = new Solution();
  console.log(sol.minLargerGroupSize(a, D));
});
```

