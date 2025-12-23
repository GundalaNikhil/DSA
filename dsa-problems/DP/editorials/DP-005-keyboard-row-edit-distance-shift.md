---
problem_id: DP_KB_EDIT_SHIFT__3179
display_id: DP-005
slug: keyboard-row-edit-distance-shift
title: "Keyboard Row Edit Distance with Shift Penalty"
difficulty: Medium
difficulty_score: 60
topics:
  - Dynamic Programming
  - String DP
  - Edit Distance
tags:
  - dp
  - strings
  - edit-distance
  - medium
premium: true
subscription_tier: basic
---

# DP-005: Keyboard Row Edit Distance with Shift Penalty

## 📋 Problem Summary

Convert string `a` to string `b` with operations:

- insert (cost 1)
- delete (cost 1)
- replace (cost depends on keyboard row/hand; 0 if same character)

This is a weighted version of Levenshtein edit distance. You must compute the minimum total cost for strings up to length 2000.

## 🌍 Real-World Scenario

**Scenario Title:** Auto-correct With Typing Effort Model

In real keyboards, some typos are “cheap” to fix and some are “expensive”:

- Mistyping within the same row is common (fingers hover near those keys).
- Mistyping across rows but with the same hand is still plausible.
- Mistyping across hands is less likely and often a bigger correction.

If you are building a smart correction system for a college typing tutor app:

- you don’t want a plain edit distance
- you want a distance that models “effort” (or likelihood) using keyboard geometry

This problem is exactly that: compute the minimum effort to transform one string to another.

**Why This Problem Matters:**

- Core interview DP: edit distance
- Reinforces recurrence design and boundary conditions
- Teaches rolling array optimization for `2000 x 2000`

![Real-World Application](../images/DP-005/real-world-scenario.png)

## ✅ Definitions (Fixed for this problem)

Keyboard rows:

- Row 1: `qwertyuiop`
- Row 2: `asdfghjkl`
- Row 3: `zxcvbnm`

Hands:

- Left hand: `qwertasdfgzxcvb`
- Right hand: `yuiophjklnm`

Replacement cost for characters `x -> y`:

- 0 if `x == y`
- 1 if same row
- 2 if different row but same hand
- 3 otherwise

Insert / delete cost = 1.

## Detailed Explanation

### Keyboard Layout and Cost Visualization

```
Keyboard Layout (QWERTY):
Row 1: Q W E R T Y U I O P
Row 2: A S D F G H J K L
Row 3: Z X C V B N M

Hand Assignment:
Left:  Q W E R T A S D F G Z X C V B
Right: Y U I O P H J K L N M

Cost Matrix Examples:
  Q to W: cost 1 (same row)
  Q to A: cost 2 (left hand, different row)
  Q to Z: cost 2 (left hand, different row)
  Q to P: cost 3 (different hand, different row)
  A to S: cost 1 (same row)
  T to G: cost 2 (left hand, Row 1 to Row 2)
  H to Y: cost 2 (right hand, Row 2 to Row 1)
```

### Classic edit distance DP state

Let:

`dp[i][j] = minimum cost to convert a[0..i-1] into b[0..j-1]`

So:

- `dp[0][0] = 0`
- `dp[i][0] = i` (delete all i chars)
- `dp[0][j] = j` (insert all j chars)

### Transition

To compute `dp[i][j]`, consider the last operation:

1) Delete last char of `a`:

`dp[i][j] = dp[i-1][j] + 1`

2) Insert last char of `b`:

`dp[i][j] = dp[i][j-1] + 1`

3) Replace / match:

`dp[i][j] = dp[i-1][j-1] + costReplace(a[i-1], b[j-1])`

Take minimum of the three.

This is identical to Levenshtein distance, except replacement cost is not 0/1—it's weighted.

### Decision Tree for Edit Operations

```
To transform a[0..i] to b[0..j]:
    │
    ├─ a[i] == b[j]?
    │   ├─ YES: dp[i][j] = dp[i-1][j-1] (cost = 0)
    │   └─ NO:  Try three operations:
    │       ├─ Replace: dp[i-1][j-1] + cost(a[i], b[j])
    │       │   └─ cost = 1 (same row)
    │       │       or 2 (different row, same hand)
    │       │       or 3 (different row, different hand)
    │       │
    │       ├─ Delete a[i]: dp[i-1][j] + 1
    │       │
    │       └─ Insert b[j]: dp[i][j-1] + 1
    │
    │           → dp[i][j] = min(Replace, Delete, Insert)
```

## Naive Approach (What students try first)

### Intuition

Try recursion:

- at each position, branch into insert/delete/replace

### Why it fails

- exponential states due to branching
- recomputation of the same suffix pairs

So we use DP.

## Optimal Approach (DP with Rolling Array)

### Key Insight

The recurrence depends only on:

- previous row (`dp[i-1][*]`)
- current row so far (`dp[i][j-1]`)

So we don’t need the full `2001 x 2001` table.

We can keep two rows:

- `prev[j] = dp[i-1][j]`
- `cur[j] = dp[i][j]`

This reduces memory to `O(m)` where `m = len(b)`.

### Complexity

- Time: `O(n*m)` ≤ `4,000,000` operations (fine)
- Space: `O(m)`

![Algorithm Visualization](../images/DP-005/algorithm-visualization.png)
![Algorithm Steps](../images/DP-005/algorithm-steps.png)

## 🔎 Replacement Cost Examples (Be Precise)

With the fixed mapping:

- Same row examples (cost 1):
  - `q -> w` (Row 1)
  - `a -> s` (Row 2)
  - `z -> x` (Row 3)

- Different rows, same hand (cost 2):
  - `t -> g` (left hand, Row 1 to Row 2)
  - `h -> y` (right hand, Row 2 to Row 1)

- Different rows, different hands (cost 3):
  - `q -> p` (Row 1 but different hands)
  - `a -> l` (Row 2 but different hands)

If you mix up the hand split, your answers will be systematically wrong.

## 📊 Complexity Comparison (Interview-ready)

| Approach | Time | Space | Notes |
|---------|------|-------|------|
| Pure recursion | exponential | `O(n+m)` | TLE |
| Full DP table | `O(n·m)` | `O(n·m)` | OK but memory-heavy |
| Rolling rows (this) | `O(n·m)` | `O(m)` | Best for constraints |

With `n,m <= 2000`, `n·m = 4e6`, which is practical.

## 🧪 Extra Example (Empty String)

If:

- `a = ""`
- `b = "abc"`

Then you must insert 3 characters, cost = 3.

Similarly, converting `"abc" -> ""` costs 3 deletions.

These are important edge cases: they also validate your DP initialization (`dp[0][j] = j`, `dp[i][0] = i`).

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final String ROW1 = "qwertyuiop";
    private static final String ROW2 = "asdfghjkl";
    private static final String ROW3 = "zxcvbnm";
    private static final String LEFT = "qwertasdfgzxcvb";

    private static int row(char c) {
        if (ROW1.indexOf(c) >= 0) return 1;
        if (ROW2.indexOf(c) >= 0) return 2;
        return 3;
    }

    private static int hand(char c) {
        return LEFT.indexOf(c) >= 0 ? 0 : 1;
    }

    private static int replaceCost(char x, char y) {
        if (x == y) return 0;
        int rx = row(x), ry = row(y);
        if (rx == ry) return 1;
        return hand(x) == hand(y) ? 2 : 3;
    }

    public int minKeyboardEditCost(String a, String b) {
        int n = a.length(), m = b.length();
        int[] prev = new int[m + 1];
        int[] cur = new int[m + 1];

        for (int j = 0; j <= m; j++) prev[j] = j;

        for (int i = 1; i <= n; i++) {
            cur[0] = i;
            char ca = a.charAt(i - 1);
            for (int j = 1; j <= m; j++) {
                char cb = b.charAt(j - 1);
                int del = prev[j] + 1;
                int ins = cur[j - 1] + 1;
                int rep = prev[j - 1] + replaceCost(ca, cb);
                cur[j] = Math.min(del, Math.min(ins, rep));
            }
            int[] tmp = prev; prev = cur; cur = tmp;
        }

        return prev[m];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.hasNextLine() ? sc.nextLine().trim() : "";
        String b = sc.hasNextLine() ? sc.nextLine().trim() : "";
        System.out.println(new Solution().minKeyboardEditCost(a, b));
        sc.close();
    }
}
```

### Python

```python
ROW1 = set("qwertyuiop")
ROW2 = set("asdfghjkl")
ROW3 = set("zxcvbnm")
LEFT = set("qwertasdfgzxcvb")

def row(c: str) -> int:
    if c in ROW1: return 1
    if c in ROW2: return 2
    return 3

def hand(c: str) -> int:
    return 0 if c in LEFT else 1

def rep_cost(x: str, y: str) -> int:
    if x == y: return 0
    if row(x) == row(y): return 1
    return 2 if hand(x) == hand(y) else 3

def min_keyboard_edit_cost(a: str, b: str) -> int:
    n, m = len(a), len(b)
    prev = list(range(m + 1))
    cur = [0] * (m + 1)

    for i in range(1, n + 1):
        cur[0] = i
        ca = a[i - 1]
        for j in range(1, m + 1):
            cb = b[j - 1]
            cur[j] = min(
                prev[j] + 1,               # delete
                cur[j - 1] + 1,            # insert
                prev[j - 1] + rep_cost(ca, cb)  # replace/match
            )
        prev, cur = cur, prev

    return prev[m]

def main():
    a = input().strip()
    b = input().strip()
    print(min_keyboard_edit_cost(a, b))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    string row1 = "qwertyuiop";
    string row2 = "asdfghjkl";
    string left = "qwertasdfgzxcvb";

    int row(char c) {
        if (row1.find(c) != string::npos) return 1;
        if (row2.find(c) != string::npos) return 2;
        return 3;
    }

    int hand(char c) {
        return left.find(c) != string::npos ? 0 : 1;
    }

    int repCost(char x, char y) {
        if (x == y) return 0;
        int rx = row(x), ry = row(y);
        if (rx == ry) return 1;
        return (hand(x) == hand(y)) ? 2 : 3;
    }

public:
    int minKeyboardEditCost(const string& a, const string& b) {
        int n = (int)a.size(), m = (int)b.size();
        vector<int> prev(m + 1), cur(m + 1);
        for (int j = 0; j <= m; j++) prev[j] = j;

        for (int i = 1; i <= n; i++) {
            cur[0] = i;
            char ca = a[i - 1];
            for (int j = 1; j <= m; j++) {
                char cb = b[j - 1];
                int del = prev[j] + 1;
                int ins = cur[j - 1] + 1;
                int rep = prev[j - 1] + repCost(ca, cb);
                cur[j] = min(del, min(ins, rep));
            }
            swap(prev, cur);
        }

        return prev[m];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    getline(cin, a);
    getline(cin, b);
    Solution sol;
    cout << sol.minKeyboardEditCost(a, b) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

const ROW1 = new Set("qwertyuiop".split(""));
const ROW2 = new Set("asdfghjkl".split(""));
const LEFT = new Set("qwertasdfgzxcvb".split(""));

function row(c) {
  if (ROW1.has(c)) return 1;
  if (ROW2.has(c)) return 2;
  return 3;
}

function hand(c) {
  return LEFT.has(c) ? 0 : 1;
}

function repCost(x, y) {
  if (x === y) return 0;
  if (row(x) === row(y)) return 1;
  return hand(x) === hand(y) ? 2 : 3;
}

class Solution {
  minKeyboardEditCost(a, b) {
    const n = a.length, m = b.length;
    let prev = new Array(m + 1);
    let cur = new Array(m + 1);
    for (let j = 0; j <= m; j++) prev[j] = j;

    for (let i = 1; i <= n; i++) {
      cur[0] = i;
      const ca = a[i - 1];
      for (let j = 1; j <= m; j++) {
        const cb = b[j - 1];
        const del = prev[j] + 1;
        const ins = cur[j - 1] + 1;
        const rep = prev[j - 1] + repCost(ca, cb);
        cur[j] = Math.min(del, ins, rep);
      }
      const tmp = prev; prev = cur; cur = tmp;
    }
    return prev[m];
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line));
rl.on("close", () => {
  const a = (lines[0] ?? "").trim();
  const b = (lines[1] ?? "").trim();
  const sol = new Solution();
  console.log(sol.minKeyboardEditCost(a, b));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
Sample:

`a = "type"`, `b = "tap"`

One optimal sequence (cost 3):

- Insert `a` after `t`: `type -> taype` (cost 1)
- Delete `y`: `taype -> tape` (cost 1)
- Delete `e`: `tape -> tap` (cost 1)

Total = 3.

### State Evolution Table

Building the DP table for `a = "type"` → `b = "tap"`:

| i | j | a[i] | b[j] | Operation | Cost Calc | dp[i][j] |
|---|---|------|------|-----------|-----------|----------|
| 0 | 0 | -    | -    | Base      | -         | 0        |
| 0 | 1 | -    | t    | Insert    | 0 + 1     | 1        |
| 0 | 2 | -    | a    | Insert    | 1 + 1     | 2        |
| 0 | 3 | -    | p    | Insert    | 2 + 1     | 3        |
| 1 | 0 | t    | -    | Delete    | 0 + 1     | 1        |
| 1 | 1 | t    | t    | Match     | dp[0][0] + 0 = 0 | 0 |
| 1 | 2 | t    | a    | Replace   | min(dp[0][1]+1, dp[1][1]+1, dp[0][2]+2) = 1 | 1 |
| 1 | 3 | t    | p    | Replace   | min(dp[0][2]+1, dp[1][2]+1, dp[0][3]+3) = 2 | 2 |
| 2 | 1 | y    | t    | Replace   | min(dp[1][0]+1, dp[2][0]+1, dp[1][1]+2) = 1 | 1 |
| 2 | 2 | y    | a    | Replace   | min(dp[1][1]+1, dp[2][1]+1, dp[1][2]+2) = 1 | 1 |
| 2 | 3 | y    | p    | Replace   | min(dp[1][2]+1, dp[2][2]+1, dp[1][3]+3) = 2 | 2 |
| 3 | 3 | p    | p    | Match     | dp[2][2] + 0 = 1 | 1 |
| 4 | 3 | e    | p    | Delete    | min(dp[3][3]+1, dp[4][2]+1, dp[3][2]+3) = 2 | 2 |

Final answer: dp[4][3] = 3 (or recompute with rolling array)

![Example Visualization](../images/DP-005/example-1.png)

## ✅ Proof of Correctness

The DP state `dp[i][j]` considers all ways to transform prefixes of the strings. Any optimal edit sequence must end with exactly one of:

- deleting the last char of `a[0..i-1]`
- inserting the last char of `b[0..j-1]`
- replacing/matching the last characters

The recurrence takes the minimum cost among these exhaustive last-step cases, so it produces the optimal cost.

Rolling arrays do not change correctness because each `dp[i][j]` depends only on the previous row and the current row prefix.

### Common Mistakes to Avoid

1. **Using normal Levenshtein replacement cost (0/1)**
2. **Forgetting replacement cost is 0 when characters match**
3. **Building a full 2D dp for 2000x2000 without need**
4. **Using the wrong hand/row mapping**
5. **Off-by-one in DP indices**
   - `dp[i][j]` is about prefixes: `a[0..i-1]` and `b[0..j-1]`.
   - If you use `a[i]` directly, you’ll shift everything by one.
6. **Incorrect input handling for empty lines**
   - Some testcases include empty strings, which appear as blank lines.
   - Use `getline` (C++) / `nextLine` (Java) / safe defaults (JS).

## 💡 Interview Extensions (Good Add-ons)

1. **Reconstruct the edit operations**

If asked to output the actual edit sequence, store parent pointers in a 2D table (increases memory) and backtrack.

2. **Different operation costs**

This same DP template supports:

- different insertion/deletion costs
- asymmetric replacement costs (if model is directional)

3. **Keyboard distance model**

Real keyboards can be modeled with (row, column) coordinates and replacement cost proportional to Manhattan distance. The DP stays the same; only `repCost` changes.


## Related Concepts

- String DP
- Levenshtein distance
- Weighted edit distance
- DP space optimization (rolling arrays)
