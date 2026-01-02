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
time_limit: 1000
memory_limit: 256
---

# GMT-010: Removal Game on Strings

## Problem Statement

You are given `n` strings.
Two players take turns making a move.
In each turn, a player must choose one string and perform the following operation:
1.  Select a **contiguous block of identical characters** (e.g., "aaa" in "bbaaac").
2.  Remove this block from the string.
3.  If the removal causes two blocks of the same character to become adjacent, they **merge** into a single block.

For example, in `aaabbbaaccc`:
- Removing `bbb` results in `aaa` and `aa` becoming adjacent.
- They merge to form `aaaaaccc`.

The player who cannot make a valid move loses.
(This happens when all strings are empty).

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-010/problem-illustration.png)

## Input Format

- The first line contains an integer `n`, the number of strings.
- The next `n` lines each contain a string `s`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 100`
- `1 <= |s| <= 10^5`
- Strings consist of characters 'a' and 'b'.

## Example

**Input:**
```
2
aaabbbaabbb
aabb
```

**Output:**
```
First
```

**Explanation:**
- String 1: `aaabbbaabbb`.
  - Groups: `a, b, a, b`. Count = 4.
- String 2: `aabb`.
  - Groups: `a, b`. Count = 2.
- Game is equivalent to Nim with pile sizes based on group counts.
- We need to find the Grundy values for group counts 4 and 2.

![Example Visualization](../images/GMT-010/example-1.png)

## Notes

- The actual characters don't matter, only the structure of groups.
- Merging reduces the number of groups by 2 (the removed group is gone, and its two neighbors merge into one).

## Related Topics

Game Theory, Sprague-Grundy Theorem, String Processing

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String stringGame(int n, String[] strings) {
        // Implementation here
        return "";
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
    # Implementation here
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
public:
    string stringGame(int n, vector<string>& strings) {
        // Implementation here
        return {};
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
    // Implementation here
    return null;
  }
}

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
