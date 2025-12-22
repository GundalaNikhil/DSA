---
problem_id: SRT_CLOSEST_PAIR_SORTED_CIRCULAR__3817
display_id: SRT-013
slug: closest-pair-sorted-circular
title: "Closest Pair in Sorted Circular Array"
difficulty: Medium
difficulty_score: 49
topics:
  - Sorting
  - Two Pointers
  - Circular Arrays
tags:
  - two-pointers
  - circular
  - search
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-013: Closest Pair in Sorted Circular Array

## Problem Statement

You are given a sorted circular array (a sorted array rotated at an unknown pivot) and a target. Find a pair of values whose sum is closest to the target.

If multiple pairs tie, return any one. Output the pair values.

![Problem Illustration](../images/SRT-013/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (rotated sorted array)
- Third line: integer `target`

## Output Format

- Two integers: the chosen pair values

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= a[i], target <= 10^9`

## Example

**Input:**

```
5
4 5 1 2 3
7
```

**Output:**

```
4 3
```

**Explanation:**

The pair (4,3) sums to 7 exactly.

![Example Visualization](../images/SRT-013/example-1.png)

## Notes

- Find the pivot (smallest element) to set two pointers
- Use a circular two-pointer technique
- Stop after one full cycle
- Time complexity: O(n)

## Related Topics

Two Pointers, Circular Arrays, Searching

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] closestPairCircular(int[] arr, int target) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int target = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.closestPairCircular(arr, target);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
```

### Python

```python
def closest_pair_circular(arr: list[int], target: int) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    target = int(next(it))

    result = closest_pair_circular(arr, target)
    print(result[0], result[1])

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
    vector<int> closestPairCircular(const vector<int>& arr, int target) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;

    Solution solution;
    vector<int> result = solution.closestPairCircular(arr, target);
    cout << result[0] << " " << result[1] << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  closestPairCircular(arr, target) {
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
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const target = parseInt(data[idx++], 10);

  const solution = new Solution();
  const result = solution.closestPairCircular(arr, target);
  console.log(result[0] + " " + result[1]);
});
```
