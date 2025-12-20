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
    public String divisorGame(int n) {
        // Your implementation here
        return "Second";
    }
}

public class Main {
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
def divisor_game(n: int) -> str:
    # Your implementation here
    return "Second"

def main():
    import sys
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
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string divisorGame(int n) {
        // Your implementation here
        return "Second";
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
  const n = parseInt(data[0]);
  const solution = new Solution();
  console.log(solution.divisorGame(n));
});
```
