---
problem_id: SRT_COUNT_WITHIN_THRESHOLD_AFTER_SELF__7028
display_id: SRT-012
slug: count-within-threshold-after-self
title: "Count Within Threshold After Self"
difficulty: Medium
difficulty_score: 56
topics:
  - Sorting
  - Divide and Conquer
  - Counting
tags:
  - merge-sort
  - counting
  - arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-012: Count Within Threshold After Self

## Problem Statement

For each element `a[i]`, count how many elements to its right satisfy `a[i] - a[j] <= T`.

Return the counts in order.

![Problem Illustration](../images/SRT-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `T`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers, the counts for each index

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `0 <= T <= 10^9`

## Example

**Input:**

```
3 1
4 1 3
```

**Output:**

```
1 1 0
```

**Explanation:**

For 4, elements to the right within threshold are {3}. For 1, elements to the right are {3} because 1 - 3 = -2 <= 1.

![Example Visualization](../images/SRT-012/example-1.png)

## Notes

- Condition `a[i] - a[j] <= T` is equivalent to `a[j] >= a[i] - T`
- Use a modified merge sort to count efficiently
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Merge Sort, Counting, Divide and Conquer

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] countWithinThreshold(int n, int t, int[] a) {
        // Implement here
        return new int[n];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int t = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            Solution sol = new Solution();
            int[] result = sol.countWithinThreshold(n, t, a);
            for (int i = 0; i < n; i++) {
                System.out.print(result[i] + (i == n - 1 ? "" : " "));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_within_threshold(self, n: int, t: int, a: list) -> list:
        # Implement here
        return [0] * n

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    t = int(input_data[1])
    a = [int(x) for x in input_data[2:]]

    sol = Solution()
    result = sol.count_within_threshold(n, t, a)
    print(*(result))

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
    vector<int> countWithinThreshold(int n, int t, vector<int>& a) {
        // Implement here
        return vector<int>(n, 0);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, t;
    if (cin >> n >> t) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution sol;
        vector<int> result = sol.countWithinThreshold(n, t, a);
        for (int i = 0; i < n; i++) {
            cout << result[i] << (i == n - 1 ? "" : " ");
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countWithinThreshold(n, t, a) {
    // Implement here
    return new Array(n).fill(0);
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
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const t = parseInt(input[1]);
  const a = input.slice(2).map(Number);

  const sol = new Solution();
  const result = sol.countWithinThreshold(n, t, a);
  console.log(result.join(" "));
});
```
