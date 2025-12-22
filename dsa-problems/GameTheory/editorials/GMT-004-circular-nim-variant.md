---
problem_id: GMT_CIRCULAR_NIM_VARIANT__4829
display_id: GMT-004
slug: circular-nim-variant
title: "Circular Nim Variant"
difficulty: Medium
difficulty_score: 55
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - impartial-game
  - memoization
  - cycle-detection
premium: true
subscription_tier: basic
---

# GMT-004: Circular Nim Variant

## 📋 Problem Summary

Players remove stones from a pile in a circle and add 1 stone to each adjacent pile. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Ripple Effect

Imagine a resource distribution network where taking resources from one node causes a slight overflow into neighboring nodes. You want to drain the network (or force the other operator to be unable to act), but every action has a side effect that might prolong the game.

**Why This Problem Matters:**

- **Side Effects:** Standard Nim moves are independent. Here, moves affect other parts of the state.
- **Cycles:** The "add" rule introduces the possibility of infinite games, requiring cycle detection.

![Real-World Application](../images/GMT-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Move Dynamics

```
State: [1, 0, 1] (Triangle)

Move on Index 0 (Size 1):
  - Remove 1 -> Size 0.
  - Add 1 to Index 2 (Left) -> 1+1=2.
  - Add 1 to Index 1 (Right) -> 0+1=1.
  - New State: [0, 1, 2].

Effect:
  - Total stones changed from 2 to 3.
  - Game state complexity increases.
```

## ✅ Input/Output Clarifications

- **Adjacent:** `(i-1+n)%n` and `(i+1)%n`.
- **Draw:** If the game enters a loop of states.

## Optimal Approach

### Key Insight

Since `n` and `piles[i]` are small, we can use **Memoization with State Tracking**.
We map each state (tuple of pile sizes) to a result: WIN, LOSS, DRAW.
- **WIN:** There exists a move to a LOSS state.
- **LOSS:** All moves lead to WIN states (or no moves).
- **DRAW:** No move to LOSS, but some move to DRAW (and others to WIN).

### Algorithm

1.  Use a Map `memo` to store results for states.
2.  Use a Set `visiting` to detect cycles in the current recursion stack.
3.  `solve(state)`:
    - If `state` in `memo`, return result.
    - If `state` in `visiting`, return DRAW (cycle detected).
    - Add `state` to `visiting`.
    - `canReachLoss = False`
    - `canReachDraw = False`
    - For each pile `i` > 0:
        - For `k` from 1 to `piles[i]`:
            - Create `next_state`.
            - `res = solve(next_state)`
            - If `res == LOSS`: `canReachLoss = True`.
            - If `res == DRAW`: `canReachDraw = True`.
    - Remove `state` from `visiting`.
    - If `canReachLoss`: Result = WIN.
    - Else if `canReachDraw`: Result = DRAW.
    - Else: Result = LOSS.
    - Store in `memo` and return.

### Time Complexity

- **Exponential**: The state space can be large. However, for small inputs, it's feasible. The "add 1" rule might limit the depth effectively or lead to quick cycles.

### Space Complexity

- **O(States)**: To store memoization table.

![Algorithm Visualization](../images/GMT-004/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    Map<String, String> memo = new HashMap<>();
    Set<String> visiting = new HashSet<>();

    public String circularNim(int n, int[] piles) {
        return solve(n, piles);
    }

    private String solve(int n, int[] piles) {
        String key = Arrays.toString(piles);
        if (memo.containsKey(key)) return memo.get(key);
        if (visiting.contains(key)) return "Draw";

        visiting.add(key);
        boolean canReachLoss = false;
        boolean canReachDraw = false;
        boolean hasMoves = false;

        for (int i = 0; i < n; i++) {
            if (piles[i] > 0) {
                for (int k = 1; k <= piles[i]; k++) {
                    hasMoves = true;
                    int[] nextPiles = piles.clone();
                    nextPiles[i] -= k;
                    nextPiles[(i - 1 + n) % n]++;
                    nextPiles[(i + 1) % n]++;
                    
                    // Optimization: Sort or canonicalize if rotationally symmetric?
                    // For now, keep as is.
                    
                    String res = solve(n, nextPiles);
                    if (res.equals("Second")) {
                        canReachLoss = true;
                        break; // Found a winning move
                    }
                    if (res.equals("Draw")) {
                        canReachDraw = true;
                    }
                }
                if (canReachLoss) break;
            }
        }

        visiting.remove(key);
        String result;
        if (canReachLoss) result = "First";
        else if (!hasMoves) result = "Second"; // No moves -> Loss
        else if (canReachDraw) result = "Draw";
        else result = "Second"; // All moves lead to First (Win for opponent)

        memo.put(key, result);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] piles = new int[n];
            for (int i = 0; i < n; i++) {
                piles[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.circularNim(n, piles));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List, Tuple

def circular_nim(n: int, piles: List[int]) -> str:
    memo = {}
    visiting = set()

    def solve(current_piles: Tuple[int], depth: int) -> str:
        if depth > 50:
            return "Draw"
        if current_piles in memo:
            return memo[current_piles]
        if current_piles in visiting:
            return "Draw"
        
        visiting.add(current_piles)
        
        can_reach_loss = False
        can_reach_draw = False
        has_moves = False
        
        for i in range(n):
            if current_piles[i] > 0:
                for k in range(1, current_piles[i] + 1):
                    has_moves = True
                    next_piles = list(current_piles)
                    next_piles[i] -= k
                    next_piles[(i - 1 + n) % n] += 1
                    next_piles[(i + 1) % n] += 1
                    
                    res = solve(tuple(next_piles), depth + 1)
                    
                    if res == "Second":
                        can_reach_loss = True
                        break
                    if res == "Draw":
                        can_reach_draw = True
                if can_reach_loss:
                    break
        
        visiting.remove(current_piles)
        
        if can_reach_loss:
            result = "First"
        elif not has_moves:
            result = "Second"
        elif can_reach_draw:
            result = "Draw"
        else:
            result = "Second"
            
        memo[current_piles] = result
        return result

    return solve(tuple(piles), 0)

def main():
    import sys
    # Increase recursion depth
    sys.setrecursionlimit(20000)
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        piles = []
        for _ in range(n):
            piles.append(int(next(iterator)))
            
        print(circular_nim(n, piles))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

class Solution {
    map<vector<int>, string> memo;
    set<vector<int>> visiting;

public:
    string circularNim(int n, vector<int>& piles) {
        return solve(n, piles);
    }

    string solve(int n, vector<int>& piles) {
        if (memo.count(piles)) return memo[piles];
        if (visiting.count(piles)) return "Draw";

        visiting.insert(piles);
        bool canReachLoss = false;
        bool canReachDraw = false;
        bool hasMoves = false;

        for (int i = 0; i < n; i++) {
            if (piles[i] > 0) {
                for (int k = 1; k <= piles[i]; k++) {
                    hasMoves = true;
                    vector<int> nextPiles = piles;
                    nextPiles[i] -= k;
                    nextPiles[(i - 1 + n) % n]++;
                    nextPiles[(i + 1) % n]++;

                    string res = solve(n, nextPiles);
                    if (res == "Second") {
                        canReachLoss = true;
                        break;
                    }
                    if (res == "Draw") {
                        canReachDraw = true;
                    }
                }
                if (canReachLoss) break;
            }
        }

        visiting.erase(piles);
        string result;
        if (canReachLoss) result = "First";
        else if (!hasMoves) result = "Second";
        else if (canReachDraw) result = "Draw";
        else result = "Second";

        return memo[piles] = result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> piles(n);
        for (int i = 0; i < n; i++) {
            cin >> piles[i];
        }
        
        Solution solution;
        cout << solution.circularNim(n, piles) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  constructor() {
    this.memo = new Map();
    this.visiting = new Set();
  }

  circularNim(n, piles) {
    return this.solve(n, piles);
  }

  solve(n, piles) {
    const key = piles.join(",");
    if (this.memo.has(key)) return this.memo.get(key);
    if (this.visiting.has(key)) return "Draw";

    this.visiting.add(key);
    let canReachLoss = false;
    let canReachDraw = false;
    let hasMoves = false;

    for (let i = 0; i < n; i++) {
      if (piles[i] > 0) {
        for (let k = 1; k <= piles[i]; k++) {
          hasMoves = true;
          const nextPiles = [...piles];
          nextPiles[i] -= k;
          nextPiles[(i - 1 + n) % n]++;
          nextPiles[(i + 1) % n]++;

          const res = this.solve(n, nextPiles);
          if (res === "Second") {
            canReachLoss = true;
            break;
          }
          if (res === "Draw") {
            canReachDraw = true;
          }
        }
        if (canReachLoss) break;
      }
    }

    this.visiting.delete(key);
    let result;
    if (canReachLoss) result = "First";
    else if (!hasMoves) result = "Second";
    else if (canReachDraw) result = "Draw";
    else result = "Second";

    this.memo.set(key, result);
    return result;
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
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  
  const piles = [];
  for (let i = 0; i < n; i++) {
      piles.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.circularNim(n, piles));
});
```

## 🧪 Test Case Walkthrough

**Input:** `[1, 0, 1]`

1.  Start `[1, 0, 1]`.
2.  Move 1: Remove 1 from index 0. Add to 2, 1. -> `[0, 1, 2]`.
3.  From `[0, 1, 2]`:
    - Move 1: Remove 1 from index 1. Add to 0, 2. -> `[1, 0, 3]`.
    - Move 2: Remove 1 from index 2. Add to 1, 0. -> `[1, 2, 1]`.
    - Move 3: Remove 2 from index 2. Add to 1, 0. -> `[1, 2, 0]`.
4.  Recursion continues. Eventually, we find that `[1, 0, 1]` can reach a state that forces the opponent to lose.

## ✅ Proof of Correctness

- **Memoization:** Ensures we don't recompute states.
- **Cycle Detection:** `visiting` set correctly identifies loops, returning "Draw".
- **Minimax Logic:** Correctly propagates Win/Loss/Draw up the recursion tree.

## 💡 Interview Extensions

- **Extension 1:** What if `n` is large?
  - *Answer:* The state space explodes. We'd need a mathematical pattern or simpler rule.
- **Extension 2:** What if we add to *all* other piles?
  - *Answer:* Different game, likely different strategy.

### C++ommon Mistakes

1.  **Infinite Recursion:**
    - ❌ Wrong: Not handling cycles.
2.  **Incorrect Adjacency:**
    - ❌ Wrong: `(i-1)%n` in Python/Java can be negative. Use `(i-1+n)%n`.

## Related Concepts

- **Memoization**
- **Graph Cycles**
- **Minimax**
