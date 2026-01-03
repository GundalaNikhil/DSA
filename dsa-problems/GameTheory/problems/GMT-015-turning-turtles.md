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

![Problem Illustration](../images/GMT-015/problem-illustration.png)

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

class Solution {
    public String turningTurtles(int n, int k, String s) {
        //Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            String s = sc.next();

            Solution solution = new Solution();
            System.out.println(solution.turningTurtles(n, k, s));
        }
        sc.close();
    }
}
```

### Python

```python
def turning_turtles(n: int, k: int, s: str) -> str:
    # //Implement here
    return 0

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
        s = next(iterator)
            
        print(turning_turtles(n, k, s))
    except StopIteration:
        pass

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
    string turningTurtles(int n, int k, string s) {
        //Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k;
    if (cin >> n >> k) {
        string s;
        cin >> s;
        
        Solution solution;
        cout << solution.turningTurtles(n, k, s) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  turningTurtles(n, k, s) {
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
  const s = flatData[idx++];

  const solution = new Solution();
  console.log(solution.turningTurtles(n, k, s));
});
```

