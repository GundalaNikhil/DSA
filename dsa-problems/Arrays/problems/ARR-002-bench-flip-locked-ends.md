---
problem_id: ARR_BENCH_FLIP_LOCKED__1397
display_id: ARR-002
slug: bench-flip-locked-ends
title: "Bench Flip With Locked Ends"
difficulty: Easy
difficulty_score: 20
topics:
  - Arrays
  - Two Pointers
  - In-place
tags:
  - arrays
  - two-pointers
  - in-place
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-002: Bench Flip With Locked Ends

## Problem Statement

Reverse the array in place, but keep the first and last elements fixed. Only the middle segment is reversed.

![Problem Illustration](../images/ARR-002/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]

## Output Format

Print the resulting array, space-separated.

## Constraints

- `2 <= n <= 200000`
- `-1000000000 <= arr[i] <= 1000000000`

## Example

**Input:**

```
5
9 3 8 1 5
```

**Output:**

```
9 1 8 3 5
```

**Explanation:**

The first and last elements stay. The middle subarray [3, 8, 1] is reversed to
[1, 8, 3].

![Example Visualization](../images/ARR-002/example-1.png)

## Notes

- If n <= 2, the array is unchanged.
- Use two pointers starting at indices 1 and n-2.

## Related Topics

Arrays, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] flipBenchLockedEnds(int n, int[] arr) {
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
        int[] result = sol.flipBenchLockedEnds(n, arr);

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
    def flip_bench_locked_ends(self, n, arr):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))

    sol = Solution()
    result = sol.flip_bench_locked_ends(n, arr)

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
    vector<int> flipBenchLockedEnds(int n, vector<int>& arr) {
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
    vector<int> result = sol.flipBenchLockedEnds(n, arr);

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
  flipBenchLockedEnds(n, arr) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  const result = sol.flipBenchLockedEnds(n, arr);

  console.log(result.join(" "));
}

solve();
```
