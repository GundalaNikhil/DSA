---
problem_id: HSH_MINIMAL_ROTATION_HASH__4729
display_id: HSH-006
slug: minimal-rotation-hash
title: "Minimal Rotation via Hash Compare"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Rotation
tags:
  - hashing
  - rotation
  - lexicographic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-006: Minimal Rotation via Hash Compare

## Problem Statement

Given a string `s`, find its lexicographically smallest rotation using hashing and binary search for comparison.

A rotation of a string is obtained by moving some prefix to the end. For example, rotations of "abc" are: "abc", "bca", "cab".

![Problem Illustration](../images/HSH-006/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single line: lexicographically smallest rotation of `s`

## Constraints

- `1 <= |s| <= 2*10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
bba
```

**Output:**

```
abb
```

**Explanation:**

String: "bba"

All rotations:

- "bba" (start at index 0)
- "bab" (start at index 1)
- "abb" (start at index 2) ← lexicographically smallest

Output: "abb"

![Example Visualization](../images/HSH-006/example-1.png)

## Notes

- Concatenate s with itself to simulate all rotations
- Use hashing with binary search to compare rotations efficiently
- For each starting position, determine lexicographic order using hash comparison
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

String Rotation, Hashing, Binary Search, Lexicographic Order

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String findMinimalRotation(String s) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        if (s == null) return;

        Solution sol = new Solution();
        System.out.println(sol.findMinimalRotation(s.trim()));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_minimal_rotation(self, s):
        # Implement here
        return ""

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return

    sol = Solution()
    print(sol.find_minimal_rotation(s))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string findMinimalRotation(string s) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    Solution sol;
    cout << sol.findMinimalRotation(s) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findMinimalRotation(s) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;

  const sol = new Solution();
  console.log(sol.findMinimalRotation(input));
}

solve();
```
