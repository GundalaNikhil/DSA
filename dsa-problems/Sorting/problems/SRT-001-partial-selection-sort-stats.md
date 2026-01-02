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
    public int[] partialSelectionSort(int[] arr, int k) {
        // Implementation here
        return new int[0];
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
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        int[] result = solution.partialSelectionSort(arr, k);
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
import sys

def partial_selection_sort(arr: list[int], k: int) -> list[int]:
    # Implementation here
    return []

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = partial_selection_sort(arr, k)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> partialSelectionSort(vector<int> arr, int k) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    vector<int> result = solution.partialSelectionSort(arr, k);
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
const fs = require("fs");

class Solution {
  partialSelectionSort(arr, k) {
    // Implementation here
    return null;
  }
}

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const k = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
const result = solution.partialSelectionSort(arr, k);
console.log(result.join(" "));
```
