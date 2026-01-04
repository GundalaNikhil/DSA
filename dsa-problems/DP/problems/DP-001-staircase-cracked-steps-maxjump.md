---
problem_id: DP_CLIMB_CRACKED_MAXJ__7314
display_id: DP-001
slug: staircase-cracked-steps-maxjump
title: "Staircase With Cracked Steps and Max Jump"
difficulty: Medium
difficulty_score: 52
topics:
  - Dynamic Programming
  - Sliding Window
  - Counting
tags:
  - dp
  - dynamic-programming
  - sliding-window
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-001: Staircase With Cracked Steps and Max Jump

## Problem Statement

You are climbing a staircase with `n` steps (numbered `1` to `n`). You start at step `0` (ground) and want to reach step `n`.

From any step `i`, you may jump to `i+1`, `i+2`, ..., `i+J` (as long as you do not go past `n`).

Some steps are **cracked** and you **cannot land** on them (but you may jump over them).

Your task is to count the number of distinct ways to reach step `n`, modulo `1_000_000_007`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513325/dsa/dp/jegachivzs2hiyvhn5nr.jpg)

## Input Format

- First line: two integers `n` and `J`
- Second line: integer `m` = number of cracked steps
- Third line: `m` space-separated integers denoting cracked step indices

## Output Format

Print one integer: the number of ways to reach step `n` modulo `1_000_000_007`.

## Constraints

- `1 <= n <= 100000`
- `1 <= J <= 50`
- `0 <= m <= 100000`
- Cracked indices are in range `1..n` (if `n` is cracked, answer is `0`)

## Example

**Input:**

```
4 3
1
2
```

**Output:**

```
3
```

**Explanation:**

Cracked step: `{2}` (cannot land on step 2).

Valid paths from step 0 to step 4 using jumps up to 3:

- `0 -> 1 -> 3 -> 4`
- `0 -> 1 -> 4`
- `0 -> 3 -> 4`

So the answer is `3`.

![Example Visualization](../images/DP-001/example-1.png)

## Notes

- You may jump **over** cracked steps; you just cannot land on them.
- Use modulo `1_000_000_007` because the number of ways grows very fast.
- If step `n` is cracked, the answer is `0` because you cannot land on the destination.

## Related Topics

Dynamic Programming, Sliding Window, Counting

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countWays(int n, int j, int m, int[] cracked) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int j = Integer.parseInt(parts[1]);

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        int[] cracked = new int[m];
        if (m > 0) {
            String cLine = br.readLine();
            if (cLine != null) {
                String[] cParts = cLine.trim().split("\\s+");
                for (int i = 0; i < m; i++) {
                    cracked[i] = Integer.parseInt(cParts[i]);
                }
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.countWays(n, j, m, cracked));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_ways(self, n, j, m, cracked):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    j = int(input_data[1])
    m = int(input_data[2])
    cracked = list(map(int, input_data[3:3+m]))

    sol = Solution()
    print(sol.count_ways(n, j, m, cracked))

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
    int countWays(int n, int j, int m, const vector<int>& cracked) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, j, m;
    if (!(cin >> n >> j)) return 0;
    if (!(cin >> m)) m = 0;

    vector<int> cracked(m);
    for (int i = 0; i < m; i++) {
        cin >> cracked[i];
    }

    Solution sol;
    cout << sol.countWays(n, j, m, cracked) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countWays(n, j, m, cracked) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const j = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);
  const cracked = [];
  for (let i = 0; i < m; i++) {
    cracked.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.countWays(n, j, m, cracked));
}

solve();
```
