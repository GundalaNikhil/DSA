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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539108/dsa/gametheory_simple/j5cq062belvp6zsdepun.jpg)

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
import java.io.*;

class Solution {
    public String determineWinner(int n, List<String> strings) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        List<String> strings = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            strings.add(br.readLine());
        }

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, strings));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n, strings):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0])
    strings = input_data[1:1+n]

    sol = Solution()
    print(sol.determine_winner(n, strings))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string determineWinner(int n, vector<string>& strings) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> strings(n);
    for (int i = 0; i < n; i++) {
        cin >> strings[i];
    }

    Solution sol;
    cout << sol.determineWinner(n, strings) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, strings) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const strings = [];
  for (let i = 0; i < n; i++) {
    strings.push(input[idx++]);
  }

  const sol = new Solution();
  console.log(sol.determineWinner(n, strings));
}

solve();
```
