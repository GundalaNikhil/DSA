---
problem_id: HEP_SLIDING_WINDOW_KTH_SMALLEST__2665
display_id: HEP-007
slug: sliding-window-kth-smallest
title: "Sliding Window Kth Smallest"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Sliding Window
  - Order Statistics
tags:
  - heaps
  - sliding-window
  - order-statistics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-007: Sliding Window Kth Smallest

## Problem Statement

Given an array `arr` of length `n`, a window size `w`, and an integer `k`, output the `k`-th smallest element in every contiguous window of size `w`.

![Problem Illustration](../images/HEP-007/problem-illustration.png)

## Input Format

- First line: integers `n`, `w`, and `k`
- Second line: `n` space-separated integers

## Output Format

- `n - w + 1` integers: the `k`-th smallest value for each window

## Constraints

- `1 <= n <= 200000`
- `1 <= w <= n`
- `1 <= k <= w`
- `-10^9 <= arr[i] <= 10^9`

## Example

**Input:**

```
5 3 2
1 3 2 6 4
```

**Output:**

```
2 3 4
```

**Explanation:**

Windows:

- [1, 3, 2] -> sorted [1, 2, 3], 2nd smallest = 2
- [3, 2, 6] -> sorted [2, 3, 6], 2nd smallest = 3
- [2, 6, 4] -> sorted [2, 4, 6], 2nd smallest = 4

![Example Visualization](../images/HEP-007/example-1.png)

## Notes

- Use two heaps to maintain lower and upper partitions
- Apply lazy deletion when elements leave the window
- Each window update runs in O(log w)
- Space complexity: O(w)

## Related Topics

Heaps, Sliding Window, Order Statistics, Median Maintenance

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> kthSmallestInWindows(int[] arr, int w, int k) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int w = sc.nextInt();
            int k = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            List<Integer> result = solution.kthSmallestInWindows(arr, w, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.size(); i++) {
                if (i > 0) sb.append(" ");
                sb.append(result.get(i));
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq
from collections import Counter, defaultdict

class Solution:
    def kth_smallest_in_windows(self, arr: list, w: int, k: int) -> list:
        # //Implement here
        return []

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        w = int(next(it))
        k = int(next(it))
        arr = []
        for _ in range(n):
            arr.append(int(next(it)))

        solution = Solution()
        result = solution.kth_smallest_in_windows(arr, w, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> kthSmallestInWindows(const vector<int>& arr, int w, int k) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w, k;
    if (cin >> n >> w >> k) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];

        Solution solution;
        vector<int> result = solution.kthSmallestInWindows(arr, w, k);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  kthSmallestInWindows(arr, w, k) {
    //Implement here
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
  const n = parseInt(data[idx++]);
  const w = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++]));
  }

  const solution = new Solution();
  const result = solution.kthSmallestInWindows(arr, w, k);
  console.log(result.join(" "));
});
```
