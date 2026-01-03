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
    public long minInversionsAfterSwap(int[] arr) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.minInversionsAfterSwap(arr));
        sc.close();
    }
}
```

### Python

```python
def min_inversions_after_swap(arr: list[int]) -> int:
    # //Implement here
    return 0

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = min_inversions_after_swap(arr)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    long long minInversionsAfterSwap(const vector<int>& arr) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.minInversionsAfterSwap(arr) << "\n";
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  minInversionsAfterSwap(arr) {
    //Implement here
    return 0;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
console.log(solution.minInversionsAfterSwap(arr).toString());
```

