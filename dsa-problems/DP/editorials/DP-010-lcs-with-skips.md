---
problem_id: DP_LCS_SKIP_BUDGET__2297
display_id: DP-010
slug: lcs-with-skips
title: "LCS With Limited Skips in A"
difficulty: Medium
difficulty_score: 55
topics:
  - Dynamic Programming
  - Strings
  - Subsequence
tags:
  - dp
  - lcs
  - strings
  - medium
premium: true
subscription_tier: basic
---

# DP-010: LCS With Limited Skips in A

## 📋 Problem Summary

Find the length of the longest common subsequence of strings `a` and `b` **under the constraint** that you delete (skip) **at most `s` characters from `a`**. Deletions from `b` are unlimited (as in normal subsequence matching).

If no common subsequence fits within the skip budget (`a` would need more than `s` deletions), return `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** API Compatibility With Limited Code Removal

Suppose `a` is an old API, `b` is a new API, and you want to keep as much of `a` as possible while matching `b`. You are allowed to remove at most `s` legacy endpoints from `a`. Removing more breaks compatibility. You can, however, ignore any endpoints in `b` (those not needed).

This is exactly “LCS with a budget on deletions from `a`”.

**Why This Problem Matters:**

- Teaches how to layer a constraint onto a classic DP (LCS)
- Reinforces interpreting DP results to enforce budgets
- Shows a simple reduction: budget on deletions from one string becomes a check on LCS length

![Real-World Application](../images/DP-010/real-world-scenario.png)

## ✅ Clarifications

- Skips (deletions) from `a` are **limited** to `s`.
- Skips from `b` are unlimited (standard subsequence notion).
- Answer `-1` means: even the maximum LCS would require more than `s` deletions from `a`.
- Empty strings are allowed.

## Detailed Explanation

### Relationship between LCS length and deletions from `a`

If the LCS length is `L`, then to form that subsequence from `a` you must delete exactly `|a| - L` characters from `a`.

Constraint: `|a| - L <= s` ⇔ `L >= |a| - s`

So the problem reduces to:

1. Compute the standard LCS length `L`.
2. If `L >= |a| - s`, it fits in the budget ⇒ answer is `L`.
3. Otherwise, no common subsequence can satisfy the budget ⇒ answer `-1`.

### Why smaller subsequences don’t help

If `L` (the maximum possible) already violates the budget, any shorter common subsequence would delete **more** from `a` (since deletions = `|a| - length`). So shorter lengths cannot satisfy the constraint. That’s why we can just compare `L` to `|a|-s`.

### LCS DP refresher (O(n·m))

`dp[i][j] = LCS length of prefixes a[0..i-1], b[0..j-1]`

Transition:

- If `a[i-1] == b[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`
- Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

Space optimization:

- Only previous row is needed ⇒ O(m) memory.

![Algorithm Visualization](../images/DP-010/algorithm-visualization.png)
![Algorithm Steps](../images/DP-010/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int lcsWithSkipLimit(String a, String b, int s) {
        int n = a.length(), m = b.length();
        int[] prev = new int[m + 1];
        int[] cur = new int[m + 1];

        for (int i = 1; i <= n; i++) {
            char ca = a.charAt(i - 1);
            cur[0] = 0;
            for (int j = 1; j <= m; j++) {
                if (ca == b.charAt(j - 1)) {
                    cur[j] = prev[j - 1] + 1;
                } else {
                    cur[j] = Math.max(prev[j], cur[j - 1]);
                }
            }
            int[] tmp = prev; prev = cur; cur = tmp;
        }

        int L = prev[m];
        return (n - L <= s) ? L : -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine().trim();
        String b = sc.nextLine().trim();
        int s = sc.nextInt();
        System.out.println(new Solution().lcsWithSkipLimit(a, b, s));
        sc.close();
    }
}
```

### Python
```python
def lcs_with_skip_limit(a: str, b: str, s: int) -> int:
    n, m = len(a), len(b)
    prev = [0] * (m + 1)
    cur = [0] * (m + 1)

    for i in range(1, n + 1):
        cur[0] = 0
        ai = a[i - 1]
        for j in range(1, m + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev, cur = cur, prev

    L = prev[m]
    return L if n - L <= s else -1


def main():
    a = input().strip()
    b = input().strip()
    s = int(input())
    print(lcs_with_skip_limit(a, b, s))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <cmath>
#include <cstring>
#include <utility>
using namespace std;

class Solution {
public:
    int lcsWithSkipLimit(const string& a, const string& b, int s) {
        int n = (int)a.size(), m = (int)b.size();
        vector<int> prev(m + 1, 0), cur(m + 1, 0);

        for (int i = 1; i <= n; i++) {
            cur[0] = 0;
            char ai = a[i - 1];
            for (int j = 1; j <= m; j++) {
                if (ai == b[j - 1]) cur[j] = prev[j - 1] + 1;
                else cur[j] = max(prev[j], cur[j - 1]);
            }
            prev.swap(cur);
        }

        int L = prev[m];
        return (n - L <= s) ? L : -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    getline(cin, a);
    getline(cin, b);
    int s;
    cin >> s;
    Solution sol;
    cout << sol.lcsWithSkipLimit(a, b, s) << '\n';
    return 0;
}
```

### JavaScript
```javascript
class Solution {
  lcsWithSkipLimit(a, b, s) {
    const n = a.length,
      m = b.length;
    let prev = new Array(m + 1).fill(0);
    let cur = new Array(m + 1).fill(0);

    for (let i = 1; i <= n; i++) {
      cur[0] = 0;
      const ai = a[i - 1];
      for (let j = 1; j <= m; j++) {
        if (ai === b[j - 1]) cur[j] = prev[j - 1] + 1;
        else cur[j] = Math.max(prev[j], cur[j - 1]);
      }
      const tmp = prev;
      prev = cur;
      cur = tmp;
    }

    const L = prev[m];
    return n - L <= s ? L : -1;
  }
}

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  let ptr = 0;
  const a = data[ptr++];
  const b = data[ptr++];
  const s = Number(data[ptr++]);

  const solution = new Solution();
  console.log(solution.lcsWithSkipLimit(a, b, s));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
Example:

`a = "abcde"`, `b = "ace"`, `s = 2`

- LCS length = 3 (`"ace"`)
- deletions from `a` = `5 - 3 = 2` ≤ `s`
- answer = 3

If `s = 1`, deletions needed (2) exceed budget ⇒ answer = -1.

![Example Visualization](../images/DP-010/example-1.png)

## ✅ Proof of Correctness

Let `L` be the LCS length between `a` and `b`. Any common subsequence of length `L'` requires deleting exactly `|a| - L'` characters from `a`.

Since `L` is the maximum achievable length, if `|a| - L > s`, then every common subsequence requires more than `s` deletions (because all shorter subsequences have `|a| - L' >= |a| - L`). Hence no feasible solution exists ⇒ return -1.

If `|a| - L <= s`, then the optimal feasible length is `L` itself.

Therefore, computing LCS and checking the deletion budget is sufficient and correct.

### Common Mistakes to Avoid

1. **Forgetting the budget check** (`n - L <= s`)
2. **Returning LCS unconditionally** (violates skip limit when `s` is small)
3. **Off-by-one in LCS DP indices**
4. **Not handling empty strings** (LCS = 0; deletions = |a|)

## Related Concepts

- LCS and edit-distance relationships
- DP space optimization
- Constraint checking on top of DP results
