---
problem_id: GMT_TURNING_TURTLES__6281
display_id: GMT-015
slug: turning-turtles
title: "Turning Turtles"
difficulty: Medium
difficulty_score: 50
topics:
  - Game Theory
  - Math
tags:
  - impartial-game
  - sprague-grundy
  - xor-sum
premium: true
subscription_tier: basic
time_limit: 1000
memory_limit: 256
---

# GMT-015: Turning Turtles

## Problem Statement

You are given a row of `N` coins, represented by a string `S` of length `N`.
Each character is either 'H' (Heads) or 'T' (Tails).
Two players take turns making a move.
In each turn, a player must:

1.  Choose an index `i` (`0 <= i < N`) such that `S[i]` is 'H'.
2.  Flip the coin at `i` from 'H' to 'T'.
3.  **Optionally**, choose another index `j` such that `i - K <= j < i` (where `K` is a given integer) and flip the coin at `j` (from 'H' to 'T' or 'T' to 'H').

The player who cannot make a valid move loses.
(This happens when all coins are 'T').

Determine if the first player has a winning strategy.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539112/dsa/gametheory_simple/bfyyf0mcqdcvdowdwvx6.jpg)

## Input Format

- The first line contains two integers `N` and `K`.
- The second line contains the string `S`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= N <= 10^5`
- `1 <= K <= 10^9`
- `S` consists of 'H' and 'T'.

## Example

**Input:**

```
5 2
THTHH
```

**Output:**

```
First
```

**Explanation:**

- `N=5, K=2`. String `THTHH`.
- Heads at indices: 1, 3, 4.
- We need to compute Grundy values `G(i)`.
- Pattern: `G(i) = (i % (K+1)) + 1`.
- `K+1 = 3`.
- `G(1) = (1 % 3) + 1 = 2`.
- `G(3) = (3 % 3) + 1 = 1`.
- `G(4) = (4 % 3) + 1 = 2`.
- XOR Sum = `2 ^ 1 ^ 2 = 1`.
- Since XOR Sum > 0, First wins.

![Example Visualization](../images/GMT-015/example-1.png)

## Notes

- The game decomposes into independent subgames for each Head.
- Flipping a coin at `j` is equivalent to adding/removing a subgame of value `G(j)`.
- The Grundy values follow a periodic pattern.

## Related Topics

Game Theory, Sprague-Grundy Theorem

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String determineWinner(int n, long k, String s) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nkLine = br.readLine();
        if (nkLine == null) return;
        String[] nkParts = nkLine.trim().split("\\s+");
        int n = Integer.parseInt(nkParts[0]);
        long k = Long.parseLong(nkParts[1]);
        String s = br.readLine();

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, k, s));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n, k, s):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    s = input_data[2]

    sol = Solution()
    print(sol.determine_winner(n, k, s))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string determineWinner(int n, long long k, string s) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    string s;
    cin >> s;

    Solution sol;
    cout << sol.determineWinner(n, k, s) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, k, s) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  const n = parseInt(input[0]);
  const k = BigInt(input[1]);
  const s = input[2];

  const sol = new Solution();
  console.log(sol.determineWinner(n, k, s));
}

solve();
```
