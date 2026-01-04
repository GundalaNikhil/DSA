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
    public int minSwapsToSort(int n, int k, int[] a) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            Solution sol = new Solution();
            System.out.println(sol.minSwapsToSort(n, k, a));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def min_swaps_to_sort(self, n: int, k: int, a: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:]]

    sol = Solution()
    print(sol.min_swaps_to_sort(n, k, a))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minSwapsToSort(int n, int k, vector<int>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (cin >> n >> k) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution sol;
        cout << sol.minSwapsToSort(n, k, a) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minSwapsToSort(n, k, a) {
    // Implement here
    return 0;
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
  const k = parseInt(input[1]);
  const a = input.slice(2).map(Number);

  const sol = new Solution();
  console.log(sol.minSwapsToSort(n, k, a));
});
```
