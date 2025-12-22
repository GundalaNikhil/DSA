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

You start with a pile of `n` stones. A move consists of splitting a pile into two non-empty piles of **different** sizes. The last player to move wins.

## 🌍 Real-World Scenario

**Scenario Title:** The Uneven Break

Imagine you are breaking a chocolate bar or a stick. The rule is you can only break it if the two resulting pieces are NOT equal. If you are left with pieces that can only be broken into equal halves (like size 2 -> 1+1) or cannot be broken at all (size 1), you are stuck.

**Why This Problem Matters:**

- **Impartial Games:** It's a classic example of a game where available moves depend only on the state, not on which player is moving.
- **Sprague-Grundy Theorem:** It demonstrates how to decompose a game into independent subgames (the two new piles) and combine their values using XOR.

![Real-World Application](../images/GMT-001/real-world-scenario.png)

## Detailed Explanation

### Diagram: Game Tree

```
Start: 6

Option A: Split into (1, 5)
  - Pile 1: No moves (Grundy 0)
  - Pile 5: Can split into (1, 4) or (2, 3)

Option B: Split into (2, 4)
  - Pile 2: No moves (Grundy 0)
  - Pile 4: Can split into (1, 3)

Option C: Split into (3, 3) -> INVALID (Equal sizes)
```

## ✅ Input/Output Clarifications

- **Different Sizes:** 4 -> 1+3 is valid. 4 -> 2+2 is invalid.
- **Non-empty:** 4 -> 0+4 is invalid.
- **Winning Condition:** If you can make a move to a state that is "Losing" for the opponent, you are in a "Winning" state.

## Optimal Approach

### Key Insight

This is **Grundy's Game**. We can calculate the **Grundy Number** (or Nim-value) `G(n)` for a pile of size `n`.
- `G(n) = mex({ G(a) ^ G(b) })` for all valid splits `a + b = n`, `a != b`.
- `mex` (Minimum Excluded value) is the smallest non-negative integer not present in the set.
- If `G(n) > 0`, the First player wins.
- If `G(n) == 0`, the Second player wins.

### Algorithm

1.  Initialize `G[0] = G[1] = G[2] = 0`.
2.  Iterate `i` from 3 to `n`.
3.  For each `i`, find all valid splits `(j, i-j)` where `1 <= j < i/2`.
4.  Calculate `xor_val = G[j] ^ G[i-j]`.
5.  Store all `xor_val` in a set.
6.  `G[i] = mex(set)`.
7.  Return "First" if `G[n] > 0`, else "Second".

### Time Complexity

- **O(N^2)**: For each `n`, we iterate roughly `n/2` splits. Sum of `i/2` for `i=1..N` is `O(N^2)`.
- Given `N <= 2000`, `N^2 = 4*10^6`, which fits well within 2 seconds.

### Space Complexity

- **O(N)**: To store Grundy values.

![Algorithm Visualization](../images/GMT-001/algorithm-visualization.png)

## Implementations

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

public class Main {
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

### Python

```python
def pile_split_game(n: int) -> str:
    if n == 0:
        return "Second"
    
    g = [0] * (n + 1)
    
    for i in range(3, n + 1):
        reachable = set()
        # Split into j and i-j.
        # j goes from 1 up to (i-1)//2
        for j in range(1, (i - 1) // 2 + 1):
            reachable.add(g[j] ^ g[i - j])
        
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
            for (int j = 1; 2 * j < i; j++) {
                reachable.insert(g[j] ^ g[i - j]);
            }
            
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
      for (let j = 1; 2 * j < i; j++) {
        reachable.add(g[j] ^ g[i - j]);
      }
      
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

## 🧪 Test Case Walkthrough

**Input:** `n = 6`

**Step-by-Step Execution:**

1.  **Initialize:** `G[0]=0, G[1]=0, G[2]=0`.
2.  **Calculate G[3]:**
    - Splits: `(1, 2)`.
    - XOR Sum: `G[1] ^ G[2] = 0 ^ 0 = 0`.
    - Set: `{0}`.
    - Mex({0}) = 1.
    - `G[3] = 1`.
3.  **Calculate G[4]:**
    - Splits: `(1, 3)`.
    - XOR Sum: `G[1] ^ G[3] = 0 ^ 1 = 1`.
    - Set: `{1}`.
    - Mex({1}) = 0.
    - `G[4] = 0`.
4.  **Calculate G[5]:**
    - Splits:
        - `(1, 4)` -> `G[1] ^ G[4] = 0 ^ 0 = 0`.
        - `(2, 3)` -> `G[2] ^ G[3] = 0 ^ 1 = 1`.
    - Set: `{0, 1}`.
    - Mex({0, 1}) = 2.
    - `G[5] = 2`.
5.  **Calculate G[6]:**
    - Splits:
        - `(1, 5)` -> `G[1] ^ G[5] = 0 ^ 2 = 2`.
        - `(2, 4)` -> `G[2] ^ G[4] = 0 ^ 0 = 0`.
        - `(3, 3)` -> Invalid.
    - Set: `{0, 2}`.
    - Mex({0, 2}) = 1.
    - `G[6] = 1`.

**Conclusion:** `G[6] = 1 > 0`. Output: "First".

## ✅ Proof of Correctness

The Sprague-Grundy theorem guarantees that any impartial game is equivalent to a Nim pile of size `G(state)`.
- A state is losing iff `G(state) == 0`.
- A state is winning iff `G(state) > 0`.
By computing `G(n)` using the mex rule over all reachable states (which are XOR sums of sub-games), we correctly determine the winner.

## 💡 Interview Extensions

- **Extension 1:** What if we can split into equal piles too?
  - *Answer:* Then `G(4)` would include `G(2)^G(2) = 0`.
- **Extension 2:** What if we have multiple piles initially?
  - *Answer:* Calculate `G(n_i)` for each pile and XOR them all.

### Common Mistakes

1.  **Assuming Odd/Even Pattern:**
    - ❌ Wrong: Thinking odd is win, even is lose. `G(6)=1` (Win), `G(4)=0` (Lose).
    - ✅ Correct: Must calculate Grundy values.
2.  **Forgetting XOR:**
    - ❌ Wrong: Trying to just check if *any* split leads to a losing state without full Grundy logic.
    - ✅ Correct: XOR is needed because the game splits into independent subgames.
3.  **Invalid Splits:**
    - ❌ Wrong: Splitting `4` into `2+2`.
    - ✅ Correct: Piles must be of **different** sizes.
4.  **Base Cases:**
    - ❌ Wrong: `G[0]=1`.
    - ✅ Correct: `G[0]=0` (Losing).

## Related Concepts

- **Mex Function**
- **XOR Sum**
- **Game States (P-position, N-position)**
