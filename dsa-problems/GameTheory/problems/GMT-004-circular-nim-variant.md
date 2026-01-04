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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513719/dsa/gametheory/nlr5mjnlgaavickudnnp.jpg)

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
import java.io.*;

class Solution {
    public String determineWinner(int n, int[] piles) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        int[] piles = new int[n];
        for (int i = 0; i < n; i++) {
            piles[i] = sc.nextInt();
        }

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, piles));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n, piles):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    piles = list(map(int, input_data[1:1+n]))

    sol = Solution()
    print(sol.determine_winner(n, piles))

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
    string determineWinner(int n, vector<int>& piles) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> piles(n);
    for (int i = 0; i < n; i++) {
        cin >> piles[i];
    }

    Solution sol;
    cout << sol.determineWinner(n, piles) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, piles) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const piles = [];
  for (let i = 0; i < n; i++) {
    piles.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.determineWinner(n, piles));
}

solve();
```
