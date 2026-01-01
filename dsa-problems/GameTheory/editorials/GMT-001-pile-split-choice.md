---
problem_id: GMT_PILE_SPLIT_CHOICE__1928
display_id: GMT-001
slug: pile-split-choice
title: "Pile Split Choice"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - grundy-numbers
  - sprague-grundy
  - impartial-game
premium: true
subscription_tier: basic
---

# GMT-001: Pile Split Choice

## 📋 Problem Summary

You start with a pile of `n` stones. A move consists of splitting a pile into two non-empty piles of **different** sizes. The last player to move wins. Determine if the first player has a winning strategy assuming both players play optimally.

## 🌍 Real-World Scenario

**Scenario Title:** The Chocolate Bar Challenge

Imagine you're at a party with your friend, and you have a chocolate bar with `n` pieces. You take turns breaking the chocolate, but there's a twist: **you can only break it into two unequal parts**. 

For example, if you have 6 pieces, you can break it into (1, 5) or (2, 4), but NOT (3, 3) because they're equal. The person who makes the last valid break wins the entire chocolate bar!

**Real-Life Example:**
- You have 5 pieces of chocolate
- Player 1 breaks it into (2, 3) - both players now have separate pieces
- Player 2 breaks the 3-piece into (1, 2)
- Player 1 can't break the 2-piece (would be 1+1, equal!)
- Player 2 can't break the 1-piece (too small!)
- Player 2 made the last move and wins! 🍫

**Why This Matters:**
- **Game Theory Fundamentals:** Understanding winning/losing positions
- **Strategic Thinking:** Planning ahead to force your opponent into bad positions
- **Real Applications:** Resource allocation, turn-based strategy games, competitive programming

![Real-World Application](../images/GMT-001/real-world-scenario.png)

## Detailed Explanation

### Concept: Grundy Numbers (Game Values)

Think of each pile size as having a "power level" called its **Grundy number** `G(n)`. This number tells us if a position is winning or losing:
- `G(n) = 0` → **Losing position** (current player will lose with optimal play)
- `G(n) > 0` → **Winning position** (current player can win with optimal play)

### Algorithm Flow Diagram

```
┌─────────────────────────────────────┐
│  Start: Calculate G(n) for pile n   │
└──────────────┬──────────────────────┘
               │
               ▼
       ┌───────────────┐
       │ Base Cases:   │
       │ G[0] = 0      │
       │ G[1] = 0      │
       │ G[2] = 0      │
       └───────┬───────┘
               │
               ▼
       ┌───────────────────────┐
       │ For i = 3 to n:       │
       └───────┬───────────────┘
               │
               ▼
       ┌───────────────────────────┐
       │ Try all valid splits:     │
       │ (j, i-j) where j < i-j    │
       └───────┬───────────────────┘
               │
               ▼
       ┌───────────────────────────┐
       │ Calculate XOR:            │
       │ xor_val = G[j] ^ G[i-j]   │
       └───────┬───────────────────┘
               │
               ▼
       ┌───────────────────────────┐
       │ Collect all xor_vals      │
       │ in a set                  │
       └───────┬───────────────────┘
               │
               ▼
       ┌───────────────────────────┐
       │ G[i] = mex(set)           │
       │ (smallest missing value)  │
       └───────┬───────────────────┘
               │
               ▼
       ┌───────────────────────────┐
       │ Return "First" if G[n]>0  │
       │ else "Second"             │
       └───────────────────────────┘
```

### Game Tree Example (n=6)

```
                    Pile: 6
                   G[6] = ?
                      |
        ┌─────────────┼─────────────┐
        │             │             │
    Split (1,5)   Split (2,4)   Split (3,3)
        │             │             ❌ INVALID
        │             │             (equal sizes)
        ▼             ▼
    G[1]^G[5]     G[2]^G[4]
     = 0^2         = 0^0
     = 2           = 0

    Set of reachable values: {0, 2}
    G[6] = mex({0, 2}) = 1 ✅ (First player wins!)
```

## ✅ Input/Output Clarifications

- **Different Sizes Required:** 
  - ✅ Valid: `6 → (1, 5)`, `6 → (2, 4)`
  - ❌ Invalid: `6 → (3, 3)` (equal sizes)
  
- **Non-empty Piles:**
  - ❌ Invalid: `4 → (0, 4)` (one pile is empty)
  
- **Winning Condition:** 
  - The player who **cannot make a move** loses
  - The player who **makes the last move** wins

- **Optimal Play:** Both players always make the best possible move

## Naive Approach

### Intuition

Try to simulate the game recursively: for each pile, try all possible splits and see if any split leads to a losing position for the opponent.

### Algorithm

```
function canWin(n):
    if n < 3:
        return false  // Cannot split
    
    for each valid split (a, b) where a + b = n and a != b:
        if not canWin(a) and not canWin(b):
            return true  // Found a winning move
    
    return false
```

### Time Complexity

- **O(2^N)**: Exponential due to overlapping subproblems
- Without memoization, we recalculate the same states multiple times

### Space Complexity

- **O(N)**: Recursion depth

### Limitations

- **Too Slow:** For `n = 2000`, this approach times out
- **No Insight:** Doesn't help us understand the pattern of winning/losing positions

## Optimal Approach

### Key Insight

This is **Grundy's Game**, a classic impartial game. We use the **Sprague-Grundy Theorem**:

1. **Grundy Number** `G(n)` represents the "value" of a game state
2. For a pile that splits into two independent piles, we **XOR** their Grundy numbers
3. `G(n) = mex({ G(a) ^ G(b) })` for all valid splits
4. **mex** (Minimum Excluded value) = smallest non-negative integer NOT in the set

**Why XOR?** When a game splits into independent subgames, the combined Grundy number is the XOR of individual Grundy numbers. This is a fundamental theorem in combinatorial game theory!

### Algorithm Steps

1. **Initialize base cases:** `G[0] = G[1] = G[2] = 0` (no valid moves → losing positions)
2. **Build up from i = 3 to n:**
   - For each pile size `i`, try all valid splits `(j, i-j)` where `j < i-j`
   - Calculate `xor_val = G[j] ^ G[i-j]` for each split
   - Collect all `xor_val` in a set
   - `G[i] = mex(set)` (smallest non-negative integer not in set)
3. **Return result:** "First" if `G[n] > 0`, else "Second"

### Time Complexity

- **O(N²)**: For each `i` from 3 to N, we check ~`i/2` splits
- Total operations: `3/2 + 4/2 + 5/2 + ... + N/2 ≈ N²/4`
- For `N = 2000`: ~1,000,000 operations ✅ Fast enough!

### Space Complexity

- **O(N)**: Array to store Grundy values `G[0..n]`

### Complexity Visualization

| Input Size (n) | Naive O(2^N) | Optimal O(N²) | Speedup |
|---------------:|-------------:|--------------:|--------:|
| 10             | ~1,024       | 100           | 10x     |
| 100            | ~10^30       | 10,000        | Massive |
| 1,000          | Impossible   | 1,000,000     | ✅      |
| 2,000          | Impossible   | 4,000,000     | ✅      |

![Algorithm Visualization](../images/GMT-001/algorithm-visualization.png)

## Implementations

### Python

```python
def pile_split_game(n: int) -> str:
    """
    Determine winner of Grundy's Game using Sprague-Grundy theorem.
    
    Args:
        n: Initial pile size
    
    Returns:
        "First" if first player wins, "Second" otherwise
    """
    if n == 0:
        return "Second"
    
    # g[i] stores the Grundy number for pile size i
    g = [0] * (n + 1)
    
    # Calculate Grundy numbers for all pile sizes from 3 to n
    for i in range(3, n + 1):
        reachable = set()
        # Try all valid splits: (j, i-j) where j < i-j
        # This ensures j != i-j (different sizes)
        for j in range(1, (i - 1) // 2 + 1):
            # XOR the Grundy numbers of the two resulting piles
            reachable.add(g[j] ^ g[i - j])
        
        # Calculate mex (minimum excluded value)
        mex = 0
        while mex in reachable:
            mex += 1
        g[i] = mex
        
    return "First" if g[n] > 0 else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    print(pile_split_game(n))

if __name__ == "__main__":
    main()
```

### Java

```java
import java.util.*;

class Solution {
    public String pileSplitGame(int n) {
        if (n == 0) return "Second";
        int[] g = new int[n + 1];
        
        for (int i = 3; i <= n; i++) {
            Set<Integer> reachable = new HashSet<>();
            // Split into j and i-j. j starts at 1.
            // Condition: j != i-j => 2*j != i.
            // Also j < i-j to avoid duplicates => 2*j < i.
            for (int j = 1; 2 * j < i; j++) {
                reachable.add(g[j] ^ g[i - j]);
            }
            
            // Calculate mex
            int mex = 0;
            while (reachable.contains(mex)) {
                mex++;
            }
            g[i] = mex;
        }
        
        return g[n] > 0 ? "First" : "Second";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.pileSplitGame(n));
        }
        sc.close();
    }
}
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

class Solution {
public:
    string pileSplitGame(int n) {
        if (n == 0) return "Second";
        vector<int> g(n + 1, 0);
        
        for (int i = 3; i <= n; i++) {
            unordered_set<int> reachable;
            // Try all valid splits where j < i-j
            for (int j = 1; 2 * j < i; j++) {
                reachable.insert(g[j] ^ g[i - j]);
            }
            
            // Calculate mex (minimum excluded value)
            int mex = 0;
            while (reachable.count(mex)) {
                mex++;
            }
            g[i] = mex;
        }
        
        return g[n] > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (cin >> n) {
        Solution solution;
        cout << solution.pileSplitGame(n) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  pileSplitGame(n) {
    if (n === 0) return "Second";
    const g = new Int32Array(n + 1);
    
    for (let i = 3; i <= n; i++) {
      const reachable = new Set();
      // Try all valid splits where j < i-j
      for (let j = 1; 2 * j < i; j++) {
        reachable.add(g[j] ^ g[i - j]);
      }
      
      // Calculate mex (minimum excluded value)
      let missing = 0;
      while (reachable.has(missing)) {
        missing++;
      }
      g[i] = missing;
    }
    
    return g[n] > 0 ? "First" : "Second";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0]);
  const solution = new Solution();
  console.log(solution.pileSplitGame(n));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `n = 6`

### Step-by-Step Execution Table

| Step | Pile Size (i) | Valid Splits | XOR Values | Reachable Set | mex Calculation | G[i] | Explanation |
|-----:|:-------------:|:-------------|:-----------|:--------------|:----------------|:----:|:------------|
| 0    | 0, 1, 2       | None         | -          | -             | -               | 0    | Base cases: no valid moves |
| 1    | 3             | (1, 2)       | G[1]^G[2] = 0^0 = 0 | {0} | mex({0}) = 1 | 1 | First missing: 1 |
| 2    | 4             | (1, 3)       | G[1]^G[3] = 0^1 = 1 | {1} | mex({1}) = 0 | 0 | First missing: 0 |
| 3    | 5             | (1, 4), (2, 3) | 0^0=0, 0^1=1 | {0, 1} | mex({0,1}) = 2 | 2 | First missing: 2 |
| 4    | 6             | (1, 5), (2, 4) | 0^2=2, 0^0=0 | {0, 2} | mex({0,2}) = 1 | 1 | First missing: 1 |

### State Transition Visualization

```
G[0] = 0    (Cannot split 0 stones)
G[1] = 0    (Cannot split 1 stone)
G[2] = 0    (Can only split into 1+1, but equal sizes not allowed)

G[3] = 1    Split (1,2) → XOR(0,0) = 0 → mex({0}) = 1
            ┌───┬───┬───┐
            │ 1 │ 1 │ 1 │  Can split!
            └───┴───┴───┘

G[4] = 0    Split (1,3) → XOR(0,1) = 1 → mex({1}) = 0
            ┌───┬───┬───┬───┐
            │ 1 │ 1 │ 1 │ 1 │  Losing position
            └───┴───┴───┴───┘

G[5] = 2    Splits: (1,4)→0, (2,3)→1 → mex({0,1}) = 2
            ┌───┬───┬───┬───┬───┐
            │ 1 │ 1 │ 1 │ 1 │ 1 │  Strong winning position
            └───┴───┴───┴───┴───┘

G[6] = 1    Splits: (1,5)→2, (2,4)→0 → mex({0,2}) = 1
            ┌───┬───┬───┬───┬───┬───┐
            │ 1 │ 1 │ 1 │ 1 │ 1 │ 1 │  Winning position
            └───┴───┴───┴───┴───┴───┘
```

**Conclusion:** `G[6] = 1 > 0` → Output: **"First"** ✅

The first player can win by splitting 6 into (2, 4), leaving the opponent with two losing positions!

## ⚠️ Common Mistakes to Avoid

### 1. Assuming Simple Odd/Even Pattern

**❌ Wrong Approach:**
```python
# Incorrect: assuming odd = win, even = lose
def wrong_solution(n):
    return "First" if n % 2 == 1 else "Second"
```

**✅ Correct Approach:**
```python
# Must calculate Grundy numbers properly
# G[6] = 1 (Win), G[4] = 0 (Lose) - no simple pattern!
```

**Why it matters:** The Grundy sequence is `0,0,0,1,0,2,1,0,2,1,0,2,1,...` which has NO simple odd/even pattern. Counterexample: `n=6` (even) is winning, but `n=4` (even) is losing.

**Example:** For `n=6`, the wrong approach returns "Second" but correct answer is "First".

### 2. Forgetting to XOR Subgame Values

**❌ Wrong Approach:**
```python
# Trying to check if ANY split leads to losing state
for j in range(1, i//2):
    if g[j] == 0 and g[i-j] == 0:  # Both losing?
        g[i] = 1  # WRONG!
```

**✅ Correct Approach:**
```python
# Must XOR the Grundy numbers
reachable = set()
for j in range(1, (i-1)//2 + 1):
    reachable.add(g[j] ^ g[i-j])  # XOR is essential!
g[i] = mex(reachable)
```

**Why it matters:** The Sprague-Grundy theorem requires XOR to combine independent subgames. Without XOR, you're not correctly computing the game value.

**Example:** For pile size 5, splits (1,4) and (2,3) give XOR values 0 and 1. Simply checking if both are 0 misses the complete picture.

### 3. Allowing Equal-Size Splits

**❌ Wrong Approach:**
```python
# Including equal splits
for j in range(1, i):  # Goes up to i-1
    reachable.add(g[j] ^ g[i-j])  # Includes j = i-j case!
```

**✅ Correct Approach:**
```python
# Only different-size splits
for j in range(1, (i-1)//2 + 1):  # Ensures j < i-j
    reachable.add(g[j] ^ g[i-j])
```

**Why it matters:** The problem explicitly states piles must have **different** sizes. Including equal splits gives wrong Grundy numbers.

**Example:** For `n=4`, allowing split (2,2) would incorrectly add `G[2]^G[2]=0` to reachable set, changing the mex value.

### 4. Incorrect Base Cases

**❌ Wrong Approach:**
```python
g[0] = 1  # WRONG!
g[1] = 1  # WRONG!
g[2] = 1  # WRONG!
```

**✅ Correct Approach:**
```python
g[0] = 0  # Cannot move from 0 stones
g[1] = 0  # Cannot split 1 stone
g[2] = 0  # Can only split into 1+1 (equal, invalid)
```

**Why it matters:** Piles of size 0, 1, and 2 have no valid moves, making them **losing positions** with Grundy number 0. Wrong base cases cascade errors through all calculations.

**Example:** If `G[2]=1`, then `G[3]` calculation becomes wrong, affecting all subsequent values.

## 💡 Interview Extensions

### 1. What if we allow equal-size splits?

**Question:** How would the algorithm change if splits like `4 → (2, 2)` were valid?

**Answer:** 
```python
# Modified loop to include equal splits
for j in range(1, i):  # Now includes j = i-j case
    reachable.add(g[j] ^ g[i-j])
```

The Grundy numbers would change:
- `G[4]` would now include `G[2]^G[2] = 0`, potentially changing mex
- Generally makes more positions winning since more moves are available

### 2. What if we start with multiple piles?

**Question:** If we start with piles of sizes `[n1, n2, n3]`, how do we determine the winner?

**Answer:**
```python
def multiple_piles(sizes):
    # Calculate Grundy number for each pile
    grundy_values = [pile_split_game_grundy(n) for n in sizes]
    
    # XOR all Grundy numbers together
    total_xor = 0
    for g in grundy_values:
        total_xor ^= g
    
    return "First" if total_xor > 0 else "Second"
```

**Why:** By Sprague-Grundy theorem, the combined game's Grundy number is the XOR of individual Grundy numbers.

### 3. Can we optimize space complexity?

**Question:** For very large `n`, can we reduce memory usage?

**Answer:** Not easily for this problem. We need `G[j]` for all `j < i` to compute `G[i]`, so we must store all values. However, if we only need to answer for specific values of `n`, we could use memoization with a hash map instead of an array.

### 4. What's the pattern in Grundy numbers?

**Question:** Is there a pattern we can exploit to avoid computing all values?

**Answer:** The Grundy sequence for this game is known to be **eventually periodic** with period 149 starting from around `n=1000`. However, for `n ≤ 2000`, it's more reliable to compute directly than to hardcode the pattern. For competitive programming, the O(N²) solution is preferred for its simplicity and correctness.

**Grundy sequence:** `0,0,0,1,0,2,1,0,2,1,0,2,1,3,2,1,3,2,1,3,2,1,...`
