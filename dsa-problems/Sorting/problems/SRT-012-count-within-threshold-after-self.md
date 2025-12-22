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
    public long[] countWithinThreshold(int[] arr, long T) {
        // Your implementation here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long T = sc.nextLong();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        long[] result = solution.countWithinThreshold(arr, T);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def count_within_threshold(arr: list[int], T: int) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    T = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    result = count_within_threshold(arr, T)
    sys.stdout.write(" ".join(str(x) for x in result))

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
    vector<long long> countWithinThreshold(const vector<int>& arr, long long T) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long T;
    if (!(cin >> n >> T)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    vector<long long> result = solution.countWithinThreshold(arr, T);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countWithinThreshold(arr, T) {
    // Your implementation here
    return [];
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
  const T = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.countWithinThreshold(arr, T);
  console.log(result.join(" "));
});
```
