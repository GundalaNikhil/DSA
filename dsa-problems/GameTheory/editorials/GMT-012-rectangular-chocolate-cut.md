---
problem_id: GMT_CHOCOLATE_CUT__8392
display_id: GMT-012
slug: rectangular-chocolate-cut
title: "Rectangular Chocolate Cut"
difficulty: Easy
difficulty_score: 30
topics:
  - Game Theory
  - Math
tags:
  - impartial-game
  - sprague-grundy
  - parity
premium: true
subscription_tier: basic
---

# GMT-012: Rectangular Chocolate Cut

## 📋 Problem Summary

Cut a `R x C` chocolate into `1 x 1` pieces. Last player to cut wins.

## 🌍 Real-World Scenario

**Scenario Title:** The Glass Cutter.

You are cutting a large sheet of glass into unit squares for a mosaic.
- Every cut takes energy.
- You and your rival are competing to see who does the last cut (maybe getting paid for finishing the job).
- The total work is fixed!

![Real-World Application](../images/GMT-012/real-world-scenario.png)

## Detailed Explanation

### Key Insight: Fixed Number of Moves

This is a "Shear Game" or "Breaking Game".
Notice that every cut increases the number of pieces by exactly 1.
- Start: 1 piece.
- End: `R * C` pieces (all `1x1`).
- Total cuts needed = `(R * C) - 1`.

Since the total number of moves is fixed and independent of the strategy (order of cuts), the winner is determined solely by the parity of the total moves.
- If `Total Moves` is Odd -> First Player makes moves 1, 3, 5... -> Last move. First Wins.
- If `Total Moves` is Even -> Second Player makes moves 2, 4, 6... -> Last move. Second Wins.

### Formula

- `Moves = R * C - 1`.
- If `(R * C - 1)` is Odd => `R * C` is Even.
- If `(R * C - 1)` is Even => `R * C` is Odd.

So:
- If `R * C` is Even -> First Wins.
- If `R * C` is Odd -> Second Wins.

### Why does this work?

This is a rare impartial game where the game length is invariant.
Usually, games can end quickly or slowly.
Here, you CANNOT reach the end state (`1x1`s) without making exactly `R*C - 1` cuts.
Every cut splits one piece into two. To get `N` pieces from 1, you need `N-1` splits.

### Complexity

- **Time:** `O(1)`.
- **Space:** `O(1)`.

![Algorithm Visualization](../images/GMT-012/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public String chocolateCut(long R, long C) {
        long area = R * C;
        return (area % 2 == 0) ? "First" : "Second";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long R = sc.nextLong();
            long C = sc.nextLong();

            Solution solution = new Solution();
            System.out.println(solution.chocolateCut(R, C));
        }
        sc.close();
    }
}
```

### Python

```python
def chocolate_cut(R: int, C: int) -> str:
    area = R * C
    return "First" if area % 2 == 0 else "Second"

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
            
        print(chocolate_cut(R, C))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string chocolateCut(long long R, long long C) {
        long long area = R * C;
        return (area % 2 == 0) ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long R, C;
    if (cin >> R >> C) {
        Solution solution;
        cout << solution.chocolateCut(R, C) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  chocolateCut(R, C) {
    const area = R * C;
    return (area % 2n === 0n) ? "First" : "Second";
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
  const R = BigInt(flatData[idx++]);
  const C = BigInt(flatData[idx++]);

  const solution = new Solution();
  console.log(solution.chocolateCut(R, C));
});
```

## 🧪 Test Case Walkthrough

**Input:** `2 2`
Area = 4 (Even).
Result: First.

**Input:** `3 3`
Area = 9 (Odd).
Result: Second.

## ✅ Proof of Correctness

- **Invariant:** Number of cuts = `Area - 1`.
- **Parity:** Winner depends only on `(Area - 1) % 2`.

## 💡 Interview Extensions

- **Extension 1:** What if we can cut multiple pieces at once (stacking)?
  - *Answer:* Then it becomes Nim with pile sizes `log2(R)` and `log2(C)`? No, much harder.
- **Extension 2:** What if we discard one piece?
  - *Answer:* Then it's Nim with `R-1` and `C-1`.

### C++ommon Mistakes

1.  **Overthinking:**
    - ❌ Wrong: Trying to use Sprague-Grundy or DP.
    - ✅ Correct: Realizing total moves is fixed.
2.  **Off-by-one:**
    - ❌ Wrong: Thinking Even Area means Even Moves.
    - ✅ Correct: Even Area means Odd Moves (First wins).

## Related Concepts

- **Game Invariants**
- **Parity**
