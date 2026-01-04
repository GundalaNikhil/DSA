---
problem_id: REC_LEXICOGRAPHIC_GRAY_CODE__6685
display_id: REC-016
slug: lexicographic-gray-code
title: "Lexicographic Gray Code"
difficulty: Medium
difficulty_score: 45
topics:
  - Recursion
  - Bit Manipulation
  - Gray Code
tags:
  - recursion
  - gray-code
  - bitwise
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-016: Lexicographic Gray Code

## Problem Statement

Generate an `n`-bit Gray code sequence using the standard recursive construction: prefix `0` to the previous sequence and prefix `1` to the reverse of the previous sequence.

Output the resulting sequence in order, one code per line.

![Problem Illustration](../images/REC-016/problem-illustration.png)

## Input Format

- First line: integer `n`

## Output Format

- `2^n` lines, each an `n`-bit string

## Constraints

- `1 <= n <= 12`

## Example

**Input:**

```
2
```

**Output:**

```
00
01
11
10
```

**Explanation:**

The recursive Gray code for `n=2` is `00, 01, 11, 10`.

![Example Visualization](../images/REC-016/example-1.png)

## Notes

- Base case: `n=1` yields `0, 1`
- Each consecutive pair differs by exactly one bit
- The sequence size is `2^n`
- Recursion makes the construction straightforward

## Related Topics

Gray Code, Recursion, Bit Manipulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void generateGrayCode(int n) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Solution sol = new Solution();
        sol.generateGrayCode(n);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def generate_gray_code(self, n):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    sol = Solution()
    sol.generate_gray_code(n)

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
    void generateGrayCode(int n) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    Solution sol;
    sol.generateGrayCode(n);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  generateGrayCode(n) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const sol = new Solution();
  sol.generateGrayCode(n);
}

solve();
```
