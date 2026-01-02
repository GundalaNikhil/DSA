---
problem_id: GMT_COIN_SPLIT__4721
display_id: GMT-014
slug: greedy-coin-split-game
title: "Greedy Coin Split Game"
difficulty: Medium
difficulty_score: 65
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - minimax
  - memoization
  - interval-dp
premium: true
subscription_tier: basic
time_limit: 1000
memory_limit: 256
---

# GMT-014: Greedy Coin Split Game

## Problem Statement

You are given `N` coins arranged in a row, each with a value `A[i]`.
Two players take turns playing a game.
In each turn, the current player (Splitter) must:
1.  Split the current row of coins into two non-empty contiguous segments (Left and Right).
2.  The other player (Chooser) then chooses one segment to **keep** (adds the sum of values in that segment to their score).
3.  The remaining segment stays on the table for the next turn.
4.  The roles swap: The Chooser becomes the Splitter for the next turn.

The game ends when the remaining segment has only 1 coin (cannot be split). This last coin is discarded.
Both players play optimally to maximize their own score minus the opponent's score.

Determine the final score difference (Player 1 Score - Player 2 Score).

![Problem Illustration](../images/GMT-014/problem-illustration.png)

## Input Format

- The first line contains an integer `N`.
- The second line contains `N` space-separated integers `A[i]`.

## Output Format

- Return the final score difference.

## Constraints

- `2 <= N <= 100`
- `1 <= A[i] <= 1000`

## Example

**Input:**
```
3
10 20 30
```

**Output:**
```
-30
```

**Explanation:**
- If P1 splits `10 | 20,30`, P2 keeps `20,30` for 50 and the game ends. Diff = -50.
- If P1 splits `10,20 | 30`, P2 keeps `10,20` for 30 and the game ends. Diff = -30.
- P1 chooses the better outcome, so the final score difference is `-30`.

![Example Visualization](../images/GMT-014/example-1.png)

## Notes

- Use Interval DP.
- Prefix sums allow `O(1)` sum calculation.
- Total complexity `O(N^3)`.

## Related Topics

Game Theory, Interval DP, Prefix Sums

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int coinSplit(int n, int[] A) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] A = new int[n];
            for (int i = 0; i < n; i++) {
                A[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.coinSplit(n, A));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

def coin_split(n: int, A: List[int]) -> int:
    # Implementation here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        A = []
        for _ in range(n):
            A.append(int(next(iterator)))
            
        print(coin_split(n, A))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int coinSplit(int n, vector<int>& A) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }
        
        Solution solution;
        cout << solution.coinSplit(n, A) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  coinSplit(n, A) {
    // Implementation here
    return null;
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
  
  const A = [];
  for (let i = 0; i < n; i++) {
      A.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.coinSplit(n, A));
});
```
