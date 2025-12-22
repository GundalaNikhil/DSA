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
---

# GMT-015: Turning Turtles

## 📋 Problem Summary

Flip 'H' to 'T' at `i`. Optionally flip `j` (`i-K <= j < i`).

## 🌍 Real-World Scenario

**Scenario Title:** The Light Switch Panel.

A row of switches. Some are ON (Heads).
- You must turn OFF the rightmost ON switch you choose.
- But the wiring is faulty: turning one OFF might toggle another switch to its left.
- You want to be the one to turn off the last light.

![Real-World Application](../images/GMT-015/real-world-scenario.png)

## Detailed Explanation

### Decomposition

The game is played with multiple Heads.
A move on Head `i` might affect Head `j`.
However, notice that we can only affect indices `j < i`.
This structure (moves only affect lower indices) allows us to treat each Head as an independent game component, summed via XOR.
Why? Because any change to `j` can be "fixed" or "used" by a move on `j` later, without affecting `i`.

### Grundy Values

For a single Head at `i`:
- Move 1: Flip `i` -> `T`. State becomes empty (0).
- Move 2: Flip `i` -> `T`, Flip `j` (`j < i`).
  - If `j` was `T`, it becomes `H`. State has Head at `j`. Value `G(j)`.
  - If `j` was `H`, it becomes `T`. State has no Heads. Value `0`?
  - Wait. If `j` was `H`, we remove `i` and remove `j`.
  - The change in XOR sum is `G(i) ^ G(j)`.
  - We want to move to a state with XOR sum `X'`.
  - We need `G(i) ^ G(j) = G(i) ^ X'`.
  - Basically, from `G(i)`, we can reach `0` (by just flipping `i`) or `G(j)` (by flipping `i` and `j` where `j` was `T`).
  - What if `j` was `H`? Then we move to state `S \ {i, j}`.
  - The value of `S` is `G(i) ^ G(j) ^ Rest`.
  - The new value is `Rest`.
  - This is equivalent to `G(i) ^ G(j)` becoming `0`.
  - This is consistent with `G(i)` being the value.

So `G(i) = mex( {0} U {G(j) | i-K <= j < i} )`.

### Pattern

Calculating `G(i)`:
- `G(0) = mex(0) = 1`.
- `G(1) = mex(0, 1) = 2`.
- ...
- `G(K) = K+1`.
- `G(K+1) = mex(0, 1, ..., K+1) \ {G(0)} = mex(0, 2, ..., K+1) = 1`.
- The pattern `1, 2, ..., K+1` repeats.
- Formula: `G(i) = (i % (K+1)) + 1`.

### Complexity

- **Time:** `O(N)`.
- **Space:** `O(1)`.

![Algorithm Visualization](../images/GMT-015/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public String turningTurtles(int n, int k, String s) {
        long xorSum = 0;
        long mod = k + 1;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'H') {
                xorSum ^= ((i % mod) + 1);
            }
        }
        return xorSum > 0 ? "First" : "Second";
    }
}

public class Main {
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
    xor_sum = 0
    mod = k + 1
    for i, char in enumerate(s):
        if char == 'H':
            xor_sum ^= ((i % mod) + 1)
    return "First" if xor_sum > 0 else "Second"

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
        long long xorSum = 0;
        long long mod = k + 1;
        for (int i = 0; i < n; i++) {
            if (s[i] == 'H') {
                xorSum ^= ((i % mod) + 1);
            }
        }
        return xorSum > 0 ? "First" : "Second";
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
    let xorSum = 0;
    const mod = k + 1;
    for (let i = 0; i < n; i++) {
      if (s[i] === 'H') {
        xorSum ^= ((i % mod) + 1);
      }
    }
    return xorSum > 0 ? "First" : "Second";
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

## 🧪 Test Case Walkthrough

**Input:** `5 2 THTHH`
- `H` at 1: `G = 1%3 + 1 = 2`.
- `H` at 3: `G = 3%3 + 1 = 1`.
- `H` at 4: `G = 4%3 + 1 = 2`.
- XOR: `2 ^ 1 ^ 2 = 1`.
- Result: First.

## ✅ Proof of Correctness

- **Independence:** Moves on `i` don't change `G(k)` for `k > i`.
- **Periodicity:** `mex` pattern is proven.

## 💡 Interview Extensions

- **Extension 1:** What if `K = N`?
  - *Answer:* `G(i) = i + 1`.
- **Extension 2:** What if we MUST flip a second coin?
  - *Answer:* Then `0` is not reachable. `G(i)` changes.

### C++ommon Mistakes

1.  **Indexing:**
    - ❌ Wrong: Using 1-based index without adjusting modulo.
    - ✅ Correct: `(i % (K+1)) + 1` for 0-based `i`.
2.  **XOR Logic:**
    - ❌ Wrong: Summing values.
    - ✅ Correct: XORing values.

## Related Concepts

- **Sprague-Grundy**
- **Nim**
