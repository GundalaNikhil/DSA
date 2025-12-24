---
problem_id: DP_MAXSUM_GAP3__7706
display_id: DP-007
slug: auditorium-max-sum-gap-three
title: "Auditorium Max Sum With Gap Three"
difficulty: Medium
difficulty_score: 45
topics:
  - Dynamic Programming
  - Array
  - Optimization
tags:
  - dp
  - arrays
  - maximum-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-007: Auditorium Max Sum With Gap Three

## Problem Statement

You are given an integer array `a` of length `n`. You want to select a subset of indices to maximize the sum of selected values, with the constraint:

For any two selected indices `i` and `j` (`i != j`), `|i - j| >= 3`.

In other words, if you pick index `i`, you cannot pick `i-1`, `i-2`, `i+1`, or `i+2`.

Return the maximum possible sum.

![Problem Illustration](../images/DP-007/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `a[i]`

## Output Format

Print one integer: the maximum sum achievable under the gap constraint.

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**
```
5
4 1 2 9 3
```

**Output:**
```
13
```

**Explanation:**

One optimal selection is indices `0` and `3`:

- `a[0] + a[3] = 4 + 9 = 13`
- Distance between indices: `3` (allowed)

So the answer is `13`.

![Example Visualization](../images/DP-007/example-1.png)

## Notes

- You are allowed to pick **no elements**; in that case the sum is `0`. This matters when all numbers are negative.
- This is a “House Robber”-style DP with a skip of 2 indices between picks.
- Use 64-bit integer arithmetic for sums.

## Related Topics

Dynamic Programming, Array DP, Maximum Sum

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxSumGapThree(long[] a) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextLong();
        System.out.println(new Solution().maxSumGapThree(a));
        sc.close();
    }
}
```

### Python

```python
def max_sum_gap_three(a: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input().strip())
    a = list(map(int, input().split()))
    print(max_sum_gap_three(a))

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
    long long maxSumGapThree(const vector<long long>& a) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution sol;
    cout << sol.maxSumGapThree(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxSumGapThree(a) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  const n = Number(lines[0]);
  const a = lines[1].split(" ").map(Number);
  const sol = new Solution();
  console.log(sol.maxSumGapThree(a));
});
```

