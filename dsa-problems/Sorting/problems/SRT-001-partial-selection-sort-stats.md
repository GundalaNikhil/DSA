---
problem_id: SRT_PARTIAL_SELECTION_SORT_STATS__6835
display_id: SRT-001
slug: partial-selection-sort-stats
title: "Partial Selection Sort Stats"
difficulty: Easy
difficulty_score: 24
topics:
  - Sorting
  - Simulation
  - Arrays
tags:
  - sorting
  - selection-sort
  - simulation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-001: Partial Selection Sort Stats

## Problem Statement

Given an array, simulate only the first `k` iterations of selection sort. In iteration `i`, find the minimum element in the subarray `a[i..n-1]` and swap it with `a[i]`.

Return the array state after exactly `k` iterations.

![Problem Illustration](../images/SRT-001/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers

## Output Format

- Single line: array after `k` iterations, space-separated

## Constraints

- `1 <= n <= 100000`
- `0 <= k <= n-1`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
4 2
4 3 1 2
```

**Output:**

```
1 2 4 3
```

**Explanation:**

Iteration 0 swaps 1 to the front, iteration 1 swaps 2 into position 1.

![Example Visualization](../images/SRT-001/example-1.png)

## Notes

- If `k = 0`, the array is unchanged
- Use an index of the minimum in the remaining suffix
- Time complexity: O(k * n)
- Space complexity: O(1)

## Related Topics

Selection Sort, Simulation, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] partialSelectionSort(int n, int k, int[] a) {
        // Implement here
        return a;
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
            int[] result = sol.partialSelectionSort(n, k, a);
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
    def partial_selection_sort(self, n: int, k: int, a: list) -> list:
        # Implement here
        return a

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:]]

    sol = Solution()
    result = sol.partial_selection_sort(n, k, a)
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
    vector<int> partialSelectionSort(int n, int k, vector<int>& a) {
        // Implement here
        return a;
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
        vector<int> result = sol.partialSelectionSort(n, k, a);
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
  partialSelectionSort(n, k, a) {
    // Implement here
    return a;
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
  const result = sol.partialSelectionSort(n, k, a);
  console.log(result.join(" "));
});
```
