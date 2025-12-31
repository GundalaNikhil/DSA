---
problem_id: SRT_K_SORTED_ARRAY_MIN_SWAPS__8347
display_id: SRT-006
slug: k-sorted-array-min-swaps
title: "K-Sorted Array Minimum Swaps"
difficulty: Medium
difficulty_score: 50
topics:
  - Sorting
  - Cycles
  - Swaps
tags:
  - sorting
  - swaps
  - cycles
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-006: K-Sorted Array Minimum Swaps

## Problem Statement

An array is k-sorted if every element is at most `k` positions away from its position in the sorted array. Given such an array and `k`, count how many elements violate the k-sorted property (i.e., are more than `k` positions away from where they belong in the sorted array). Return the count of violations divided by (k+1), rounded down.

**Key Insight:** The problem evaluates how "far from k-sorted" an array is, measured by the number of constraint violations scaled by the k parameter.

![Problem Illustration](../images/SRT-006/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers

## Output Format

- Single integer: minimum swaps to sort the array

## Constraints

- `1 <= n <= 200000`
- `0 <= k < n`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
3 2
3 1 2
```

**Output:**

```
2
```

**Explanation:**

Swap 3 with 1, then swap 3 with 2 to obtain `[1,2,3]`.

![Example Visualization](../images/SRT-006/example-1.png)

## Notes

- Use value-index pairs to compute target positions
- Count cycles in the permutation mapping
- Minimum swaps equals sum of (cycle length - 1)
- k only guarantees proximity, not a faster algorithm requirement

## Related Topics

Sorting, Cycles in Permutations, Swaps

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public long minSwapsToSort(int[] arr) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.minSwapsToSort(arr));
        sc.close();
    }
}
```

### Python

```python
def min_swaps_to_sort(arr: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    print(min_swaps_to_sort(arr))

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
    long long minSwapsToSort(const vector<int>& arr) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    cout << solution.minSwapsToSort(arr) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minSwapsToSort(arr) {
    // Your implementation here
    return 0;
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
  const k = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.minSwapsToSort(arr);
  console.log(result.toString());
});
```
