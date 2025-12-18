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
    private static final int MOD = 1_000_000_007;

    public int countWays(int n, int J, boolean[] cracked) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int J = sc.nextInt();
        int m = sc.nextInt();
        boolean[] cracked = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            int idx = sc.nextInt();
            if (0 <= idx && idx <= n) cracked[idx] = true;
        }

        Solution solution = new Solution();
        System.out.println(solution.countWays(n, J, cracked));
        sc.close();
    }
}
```

### Python

```python
MOD = 1_000_000_007

def count_ways(n: int, J: int, cracked: list[bool]) -> int:
    # Your implementation here
    return 0

def main():
    n, J = map(int, input().split())
    m = int(input().strip())
    cracked = [False] * (n + 1)
    if m > 0:
        arr = list(map(int, input().split()))
        for x in arr:
            if 0 <= x <= n:
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
    static const int MOD = 1000000007;

    int countWays(int n, int J, const vector<bool>& cracked) {
        // Your implementation here
        return 0;
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
        int idx;
        cin >> idx;
        if (0 <= idx && idx <= n) cracked[idx] = true;
    }

    Solution solution;
    cout << solution.countWays(n, J, cracked) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const MOD = 1000000007;

class Solution {
  countWays(n, J, cracked) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  const [n, J] = data[ptr++].split(" ").map(Number);
  const m = Number(data[ptr++]);
  const cracked = new Array(n + 1).fill(false);
  if (m > 0 && ptr < data.length) {
    const arr = data[ptr++].split(" ").map(Number);
    for (const x of arr) {
      if (0 <= x && x <= n) cracked[x] = true;
    }
  }

  const solution = new Solution();
  console.log(solution.countWays(n, J, cracked));
});
```

