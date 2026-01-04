---
problem_id: GMT_DIVISOR_TURN__6832
display_id: GMT-006
slug: divisor-turn-game
title: "Divisor Turn Game"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Number Theory
  - Dynamic Programming
tags:
  - impartial-game
  - divisors
  - memoization
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GMT-006: Divisor Turn Game

## Problem Statement

Two players are playing a game with a number `n`.
In each turn, a player must replace the current number `n` with one of its **proper divisors** `d` such that `d > 1`.
(A proper divisor of `n` is a divisor strictly less than `n`.)
The player who cannot make a valid move loses.
This happens when the current number is prime (since its only divisors are 1 and itself, and we require `d > 1` and `d < n`).

Determine if the first player has a winning strategy for a given `n`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539105/dsa/gametheory_simple/qc9rkazlzst0cbe4mu4z.jpg)

## Input Format

- A single integer `n`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `2 <= n <= 10^6`

## Example

**Input:**

```
2
```

**Output:**

```
Second
```

**Explanation:**

- `n = 2`.
- Divisors of 2 are 1, 2.
- Proper divisors: 1.
- Valid moves require `d > 1`.
- No valid moves.
- First player loses immediately.

**Input:**

```
6
```

**Output:**

```
First
```

**Explanation:**

- `n = 6`.
- Proper divisors > 1: 2, 3.
- If P1 chooses 2: P2 receives 2. P2 has no moves (2 is prime). P2 loses.
- If P1 chooses 3: P2 receives 3. P2 has no moves (3 is prime). P2 loses.
- Since P1 can force P2 to lose, P1 wins.

![Example Visualization](../images/GMT-006/example-1.png)

## Notes

- Primes are losing positions.
- Composite numbers can be winning or losing depending on their divisors.

## Related Topics

Game Theory, Sieve of Eratosthenes, Memoization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String determineWinner(int n) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n):
        # Implement here
        return ""

def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)

    sol = Solution()
    print(sol.determine_winner(n))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string determineWinner(int n) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    Solution sol;
    cout << sol.determineWinner(n) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const n = parseInt(input);

  const sol = new Solution();
  console.log(sol.determineWinner(n));
}

solve();
```
