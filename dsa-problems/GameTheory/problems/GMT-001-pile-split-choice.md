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
time_limit: 2000
memory_limit: 256
---

# GMT-001: Pile Split Choice

## Problem Statement

You are given a single pile of `n` stones. Two players take turns making a move.

In each turn, a player must choose one pile of stones and split it into **two non-empty piles of different sizes**.
For example, a pile of size 6 can be split into (1, 5) or (2, 4), but not (3, 3) because the sizes must be different.

The player who cannot make a valid move loses the game.

Determine if the first player has a winning strategy assuming both players play optimally.

![Problem Illustration](../images/GMT-001/problem-illustration.png)

## Input Format

- A single integer `n`, representing the initial number of stones in the pile.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 2000`

## Example

**Input:**
```
3
```

**Output:**
```
First
```

**Explanation:**
- Initial pile: 3.
- Player 1 splits 3 into (1, 2).
- Player 2 receives piles {1, 2}.
- Pile 1 cannot be split (size < 3).
- Pile 2 cannot be split (only split is 1+1, which is equal sizes, not allowed).
- Player 2 has no valid moves and loses.
- Therefore, Player 1 wins.

![Example Visualization](../images/GMT-001/example-1.png)

## Notes

- This is a classic impartial game known as "Grundy's Game".
- The game always ends because the number of piles increases and their sizes decrease.

## Related Topics

Game Theory, Sprague-Grundy Theorem, Dynamic Programming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String pileSplitGame(int n) {
        //Implement here
        return "";
    }
}

class Main {
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
    # //Implement here
    return 0

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
        //Implement here
        return "";
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
    //Implement here
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
  const n = parseInt(data[0]);
  const solution = new Solution();
  console.log(solution.pileSplitGame(n));
});
```

