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
time_limit: 2000
memory_limit: 256
---

# GMT-004: Circular Nim Variant

## Problem Statement

You are given `n` piles of stones arranged in a circle, indexed from `0` to `n-1`.
Two players take turns making moves.
In each turn, a player must choose a pile `i` that has at least one stone (`piles[i] > 0`).
The player removes `k` stones from pile `i` (where `1 <= k <= piles[i]`).
Then, the player **adds 1 stone** to each of the adjacent piles `(i-1)%n` and `(i+1)%n`.
(Note: Indices are modulo `n`. For `n=1`, there are no distinct adjacent piles, so no stones are added? Assume `n >= 3` for circular adjacency, or standard neighbors modulo n).

The player who cannot make a valid move loses.
If the game goes on forever (cycle), it is considered a Draw.

Determine the winner given the initial configuration. Output "First", "Second", or "Draw".

![Problem Illustration](../images/GMT-004/problem-illustration.png)

## Input Format

- The first line contains an integer `n`.
- The second line contains `n` space-separated integers representing the initial number of stones in each pile.

## Output Format

- Return "First", "Second", or "Draw".

## Constraints

- `3 <= n <= 20`
- `0 <= piles[i] <= 15`
- The total number of stones in any reachable state will not exceed reasonable limits for the provided test cases.

## Example

**Input:**
```
3
1 0 1
```

**Output:**
```
First
```

**Explanation:**
- Piles: `[1, 0, 1]` (indices 0, 1, 2).
- Player 1 chooses index 0. Removes 1. Adds to 2 and 1.
  - New state: `[0, 1, 2]`.
- From `[0, 1, 2]`, Player 2 must move.
  - If P2 picks index 1 (size 1): Remove 1. Add to 0, 2. -> `[1, 0, 3]`.
  - If P2 picks index 2 (size 2):
    - Remove 1 -> `[0, 2, 1]`.
    - Remove 2 -> `[0, 2, 0]`.
- It turns out that from `[1, 0, 1]`, Player 1 can force a win.

![Example Visualization](../images/GMT-004/example-1.png)

## Notes

- The "add to adjacent" rule can increase the total number of stones.
- Use memoization to handle states and detect cycles.

## Related Topics

Game Theory, Memoization, Graph Cycle Detection

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    Map<String, String> memo = new HashMap<>();
    Set<String> visiting = new HashSet<>();

    public String circularNim(int n, int[] piles) {
        return "";
    }

    private String solve(int n, int[] piles, int depth) {
        if (depth > 50) return "Draw";
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
                    piles[i] -= k;
                    piles[(i - 1 + n) % n]++;
                    piles[(i + 1) % n]++;
                    
                    String res = solve(n, piles, depth + 1);
                    
                    piles[(i + 1) % n]--;
                    piles[(i - 1 + n) % n]--;
                    piles[i] += k;

                    if (res.equals("Second")) {
                        canReachLoss = true;
                        break;
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

class Main {
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
    return ""
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
        return "";
    }

    string solve(int n, vector<int>& piles, int depth) {
        return "";
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
    return 0;
  }

  solve(n, piles, depth) {
    return 0;
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

