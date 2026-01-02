---
problem_id: ARR_POWER_WINDOW_DROP__2879
display_id: ARR-016
slug: power-window-with-drop
title: "Power Window With Drop"
difficulty: Medium
difficulty_score: 49
topics:
  - Arrays
  - Sliding Window
  - Greedy
tags:
  - arrays
  - sliding-window
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-016: Power Window With Drop

## Problem Statement

Given positive integers and a window size k, find the maximum sum of any window after optionally removing one element from that window (you may also remove none).

![Problem Illustration](../images/ARR-016/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer k

## Output Format

Print the maximum adjusted window sum.

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- `1 <= arr[i] <= 1000000000`

## Example

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

Window [5, 3, 2] sums to 10 with no drop, which is the maximum.

![Example Visualization](../images/ARR-016/example-1.png)

## Notes

- You may drop at most one element per window.
- All elements are positive.

## Related Topics

Sliding Window, Greedy, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxWindowSumWithDrop(int[] arr, int k) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        
        int k = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.maxWindowSumWithDrop(arr, k);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
import sys

def max_window_sum_with_drop(arr: list[int], k: int) -> int:
    return 0
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
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maxWindowSumWithDrop(vector<int>& arr, int k) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    
    int k;
    cin >> k;

    Solution solution;
    cout << solution.maxWindowSumWithDrop(arr, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxWindowSumWithDrop(arr, k) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const arr = [];
    for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));
    
    const k = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maxWindowSumWithDrop(arr, k));
});
```

