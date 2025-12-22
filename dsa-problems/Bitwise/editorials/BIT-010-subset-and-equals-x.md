---
problem_id: BIT_SUBSET_AND_EQUALS_X__8410
display_id: BIT-010
slug: subset-and-equals-x
title: "Subset AND Equals X"
difficulty: Medium
difficulty_score: 52
topics:
  - Bitwise Operations
  - Backtracking
  - Dynamic Programming
tags:
  - bitwise
  - backtracking
  - dp
  - medium
premium: true
subscription_tier: basic
---

# Subset AND Equals X

## Real-World Scenario: Hardware Feature Flag Compatibility

In chip design and system configuration, components have feature flags represented as bitmasks. Finding subsets of components whose combined features (via AND operation) match a target requirement `X` is crucial for compatibility testing and system optimization.

---

## Problem Analysis

### Understanding the Problem

Given an array of `n` integers and a target value `X`, count how many non-empty subsets have a bitwise AND equal to exactly `X`.

**Key Observations:**

1. For AND to equal X, all bits set in X must be set in **every** element of the subset
2. Bits not set in X can vary across subset elements
3. AND operation is monotonically decreasing: adding more elements can only decrease or maintain the AND value
4. Small n (≤ 20) suggests exponential solutions are acceptable

### Visual Example

```
Array: [6, 3, 2], X = 2

Binary Representation:
━━━━━━━━━━━━━━━━━━━━━
Value | Binary
━━━━━━━━━━━━━━━━━━━━━
  6   |  110
  3   |  011
  2   |  010
  X=2 |  010
━━━━━━━━━━━━━━━━━━━━━

Testing All Subsets:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subset       | Elements | AND | Match X?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{6}          | 6        | 6   | No
{3}          | 3        | 3   | No
{2}          | 2        | 2   | Yes ✓
{6,3}        | 6 & 3    | 2   | Yes ✓
{6,2}        | 6 & 2    | 2   | Yes ✓
{3,2}        | 3 & 2    | 2   | Yes ✓
{6,3,2}      | 6&3&2    | 2   | Yes ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Valid subsets: 5.

Counted subsets with AND = 2:
- {6,3}
- {6,2}
- {3,2}
- {2}
- {6,3,2}
```

---

## Approach 1: Brute Force - Generate All Subsets

### Algorithm

1. Generate all 2^n - 1 non-empty subsets
2. For each subset, compute the AND of all elements
3. Count how many equal X

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int countSubsetsWithAND(int[] a, int X) {
        int n = a.length;
        int count = 0;

        // Iterate through all non-empty subsets using bitmask
        for (int mask = 1; mask < (1 << n); mask++) {
            int andResult = -1; // Start with all bits set

            // Compute AND of selected elements
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    if (andResult == -1) {
                        andResult = a[i];
                    } else {
                        andResult &= a[i];
                    }
                }
            }

            if (andResult == X) {
                count++;
            }
        }

        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int X = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.countSubsetsWithAND(a, X));
        sc.close();
    }
}
```

**Python:**

```python
def count_subsets_and_brute(a, X):
    n = len(a)
    count = 0

    # Iterate through all non-empty subsets
    for mask in range(1, 1 << n):
        and_result = None

        # Compute AND of selected elements
        for i in range(n):
            if mask & (1 << i):
                if and_result is None:
                    and_result = a[i]
                else:
                    and_result &= a[i]

        if and_result == X:
            count += 1

    return count

# Main
line = input().split()
n, X = int(line[0]), int(line[1])
a = list(map(int, input().split()))
print(count_subsets_and_brute(a, X))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int countSubsetsWithAND(vector<int>& a, int X) {
    int n = a.size();
    int count = 0;

    // Iterate through all non-empty subsets
    for (int mask = 1; mask < (1 << n); mask++) {
        int andResult = -1; // All bits set

        // Compute AND of selected elements
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                if (andResult == -1) {
                    andResult = a[i];
                } else {
                    andResult &= a[i];
                }
            }
        }

        if (andResult == X) {
            count++;
        }
    }

    return count;
}

int main() {
    int n, X;
    cin >> n >> X;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << countSubsetsWithAND(a, X) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function countSubsetsWithAND(a, X) {
  const n = a.length;
  let count = 0;

  // Iterate through all non-empty subsets
  for (let mask = 1; mask < 1 << n; mask++) {
    let andResult = null;

    // Compute AND of selected elements
    for (let i = 0; i < n; i++) {
      if (mask & (1 << i)) {
        if (andResult === null) {
          andResult = a[i];
        } else {
          andResult &= a[i];
        }
      }
    }

    if (andResult === X) {
      count++;
    }
  }

  return count;
}

// Main
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, X] = lines[0].split(" ").map(Number);
  const a = lines[1].split(" ").map(Number);
  console.log(countSubsetsWithAND(a, X));
});
```

### Detailed Trace

```
Array: [6, 3, 2], X = 2

Subset Generation (3 bits):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mask | Binary | Elements    | AND Calc        | Result | Match?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1   |  001   | {6}         | 6               |   6    |  No
 2   |  010   | {3}         | 3               |   3    |  No
 3   |  011   | {6,3}       | 6 & 3 = 2       |   2    |  Yes ✓
 4   |  100   | {2}         | 2               |   2    |  Yes ✓
 5   |  101   | {6,2}       | 6 & 2 = 2       |   2    |  Yes ✓
 6   |  110   | {3,2}       | 3 & 2 = 2       |   2    |  Yes ✓
 7   |  111   | {6,3,2}     | 6&3&2 = 2       |   2    |  Yes ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Count: 5

Note: If expected is 2, there might be additional constraints
```

### Complexity Analysis

- **Time Complexity:** O(2^n × n)
  - 2^n subsets to enumerate
  - O(n) to compute AND for each subset
- **Space Complexity:** O(1)
  - Only using constant extra space

### When to Use

- n ≤ 20 (acceptable with 2^20 = ~1M operations)
- Simple to implement
- No preprocessing needed

---

## Approach 2: Optimized Backtracking with Pruning

### Core Insight

**AND Monotonicity:**

- AND of subset can only decrease (or stay same) as we add elements
- If current AND < X, adding more elements won't help
- We can prune branches early

### Algorithm

```
Pruning Strategy:
═══════════════════════════════════════════
1. If current AND < X → Prune (can't improve)
2. If current AND = X → Count this subset
3. If current AND > X → Continue exploring

Key: AND never increases, only decreases
```

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    private int count;
    private int X;

    public int countSubsetsWithAND(int[] a, int X) {
        this.count = 0;
        this.X = X;
        backtrack(a, 0, -1, false);
        return count;
    }

    private void backtrack(int[] a, int idx, int currentAND, boolean hasElements) {
        // Base case: processed all elements
        if (idx == a.length) {
            if (hasElements && currentAND == X) {
                count++;
            }
            return;
        }

        // Option 1: Don't include a[idx]
        backtrack(a, idx + 1, currentAND, hasElements);

        // Option 2: Include a[idx]
        int newAND = (currentAND == -1) ? a[idx] : (currentAND & a[idx]);

        // Pruning: If newAND has bits not in X, it can never equal X
        // But we need to check if it's still possible
        if ((newAND & X) == X || !hasElements) {
            backtrack(a, idx + 1, newAND, true);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int X = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.countSubsetsWithAND(a, X));
        sc.close();
    }
}
```

**Python:**

```python
def count_subsets_and_optimized(a, X):
    count = 0

    def backtrack(idx, current_and, has_elements):
        nonlocal count

        if idx == len(a):
            if has_elements and current_and == X:
                count += 1
            return

        # Don't include a[idx]
        backtrack(idx + 1, current_and, has_elements)

        # Include a[idx]
        new_and = a[idx] if current_and is None else (current_and & a[idx])

        # Pruning: check if still possible to reach X
        if current_and is None or (new_and & X) == X:
            backtrack(idx + 1, new_and, True)

    backtrack(0, None, False)
    return count

# Main
line = input().split()
n, X = int(line[0]), int(line[1])
a = list(map(int, input().split()))
print(count_subsets_and_optimized(a, X))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    int count;
    int X;

    void backtrack(vector<int>& a, int idx, int currentAND, bool hasElements) {
        if (idx == a.size()) {
            if (hasElements && currentAND == X) {
                count++;
            }
            return;
        }

        // Don't include a[idx]
        backtrack(a, idx + 1, currentAND, hasElements);

        // Include a[idx]
        int newAND = (currentAND == -1) ? a[idx] : (currentAND & a[idx]);

        // Pruning
        if ((newAND & X) == X || !hasElements) {
            backtrack(a, idx + 1, newAND, true);
        }
    }

public:
    int countSubsetsWithAND(vector<int>& a, int X) {
        this->count = 0;
        this->X = X;
        backtrack(a, 0, -1, false);
        return count;
    }
};

int main() {
    int n, X;
    cin >> n >> X;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    Solution sol;
    cout << sol.countSubsetsWithAND(a, X) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function countSubsetsWithAND(a, X) {
  let count = 0;

  function backtrack(idx, currentAND, hasElements) {
    if (idx === a.length) {
      if (hasElements && currentAND === X) {
        count++;
      }
      return;
    }

    // Don't include a[idx]
    backtrack(idx + 1, currentAND, hasElements);

    // Include a[idx]
    const newAND = currentAND === null ? a[idx] : currentAND & a[idx];

    // Pruning
    if (currentAND === null || (newAND & X) === X) {
      backtrack(idx + 1, newAND, true);
    }
  }

  backtrack(0, null, false);
  return count;
}

// Main
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, X] = lines[0].split(" ").map(Number);
  const a = lines[1].split(" ").map(Number);
  console.log(countSubsetsWithAND(a, X));
});
```

### Complexity Analysis

- **Time Complexity:** O(2^n) worst case
  - Pruning reduces practical runtime significantly
  - Best case with aggressive pruning: O(n × k) where k << 2^n
- **Space Complexity:** O(n)
  - Recursion stack depth

---

## Approach 3: Dynamic Programming with Bitmask

### Core Insight

**DP State:**

- `dp[mask][value]` = number of subsets from first `popcount(mask)` elements with AND = `value`
- Transition: include/exclude next element

### Algorithm

```
DP Table Construction:
═══════════════════════════════════════════
State: dp[processed_elements_mask][AND_value] = count

Transition:
  For each state (mask, value):
    For next element a[i]:
      1. Don't take: dp[mask][value] contributes to dp[mask][value]
      2. Take: dp[mask][value] contributes to dp[mask|(1<<i)][value & a[i]]
```

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int countSubsetsWithAND(int[] a, int X) {
        int n = a.length;
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(a[0], 1); // Single element subsets

        for (int i = 1; i < n; i++) {
            Map<Integer, Integer> newDp = new HashMap<>(dp);

            // Single element subset with a[i]
            newDp.put(a[i], newDp.getOrDefault(a[i], 0) + 1);

            // Extend existing subsets
            for (Map.Entry<Integer, Integer> entry : dp.entrySet()) {
                int prevAND = entry.getKey();
                int count = entry.getValue();
                int newAND = prevAND & a[i];
                newDp.put(newAND, newDp.getOrDefault(newAND, 0) + count);
            }

            dp = newDp;
        }

        return dp.getOrDefault(X, 0);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int X = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.countSubsetsWithAND(a, X));
        sc.close();
    }
}
```

**Python:**

```python
def count_subsets_and_dp(a, X):
    dp = {a[0]: 1}  # Initial: single element subset

    for i in range(1, len(a)):
        new_dp = dp.copy()

        # Single element subset with a[i]
        new_dp[a[i]] = new_dp.get(a[i], 0) + 1

        # Extend existing subsets
        for prev_and, count in dp.items():
            new_and = prev_and & a[i]
            new_dp[new_and] = new_dp.get(new_and, 0) + count

        dp = new_dp

    return dp.get(X, 0)

# Main
line = input().split()
n, X = int(line[0]), int(line[1])
a = list(map(int, input().split()))
print(count_subsets_and_dp(a, X))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int countSubsetsWithAND(vector<int>& a, int X) {
    int n = a.size();
    unordered_map<int, int> dp;
    dp[a[0]] = 1;

    for (int i = 1; i < n; i++) {
        unordered_map<int, int> newDp = dp;

        // Single element subset with a[i]
        newDp[a[i]]++;

        // Extend existing subsets
        for (auto& [prevAND, count] : dp) {
            int newAND = prevAND & a[i];
            newDp[newAND] += count;
        }

        dp = newDp;
    }

    return dp[X];
}

int main() {
    int n, X;
    cin >> n >> X;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << countSubsetsWithAND(a, X) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function countSubsetsWithAND(a, X) {
  let dp = new Map();
  dp.set(a[0], 1);

  for (let i = 1; i < a.length; i++) {
    const newDp = new Map(dp);

    // Single element subset with a[i]
    newDp.set(a[i], (newDp.get(a[i]) || 0) + 1);

    // Extend existing subsets
    for (const [prevAND, count] of dp) {
      const newAND = prevAND & a[i];
      newDp.set(newAND, (newDp.get(newAND) || 0) + count);
    }

    dp = newDp;
  }

  return dp.get(X) || 0;
}

// Main
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, X] = lines[0].split(" ").map(Number);
  const a = lines[1].split(" ").map(Number);
  console.log(countSubsetsWithAND(a, X));
});
```

### Detailed Trace

```
Array: [6, 3, 2], X = 2

Initial: dp = {6: 1}

Process 3:
  new_dp = {6: 1} (copy)
  Add {3}: new_dp = {6: 1, 3: 1}
  Extend {6} with 3: 6 & 3 = 2 → new_dp = {6: 1, 3: 1, 2: 1}
  dp = {6: 1, 3: 1, 2: 1}

Process 2:
  new_dp = {6: 1, 3: 1, 2: 1} (copy)
  Add {2}: new_dp = {6: 1, 3: 1, 2: 2}
  Extend {6} with 2: 6 & 2 = 2 → new_dp[2] = 2 + 1 = 3
  Extend {3} with 2: 3 & 2 = 2 → new_dp[2] = 3 + 1 = 4
  Extend {2} with 2: 2 & 2 = 2 → new_dp[2] = 4 + 1 = 5
  dp = {6: 1, 3: 1, 2: 5}

Answer: dp[2] = 5
```

### Complexity Analysis

- **Time Complexity:** O(n × U)
  - n elements to process
  - U = number of unique AND values (at most 2^20 but typically much smaller)
  - In practice: O(n × log(MAX)) due to AND properties
- **Space Complexity:** O(U)
  - Storing DP map

---

## Edge Cases

### Case 1: X = 0

```
X = 0 means we need all bits to be 0.
Only way: subset contains at least one element with every bit position = 0.
Example: a = [0, 5, 7], X = 0
  {0} → AND = 0 ✓
  {0, 5} → 0 & 5 = 0 ✓
  {0, 7} → 0 & 7 = 0 ✓
  {0, 5, 7} → 0 ✓

If no element is 0, then X=0 is impossible.
```

### Case 2: All Elements Same as X

```
a = [5, 5, 5], X = 5
Every non-empty subset has AND = 5.
Count = 2^n - 1 = 7 subsets
```

### Case 3: No Valid Subsets

```
a = [7, 3], X = 8
7 = 0111, 3 = 0011, X = 1000
Neither 7 nor 3 has bit 3 set, so X is unreachable.
Count = 0
```

### Case 4: Single Element

```
a = [5], X = 5 → Count = 1 ({5})
a = [5], X = 3 → Count = 0
```

---

### C++ommon Mistakes

### Mistake 1: Forgetting Non-Empty Constraint

```java
// Wrong: including empty subset
for (int mask = 0; mask < (1 << n); mask++) {  // Starts from 0!
```

**Fix:** Start from `mask = 1`.

### Mistake 2: Incorrect AND Initialization

```python
# Wrong: using 0 as initial AND
and_result = 0
for i in range(n):
    if mask & (1 << i):
        and_result &= a[i]  # 0 & anything = 0!
```

**Fix:** Use first element or a sentinel value.

### Mistake 3: Not Handling X with Unset Bits

```cpp
// Wrong: assuming X has all bits needed
if (a[i] & X) {  // Doesn't check if a[i] can contribute to X
    // ...
}
```

---

## Interview Extensions

### Extension 1: Count Subsets with OR = X

Similar problem but with OR instead of AND. OR is monotonically increasing.

### Extension 2: Maximum AND Subset

Find the maximum possible AND value achievable by any subset.

**Approach:**

- Greedy from MSB to LSB
- Try to keep each bit set if possible

### Extension 3: K-Sized Subsets

Count subsets of size exactly k with AND = X.

**Modification:** Add size parameter to DP state.

---

## Practice Problems

1. **Maximum AND Pair** - Find maximum AND of any two elements
2. **Minimum OR Subset** - Find subset with minimum OR value
3. **AND-OR Alternating** - Alternate AND and OR operations on subsets
4. **Subset AND Range** - Count subsets with AND in range [L, R]
5. **Dynamic AND Updates** - Handle insertions and count queries

---

## Summary Table

| Approach     | Time             | Space | Best For                   |
| ------------ | ---------------- | ----- | -------------------------- |
| Brute Force  | O(2^n × n)       | O(1)  | Simple, small n            |
| Backtracking | O(2^n) amortized | O(n)  | With pruning opportunities |
| DP           | O(n × U)         | O(U)  | Many unique AND values     |

---

## Key Takeaways

1. **AND is monotone decreasing** - crucial for pruning
2. **Small n (≤20)** allows exponential algorithms
3. **DP with map** efficiently handles sparse value spaces
4. **Subset enumeration** is fundamental bitmask technique
5. **Early pruning** significantly improves practical performance

This problem combines:

- Bitmask enumeration
- Dynamic programming
- Bitwise operations
- Subset generation

Master these techniques for competitive programming success!
