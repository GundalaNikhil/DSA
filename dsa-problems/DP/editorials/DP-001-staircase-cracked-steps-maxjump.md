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
---

# DP-001: Staircase With Cracked Steps and Max Jump

## 📋 Problem Summary

You need to count how many distinct ways you can reach step `n` from step `0` when you can jump `1..J` steps at a time, but you are not allowed to **land** on cracked steps. Since the number of ways can explode quickly, you must return the answer modulo `1_000_000_007`.

This is a classic “counting DP” problem with an extra constraint (blocked states) and a performance requirement (`n` up to `10^5`).

## 🌍 Real-World Scenario

**Scenario Title:** Campus Building Staircase During Renovation

Your college is renovating an old academic block. The staircase is open, but some steps are damaged and marked “DO NOT STEP”. Students can still climb quickly by skipping steps, but they must not land on the cracked ones.

Now imagine you’re building a “safe navigation” feature for a campus accessibility app. The app knows:

- total steps to the destination (`n`)
- how big a jump a person can reasonably take (`J`)
- which steps are unsafe to land on (cracked list)

The app wants to show the number of safe ways to reach the destination. This isn’t just a math puzzle—counting feasible paths under constraints shows up in routing, workflow planning, and scheduling.

**Why This Problem Matters:**

- Helps you recognize when a brute force search becomes impossible (`n=10^5`)
- Trains you to model “blocked states” cleanly in DP
- Introduces a common optimization: sliding window / prefix-sum DP to remove an inner loop

![Real-World Application](../images/DP-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Staircase Structure

```
Staircase with J=3 (max jump), cracked step at 2:

  Step:  0    1    2    3    4
         ●────●────✗────●────●
              └───┘ ↑
              └─────┘ (J=3)

Jumps from 0: can reach 1, 2, 3 (but 2 is cracked)
Jump paths:
  0 → 1 (jump 1 step)
  0 → 2 (jump 2 steps, but CRACKED - blocked)
  0 → 3 (jump 3 steps)

Legend:
  ● = valid step
  ✗ = cracked step (cannot land)
  → = possible jump
```

## ✅ Input/Output Clarifications (Read This Before Coding)

These details decide whether your solution is correct:

- You start at step `0`, so `dp[0] = 1` (one way to be at the start).
- You may jump **over** cracked steps; you just cannot **land** on them.
- If step `n` is cracked, answer is `0` (destination is blocked).
- Apply modulo `1_000_000_007` at every step to prevent overflow.

Common interpretation mistake:

- ❌ “Cracked steps cannot be crossed.”  
  ✅ Wrong. They can be crossed (jumped over). Only landing is forbidden.

### Step numbering and what “ways” means

- Steps are numbered `1..n`
- You start at `0` (ground)
- You want to land exactly at `n`
- Allowed moves from `i`: go to any `i + k` where `1 <= k <= J` and `i+k <= n`
- If step `x` is cracked, you cannot land on `x` (but can jump over it)

### Define the DP state (this is the heart)

Let:

`dp[i] = number of ways to land on step i`

Base case:

- `dp[0] = 1` (there is exactly one way to “be at the start”: do nothing)

Transition:

To land on step `i`, you must come from one of the previous `J` steps:

`dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-J]` (only valid indices)

But if step `i` is cracked:

`dp[i] = 0` (you cannot land there)

We compute everything modulo `MOD = 1_000_000_007`.

### Why naive summation is too slow

If you compute `dp[i]` by looping `k=1..J`, you do `J` work per `i`.

- Time: `O(n * J)`
- With `n=100000` and `J=50`, that is `5,000,000` operations—this is actually okay in many languages.

But this is the “bare minimum”. In real systems and contests, you are expected to notice that the sum is a **sliding window** and can be optimized to `O(n)` with the same correctness.

Also, `J` could be larger in variants (and interviewers love asking that).

## Naive Approach

### Intuition

Try all possible jumps recursively:

- From step 0, try jumping 1..J
- From each reachable step, try again
- Avoid landing on cracked steps

This is the most natural first thought, and it is also the fastest way to TLE.

### Algorithm

1. Start at step `0`
2. For each step `i`, try all jumps `k=1..J` to reach `i+k`
3. If you hit `n`, count 1 way
4. Sum ways over all branches

### Time Complexity

- Exponential in `n` (roughly `O(J^n)` in the worst case)

### Space Complexity

- `O(n)` recursion depth in worst case

### Why This Works

It enumerates all valid paths and counts them.

### Limitations

- Completely infeasible for `n` as small as a few thousand, forget `10^5`.
- Recomputes the same subproblems again and again (classic overlapping subproblems).

## Better (But Still Not Best): Classic DP in O(n·J)

If you jump directly from recursion to the optimized solution, you miss an important DP learning step.

### Intuition

Once we define `dp[i] = number of ways to land on step i`, we can compute answers in increasing `i`:

`dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-J]` (only indices `>= 0`)

If `i` is cracked, we force `dp[i] = 0`.

### Algorithm

1. Build `cracked[]`.
2. Set `dp[0] = 1`.
3. For `i` from `1..n`:
   - If cracked: `dp[i] = 0`
   - Else: `dp[i] = sum(dp[i-k]) for k=1..J and i-k>=0`
4. Return `dp[n]`.

### Time Complexity

- `O(n * J)`

With `n=100000` and `J=50`, this is about 5 million additions, which usually passes. But there is a cleaner `O(n)` way using a sliding window, and that is what interviewers want.

### Space Complexity

- `O(n)`

### Decision Tree for DP Transition

```
For each step i (from 1 to n):
    │
    ├─ Is step i cracked?
    │   │
    │   ├─ YES: dp[i] = 0
    │   │        (cannot land on cracked step)
    │   │
    │   └─ NO:  dp[i] = windowSum
    │            (sum of previous J valid steps)
    │
    └─ Update sliding window for next iteration:
        │
        ├─ Add dp[i] to windowSum
        │   windowSum = (windowSum + dp[i]) % MOD
        │
        └─ Remove dp[i-J] if it exists (i-J >= 0)
            windowSum = (windowSum - dp[i-J] + MOD) % MOD

            (This maintains the invariant that windowSum
             always holds the sum of the last J dp values)
```

## Optimal Approach

### Key Insight

The transition is a sum of the previous `J` DP values:

`dp[i] = sum(dp[i-J .. i-1])`

This is a sliding window sum. If you maintain:

`windowSum = dp[i-1] + dp[i-2] + ... + dp[i-J]`

then:

- `dp[i] = windowSum` (if not cracked)
- update window for next index by:
  - adding `dp[i]`
  - removing `dp[i-J]` (the value that falls out of the window)

Cracked steps are handled naturally: they force `dp[i]=0`, which contributes nothing to future sums (exactly what we want).

### Algorithm

1. Create `cracked[0..n]` boolean array.
2. Initialize:
   - `dp[0] = 1`
   - `windowSum = dp[0]` (for i=1, window includes dp[0])
3. For `i` from `1` to `n`:
   - If `cracked[i]` is true: `dp[i] = 0`
   - Else: `dp[i] = windowSum`
   - Update `windowSum = (windowSum + dp[i]) % MOD`
   - If `i - J >= 0`, remove the outgoing term:
     - `windowSum = (windowSum - dp[i - J] + MOD) % MOD`
4. Answer is `dp[n]`.

### Time Complexity

- `O(n + m)` where `m` is number of cracked steps
- DP loop is `O(n)` and each iteration is O(1)

### Space Complexity

- `O(n)` for `dp` and `cracked`
- You can reduce `dp` to `O(J)` using a ring buffer, but `O(n)` is fine for `n=10^5`.

### Why This Is Optimal

Because you must at least look at each step once to know if it is cracked and compute the result. The sliding window removes redundant summations and keeps each iteration constant time.

![Algorithm Visualization](../images/DP-001/algorithm-visualization.png)
![Algorithm Steps](../images/DP-001/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int countWays(int n, int J, boolean[] cracked) {
        if (cracked[n]) return 0;

        long[] dp = new long[n + 1];
        dp[0] = 1;
        long windowSum = dp[0]; // sum of dp[max(0, i-J) .. i-1] for current i (starts at i=1)

        for (int i = 1; i <= n; i++) {
            // You cannot land on cracked steps.
            if (cracked[i]) {
                dp[i] = 0;
            } else {
                dp[i] = windowSum;
            }

            // Slide window: include dp[i] for future steps.
            windowSum = (windowSum + dp[i]) % MOD;
            int out = i - J;
            if (out >= 0) {
                // Remove the value that is now too old to contribute.
                windowSum = (windowSum - dp[out]) % MOD;
                if (windowSum < 0) windowSum += MOD;
            }
        }
        return (int) (dp[n] % MOD);
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
MOD = 1_000_000_007

def count_ways(n: int, J: int, cracked: list[bool]) -> int:
    if cracked[n]:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    window_sum = 1  # sum of dp[max(0, i-J) .. i-1] when processing i

    for i in range(1, n + 1):
        # Block landing on cracked steps.
        dp[i] = 0 if cracked[i] else window_sum
        window_sum = (window_sum + dp[i]) % MOD
        out = i - J
        if out >= 0:
            window_sum = (window_sum - dp[out]) % MOD

    return dp[n]

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
    static const int MOD = 1000000007;

    int countWays(int n, int J, const vector<bool>& cracked) {
        if (cracked[n]) return 0;

        vector<long long> dp(n + 1, 0);
        dp[0] = 1;
        long long windowSum = 1;

        for (int i = 1; i <= n; i++) {
            dp[i] = cracked[i] ? 0 : windowSum;
            windowSum = (windowSum + dp[i]) % MOD;
            int out = i - J;
            if (out >= 0) {
                windowSum = (windowSum - dp[out]) % MOD;
                if (windowSum < 0) windowSum += MOD;
            }
        }
        return (int)(dp[n] % MOD);
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

## 🧪 Test Case Walkthrough (Dry Run)

Use the sample:

- `n = 4`, `J = 3`
- cracked steps: `{2}`

We maintain:

- `dp[i]` = ways to land on step `i`
- `windowSum` = sum of the previous `J` dp values needed to compute next dp

Initialize:

- `dp[0] = 1`
- When computing `i = 1`, the window is just `{dp[0]}`, so `windowSum = 1`.

Now iterate:

| i | cracked? | dp[i] | Explanation | Window State Before | windowSum After |
|---:|:--------:|------:|-------------|---------------------|----------------:|
| 1 | no | 1 | from dp[0] | {dp[0]} = {1} | 2 |
| 2 | yes | 0 | cannot land on 2 | {dp[1], dp[0]} = {1, 1} | 2 |
| 3 | no | 2 | from dp[2]+dp[1]+dp[0] = 0+1+1 | {dp[2], dp[1], dp[0]} = {0, 1, 1} | 3 |
| 4 | no | 3 | from dp[3]+dp[2]+dp[1] = 2+0+1 | {dp[3], dp[2], dp[1]} = {2, 0, 1} | 5 |

Note: Window State shows which dp values are summed (the sliding window of J=3 previous steps).

Answer is `dp[4] = 3`.

This matches the three valid paths:

- `0 -> 1 -> 3 -> 4`
- `0 -> 1 -> 4`
- `0 -> 3 -> 4`

![Example Visualization](../images/DP-001/example-1.png)

## ✅ Proof of Correctness (Optimized Sliding Window DP)

### Invariant

Before computing `dp[i]` (for `i >= 1`), `windowSum` equals:

`windowSum = dp[i-1] + dp[i-2] + ... + dp[max(0, i-J)] (mod MOD)`

### Why the recurrence is correct

Any valid path that lands on step `i` must come from exactly one predecessor step `i-k` where:

- `1 <= k <= J`, and
- `i-k >= 0`

So the number of ways to reach `i` is the sum of ways to reach all those predecessors:

`dp[i] = sum(dp[i-k])`

If step `i` is cracked, there are zero valid paths landing there, so `dp[i] = 0`.

By the invariant, that predecessor sum is exactly what `windowSum` stores, hence computing `dp[i] = windowSum` (when not cracked) is correct.

### Why the window update preserves the invariant

After computing `dp[i]`, the next step `(i+1)` should sum `dp[i]` down to `dp[i-J+1]`.

- Adding `dp[i]` includes the new dp value in the range.
- Subtracting `dp[i-J]` (when `i-J >= 0`) removes the value that is no longer in range.

Thus `windowSum` remains the correct sliding sum for the next iteration, and by induction all dp values are correct, including `dp[n]`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Space optimization:** keep only the last `J` values (ring buffer) instead of a full `dp[]` array.
- **If `J` is not small:** `O(n·J)` will fail; sliding window becomes mandatory.
- **Edge-case discipline:** explicitly handle “destination is cracked” early (return 0).

### Common Mistakes to Avoid

1. **Forgetting `dp[0] = 1`**

   - Without the correct base case, every value becomes 0.
   - ✅ Always define exactly one way to be at the start.

2. **Treating cracked steps as “unreachable but still countable”**

   - ❌ Some students compute dp normally and “skip it later”.
   - ✅ If step `i` is cracked, force `dp[i] = 0` immediately.

3. **Off-by-one on the sliding window removal**

   - Many bugs come from removing `dp[i-J-1]` instead of `dp[i-J]`.
   - ✅ Maintain the invariant: `windowSum = sum(dp[max(0,i-J) .. i-1])` for the current `i`.

4. **Modulo subtraction becoming negative**

   - In Java/C++/JS, `a - b` can become negative.
   - ✅ Fix by adding `MOD` before taking `% MOD`.

5. **Assuming the cracked list is always on a single line**

   - In many judges, `m` integers can be split across multiple lines.
   - ✅ Robust input parsing should read `m` integers regardless of line breaks (especially in Java/C++).


## Related Concepts

- Sliding window DP / prefix-sum DP
- Counting paths in DAGs
- Handling blocked states in DP
- Modulo arithmetic in combinatorics
