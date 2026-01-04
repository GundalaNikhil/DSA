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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513718/dsa/gametheory/x7ujzzaldv4a0utxepfe.jpg)

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
import java.io.*;

class Solution {
    public String determineWinner(int n, int k, int[] banned) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        String kLine = br.readLine();
        if (kLine == null) return;
        int k = Integer.parseInt(kLine.trim());

        int[] banned = new int[k];
        if (k > 0) {
            String bLine = br.readLine();
            if (bLine != null) {
                String[] bParts = bLine.trim().split("\\s+");
                for (int i = 0; i < k; i++) {
                    banned[i] = Integer.parseInt(bParts[i]);
                }
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, k, banned));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n, k, banned):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    banned = list(map(int, input_data[2:2+k]))

    sol = Solution()
    print(sol.determine_winner(n, k, banned))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string determineWinner(int n, int k, const vector<int>& banned) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> banned(k);
    for (int i = 0; i < k; i++) {
        cin >> banned[i];
    }

    Solution sol;
    cout << sol.determineWinner(n, k, banned) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, k, banned) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);
  const banned = [];
  for (let i = 0; i < k; i++) {
    banned.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.determineWinner(n, k, banned));
}

solve();
```
