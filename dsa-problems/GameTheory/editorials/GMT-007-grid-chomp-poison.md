---
problem_id: GMT_GRID_CHOMP_POISON__7391
display_id: GMT-007
slug: grid-chomp-poisoned
title: "Grid Chomp with Poisoned Cells"
difficulty: Hard
difficulty_score: 60
topics:
  - Game Theory
  - Dynamic Programming
  - Bitmask
tags:
  - impartial-game
  - memoization
  - state-compression
premium: true
subscription_tier: basic
---

# GMT-007: Grid Chomp with Poisoned Cells

## 📋 Problem Summary

Play Chomp on an `R x C` grid with poisoned cells. You cannot make a move that eats a poisoned cell. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Minefield Cleanup

Imagine clearing a field of mines (poisoned cells). You can clear rectangular areas starting from a point to the boundary. However, you must not trigger any mines. The person who cannot make a safe clearance move is stuck and loses.

**Why This Problem Matters:**

- **Constrained Moves:** Shows how constraints (poison) reshape the game tree.
- **State Representation:** Teaches how to represent complex grid states (Young Diagrams) efficiently.

![Real-World Application](../images/GMT-007/real-world-scenario.png)

## Detailed Explanation

### Young Diagram State

```
Grid 3x3
State represented by column heights: [3, 2, 1]
X X X
X X .
X . .

Move at (1, 1):
- Remove (x>=1, y>=1).
- (1, 1) is removed.
- New heights: [3, 1, 1]
X X X
X . .
X . .
```

## ✅ Input/Output Clarifications

- **Poisoned Cell:** If `(pr, pc)` is poison, you cannot pick `(r, c)` if `pr >= r` and `pc >= c`.
- **Loss:** No valid moves available.

## Optimal Approach

### Key Insight

The state of the game is always defined by the heights of the columns `h[0], h[1], ..., h[C-1]`, where `R >= h[0] >= h[1] >= ... >= h[C-1] >= 0`.
This is because removing a rectangle `(r, c)` cuts the heights of columns `c` through `C-1` to be at most `r`.
We can memoize this state.
Since `R, C <= 8`, we can encode the state tuple into a Map or Integer (if small enough).
For `R, C <= 8`, the number of states is `(R+C) choose R` = `16 choose 8` = `12870`. Very small!
We can simply use a Map.

### Algorithm

1.  Identify all poisoned cells.
2.  Initial state: `[R, R, ..., R]` (C times).
3.  `solve(state)`:
    - If `state` in `memo`, return.
    - Iterate all possible moves `(r, c)`:
        - `c` from `0` to `C-1`.
        - `r` from `0` to `state[c]-1`.
        - Check if move `(r, c)` is valid (doesn't eat poison).
            - A move `(r, c)` eats poison `(pr, pc)` if `pr >= r` and `pc >= c`.
            - So `(r, c)` is valid if for ALL poisons `(pr, pc)`, NOT (`pr >= r` and `pc >= c`).
        - If valid, compute `next_state`:
            - `new_h[i] = min(state[i], r)` for `i` from `c` to `C-1`.
            - `new_h[i] = state[i]` for `i < c`.
        - If `!solve(next_state)`, then `state` is Winning.
    - If no move leads to Losing, `state` is Losing.

### Time Complexity

- **O(States * R * C)**: Number of states is small (~13k). Transitions `R*C`. Total operations ~10^6.

### Space Complexity

- **O(States)**: To store memoization.

![Algorithm Visualization](../images/GMT-007/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    Map<List<Integer>, Boolean> memo = new HashMap<>();
    int[][] poisons;
    int K;

    public String chompGame(int R, int C, int[][] poisons) {
        this.poisons = poisons;
        this.K = poisons.length;
        List<Integer> initialState = new ArrayList<>();
        for (int i = 0; i < C; i++) initialState.add(R);
        
        return canWin(initialState) ? "First" : "Second";
    }

    private boolean canWin(List<Integer> state) {
        if (memo.containsKey(state)) return memo.get(state);

        boolean canReachLosing = false;
        int C = state.size();

        // Try all possible moves (r, c)
        // A move is valid if r < state[c] (cell exists)
        // AND it doesn't eat any poison
        for (int c = 0; c < C; c++) {
            for (int r = 0; r < state.get(c); r++) {
                if (isValid(r, c)) {
                    List<Integer> nextState = new ArrayList<>(state);
                    // Update heights for columns >= c
                    for (int i = c; i < C; i++) {
                        nextState.set(i, Math.min(nextState.get(i), r));
                    }
                    
                    // Optimization: If state didn't change, it's not a move (eating nothing)
                    // But here r < state[c], so we always remove at least (r, c).
                    
                    if (!canWin(nextState)) {
                        canReachLosing = true;
                        break;
                    }
                }
            }
            if (canReachLosing) break;
        }

        memo.put(state, canReachLosing);
        return canReachLosing;
    }

    private boolean isValid(int r, int c) {
        for (int[] p : poisons) {
            if (p[0] >= r && p[1] >= c) return false;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int R = sc.nextInt();
            int C = sc.nextInt();
            int K = sc.nextInt();
            int[][] poisons = new int[K][2];
            for (int i = 0; i < K; i++) {
                poisons[i][0] = sc.nextInt();
                poisons[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.chompGame(R, C, poisons));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List, Tuple

def chomp_game(R: int, C: int, poisons: List[List[int]]) -> str:
    memo = {}
    
    def is_valid(r, c):
        for pr, pc in poisons:
            if pr >= r and pc >= c:
                return False
        return True

    def can_win(state: Tuple[int]) -> bool:
        if state in memo:
            return memo[state]
        
        # Try all moves
        for c in range(C):
            for r in range(state[c]):
                if is_valid(r, c):
                    # Construct next state
                    next_state_list = list(state)
                    for i in range(c, C):
                        next_state_list[i] = min(next_state_list[i], r)
                    next_state = tuple(next_state_list)
                    
                    if not can_win(next_state):
                        memo[state] = True
                        return True
        
        memo[state] = False
        return False

    initial_state = tuple([R] * C)
    return "First" if can_win(initial_state) else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        R = int(next(iterator))
        C = int(next(iterator))
        K = int(next(iterator))
        poisons = []
        for _ in range(K):
            r = int(next(iterator))
            c = int(next(iterator))
            poisons.append([r, c])
            
        print(chomp_game(R, C, poisons))
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
#include <algorithm>

using namespace std;

class Solution {
    map<vector<int>, bool> memo;
    vector<vector<int>> poisons;

    bool isValid(int r, int c) {
        for (const auto& p : poisons) {
            if (p[0] >= r && p[1] >= c) return false;
        }
        return true;
    }

    bool canWin(vector<int>& state) {
        if (memo.count(state)) return memo[state];

        int C = state.size();
        bool canReachLosing = false;

        for (int c = 0; c < C; c++) {
            for (int r = 0; r < state[c]; r++) {
                if (isValid(r, c)) {
                    vector<int> nextState = state;
                    for (int i = c; i < C; i++) {
                        nextState[i] = min(nextState[i], r);
                    }
                    if (!canWin(nextState)) {
                        canReachLosing = true;
                        goto end;
                    }
                }
            }
        }
        end:;

        return memo[state] = canReachLosing;
    }

public:
    string chompGame(int R, int C, vector<vector<int>>& poisons) {
        this->poisons = poisons;
        vector<int> initialState(C, R);
        return canWin(initialState) ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int R, C, K;
    if (cin >> R >> C >> K) {
        vector<vector<int>> poisons(K, vector<int>(2));
        for (int i = 0; i < K; i++) {
            cin >> poisons[i][0] >> poisons[i][1];
        }
        
        Solution solution;
        cout << solution.chompGame(R, C, poisons) << "\n";
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
  }

  chompGame(R, C, poisons) {
    this.poisons = poisons;
    const initialState = new Array(C).fill(R);
    return this.canWin(initialState) ? "First" : "Second";
  }

  canWin(state) {
    const key = state.join(",");
    if (this.memo.has(key)) return this.memo.get(key);

    let canReachLosing = false;
    const C = state.length;

    for (let c = 0; c < C; c++) {
      for (let r = 0; r < state[c]; r++) {
        if (this.isValid(r, c)) {
          const nextState = [...state];
          for (let i = c; i < C; i++) {
            nextState[i] = Math.min(nextState[i], r);
          }
          
          if (!this.canWin(nextState)) {
            canReachLosing = true;
            break;
          }
        }
      }
      if (canReachLosing) break;
    }

    this.memo.set(key, canReachLosing);
    return canReachLosing;
  }

  isValid(r, c) {
    for (const [pr, pc] of this.poisons) {
      if (pr >= r && pc >= c) return false;
    }
    return true;
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
  const R = parseInt(flatData[idx++]);
  const C = parseInt(flatData[idx++]);
  const K = parseInt(flatData[idx++]);
  
  const poisons = [];
  for (let i = 0; i < K; i++) {
      const r = parseInt(flatData[idx++]);
      const c = parseInt(flatData[idx++]);
      poisons.push([r, c]);
  }

  const solution = new Solution();
  console.log(solution.chompGame(R, C, poisons));
});
```

## 🧪 Test Case Walkthrough

**Input:** `2x2` Grid, Poison at `(0, 0)`.

**Step-by-Step Execution:**

1.  **Initial State:** `[2, 2]` (Col 0 height 2, Col 1 height 2).
2.  **Possible Moves from `[2, 2]`:**
    - Pick `(1, 1)`: Reduces Col 1 to height 1. New State: `[2, 1]`.
    - Pick `(0, 1)`: Reduces Col 1 to height 0. New State: `[2, 0]`.
    - Pick `(1, 0)`: Reduces Col 0 to height 1, Col 1 to height 0. New State: `[1, 0]`? No.
      - `(1, 0)` sets `h[0] = min(2, 1) = 1`. `h[1] = min(2, 1) = 1`. New State: `[1, 1]`.
    - Pick `(0, 0)`: Invalid (Poison).

3.  **Analyze Next States:**
    - **Analyze `[2, 1]`:**
        - Moves:
            - `(0, 1)` -> `[2, 0]`.
            - `(1, 0)` -> `[1, 1]`.
        - If `[2, 0]` and `[1, 1]` are Winning, then `[2, 1]` is **Losing**.
    - **Analyze `[2, 0]`:**
        - Moves:
            - `(1, 0)` -> `[1, 0]`.
        - If `[1, 0]` is Losing, then `[2, 0]` is **Winning**.
    - **Analyze `[1, 1]`:**
        - Moves:
            - `(0, 1)` -> `[1, 0]`.
        - If `[1, 0]` is Losing, then `[1, 1]` is **Winning**.
    - **Analyze `[1, 0]`:**
        - Moves:
            - `(0, 0)` is Poison. No valid moves.
        - **Losing State**.

4.  **Backpropagate Results:**
    - `[1, 0]` is **Losing**.
    - `[2, 0]` -> `[1, 0]` (Losing). So `[2, 0]` is **Winning**.
    - `[1, 1]` -> `[1, 0]` (Losing). So `[1, 1]` is **Winning**.
    - `[2, 1]` -> `[2, 0]` (Winning) and `[1, 1]` (Winning). All moves lead to Winning. So `[2, 1]` is **Losing**.
    - `[2, 2]` -> `[2, 1]` (Losing). So `[2, 2]` is **Winning**.

**Conclusion:** First player wins by picking `(1, 1)`.

## ✅ Proof of Correctness

- **State Representation:** Young Diagrams cover all reachable states.
- **Memoization:** Handles overlapping subproblems.
- **Small Constraints:** `R, C <= 8` ensures feasible state space.

## 💡 Interview Extensions

- **Extension 1:** What if `R, C` are large?
  - *Answer:* Unsolved problem.
- **Extension 2:** What if we can eat non-rectangular shapes?
  - *Answer:* State representation becomes complex (bitmask of all cells).

### Common Mistakes

1.  **Invalid Moves:**
    - ❌ Wrong: Thinking `(1, 0)` eats `(0, 0)`. It doesn't. `(1, 0)` eats `(r>=1, c>=0)`.
    - ✅ Correct: Check `pr >= r` AND `pc >= c`.
2.  **Poison Logic:**
    - ❌ Wrong: Checking if `(r, c)` IS poison.
    - ✅ Correct: Must check if `(r, c)` **EATS** any poison.
3.  **State Updates:**
    - ❌ Wrong: Only updating column `c`.
    - ✅ Correct: Must update all columns `i >= c` because the rectangle extends to the right boundary. `h[i] = min(h[i], r)`.
4.  **Base Case:**
    - ❌ Wrong: Assuming empty grid is Winning.
    - ✅ Correct: Empty grid (or grid with only poisons) has no moves, so it is Losing.

## Related Concepts

- **Young Tableaux**
- **Partitions**
