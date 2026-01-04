---
problem_id: ARR_FIXED_ONES_SORT__5412
display_id: ARR-014
slug: boarding-order-fixed-ones
title: "Boarding Order With Fixed Ones"
difficulty: Medium
difficulty_score: 48
topics:
  - Arrays
  - Sorting
  - Two Pointers
tags:
  - arrays
  - sorting
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-014: Boarding Order With Fixed Ones

## Problem Statement

The array contains only 0s, 1s, and 2s. All 1s are fixed in their current positions and cannot move. Sort the array so 0s come first, then 1s, then 2s, while keeping every 1 in place.

![Problem Illustration](../images/ARR-014/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i] (each 0, 1, or 2)

## Output Format

Print the resulting array, space-separated.

## Constraints

- `1 <= n <= 200000`
- `arr[i] in {0, 1, 2}`

## Example

**Input:**

```
6
2 1 0 2 0 1
```

**Output:**

```
0 1 0 1 2 2
```

**Explanation:**

The 1s remain at indices 1 and 5. The remaining positions are filled with 0s
from left to right and 2s from right to left.

![Example Visualization](../images/ARR-014/example-1.png)

## Notes

- Do not move any index containing 1.
- The array should be sorted around the fixed 1s.

## Related Topics

Arrays, Sorting, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] sortWithFixedOnes(int n, int[] arr) {
        // Implement here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] arr = new int[n];
        String arrLine = br.readLine();
        if (arrLine != null) {
            String[] parts = arrLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(parts[i]);
            }
        }

        Solution sol = new Solution();
        int[] result = sol.sortWithFixedOnes(n, arr);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def sort_with_fixed_ones(self, n, arr):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))

    sol = Solution()
    result = sol.sort_with_fixed_ones(n, arr)

    print(*(result))

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
    vector<int> sortWithFixedOnes(int n, vector<int>& arr) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution sol;
    vector<int> result = sol.sortWithFixedOnes(n, arr);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  sortWithFixedOnes(n, arr) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(readInt());

  const sol = new Solution();
  const result = sol.sortWithFixedOnes(n, arr);

  console.log(result.join(" "));
}

solve();
```
