---
problem_id: SRT_MIN_INVERSIONS_ONE_SWAP__7419
display_id: SRT-004
slug: min-inversions-one-swap
title: "Minimum Inversions After One Swap"
difficulty: Medium
difficulty_score: 54
topics:
  - Sorting
  - Fenwick Tree
  - Inversions
tags:
  - inversions
  - fenwick
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-004: Minimum Inversions After One Swap

## Problem Statement

Given an array `a`, you may perform at most one swap of two elements. Compute the minimum possible inversion count after the swap.

An inversion is a pair `(i, j)` with `i < j` and `a[i] > a[j]`.

![Problem Illustration](../images/SRT-004/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single integer: minimum inversion count after at most one swap

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
3
2 1 3
```

**Output:**

```
0
```

**Explanation:**

Swap 2 and 1 to obtain `[1,2,3]` with zero inversions.

![Example Visualization](../images/SRT-004/example-1.png)

## Notes

- The answer is at most the original inversion count
- Try candidate swaps that fix out-of-order pairs
- Use BIT to compute inversion contributions efficiently
- Output fits in 64-bit signed integer

## Related Topics

Inversion Count, Fenwick Tree, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minInversionsAfterOneSwap(int n, long[] a) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextLong();

            Solution sol = new Solution();
            System.out.println(sol.minInversionsAfterOneSwap(n, a));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def min_inversions_after_one_swap(self, n: int, a: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:]]

    sol = Solution()
    print(sol.min_inversions_after_one_swap(n, a))

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
    long long minInversionsAfterOneSwap(int n, vector<long long>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution sol;
        cout << sol.minInversionsAfterOneSwap(n, a) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minInversionsAfterOneSwap(n, a) {
    // Implement here
    return 0n;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const a = input.slice(1).map(BigInt);

  const sol = new Solution();
  console.log(sol.minInversionsAfterOneSwap(n, a).toString());
});
```
