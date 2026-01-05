---
problem_id: GRD_LIBRARY_POWER_BACKUP__4928
display_id: GRD-004
slug: library-power-backup
title: "Library Power Backup"
difficulty: Medium
difficulty_score: 40
topics:
  - Greedy Algorithms
  - Sorting
  - Optimization
tags:
  - greedy
  - sorting
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-004: Library Power Backup

## Problem Statement

A library server needs continuous power for `T` hours. You have `n` backup batteries, where battery `i` has a capacity of `c[i]` hours.

Each hour, you must draw power from exactly one battery until it is depleted. When a battery runs out, you switch to another battery (if available).

Your goal is to minimize the number of battery swaps (the number of times you change from one battery to another) while ensuring the server runs for the full `T` hours.

Return the minimum number of swaps, or `-1` if it's impossible to power the server for `T` hours.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-004.jpg)

## Input Format

- First line: two integers `n T` (number of batteries and required hours)
- Second line: `n` space-separated integers representing battery capacities `c[0], c[1], ..., c[n-1]`

## Output Format

- Single integer: minimum number of battery swaps, or `-1` if impossible

## Constraints

- `1 <= n <= 10^5`
- `1 <= c[i] <= 10^9`
- `1 <= T <= 10^9`

## Example

**Input:**

```
3 7
3 5 2
```

**Output:**

```
1
```

**Explanation:**

Batteries: [3, 5, 2] hours each
Required time: 7 hours
Total capacity: 3 + 5 + 2 = 10 hours (sufficient)

Greedy strategy (use largest capacities first):

1. Sort batteries by capacity: [5, 3, 2]
2. Use battery with 5 hours → powers for hours 0-4
3. Switch to battery with 3 hours → powers for hours 5-7 (only need 2 hours)

Total swaps: 1 (from first battery to second battery)

![Example Visualization](../images/GRD-004/example-1.png)

## Notes

- First check if total capacity >= T; if not, return -1
- Sort batteries in descending order by capacity
- Greedily use largest batteries first to minimize switches
- Number of swaps = (number of batteries used) - 1
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Sorting, Resource Allocation, Optimization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int minSwaps(int n, long t, long[] c) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ntLine = br.readLine();
        if (ntLine == null) return;
        String[] nt = ntLine.trim().split("\\s+");
        int n = Integer.parseInt(nt[0]);
        long t = Long.parseLong(nt[1]);

        long[] c = new long[n];
        String[] cLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) {
            c[i] = Long.parseLong(cLine[i]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minSwaps(n, t, c));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_swaps(self, n, t, c):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    t = int(input_data[1])
    c = list(map(int, input_data[2:2+n]))

    sol = Solution()
    print(sol.min_swaps(n, t, c))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minSwaps(int n, long long t, vector<long long>& c) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long t;
    if (!(cin >> n >> t)) return 0;

    vector<long long> c(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }

    Solution sol;
    cout << sol.minSwaps(n, t, c) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minSwaps(n, t, c) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const t = BigInt(input[idx++]);
  const c = [];
  for (let i = 0; i < n; i++) {
    c.push(BigInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.minSwaps(n, t, c));
}

solve();
```
