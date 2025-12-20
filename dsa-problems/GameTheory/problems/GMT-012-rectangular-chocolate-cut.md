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
- The total number of cuts is fixed regardless of strategy?
  - A `R x C` piece requires `R*C - 1` cuts to reduce to `1x1`s?
  - Let's check.
  - `2x2` (Area 4). Cuts: 3. `4-1=3`.
  - `1x3` (Area 3). Cuts: `1x3 -> 1x1, 1x2 -> 1x1, 1x1, 1x1`. Total 2 cuts. `3-1=2`.
  - Yes, the total number of cuts is always `Area - 1`.
- Wait, if total moves is fixed, then the winner is determined solely by `(R*C - 1) % 2`.
- If `Area - 1` is Odd -> First wins.
- If `Area - 1` is Even -> Second wins.
- `Area - 1` Odd <=> `Area` Even.
- So if `R*C` is Even, First wins.
- If `R*C` is Odd, Second wins.
- This matches my Grundy analysis! `G = 1 - (Area % 2)`.

## Related Topics

Game Theory, Parity Analysis

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String chocolateCut(long R, long C) {
        // Your implementation here
        return "Second";
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
    # Your implementation here
    return "Second"

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
        // Your implementation here
        return "Second";
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
    // Your implementation here
    return "Second";
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
