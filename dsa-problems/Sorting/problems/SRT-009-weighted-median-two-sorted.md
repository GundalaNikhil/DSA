---
problem_id: SRT_WEIGHTED_MEDIAN_TWO_SORTED__3086
display_id: SRT-009
slug: weighted-median-two-sorted
title: "Weighted Median of Two Sorted Arrays"
difficulty: Medium
difficulty_score: 60
topics:
  - Sorting
  - Binary Search
  - Median
tags:
  - median
  - binary-search
  - sorted-arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-009: Weighted Median of Two Sorted Arrays

## Problem Statement

You are given two sorted arrays `A` and `B` along with positive weights `wA` and `wB`. Treat each element of `A` as appearing `wA` times and each element of `B` as appearing `wB` times.

Return the median of the combined multiset without expanding it.

If the total count is even, return the average of the two middle values as a decimal (e.g., `2.5`).

![Problem Illustration](../images/SRT-009/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Second line: `n` space-separated integers (array `A`)
- Third line: `m` space-separated integers (array `B`)
- Fourth line: integers `wA` and `wB`

## Output Format

- Single number: the weighted median

## Constraints

- `1 <= n, m <= 100000`
- `1 <= wA, wB <= 10^6`
- Arrays are sorted in nondecreasing order

## Example

**Input:**

```
2 2
1 3
2 7
1 2
```

**Output:**

```
2.5
```

**Explanation:**

Expanded multiset is `[1, 3, 2, 2, 7, 7]` -> sorted `[1,2,2,3,7,7]`. Median is average of 3rd and 4th: `(2+3)/2`.

![Example Visualization](../images/SRT-009/example-1.png)

## Notes

- Use binary search on value space or k-th order logic
- Total count is `n*wA + m*wB`
- Keep all arithmetic in 64-bit integers
- Output with `.5` when needed

## Related Topics

Median, Binary Search, Sorted Arrays

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public String weightedMedian(int[] A, int[] B, long wA, long wB) {
        // Your implementation here
        return "0";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] A = new int[n];
        int[] B = new int[m];
        for (int i = 0; i < n; i++) A[i] = sc.nextInt();
        for (int i = 0; i < m; i++) B[i] = sc.nextInt();
        long wA = sc.nextLong();
        long wB = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.weightedMedian(A, B, wA, wB));
        sc.close();
    }
}
```

### Python

```python
def weighted_median(A: list[int], B: list[int], wA: int, wB: int) -> str:
    # Your implementation here
    return "0"

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    A = [int(next(it)) for _ in range(n)]
    B = [int(next(it)) for _ in range(m)]
    wA = int(next(it))
    wB = int(next(it))

    print(weighted_median(A, B, wA, wB))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string weightedMedian(const vector<int>& A, const vector<int>& B, long long wA, long long wB) {
        // Your implementation here
        return "0";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<int> A(n), B(m);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < m; i++) cin >> B[i];
    long long wA, wB;
    cin >> wA >> wB;

    Solution solution;
    cout << solution.weightedMedian(A, B, wA, wB) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  weightedMedian(A, B, wA, wB) {
    // Your implementation here
    return "0";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const A = [];
  const B = [];
  for (let i = 0; i < n; i++) A.push(parseInt(data[idx++], 10));
  for (let i = 0; i < m; i++) B.push(parseInt(data[idx++], 10));
  const wA = parseInt(data[idx++], 10);
  const wB = parseInt(data[idx++], 10);

  const solution = new Solution();
  const result = solution.weightedMedian(A, B, wA, wB);
  console.log(result.toString());
});
```
