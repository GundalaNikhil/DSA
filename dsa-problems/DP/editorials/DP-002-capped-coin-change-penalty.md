---
problem_id: DP_COIN_CAP_PENALTY__1842
display_id: DP-002
slug: capped-coin-change-penalty
title: "Capped Coin Change With Penalty"
difficulty: Medium
difficulty_score: 58
topics:
  - Dynamic Programming
  - Knapsack
  - Optimization
tags:
  - dp
  - knapsack
  - bounded-knapsack
  - medium
premium: true
subscription_tier: basic
---

# DP-002: Capped Coin Change With Penalty

## 📋 Problem Summary

You must form an exact sum `target` using `k` coin types. Each type has a denomination `d[i]` and a maximum count `c[i]`. The base cost is the total number of coins used. But there is a twist: if you use **more than** `floor(c[i]/2)` coins of a type, you pay a one-time penalty `p[i]` for that type.

Return the minimum possible cost, or `-1` if the target cannot be formed.

## 🌍 Real-World Scenario

**Scenario Title:** Hostel Canteen Tokens With “Bulk Usage” Fee

Your hostel canteen issues meal tokens in different denominations (₹1, ₹5, ₹10, ...). Each denomination is limited because tokens are physically counted and distributed (that’s your `c[i]`).

To discourage students from exhausting a single denomination, the canteen adds a rule:

- If you use “too many” tokens of a certain type (more than half the available stock of that denomination), you pay an extra service fee (the penalty).

As a developer building the billing system:

- you must respect the limited stock
- you want to minimize the total “cost” (number of tokens + any fees)
- and you must return `-1` if a bill cannot be paid exactly with available tokens

This maps directly to a bounded knapsack with a threshold-based activation cost.

**Why This Problem Matters:**

- Forces you to model per-type constraints (bounded knapsack, not unbounded)
- Introduces “activation cost” patterns (pay once if you cross a threshold)
- Tests whether you can optimize DP beyond naive triple loops for `target <= 5000`

![Real-World Application](../images/DP-002/real-world-scenario.png)

## ✅ Input/Output Clarifications (Non-Negotiable)

- You must form **exactly** `target`. Not “at least”.
- For each type `i`, you may use `0..c[i]` coins.
- The penalty `p[i]` is charged:
  - **once per type** (not per coin)
  - only if `used_i > floor(c[i]/2)`
- If `c[i]` is huge (even 10^9), you still cannot use more than `target / d[i]` coins of that type because you cannot exceed `target`.
- Output can be large; use 64-bit integers (`long long` / `long`).

## Detailed Explanation

### ASCII Diagram: Coins with Caps and Penalties

```
Coins with caps and penalties:

┌──────┬──────┬──────────┬──────────────┐
│ Type │ Denom│   Cap    │   Penalty    │
├──────┼──────┼──────────┼──────────────┤
│  1   │   1  │     5    │  2 (if >2)   │
│  2   │   5  │    10    │  3 (if >5)   │
│  3   │  10  │    20    │  5 (if >10)  │
└──────┴──────┴──────────┴──────────────┘

Penalty Threshold = floor(Cap/2)

Example: Target = 26
Possible combinations (showing cost calculation):

Option A: 1×10 + 3×5 + 1×1
  - Type 3: 1 coin (≤10, no penalty) → cost: 1
  - Type 2: 3 coins (≤5, no penalty) → cost: 3
  - Type 1: 1 coin (≤2, no penalty) → cost: 1
  Total cost: 5 coins

Option B: 2×10 + 1×5 + 1×1
  - Type 3: 2 coins (≤10, no penalty) → cost: 2
  - Type 2: 1 coin (≤5, no penalty) → cost: 1
  - Type 1: 1 coin (≤2, no penalty) → cost: 1
  Total cost: 4 coins ✓ Better!
```

### Cost function per coin type

Suppose you decide to use `x` coins of type `i`.

- Denomination contribution: `x * d[i]`
- Base coin cost: `x`
- Penalty rule:
  - let `t = floor(c[i]/2)`
  - penalty is `0` if `x <= t`
  - penalty is `p[i]` if `x >= t+1`

So:

`cost_i(x) = x + (x > t ? p[i] : 0)`

This is a “linear cost” with a one-time jump at `t+1`.

### DP state (standard knapsack style)

Let:

`dp[s] = minimum cost to form sum s using the first few coin types`

Initialize:

- `dp[0] = 0` (use no coins to make sum 0)
- `dp[s] = INF` for `s > 0`

We process coin types one by one and update dp.

## Naive Approach (and why it’s risky)

### Intuition

For each type, try all possible counts `x` and update dp.

### Algorithm

For each coin type `i`:

1. Create `newDp` filled with `INF`.
2. For every sum `s`:
   - if `dp[s]` is reachable:
     - try taking `x = 0..cap` coins of this type
     - update `newDp[s + x*d[i]] = min(newDp[...], dp[s] + cost_i(x))`
3. Replace `dp = newDp`.

Where `cap = min(c[i], target / d[i])`.

### Time Complexity

Worst case:

- `k = 50`
- `target = 5000`
- `d[i] = 1` and `cap = 5000`

Then the triple loop is around:

`O(k * target * cap) = 50 * 5000 * 5000 = 1.25e9` updates

That is not “maybe slow”. That is dead on arrival in most languages.

### Space Complexity

- `O(target)`

### Why This Works (Correctness)

It considers all valid choices for each type and takes the minimum.

### Limitations

- Time is too high in worst-case constraints.

## Optimal Approach (O(k · target)) Using Monotonic Queue Optimization

### Key Insight

For a fixed denomination `d`, sums can be grouped by the same remainder modulo `d`.

Example with `d=3`:

- remainder 0: 0, 3, 6, 9, ...
- remainder 1: 1, 4, 7, 10, ...
- remainder 2: 2, 5, 8, 11, ...

Within one remainder group, the DP transition becomes a 1D problem where every step moves by `d`.

### Rewrite DP transition within a remainder class

Fix a coin type with:

- denomination `d`
- effective cap `cap = min(c, target/d)` (in coins)
- threshold `t = min(floor(c/2), cap)`
- penalty `p`

For a fixed remainder `r` (0..d-1), define:

- `sum = r + q*d` where `q` is the “index” in that remainder class
- `prev[q] = dp[r + q*d]`
- `next[q] = newDp[r + q*d]`

Now if you use `x` coins of this type:

`next[q] = min(prev[q-x] + x + penalty(x))` over all `x` allowed.

Where:

- `0 <= x <= cap`
- penalty(x) = 0 if x <= t else p

Let `y = q - x` ⇒ `x = q - y`:

`next[q] = min(prev[y] + (q - y) + penalty(q - y))`

Rearrange:

`next[q] = q + min( prev[y] - y + penalty(q - y) )`

Now the only hard part is penalty(q-y), but it has only two cases:

#### Case A: No penalty (x <= t)

x = q - y <= t  ⇒  y >= q - t

Also x <= cap ⇒ y >= q - cap.

So:

`y` is in `[q - min(cap, t), q]`.

Let `L1 = min(cap, t)`.

Then:

`bestNoPen[q] = min_{y in [q-L1, q]} (prev[y] - y)`

and candidate:

`candNoPen = q + bestNoPen[q]`

#### Case B: Penalty active (x >= t+1)

x = q - y >= t+1  ⇒  y <= q - (t+1)

Also x <= cap ⇒ y >= q - cap.

So:

`y` is in `[q - cap, q - (t+1)]` (only if `cap > t`).

This interval length is constant (`cap - t`) as q slides.

`bestPen[q] = min_{y in [q-cap, q-(t+1)]} (prev[y] - y)`

and candidate:

`candPen = q + p + bestPen[q]`

### Sliding minimum = Monotonic deque

Both `bestNoPen[q]` and `bestPen[q]` are “min over a sliding window” of the sequence:

`value[y] = prev[y] - y`

We can maintain the minimum of a sliding window in O(1) amortized per step using a deque (monotonic queue).

So for each remainder class, we compute all `next[q]` in O(number of q values).

Across all remainders, total states are `target+1`, so per coin type we do O(target) work.

### Final complexity

- Time: `O(k * target)` which is at most `50 * 5000 = 250000` (plus small constants)
- Space: `O(target)`

This is the level of optimization that matches the constraints without hand-waving.

### Decision Tree for Coin Selection

```
For each coin type i (denom=d, cap=c, penalty=p):
    │
    ├─ Process all sums in remainder classes (r = 0..d-1)
    │   │
    │   └─ For each sum s = r + q*d:
    │       │
    │       ├─ Can we use x coins of this type to reach s?
    │       │   │
    │       │   ├─ YES: Calculate cost based on x
    │       │   │   │
    │       │   │   ├─ Is x <= threshold (floor(c/2))?
    │       │   │   │   │
    │       │   │   │   ├─ YES: cost = prev_cost + x
    │       │   │   │   │        (no penalty applied)
    │       │   │   │   │
    │       │   │   │   └─ NO:  cost = prev_cost + x + p
    │       │   │   │            (penalty applies)
    │       │   │   │
    │       │   │   └─ Update dp[s] = min(dp[s], cost)
    │       │   │
    │       │   └─ NO: Skip this combination
    │       │
    │       └─ Use monotonic deque to optimize:
    │           - Track minimum (prev[y] - y) in sliding window
    │           - Maintain two deques: one for no-penalty, one for penalty
    │           - Each deque handles a different range of coin counts
```

![Algorithm Visualization](../images/DP-002/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long INF = Long.MAX_VALUE / 4;

    private static long key(long dpVal, int y) {
        return dpVal - (long) y;
    }

    public long minCost(int k, int target, int[] d, long[] c, long[] p) {
        long[] dp = new long[target + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int i = 0; i < k; i++) {
            int denom = d[i];
            int cap = (int) Math.min(c[i], target / (long) denom);
            long thresholdRaw = c[i] / 2L;
            int t = (int) Math.min(thresholdRaw, (long) cap);
            long penalty = p[i];

            long[] next = new long[target + 1];
            Arrays.fill(next, INF);

            for (int r = 0; r < denom; r++) {
                int qMax = (target - r) / denom;
                if (qMax < 0) continue;

                int L1 = Math.min(cap, t); // no-pen window length in q-space

                ArrayDeque<Integer> dqNoPen = new ArrayDeque<>();
                ArrayDeque<Integer> dqPen = new ArrayDeque<>();

                for (int q = 0; q <= qMax; q++) {
                    int sumY = r + q * denom;
                    long dpVal = dp[sumY];
                    if (dpVal < INF) {
                        long kVal = key(dpVal, q);
                        while (!dqNoPen.isEmpty()) {
                            int last = dqNoPen.peekLast();
                            long lastVal = key(dp[r + last * denom], last);
                            if (kVal <= lastVal) dqNoPen.pollLast();
                            else break;
                        }
                        dqNoPen.addLast(q);
                    }

                    int minYNoPen = q - L1;
                    while (!dqNoPen.isEmpty() && dqNoPen.peekFirst() < minYNoPen) dqNoPen.pollFirst();

                    long best = INF;
                    if (!dqNoPen.isEmpty()) {
                        int y = dqNoPen.peekFirst();
                        long base = key(dp[r + y * denom], y);
                        best = Math.min(best, (long) q + base);
                    }

                    if (cap > t) {
                        int yAdd = q - (t + 1);
                        if (yAdd >= 0) {
                            int sumAdd = r + yAdd * denom;
                            long dpAdd = dp[sumAdd];
                            if (dpAdd < INF) {
                                long kVal = key(dpAdd, yAdd);
                                while (!dqPen.isEmpty()) {
                                    int last = dqPen.peekLast();
                                    long lastVal = key(dp[r + last * denom], last);
                                    if (kVal <= lastVal) dqPen.pollLast();
                                    else break;
                                }
                                dqPen.addLast(yAdd);
                            }
                        }

                        int minYPen = q - cap;
                        while (!dqPen.isEmpty() && dqPen.peekFirst() < minYPen) dqPen.pollFirst();

                        if (!dqPen.isEmpty()) {
                            int y = dqPen.peekFirst();
                            long base = key(dp[r + y * denom], y);
                            best = Math.min(best, (long) q + penalty + base);
                        }
                    }

                    int sum = r + q * denom;
                    if (best < next[sum]) next[sum] = best;
                }
            }

            dp = next;
        }

        return dp[target] >= INF ? -1 : dp[target];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int target = sc.nextInt();
        int[] d = new int[k];
        long[] c = new long[k];
        long[] p = new long[k];
        for (int i = 0; i < k; i++) {
            d[i] = sc.nextInt();
            c[i] = sc.nextLong();
            p[i] = sc.nextLong();
        }
        System.out.println(new Solution().minCost(k, target, d, c, p));
        sc.close();
    }
}
```

### Python

```python
from collections import deque

INF = 10**30

def min_cost(k: int, target: int, d: list[int], c: list[int], p: list[int]) -> int:
    dp = [INF] * (target + 1)
    dp[0] = 0

    for i in range(k):
        denom = d[i]
        cap = min(c[i], target // denom)
        t = min(c[i] // 2, cap)
        penalty = p[i]

        nxt = [INF] * (target + 1)

        for r in range(denom):
            qmax = (target - r) // denom
            if qmax < 0:
                continue

            L1 = min(cap, t)
            dq_no = deque()
            dq_pen = deque()

            def key(sum_idx: int, q: int) -> int:
                return dp[sum_idx] - q

            for q in range(qmax + 1):
                s_q = r + q * denom

                # push into no-pen deque (window [q-L1, q])
                if dp[s_q] < INF:
                    kv = dp[s_q] - q
                    while dq_no and kv <= key(r + dq_no[-1] * denom, dq_no[-1]):
                        dq_no.pop()
                    dq_no.append(q)

                min_y = q - L1
                while dq_no and dq_no[0] < min_y:
                    dq_no.popleft()

                best = INF
                if dq_no:
                    y = dq_no[0]
                    best = min(best, q + key(r + y * denom, y))

                # penalty deque (window [q-cap, q-(t+1)])
                if cap > t:
                    y_add = q - (t + 1)
                    if y_add >= 0:
                        s_add = r + y_add * denom
                        if dp[s_add] < INF:
                            kv = dp[s_add] - y_add
                            while dq_pen and kv <= key(r + dq_pen[-1] * denom, dq_pen[-1]):
                                dq_pen.pop()
                            dq_pen.append(y_add)

                    min_y_pen = q - cap
                    while dq_pen and dq_pen[0] < min_y_pen:
                        dq_pen.popleft()

                    if dq_pen:
                        y = dq_pen[0]
                        best = min(best, q + penalty + key(r + y * denom, y))

                s = r + q * denom
                nxt[s] = min(nxt[s], best)

        dp = nxt

    return -1 if dp[target] >= INF else dp[target]


def main():
    k, target = map(int, input().split())
    d, c, p = [], [], []
    for _ in range(k):
        di, ci, pi = map(int, input().split())
        d.append(di); c.append(ci); p.append(pi)
    print(min_cost(k, target, d, c, p))


if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    static constexpr long long INF = (1LL<<62);
public:
    long long minCost(int k, int target, const vector<int>& d,
                      const vector<long long>& c, const vector<long long>& p) {
        vector<long long> dp(target + 1, INF);
        dp[0] = 0;

        for (int i = 0; i < k; i++) {
            int denom = d[i];
            int cap = (int)min<long long>(c[i], target / (long long)denom);
            int t = (int)min<long long>(c[i] / 2LL, cap);
            long long penalty = p[i];

            vector<long long> nxt(target + 1, INF);

            for (int r = 0; r < denom; r++) {
                int qMax = (target - r) / denom;
                if (qMax < 0) continue;

                int L1 = min(cap, t);
                deque<int> dqNo, dqPen;

                auto key = [&](int q) -> long long {
                    long long val = dp[r + q * denom];
                    return val - (long long)q;
                };

                for (int q = 0; q <= qMax; q++) {
                    int sQ = r + q * denom;

                    if (dp[sQ] < INF) {
                        long long kv = key(q);
                        while (!dqNo.empty() && kv <= key(dqNo.back())) dqNo.pop_back();
                        dqNo.push_back(q);
                    }

                    int minY = q - L1;
                    while (!dqNo.empty() && dqNo.front() < minY) dqNo.pop_front();

                    long long best = INF;
                    if (!dqNo.empty()) best = min(best, (long long)q + key(dqNo.front()));

                    if (cap > t) {
                        int yAdd = q - (t + 1);
                        if (yAdd >= 0) {
                            int sAdd = r + yAdd * denom;
                            if (dp[sAdd] < INF) {
                                long long kv = key(yAdd);
                                while (!dqPen.empty() && kv <= key(dqPen.back())) dqPen.pop_back();
                                dqPen.push_back(yAdd);
                            }
                        }

                        int minYPen = q - cap;
                        while (!dqPen.empty() && dqPen.front() < minYPen) dqPen.pop_front();

                        if (!dqPen.empty()) best = min(best, (long long)q + penalty + key(dqPen.front()));
                    }

                    int s = r + q * denom;
                    nxt[s] = min(nxt[s], best);
                }
            }

            dp.swap(nxt);
        }

        return dp[target] >= INF ? -1 : dp[target];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, target;
    cin >> k >> target;
    vector<int> d(k);
    vector<long long> c(k), p(k);
    for (int i = 0; i < k; i++) cin >> d[i] >> c[i] >> p[i];

    Solution sol;
    cout << sol.minCost(k, target, d, c, p) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

const INF = 10n ** 30n;

class Deque {
  constructor() {
    this.a = [];
    this.h = 0;
  }
  pushBack(x) { this.a.push(x); }
  popBack() { this.a.pop(); }
  popFront() { this.h++; }
  front() { return this.a[this.h]; }
  back() { return this.a[this.a.length - 1]; }
  empty() { return this.h >= this.a.length; }
  cleanup() {
    if (this.h > 1024 && this.h * 2 > this.a.length) {
      this.a = this.a.slice(this.h);
      this.h = 0;
    }
  }
}

class Solution {
  minCost(k, target, d, c, p) {
    let dp = new Array(target + 1).fill(INF);
    dp[0] = 0n;

    for (let i = 0; i < k; i++) {
      const denom = d[i];
      const cap = Math.min(c[i], Math.floor(target / denom));
      const t = Math.min(Math.floor(c[i] / 2), cap);
      const penalty = BigInt(p[i]);

      const nxt = new Array(target + 1).fill(INF);

      for (let r = 0; r < denom; r++) {
        const qMax = Math.floor((target - r) / denom);
        if (qMax < 0) continue;

        const L1 = Math.min(cap, t);
        const dqNo = new Deque();
        const dqPen = new Deque();

        const key = (q) => {
          const s = r + q * denom;
          return dp[s] - BigInt(q);
        };

        for (let q = 0; q <= qMax; q++) {
          const sQ = r + q * denom;

          if (dp[sQ] < INF) {
            const kv = key(q);
            while (!dqNo.empty() && kv <= key(dqNo.back())) dqNo.popBack();
            dqNo.pushBack(q);
          }

          const minY = q - L1;
          while (!dqNo.empty() && dqNo.front() < minY) dqNo.popFront();
          dqNo.cleanup();

          let best = INF;
          if (!dqNo.empty()) {
            best = BigInt(q) + key(dqNo.front());
          }

          if (cap > t) {
            const yAdd = q - (t + 1);
            if (yAdd >= 0) {
              const sAdd = r + yAdd * denom;
              if (dp[sAdd] < INF) {
                const kv = key(yAdd);
                while (!dqPen.empty() && kv <= key(dqPen.back())) dqPen.popBack();
                dqPen.pushBack(yAdd);
              }
            }

            const minYPen = q - cap;
            while (!dqPen.empty() && dqPen.front() < minYPen) dqPen.popFront();
            dqPen.cleanup();

            if (!dqPen.empty()) {
              const cand = BigInt(q) + penalty + key(dqPen.front());
              if (cand < best) best = cand;
            }
          }

          const s = r + q * denom;
          if (best < nxt[s]) nxt[s] = best;
        }
      }

      dp = nxt;
    }

    return dp[target] >= INF ? -1 : dp[target].toString();
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [kStr, targetStr] = lines[idx++].split(" ");
  const k = Number(kStr);
  const target = Number(targetStr);
  const d = new Array(k), c = new Array(k), p = new Array(k);
  for (let i = 0; i < k; i++) {
    const [di, ci, pi] = lines[idx++].split(" ").map(Number);
    d[i] = di; c[i] = ci; p[i] = pi;
  }
  const sol = new Solution();
  console.log(sol.minCost(k, target, d, c, p));
});
```

## 🧪 Test Case Walkthrough

Sample:

```
k=2, target=7
(d,c,p):
1 4 2
5 2 1
```

Thresholds:

- For denom 1: `t=floor(4/2)=2`, penalty `2` triggers if we use 3 or 4 ones.
- For denom 5: `t=floor(2/2)=1`, penalty `1` triggers only if we use 2 fives.

### State Evolution Table

| Amount | Min Cost | Coin Selection | Breakdown |
|--------|----------|----------------|-----------|
| 0 | 0 | none | base case |
| 1 | 1 | 1×(denom=1) | 1 coin, no penalty |
| 2 | 2 | 2×(denom=1) | 2 coins, no penalty |
| 3 | 3 | 3×(denom=1) | 3 coins + penalty(2) = 5 OR just 3 |
| 4 | 4 | 4×(denom=1) | 4 coins + penalty(2) = 6 OR just 4 |
| 5 | 1 | 1×(denom=5) | 1 coin, no penalty (better than 5×denom1) |
| 6 | 2 | 1×(denom=5) + 1×(denom=1) | 2 coins, no penalty |
| 7 | 3 | 1×(denom=5) + 2×(denom=1) | 3 coins, no penalty ✓ |

To make 7, the sensible candidates are:

- `5 + 1 + 1`:
  - ones used=2 (no penalty)
  - fives used=1 (no penalty)
  - total cost = 3 ✅
- `1+1+1+1+1+1+1`:
  - ones used=7, but cap is 4 so invalid

So minimum cost is 3.

![Example Visualization](../images/DP-002/example-1.png)

## ✅ Proof Sketch (Why the deque optimization is correct)

For each remainder class, the transition reduces to taking a minimum of the form:

`next[q] = q + min(value[y])` over a sliding window of valid `y` indices, where `value[y] = prev[y] - y`.

Since the window moves by 1 each step and `value[y]` depends only on `y`, a monotonic deque maintains the window minimum correctly in O(1) amortized time. We compute two such minima (no-penalty window and penalty window) and take the smaller candidate.

## Common Mistakes to Avoid

1. **Misunderstanding the penalty condition**

   - Penalty triggers on `used_i > floor(c[i]/2)`, not `>=`.
   - Example: if `c=4`, then `floor(c/2)=2`:
     - using 2 coins: no penalty
     - using 3 coins: penalty applies

2. **Ignoring “effective cap”**

   - If `c[i]` is huge, you still can’t use more than `target / d[i]`.
   - ✅ Always set `cap = min(c[i], target/d[i])`.

3. **Triple-loop DP that times out**

   - `k=50`, `target=5000`, `d=1` is the stress case.
   - ✅ Use the modulo-class + deque optimization to get O(k·target).

4. **Using 32-bit integers for cost**

   - Costs can exceed 2^31.
   - ✅ Use `long` / `long long`.


## Related Concepts

- Bounded knapsack optimization (monotonic queue by remainder classes)
- DP with activation costs / step costs
- Min-plus convolution intuition
- Sliding window minimum (monotonic deque)
