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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513328/dsa/dp/ipxu05uc5xicsfh3q83a.jpg)

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
import java.io.*;

class Solution {
    public int minEditDistance(String a, String b) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        if (a == null) a = "";
        if (b == null) b = "";

        Solution sol = new Solution();
        System.out.println(sol.minEditDistance(a, b));
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep DP if needed
sys.setrecursionlimit(5000)

class Solution:
    def min_edit_distance(self, a, b):
        # Implement here
        return 0

def solve():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    sol = Solution()
    print(sol.min_edit_distance(a, b))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minEditDistance(string a, string b) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string a, b;
    if (!(getline(cin, a))) a = "";
    if (!(getline(cin, b))) b = "";

    // Trim potential \r from windows-style endings
    if (!a.empty() && a.back() == '\r') a.pop_back();
    if (!b.empty() && b.back() == '\r') b.pop_back();

    Solution sol;
    cout << sol.minEditDistance(a, b) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minEditDistance(a, b) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  const a = input[0] || "";
  const b = input[1] || "";

  const sol = new Solution();
  console.log(sol.minEditDistance(a, b));
}

solve();
```
