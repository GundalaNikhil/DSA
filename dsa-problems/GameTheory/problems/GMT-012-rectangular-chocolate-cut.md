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
time_limit: 1000
memory_limit: 256
---

# GMT-012: Rectangular Chocolate Cut

## Problem Statement

You are given a rectangular bar of chocolate of size `R x C` (R rows, C columns).
Two players take turns making a cut.
In each turn, a player must:

1.  Choose one piece of chocolate currently on the table.
2.  Make a straight cut along a grid line (horizontal or vertical) to split it into two smaller rectangular pieces.
3.  Both new pieces remain in play.

The game ends when all pieces are of size `1 x 1` (no more cuts possible).
The player who cannot make a valid move loses.

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-012/problem-illustration.png)

## Input Format

- The first line contains two integers `R` and `C`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= R, C <= 10^9`

## Example

**Input:**

```
2 2
```

**Output:**

```
First
```

**Explanation:**

- Start: One `2x2` piece.
- P1 cuts horizontally -> Two `1x2` pieces.
- P2 must choose one `1x2` piece and cut it -> One `1x1`, one `1x1`, one `1x2`.
- P1 cuts the remaining `1x2` -> Four `1x1` pieces.
- No more cuts. P2 loses.
- Total moves: 3. P1 made the last move.

![Example Visualization](../images/GMT-012/example-1.png)

## Notes

- The game is impartial.
- The total number of cuts is fixed regardless of strategy.
- A rectangular piece of size `R x C` (area = `R*C`) requires exactly `R*C - 1` cuts to reduce to all `1x1` pieces.
  - Example: `2x2` piece (area 4) requires 3 cuts.
  - Example: `1x3` piece (area 3) requires 2 cuts.
- Since the total number of moves is always `Area - 1`, the winner is determined by the parity of `R*C - 1`:
  - If `R*C - 1` is odd → First player wins
  - If `R*C - 1` is even → Second player wins
- Equivalently:
  - If `R*C` is even → First player wins
  - If `R*C` is odd → Second player wins

## Related Topics

Game Theory, Parity Analysis

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String chocolateCut(long R, long C) {
        // Implementation here
        return "";
    }
}

class Main {
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
import sys

def chocolate_cut(R: int, C: int) -> str:
    # Implementation here
    return ""

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
        // Implementation here
        return {};
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
    // Implementation here
    return null;
  }
}

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
