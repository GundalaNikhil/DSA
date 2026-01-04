---
problem_id: ARR_BEST_STREAK_SMOOTH__2467
display_id: ARR-009
slug: best-streak-one-smoothing
title: "Best Streak With One Smoothing"
difficulty: Medium
difficulty_score: 54
topics:
  - Arrays
  - Dynamic Programming
  - Kadane
tags:
  - arrays
  - dynamic-programming
  - kadane
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-009: Best Streak With One Smoothing

## Problem Statement

You must pick exactly one index i (1 <= i <= n-2) and replace a[i] with floor((a[i-1] + a[i] + a[i+1]) / 3). After this smoothing, compute the maximum subarray sum. Return the maximum possible value.

![Problem Illustration](../images/ARR-009/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the maximum subarray sum achievable after one smoothing.

## Constraints

- `3 <= n <= 200000`
- `-1000000000 <= a[i] <= 1000000000`

## Example

**Input:**

```
4
-2 3 -4 5
```

**Output:**

```
9
```

**Explanation:**

Smooth index 2: (-4) becomes floor((3 - 4 + 5)/3) = 1. The array becomes
[-2, 3, 1, 5], whose maximum subarray sum is 9.

![Example Visualization](../images/ARR-009/example-1.png)

## Notes

- You must smooth exactly one middle element.
- Use 64-bit arithmetic for sums.

## Related Topics

Kadane, Dynamic Programming, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxStreakWithSmoothing(int n, int[] a) {
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

        int[] a = new int[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] parts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(parts[i]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.maxStreakWithSmoothing(n, a));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_streak_with_smoothing(self, n, a):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))

    sol = Solution()
    print(sol.max_streak_with_smoothing(n, a))

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
    long long maxStreakWithSmoothing(int n, vector<int>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution sol;
    cout << sol.maxStreakWithSmoothing(n, a) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxStreakWithSmoothing(n, a) {
    // Implement here
    return BigInt(0);
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
  const a = [];
  for (let i = 0; i < n; i++) a.push(readInt());

  const sol = new Solution();
  console.log(sol.maxStreakWithSmoothing(n, a).toString());
}

solve();
```
