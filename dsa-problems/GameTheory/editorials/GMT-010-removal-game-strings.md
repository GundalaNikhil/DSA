---
problem_id: GMT_STRING_REMOVE__2847
display_id: GMT-010
slug: removal-game-strings
title: "Removal Game on Strings"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Strings
tags:
  - impartial-game
  - sprague-grundy
  - ad-hoc
premium: true
subscription_tier: basic
---

# GMT-010: Removal Game on Strings

## 📋 Problem Summary

You are given `n` binary strings (`a`/`b`). Players take turns choosing a string,
removing a contiguous block of identical characters, and merging neighbors if
they become equal. The player who cannot move loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The collapsing tunnel.

Imagine a tunnel supported by segments of different materials (Concrete, Steel, Concrete, Wood).
- Removing a segment causes the tunnel to collapse/compress.
- If two Concrete segments touch after a removal, they fuse into one stronger segment.
- You want to be the one to make the last safe removal.

![Real-World Application](../images/GMT-010/real-world-scenario.png)

## Detailed Explanation

### Key Observations

1. Compress each string into consecutive groups (blocks) of identical characters.
   Example: `aaabbbaabbb` -> `a, b, a, b` (4 groups).
2. The input alphabet is only `{a, b}`, so in the compressed form the groups
   **always alternate**.
3. If you remove a group in the middle, the two neighbors are the same
   character and merge, so the number of groups decreases by **2**.
4. If you remove an end group, the number of groups decreases by **1**.

So for a string with `k` groups, the moves are exactly:
- `k -> k - 1`
- `k -> k - 2`

This is a single-pile impartial game. The Grundy values are:
- `G(0)=0`, `G(1)=1`, `G(2)=0`
- For `k >= 3`, the pattern repeats with period 3:
  - `k % 3 == 1 -> 1`
  - `k % 3 == 2 -> 0`
  - `k % 3 == 0 -> 2`

Each string is a pile with size = number of groups. The overall game is the XOR
of the Grundy values across all strings.

### Algorithm


1.  For each string:
    - Compress to find number of groups `k`.
    - Compute `g = grundy(k)`.
    - `xor_sum ^= g`.
2.  Return "First" if `xor_sum > 0`.

### Time Complexity

- **O(N * |S|)** to parse strings.

### Space Complexity

- **O(1)** if processing on the fly.

![Algorithm Visualization](../images/GMT-010/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private int getGrundy(int k) {
        if (k == 0) return 0;
        if (k == 1) return 1;
        if (k == 2) return 0;
        // Pattern for k >= 3: 2, 1, 0 repeating
        int rem = k % 3;
        if (rem == 0) return 2;
        if (rem == 1) return 1;
        return 0;
    }

    public String stringGame(int n, String[] strings) {
        int xorSum = 0;
        for (String s : strings) {
            if (s.isEmpty()) continue;
            int groups = 1;
            for (int i = 1; i < s.length(); i++) {
                if (s.charAt(i) != s.charAt(i - 1)) {
                    groups++;
                }
            }
            xorSum ^= getGrundy(groups);
        }
        return xorSum > 0 ? "First" : "Second";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            String[] strings = new String[n];
            for (int i = 0; i < n; i++) {
                strings[i] = sc.next();
            }

            Solution solution = new Solution();
            System.out.println(solution.stringGame(n, strings));
        }
        sc.close();
    }
}
```

### Python
```python
from typing import List

def get_grundy(k: int) -> int:
    if k == 0: return 0
    if k == 1: return 1
    if k == 2: return 0
    rem = k % 3
    if rem == 0: return 2
    if rem == 1: return 1
    return 0

def string_game(n: int, strings: List[str]) -> str:
    xor_sum = 0
    for s in strings:
        if not s:
            continue
        groups = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                groups += 1
        xor_sum ^= get_grundy(groups)
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
        strings = []
        for _ in range(n):
            strings.append(next(iterator))
            
        print(string_game(n, strings))
    except StopIteration:
        pass

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
    int getGrundy(int k) {
        if (k == 0) return 0;
        if (k == 1) return 1;
        if (k == 2) return 0;
        int rem = k % 3;
        if (rem == 0) return 2;
        if (rem == 1) return 1;
        return 0;
    }
public:
    string stringGame(int n, vector<string>& strings) {
        int xorSum = 0;
        for (const string& s : strings) {
            if (s.empty()) continue;
            int groups = 1;
            for (size_t i = 1; i < s.length(); i++) {
                if (s[i] != s[i - 1]) {
                    groups++;
                }
            }
            xorSum ^= getGrundy(groups);
        }
        return xorSum > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<string> strings(n);
        for (int i = 0; i < n; i++) {
            cin >> strings[i];
        }
        
        Solution solution;
        cout << solution.stringGame(n, strings) << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  getGrundy(k) {
    if (k === 0) return 0;
    if (k === 1) return 1;
    if (k === 2) return 0;
    const rem = k % 3;
    if (rem === 0) return 2;
    if (rem === 1) return 1;
    return 0;
  }

  stringGame(n, strings) {
    let xorSum = 0;
    for (const s of strings) {
      if (s.length === 0) continue;
      let groups = 1;
      for (let i = 1; i < s.length; i++) {
        if (s[i] !== s[i - 1]) {
          groups++;
        }
      }
      xorSum ^= this.getGrundy(groups);
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
  
  const strings = [];
  for (let i = 0; i < n; i++) {
      strings.push(flatData[idx++]);
  }

  const solution = new Solution();
  console.log(solution.stringGame(n, strings));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
Groups: 4.
`G(4) = 1`.
Result: First.

**Input:** `[aabb]`
Groups: 2.
`G(2) = 0`.
Result: Second.

## ✅ Proof of Correctness

- **Reduction:** Binary string -> Alternating groups -> Game on length `L`.
- **Moves:** `L -> L-1` or `L -> L-2`.
- **Pattern:** Verified manually.

## 💡 Interview Extensions

- **Extension 1:** What if alphabet size > 2?
  - *Answer:* Merging is not guaranteed. Much harder.
- **Extension 2:** What if we can remove non-contiguous characters?
  - *Answer:* Different game.

### Common Mistakes

1.  **Counting Characters:**
    - ❌ Wrong: Using string length.
    - ✅ Correct: Using group count.
2.  **Wrong Pattern:**
    - ❌ Wrong: `L % 3`.
    - ✅ Correct: `0, 1, 0, 2, 1, 0...`

## Related Concepts

- **Nim**
- **Sprague-Grundy**
- **String Compression**
