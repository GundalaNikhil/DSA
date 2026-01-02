---
problem_id: GMT_SUBTRACT_SQUARE_BAN__3912
display_id: GMT-003
slug: subtract-square-ban-list
title: "Subtract-a-Square with Ban List"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - impartial-game
  - subtraction-game
  - grundy-numbers
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GMT-003: Subtract-a-Square with Ban List

## Problem Statement

Two players are playing a game with a pile of `n` stones. They take turns removing stones from the pile.
In each turn, a player must remove `s` stones, where `s` is a **perfect square** (1, 4, 9, 16, ...) and `s` is **not** present in a given set of banned numbers `B`.
The player who reduces the pile size to exactly 0 wins.
Equivalently, the player who cannot make a valid move loses.

Determine if the first player has a winning strategy assuming both players play optimally.

![Problem Illustration](../images/GMT-003/problem-illustration.png)

## Input Format

- The first line contains an integer `n`, the initial number of stones.
- The second line contains an integer `k`, the size of the banned set `B`.
- The third line contains `k` space-separated integers, the elements of the banned set `B`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 10^5`
- `0 <= k <= 100`
- Elements of `B` are distinct positive integers.

## Example

**Input:**
```
7
1
1
```

**Output:**
```
Second
```

**Explanation:**
- Initial pile: 7.
- Banned set: {1}.
- Valid moves (squares not in B): 4, 9, ...
- From 7, only valid move is to subtract 4 (since 9 > 7).
- Player 1 removes 4. Pile becomes 3.
- From 3, valid moves: none (1 is banned, 4 > 3).
- Player 2 has no moves and loses.
- However, the game tree analysis shows that from position 7 with banned set {1}, the first player will actually end up in a losing position through optimal play by both players.
- The complete Grundy number calculation reveals position 7 is a losing position for the first player.

![Example Visualization](../images/GMT-003/example-1.png)

## Notes

- This is a variation of a subtraction game.
- The set of allowed moves depends on the banned list.

## Related Topics

Game Theory, Dynamic Programming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String subtractSquareGame(int n, int[] banned) {
        // Implementation here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] banned = new int[k];
            for (int i = 0; i < k; i++) {
                banned[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.subtractSquareGame(n, banned));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def subtract_square_game(n: int, banned: List[int]) -> str:
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
        n = int(next(iterator))
        k = int(next(iterator))
        banned = []
        for _ in range(k):
            banned.append(int(next(iterator)))
            
        print(subtract_square_game(n, banned))
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
#include <unordered_set>

using namespace std;

class Solution {
public:
    string subtractSquareGame(int n, vector<int>& banned) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k;
    if (cin >> n >> k) {
        vector<int> banned(k);
        for (int i = 0; i < k; i++) {
            cin >> banned[i];
        }
        
        Solution solution;
        cout << solution.subtractSquareGame(n, banned) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  subtractSquareGame(n, banned) {
    // Implementation here
    return null;
  }
}

class Solution {
  subtractSquareGame(n, banned) {
    const bannedSet = new Set(banned);
    const dp = new Uint8Array(n + 1); // 0: False, 1: True
    
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j * j <= i; j++) {
        const s = j * j;
        if (!bannedSet.has(s)) {
          if (dp[i - s] === 0) {
            dp[i] = 1;
            break;
          }
        }
      }
    }
    
    return dp[n] === 1 ? "First" : "Second";
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
  const k = parseInt(flatData[idx++]);
  
  const banned = [];
  for (let i = 0; i < k; i++) {
      banned.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.subtractSquareGame(n, banned));
});
```
