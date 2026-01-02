---
problem_id: DP_KB_EDIT_SHIFT__3179
display_id: DP-005
slug: keyboard-row-edit-distance-shift
title: "Keyboard Row Edit Distance with Shift Penalty"
difficulty: Medium
difficulty_score: 60
topics:
  - Dynamic Programming
  - String DP
  - Edit Distance
tags:
  - dp
  - strings
  - edit-distance
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-005: Keyboard Row Edit Distance with Shift Penalty

## Problem Statement

You are given two lowercase strings `a` and `b`. You want to convert `a` into `b` using the following operations:

1. **Insert** one character (cost = 1)
2. **Delete** one character (cost = 1)
3. **Replace** one character `x` with another character `y` (cost depends on keyboard position):
   - cost = 1 if `x` and `y` are on the **same keyboard row**
   - cost = 2 if they are on **different rows** but typed with the **same hand**
   - cost = 3 otherwise (different rows and different hands)

Keyboard rows (QWERTY):

- Row 1: `qwertyuiop`
- Row 2: `asdfghjkl`
- Row 3: `zxcvbnm`

Hands (fixed for this problem):

- Left hand: `qwertasdfgzxcvb`
- Right hand: `yuiophjklnm`

Compute the minimum total cost to convert `a` to `b`.

![Problem Illustration](../images/DP-005/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`

## Output Format

Print one integer: the minimum conversion cost.

## Constraints

- `0 <= len(a), len(b) <= 2000`
- `a` and `b` contain only lowercase English letters `a..z`

## Example

**Input:**
```
type
tap
```

**Output:**
```
3
```

**Explanation:**

One optimal sequence:

- Insert `a` after `t` (cost 1): `type -> taype`
- Delete `y` (cost 1): `taype -> tape`
- Delete `e` (cost 1): `tape -> tap`

Total cost = `1 + 1 + 1 = 3`.

![Example Visualization](../images/DP-005/example-1.png)

## Notes

- Replacing a character with itself costs 0 (no operation).
- This is a weighted version of classic edit distance (Levenshtein distance).

## Related Topics

Dynamic Programming, Edit Distance, String DP

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minKeyboardEditCost(String a, String b) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.hasNextLine() ? sc.nextLine().trim() : "";
        String b = sc.hasNextLine() ? sc.nextLine().trim() : "";
        System.out.println(new Solution().minKeyboardEditCost(a, b));
        sc.close();
    }
}
```

### Python

```python
import sys

def row(c: str) -> int:
    # Implementation here
    return 0

def main():
    try:
        a = input()
        if a.endswith('\n'):
            a = a[:-1]
    except EOFError:
        a = ""

    try:
        b = input()
        if b.endswith('\n'):
            b = b[:-1]
    except EOFError:
        b = ""

    print(min_keyboard_edit_cost(a, b))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>

using namespace std;

class Solution {
public:
    int minKeyboardEditCost(const string& a, const string& b) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    getline(cin, a);
    getline(cin, b);
    Solution sol;
    cout << sol.minKeyboardEditCost(a, b) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minKeyboardEditCost(a, b) {
    // Implementation here
    return null;
  }
}

const ROW1 = new Set("qwertyuiop".split(""));
const ROW2 = new Set("asdfghjkl".split(""));
const LEFT = new Set("qwertasdfgzxcvb".split(""));

function row(c) {
  if (ROW1.has(c)) return 1;
  if (ROW2.has(c)) return 2;
  return 3;
}

function hand(c) {
  return LEFT.has(c) ? 0 : 1;
}

function repCost(x, y) {
  if (x === y) return 0;
  if (row(x) === row(y)) return 1;
  return hand(x) === hand(y) ? 2 : 3;
}

class Solution {
  minKeyboardEditCost(a, b) {
    const n = a.length, m = b.length;
    let prev = new Array(m + 1);
    let cur = new Array(m + 1);
    for (let j = 0; j <= m; j++) prev[j] = j;

    for (let i = 1; i <= n; i++) {
      cur[0] = i;
      const ca = a[i - 1];
      for (let j = 1; j <= m; j++) {
        const cb = b[j - 1];
        const del = prev[j] + 1;
        const ins = cur[j - 1] + 1;
        const rep = prev[j - 1] + repCost(ca, cb);
        cur[j] = Math.min(del, ins, rep);
      }
      const tmp = prev; prev = cur; cur = tmp;
    }
    return prev[m];
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line));
rl.on("close", () => {
  const a = (lines[0] ?? "").trim();
  const b = (lines[1] ?? "").trim();
  const sol = new Solution();
  console.log(sol.minKeyboardEditCost(a, b));
});
```
