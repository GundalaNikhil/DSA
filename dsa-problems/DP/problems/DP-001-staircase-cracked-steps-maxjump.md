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

![Problem Illustration](../images/DP-001/problem-illustration.png)

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

class Solution {
    public int countWays(int n, int J, boolean[] cracked) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int J = sc.nextInt();
        int m = sc.nextInt();
        boolean[] cracked = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            int idx = sc.nextInt();
            if (1 <= idx && idx <= n) cracked[idx] = true;
        }
        System.out.println(new Solution().countWays(n, J, cracked));
        sc.close();
    }
}
```

### Python

```python
import sys

def count_ways(n: int, J: int, cracked: list[bool]) -> int:
    # Implementation here
    return 0

def main():
    n, J = map(int, input().split())
    m = int(input().strip())
    cracked = [False] * (n + 1)
    if m > 0:
        arr = list(map(int, input().split()))
        for x in arr:
            if 1 <= x <= n:
                cracked[x] = True
    print(count_ways(n, J, cracked))

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
    int countWays(int n, int J, const vector<bool>& cracked) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, J;
    cin >> n >> J;
    int m;
    cin >> m;
    vector<bool> cracked(n + 1, false);
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        if (1 <= x && x <= n) cracked[x] = true;
    }

    Solution sol;
    cout << sol.countWays(n, J, cracked) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countWays(n, J, cracked) {
    // Implementation here
    return null;
  }
}

const MOD = 1000000007n;

class Solution {
  countWays(n, J, cracked) {
    if (cracked[n]) return 0;

    const dp = new Array(n + 1).fill(0n);
    dp[0] = 1n;
    let windowSum = 1n;

    for (let i = 1; i <= n; i++) {
      dp[i] = cracked[i] ? 0n : windowSum;
      windowSum = (windowSum + dp[i]) % MOD;

      const out = i - J;
      if (out >= 0) {
        windowSum = (windowSum - dp[out]) % MOD;
        if (windowSum < 0n) windowSum += MOD;
      }
    }
    return Number(dp[n] % MOD);
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [nStr, jStr] = lines[idx++].split(" ");
  const n = Number(nStr);
  const J = Number(jStr);
  const m = Number(lines[idx++]);

  const cracked = new Array(n + 1).fill(false);
  if (m > 0) {
    const arr = (lines[idx++] ?? "").split(" ").filter(Boolean).map(Number);
    for (const x of arr) {
      if (1 <= x && x <= n) cracked[x] = true;
    }
  }

  const sol = new Solution();
  console.log(sol.countWays(n, J, cracked));
});
```
