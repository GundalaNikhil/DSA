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
    public String weightedMedian(int n, int m, int[] A, int[] B, long wA, long wB) {
        // Implement here
        return "0.0";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] A = new int[n];
            for (int i = 0; i < n; i++) A[i] = sc.nextInt();
            int[] B = new int[m];
            for (int i = 0; i < m; i++) B[i] = sc.nextInt();
            long wA = sc.nextLong();
            long wB = sc.nextLong();

            Solution sol = new Solution();
            System.out.println(sol.weightedMedian(n, m, A, B, wA, wB));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def weighted_median(self, n, m, A, B, wA, wB) -> str:
        # Implement here
        return "0.0"

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    A = [int(x) for x in input_data[2:2+n]]
    B = [int(x) for x in input_data[2+n : 2+n+m]]
    wA = int(input_data[2+n+m])
    wB = int(input_data[3+n+m])

    sol = Solution()
    print(sol.weighted_median(n, m, A, B, wA, wB))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

class Solution {
public:
    string weightedMedian(int n, int m, const vector<int>& A, const vector<int>& B, long long wA, long long wB) {
        // Implement here
        return "0.0";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (cin >> n >> m) {
        vector<int> A(n), B(m);
        for (int i = 0; i < n; i++) cin >> A[i];
        for (int i = 0; i < m; i++) cin >> B[i];
        long long wA, wB;
        cin >> wA >> wB;

        Solution sol;
        cout << sol.weightedMedian(n, m, A, B, wA, wB) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  weightedMedian(n, m, A, B, wA, wB) {
    // Implement here
    return "0.0";
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
  if (input.length < 4) return;
  const n = parseInt(input[0]);
  const m = parseInt(input[1]);
  const A = input.slice(2, 2 + n).map(Number);
  const B = input.slice(2 + n, 2 + n + m).map(Number);
  const wA = BigInt(input[2 + n + m]);
  const wB = BigInt(input[3 + n + m]);

  const sol = new Solution();
  console.log(sol.weightedMedian(n, m, A, B, wA, wB));
});
```
