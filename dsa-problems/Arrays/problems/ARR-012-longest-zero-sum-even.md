---
problem_id: ARR_ZERO_SUM_EVEN__6774
display_id: ARR-012
slug: longest-zero-sum-even
title: "Longest Zero-Sum Even Length"
difficulty: Medium
difficulty_score: 52
topics:
  - Arrays
  - Prefix Sum
  - Hashing
tags:
  - arrays
  - prefix-sum
  - hashing
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-012: Longest Zero-Sum Even Length

## Problem Statement

Find the maximum even length of a subarray whose sum is zero. If no such subarray exists, return 0.

![Problem Illustration](../images/ARR-012/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]

## Output Format

Print the maximum even length of a zero-sum subarray.

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= arr[i] <= 1000000000`

## Example

**Input:**

```
5
1 -1 3 -3 2
```

**Output:**

```
4
```

**Explanation:**

The subarray from index 0 to 3 has sum 0 and length 4, which is even.

![Example Visualization](../images/ARR-012/example-1.png)

## Notes

- Return 0 if no even-length zero-sum subarray exists.
- Use prefix sums with parity to enforce even length.

## Related Topics

Prefix Sum, Hashing, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int findMaxZeroSumEvenLength(int n, int[] arr) {
        // Implement here
        return 0;
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
        System.out.println(sol.findMaxZeroSumEvenLength(n, arr));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_max_zero_sum_even_length(self, n, arr):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))

    sol = Solution()
    print(sol.find_max_zero_sum_even_length(n, arr))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findMaxZeroSumEvenLength(int n, vector<int>& arr) {
        // Implement here
        return 0;
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
    cout << sol.findMaxZeroSumEvenLength(n, arr) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findMaxZeroSumEvenLength(n, arr) {
    // Implement here
    return 0;
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
  console.log(sol.findMaxZeroSumEvenLength(n, arr));
}

solve();
```
