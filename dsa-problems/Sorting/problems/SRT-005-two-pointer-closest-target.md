---
problem_id: SRT_TWO_POINTER_CLOSEST_TARGET__2651
display_id: SRT-005
slug: two-pointer-closest-target
title: "Two-Pointer Sum Closest to Target"
difficulty: Easy
difficulty_score: 28
topics:
  - Sorting
  - Two Pointers
  - Searching
tags:
  - two-pointers
  - sorted-array
  - search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-005: Two-Pointer Sum Closest to Target

## Problem Statement

You are given a sorted array and a target value. Find the pair of values whose sum is closest to the target.

If there are multiple valid pairs with the same distance to the target, return the pair with the smaller first value.

![Problem Illustration](../images/SRT-005/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (sorted ascending)
- Third line: integer `target`

## Output Format

- Two integers: the pair values in increasing order

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= a[i], target <= 10^9`

## Example

**Input:**

```
4
1 4 6 8
10
```

**Output:**

```
4 6
```

**Explanation:**

The sum 4 + 6 = 10 exactly matches the target.

![Example Visualization](../images/SRT-005/example-1.png)

## Notes

- Use a two-pointer scan from both ends
- Track the closest difference seen so far
- If equal differences occur, pick the smaller first value
- Time complexity: O(n)

## Related Topics

Two Pointers, Sorted Array, Searching

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] closestPair(int[] arr, int target) {
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
        int target = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        int[] result = solution.closestPair(arr, target);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
```

### Python

```python
import sys

def closest_pair(arr: list[int], target: int) -> list[int]:
    # Implementation here
    return []

def main():
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = closest_pair(arr, target)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> closestPair(const vector<int>& arr, int target) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, target;
    if (!(cin >> n >> target)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    vector<int> result = solution.closestPair(arr, target);
    if (result.size() >= 2) {
        cout << result[0] << " " << result[1] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const fs = require("fs");

class Solution {
  closestPair(arr, target) {
    // Implementation here
    return null;
  }
}

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const target = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
const result = solution.closestPair(arr, target);
console.log(result[0] + " " + result[1]);
```
