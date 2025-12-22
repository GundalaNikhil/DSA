---
problem_id: BIT_MINIMIZE_MAX_PAIR_XOR__8413
display_id: BIT-013
slug: minimize-max-pair-xor
title: Minimize Max Pair XOR
difficulty: Medium
difficulty_score: 58
topics:
- Bitwise Operations
- Dynamic Programming
- Bitmask
tags:
- bitwise
- dp
- bitmask
- medium
premium: true
subscription_tier: basic
---
# BIT-013: Minimize Max Pair XOR

## Real-World Scenario: Load Balancing Network Links

In distributed systems, pairing servers to balance communication overhead is crucial. When data is transmitted between paired servers, the XOR of their IDs represents routing complexity. Minimizing the maximum XOR across all pairs ensures balanced network load and prevents bottlenecks.

---

## Problem Analysis

### Understanding the Problem

Given an even-sized array of `n` elements, partition them into `n/2` pairs such that the maximum XOR value among all pairs is minimized.

**Key Observations:**

1. We have `n!!` (double factorial) possible pairings for n elements
2. Small n (≤16) allows exponential solutions
3. Need to try different pairings to find optimal
4. Bitmask DP tracks which elements are already paired

### Visual Example

```
Array: [1, 2, 3, 4]
Binary: [001, 010, 011, 100]

All Possible Pairings:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pairing | Pairs          | XORs          | Max XOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   1    | (1,2), (3,4)   | 3, 7          |   7
   2    | (1,3), (2,4)   | 2, 6          |   6
   3    | (1,4), (2,3)   | 5, 1          |   5  ← Minimum!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

XOR Calculations:
  1 ^ 2 = 001 ^ 010 = 011 = 3
  3 ^ 4 = 011 ^ 100 = 111 = 7

  1 ^ 3 = 001 ^ 011 = 010 = 2
  2 ^ 4 = 010 ^ 100 = 110 = 6

  1 ^ 4 = 001 ^ 100 = 101 = 5
  2 ^ 3 = 010 ^ 011 = 001 = 1

Answer: 5
```

### Number of Pairings Formula

```
Number of ways to pair n elements:
═══════════════════════════════════════════
n = 2: 1 way
n = 4: 3 ways
n = 6: 15 ways
n = 8: 105 ways
...
Formula: (n-1)!! = (n-1) × (n-3) × (n-5) × ... × 1

For n=16: 2,027,025 pairings
Still manageable with DP!
```

---

## Approach 1: Brute Force - Try All Pairings

### Algorithm

1. Generate all possible pairings recursively
2. For each pairing, compute maximum XOR
3. Track minimum across all pairings

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    private int minMaxXOR;

    public int minimizeMaxPairXOR(int[] a) {
        minMaxXOR = Integer.MAX_VALUE;
        generatePairings(a, 0, new ArrayList<>());
        return minMaxXOR;
    }

    private void generatePairings(int[] a, int mask, List<int[]> pairs) {
        int n = a.length;

        // All elements paired
        if (Integer.bitCount(mask) == n) {
            int maxXOR = 0;
            for (int[] pair : pairs) {
                maxXOR = Math.max(maxXOR, a[pair[0]] ^ a[pair[1]]);
            }
            minMaxXOR = Math.min(minMaxXOR, maxXOR);
            return;
        }

        // Find first unpaired element
        int first = -1;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) {
                first = i;
                break;
            }
        }

        // Try pairing with all other unpaired elements
        for (int second = first + 1; second < n; second++) {
            if ((mask & (1 << second)) == 0) {
                pairs.add(new int[]{first, second});
                generatePairings(a, mask | (1 << first) | (1 << second), pairs);
                pairs.remove(pairs.size() - 1);
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.minimizeMaxPairXOR(a));
        sc.close();
    }
}
```

**Python:**

```python
def minimize_max_pair_xor_brute(a):
    n = len(a)
    min_max_xor = float('inf')

    def generate_pairings(mask, pairs):
        nonlocal min_max_xor

        # All elements paired
        if bin(mask).count('1') == n:
            max_xor = max(a[i] ^ a[j] for i, j in pairs)
            min_max_xor = min(min_max_xor, max_xor)
            return

        # Find first unpaired element
        first = -1
        for i in range(n):
            if not (mask & (1 << i)):
                first = i
                break

        # Try pairing with all other unpaired elements
        for second in range(first + 1, n):
            if not (mask & (1 << second)):
                generate_pairings(
                    mask | (1 << first) | (1 << second),
                    pairs + [(first, second)]
                )

    generate_pairings(0, [])
    return min_max_xor

# Main
n = int(input())
a = list(map(int, input().split()))
print(minimize_max_pair_xor_brute(a))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    int minMaxXOR;
    vector<int> a;
    int n;

    void generatePairings(int mask, vector<pair<int,int>>& pairs) {
        // All elements paired
        if (__builtin_popcount(mask) == n) {
            int maxXOR = 0;
            for (auto& [i, j] : pairs) {
                maxXOR = max(maxXOR, a[i] ^ a[j]);
            }
            minMaxXOR = min(minMaxXOR, maxXOR);
            return;
        }

        // Find first unpaired element
        int first = -1;
        for (int i = 0; i < n; i++) {
            if (!(mask & (1 << i))) {
                first = i;
                break;
            }
        }

        // Try pairing with all other unpaired elements
        for (int second = first + 1; second < n; second++) {
            if (!(mask & (1 << second))) {
                pairs.push_back({first, second});
                generatePairings(mask | (1 << first) | (1 << second), pairs);
                pairs.pop_back();
            }
        }
    }

public:
    int minimizeMaxPairXOR(vector<int>& arr) {
        a = arr;
        n = a.size();
        minMaxXOR = INT_MAX;
        vector<pair<int,int>> pairs;
        generatePairings(0, pairs);
        return minMaxXOR;
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    Solution sol;
    cout << sol.minimizeMaxPairXOR(a) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function minimizeMaxPairXOR(a) {
  const n = a.length;
  let minMaxXOR = Infinity;

  function generatePairings(mask, pairs) {
    // All elements paired
    if (countBits(mask) === n) {
      let maxXOR = 0;
      for (const [i, j] of pairs) {
        maxXOR = Math.max(maxXOR, a[i] ^ a[j]);
      }
      minMaxXOR = Math.min(minMaxXOR, maxXOR);
      return;
    }

    // Find first unpaired element
    let first = -1;
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i))) {
        first = i;
        break;
      }
    }

    // Try pairing with all other unpaired elements
    for (let second = first + 1; second < n; second++) {
      if (!(mask & (1 << second))) {
        generatePairings(mask | (1 << first) | (1 << second), [
          ...pairs,
          [first, second],
        ]);
      }
    }
  }

  function countBits(n) {
    let count = 0;
    while (n) {
      count += n & 1;
      n >>= 1;
    }
    return count;
  }

  generatePairings(0, []);
  return minMaxXOR;
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
  const n = parseInt(lines[0]);
  const a = lines[1].split(" ").map(Number);
  console.log(minimizeMaxPairXOR(a));
});
```

### Complexity Analysis

- **Time Complexity:** O((n-1)!! × n)
  - (n-1)!! pairings to generate
  - O(n) to compute max XOR for each pairing
  - For n=16: ~2M × 16 = 32M operations
- **Space Complexity:** O(n)
  - Recursion depth and pair storage

---

## Approach 2: Dynamic Programming with Bitmask (Optimal)

### Core Insight

**DP State:**

- `dp[mask]` = minimum possible maximum XOR for elements represented in mask
- Transition: Pick first unpaired element, try pairing with all others
- Result: `dp[(1<<n) - 1]`

### Algorithm

```
DP with Bitmask:
═══════════════════════════════════════════
dp[mask] = minimum of maximum XOR when elements in mask are paired

Base case: dp[0] = 0 (no elements, no XOR)

Transition:
  For each mask:
    Find first unpaired bit i
    For each other unpaired bit j > i:
      newMask = mask | (1<<i) | (1<<j)
      dp[newMask] = min(dp[newMask], max(dp[mask], a[i] ^ a[j]))
```

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int minimizeMaxPairXOR(int[] a) {
        int n = a.length;
        int fullMask = (1 << n) - 1;
        int[] dp = new int[1 << n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == Integer.MAX_VALUE) continue;

            // Find first unpaired element
            int first = -1;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) {
                    first = i;
                    break;
                }
            }

            if (first == -1) continue; // All paired

            // Try pairing with all other unpaired elements
            for (int second = first + 1; second < n; second++) {
                if ((mask & (1 << second)) == 0) {
                    int newMask = mask | (1 << first) | (1 << second);
                    int pairXOR = a[first] ^ a[second];
                    int newMaxXOR = Math.max(dp[mask], pairXOR);
                    dp[newMask] = Math.min(dp[newMask], newMaxXOR);
                }
            }
        }

        return dp[fullMask];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.minimizeMaxPairXOR(a));
        sc.close();
    }
}
```

**Python:**

```python
def minimize_max_pair_xor_dp(a):
    n = len(a)
    full_mask = (1 << n) - 1
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue

        # Find first unpaired element
        first = -1
        for i in range(n):
            if not (mask & (1 << i)):
                first = i
                break

        if first == -1:  # All paired
            continue

        # Try pairing with all other unpaired elements
        for second in range(first + 1, n):
            if not (mask & (1 << second)):
                new_mask = mask | (1 << first) | (1 << second)
                pair_xor = a[first] ^ a[second]
                new_max_xor = max(dp[mask], pair_xor)
                dp[new_mask] = min(dp[new_mask], new_max_xor)

    return dp[full_mask]

# Main
n = int(input())
a = list(map(int, input().split()))
print(minimize_max_pair_xor_dp(a))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int minimizeMaxPairXOR(vector<int>& a) {
    int n = a.size();
    int fullMask = (1 << n) - 1;
    vector<int> dp(1 << n, INT_MAX);
    dp[0] = 0;

    for (int mask = 0; mask < (1 << n); mask++) {
        if (dp[mask] == INT_MAX) continue;

        // Find first unpaired element
        int first = -1;
        for (int i = 0; i < n; i++) {
            if (!(mask & (1 << i))) {
                first = i;
                break;
            }
        }

        if (first == -1) continue; // All paired

        // Try pairing with all other unpaired elements
        for (int second = first + 1; second < n; second++) {
            if (!(mask & (1 << second))) {
                int newMask = mask | (1 << first) | (1 << second);
                int pairXOR = a[first] ^ a[second];
                int newMaxXOR = max(dp[mask], pairXOR);
                dp[newMask] = min(dp[newMask], newMaxXOR);
            }
        }
    }

    return dp[fullMask];
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << minimizeMaxPairXOR(a) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function minimizeMaxPairXOR(a) {
  const n = a.length;
  const fullMask = (1 << n) - 1;
  const dp = new Array(1 << n).fill(Infinity);
  dp[0] = 0;

  for (let mask = 0; mask < 1 << n; mask++) {
    if (dp[mask] === Infinity) continue;

    // Find first unpaired element
    let first = -1;
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i))) {
        first = i;
        break;
      }
    }

    if (first === -1) continue; // All paired

    // Try pairing with all other unpaired elements
    for (let second = first + 1; second < n; second++) {
      if (!(mask & (1 << second))) {
        const newMask = mask | (1 << first) | (1 << second);
        const pairXOR = a[first] ^ a[second];
        const newMaxXOR = Math.max(dp[mask], pairXOR);
        dp[newMask] = Math.min(dp[newMask], newMaxXOR);
      }
    }
  }

  return dp[fullMask];
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
  const n = parseInt(lines[0]);
  const a = lines[1].split(" ").map(Number);
  console.log(minimizeMaxPairXOR(a));
});
```

### Detailed Trace

```
Array: [1, 2, 3, 4]
n = 4, masks from 0000 to 1111 (binary)

Initial: dp[0000] = 0

From mask 0000:
  first = 0 (element 1)
  Pair with 1 (element 2): dp[0011] = max(0, 1^2=3) = 3
  Pair with 2 (element 3): dp[0101] = max(0, 1^3=2) = 2
  Pair with 3 (element 4): dp[1001] = max(0, 1^4=5) = 5

From mask 0011:
  first = 2 (element 3)
  Pair with 3 (element 4): dp[1111] = max(3, 3^4=7) = 7

From mask 0101:
  first = 1 (element 2)
  Pair with 3 (element 4): dp[1101] = max(2, 2^4=6) = 6

From mask 1001:
  first = 1 (element 2)
  Pair with 2 (element 3): dp[1011] = max(5, 2^3=1) = 5

From mask 1101:
  1101 has an odd number of set bits, so it should not be processed.
  Transitions only apply to masks with even popcount.

Final: dp[1111] = 5
```

### Complexity Analysis

- **Time Complexity:** O(2^n × n²)
  - 2^n states
  - For each state, O(n²) to try all pairs
- **Space Complexity:** O(2^n)
  - DP array

---

## Edge Cases

### Case 1: Two Elements

```
Array: [5, 7]
Only one pairing: (5,7)
XOR = 5 ^ 7 = 2
Answer: 2
```

### Case 2: All Same

```
Array: [3, 3, 3, 3]
All pairs have XOR = 0
Answer: 0
```

### Case 3: Powers of 2

```
Array: [1, 2, 4, 8]
Best pairing: (1,2):3 and (4,8):12
Or: (1,4):5 and (2,8):10
Or: (1,8):9 and (2,4):6
Answer: 6
```

---

### C++ommon Mistakes

### Mistake 1: Greedy Approach Fails

```
// Wrong: pairing smallest XORs greedily doesn't work
// Counter-example: [1,2,3,4]
// Greedy: pair (2,3) first (XOR=1), then (1,4) (XOR=5) → max=5
// But (1,2):3 and (3,4):7 → max=7 is worse!
```

### Mistake 2: Incorrect DP Transition

```python
# Wrong: forgetting to track maximum
dp[new_mask] = min(dp[new_mask], pair_xor)  # Wrong!
# Correct: track max XOR across all pairs in this configuration
dp[new_mask] = min(dp[new_mask], max(dp[mask], pair_xor))
```

---

## Interview Extensions

### Extension 1: Minimize Sum Instead of Max

Minimize the sum of all pair XORs.

**Solution:** Still need DP, but track sum instead of max.

### Extension 2: K-way Partitioning

Partition into groups of size k (not just pairs).

### Extension 3: Weighted Elements

Each element has a weight; minimize weighted maximum XOR.

---

## Practice Problems

1. **Minimum XOR Sum of Two Arrays** - LeetCode 1879
2. **Partition Equal Subset Sum** - Similar DP bitmask
3. **Maximum Score from Performing Multiplication Operations** - DP optimization
4. **Optimal Account Balancing** - Similar pairing problem
5. **TSP with Bitmask DP** - Classic bitmask DP

---

## Summary Table

| Approach              | Time           | Space  | Best For               |
| --------------------- | -------------- | ------ | ---------------------- |
| Brute Force Recursion | O((n-1)!! × n) | O(n)   | Understanding problem  |
| Bitmask DP            | O(2^n × n²)    | O(2^n) | Optimal solution, n≤16 |

---

## Key Takeaways

1. **Small n enables exponential** algorithms
2. **Bitmask DP** tracks subset states efficiently
3. **Pairing problems** often need DP or backtracking
4. **Greedy fails** on this problem
5. **Min-max optimization** requires trying all configurations

This problem combines:

- Bitmask dynamic programming
- Pairing optimization
- XOR operations
- State space exploration

Perfect for advanced competitive programming and algorithm design interviews!
