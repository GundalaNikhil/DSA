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

You are given a string of 'H'/'T'. On each move, pick an index `i` with 'H',
flip it to 'T', and optionally flip one `j` with `i-K <= j < i`. The player who
cannot move loses. Determine whether the first player wins.

## 🌍 Real-World Scenario

**Scenario Title:** The Light Switch Panel.

A row of switches. Some are ON (Heads).
- You must turn OFF a chosen ON switch.
- But the wiring is faulty: turning one OFF can toggle another switch to its left.
- You want to be the one to turn off the last light.

![Real-World Application](../images/GMT-015/real-world-scenario.png)

## Detailed Explanation

### Decomposition

Each position with a head contributes an independent subgame. A move on index
`i` never changes any position `> i`, so it does not affect the options for
heads to the right. This is the standard setting where the overall position is
the XOR of per-head Grundy values.

### Grundy Values

Define `G(i)` as the Grundy value contributed by a head at position `i`.
Flipping `i` always removes that head. If you do **not** flip a `j`, the move
reaches value `0`. If you **do** flip a `j` in `[i-K, i-1]`, you toggle the head
status at `j`, which changes the XOR by `G(j)`. Therefore the reachable set is:
```
{0} ∪ {G(j) | i-K <= j < i}
```
and:
```
G(i) = mex( {0} ∪ {G(j) | i-K <= j < i} )
```

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
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'H') {
                xorSum ^= ((i % mod) + 1);
            }
        }
        return xorSum > 0 ? "First" : "Second";
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
        for (int i = 0; i < (int)s.length(); i++) {
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
    for (let i = 0; i < s.length; i++) {
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

## 🧪 Test Case Walkthrough (Dry Run)
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

### Common Mistakes

1.  **Indexing:**
    - ❌ Wrong: Using 1-based index without adjusting modulo.
    - ✅ Correct: `(i % (K+1)) + 1` for 0-based `i`.
2.  **XOR Logic:**
    - ❌ Wrong: Summing values.
    - ✅ Correct: XORing values.

## Related Concepts

- **Sprague-Grundy**
- **Nim**
