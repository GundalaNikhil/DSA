---
problem_id: ARR_SLIDE_MAX__14AE
display_id: ARR-016
slug: power-window-drop
title: "Power Window With Drop"
difficulty: Hard
difficulty_score: 75
topics:
  - Array
  - Sliding Window
  - Optimization
  - Maximum Subarray
  - Greedy
  - Dynamic Programming
tags:
  - arrays
  - sliding-window
  - greedy
  - hard
premium: true
subscription_tier: pro
time_limit: 2000
memory_limit: 256
---

# Power Window With Drop

## Problem Statement

Given an array of integers (positive or negative) and a window size `k`, consider every contiguous window of length `k`. For each window you may optionally remove at most one element (or remove none) to maximize the sum of the remaining elements. Return the maximum achievable window sum after this optional single drop.

![Problem Illustration](../images/ARR-016/problem-illustration.png)


## Input Format

- First line: Integer `n` — size of the array (1 ≤ n ≤ 2 × 10^5)
- Second line: `n` space-separated integers
- Third line: Integer `k` — window size (1 ≤ k ≤ n)

## Output Format

Print a single integer — the maximum window sum obtainable after removing at most one element from that window.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- 1 ≤ k ≤ n
- -10^9 ≤ arr[i] ≤ 10^9

## Examples

### Example 1

**Input:**

```
5
2 1 5 3 2
3
```

**Output:**

```
10
```

**Explanation:**

Windows of size 3:
- [2, 1, 5] sum=8, drop 1 ⇒ 7
- [1, 5, 3] sum=9, drop 1 ⇒ 8
- [5, 3, 2] sum=10, no drop needed ⇒ 10 (maximum)

![Example 1 Visualization](../images/ARR-016/example-1.png)

### Example 2

**Input:**

```
4
10 1 20 30
3
```

**Output:**

```
50
```

**Explanation:**

For window [1, 20, 30] sum=51; dropping 1 yields 50, which is the best achievable.

## Notes

- Maintain the running sum of the window and track its minimum element; the best sum for a window is `window_sum` (no drop) or `window_sum - min_element` (drop one).

## Related Topics

Array, Sliding Window, Optimization, Maximum Subarray, Greedy, Dynamic Programming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxWindowSumWithDrop(int[] arr, int k) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.maxWindowSumWithDrop(arr, k);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def max_window_sum_with_drop(arr: List[int], k: int) -> int:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    result = max_window_sum_with_drop(arr, k)
    print(result)

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
    int maxWindowSumWithDrop(vector<int>& arr, int k) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int k;
    cin >> k;

    Solution solution;
    int result = solution.maxWindowSumWithDrop(arr, k);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    maxWindowSumWithDrop(arr, k) {
        // Your implementation here
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];
rl.on('line', (line) => {
    lines.push(line);
    if (lines.length === 3) {
        const n = parseInt(lines[0]);
        const arr = lines[1].split(' ').map(Number);
        const k = parseInt(lines[2]);

        const solution = new Solution();
        const result = solution.maxWindowSumWithDrop(arr, k);

        console.log(result);
        rl.close();
    }
});
```
