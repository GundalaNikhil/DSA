---
problem_id: REC_LAB_ID_PERMUTATIONS_NO_TWINS__9064
display_id: REC-002
slug: lab-id-permutations-no-twins
title: "Lab ID Permutations With No Adjacent Twins"
difficulty: Easy
difficulty_score: 30
topics:
  - Recursion
  - Backtracking
  - Strings
tags:
  - recursion
  - backtracking
  - permutations
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-002: Lab ID Permutations With No Adjacent Twins

## Problem Statement

Given a string `s` (may contain duplicate characters), generate all unique permutations such that no two identical characters are adjacent. Output permutations in lexicographic order.

![Problem Illustration](../images/REC-002/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Each valid permutation on its own line, in lexicographic order
- If no permutation exists, output `NONE`

## Constraints

- `1 <= |s| <= 8`
- `s` contains lowercase English letters

## Example

**Input:**

```
aab
```

**Output:**

```
aba
```

**Explanation:**

The permutations are `aab`, `aba`, `baa`. Only `aba` avoids adjacent identical letters.

![Example Visualization](../images/REC-002/example-1.png)

## Notes

- Sort the characters and use a visited array for lexicographic order
- Skip duplicates by checking previous identical characters
- Track the last placed character to avoid twins
- Time complexity is bounded by O(n! ) for `n <= 8`

## Related Topics

Backtracking, Permutations, Pruning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void generatePermutations(String s) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        Solution sol = new Solution();
        sol.generatePermutations(s);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def generate_permutations(self, s):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    sol = Solution()
    sol.generate_permutations(input_data)

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
    void generatePermutations(string s) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    Solution sol;
    sol.generatePermutations(s);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  generatePermutations(s) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const sol = new Solution();
  sol.generatePermutations(input);
}

solve();
```
