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

![Problem Illustration](../images/GMT-006/problem-illustration.png)

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

class Solution {
    int[] memo; // 0: unknown, 1: First, 2: Second

    public String divisorGame(int n) {
        return "";
    }

    private boolean canWin(int n) {
        if (memo[n] != 0) return memo[n] == 1;

        boolean canReachLosing = false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                int d1 = i;
                if (!canWin(d1)) {
                    canReachLosing = true;
                    break;
                }
                int d2 = n / i;
                if (d2 < n && !canWin(d2)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[n] = canReachLosing ? 1 : 2;
        return canReachLosing;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.divisorGame(n));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case, though depth is log(N)
sys.setrecursionlimit(20000)

def divisor_game(n: int) -> str:
    return ""
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    print(divisor_game(n))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
    vector<int> memo; // 0: unknown, 1: Win, 2: Loss

    bool canWin(int n) {
        return false;
    }

public:
    string divisorGame(int n) {
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (cin >> n) {
        Solution solution;
        cout << solution.divisorGame(n) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  divisorGame(n) {
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
  console.log(solution.divisorGame(n));
});
```

