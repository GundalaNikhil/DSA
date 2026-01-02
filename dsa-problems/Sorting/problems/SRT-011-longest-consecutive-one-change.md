---
problem_id: SRT_LONGEST_CONSECUTIVE_ONE_CHANGE__6194
display_id: SRT-011
slug: longest-consecutive-one-change
title: "Longest Consecutive After At Most One Change"
difficulty: Medium
difficulty_score: 53
topics:
  - Sorting
  - Prefix Suffix
  - Arrays
tags:
  - arrays
  - prefix-suffix
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-011: Longest Consecutive After At Most One Change

## Problem Statement

Given an array, you may change at most one element to any value. Find the maximum length of a strictly increasing contiguous subarray you can obtain.

![Problem Illustration](../images/SRT-011/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single integer: maximum possible length

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
6
1 2 3 7 5 6
```

**Output:**

```
6
```

**Explanation:**

Change `7` to `4` to get `[1,2,3,4,5,6]`.

![Example Visualization](../images/SRT-011/example-1.png)

## Notes

- Precompute longest increasing prefix and suffix lengths
- Try bridging around each index with one change
- The answer is at least the original longest run
- Time complexity: O(n)

## Related Topics

Arrays, Prefix/Suffix, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int longestAfterChange(int[] arr) {
        // Implementation here
        return 0;
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
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.longestAfterChange(arr));
        sc.close();
    }
}
```

### Python

```python
import sys

def longest_after_change(arr: list[int]) -> int:
    # Implementation here
    return 0

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_after_change(arr)
    print(result)

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
    int longestAfterChange(const vector<int>& arr) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.longestAfterChange(arr) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const fs = require("fs");

class Solution {
  longestAfterChange(arr) {
    // Implementation here
    return null;
  }
}

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
console.log(solution.longestAfterChange(arr).toString());
```
