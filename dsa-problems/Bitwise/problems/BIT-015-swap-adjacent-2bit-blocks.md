---
problem_id: BIT_SWAP_ADJACENT_2BIT_BLOCKS__8415
display_id: BIT-015
slug: swap-adjacent-2bit-blocks
title: "Swap Adjacent 2-Bit Blocks"
difficulty: Medium
difficulty_score: 35
topics:
  - Bitwise Operations
  - Bit Manipulation
  - Masking
tags:
  - bitwise
  - bit-swapping
  - masking
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-015: Swap Adjacent 2-Bit Blocks

## Problem Statement

Treat the 32-bit representation of x as 2-bit blocks. Swap each pair of adjacent blocks (bits 0-1 with 2-3, 4-5 with 6-7, and so on). Return the resulting integer.

![Problem Illustration](../images/BIT-015/problem-illustration.png)

## Input Format

- Single line: integer x

## Output Format

Print the integer after swapping adjacent 2-bit blocks.

## Constraints

- `0 <= x <= 1000000000`

## Example

**Input:**

```
6
```

**Output:**

```
9
```

**Explanation:**

6 is 0110 in binary. Blocks are 01|10; swapping gives 10|01, which is 9.

![Example Visualization](../images/BIT-015/example-1.png)

## Notes

- Assume unsigned 32-bit operations.
- Only pairs of 2-bit blocks are swapped.

## Related Topics

Bitwise Operations

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int swapAdjacent2BitBlocks(int x) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int x = sc.nextInt();

        Solution sol = new Solution();
        System.out.println(sol.swapAdjacent2BitBlocks(x));
    }
}
```

### Python

```python
import sys

class Solution:
    def swap_adjacent_2bit_blocks(self, x):
        # Implement here
        return 0

def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    x = int(line)

    sol = Solution()
    print(sol.swap_adjacent_2bit_blocks(x))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    int swapAdjacent2BitBlocks(int x) {
        // Implement here
        return 0;
    }
};

int main() {
    int x;
    if (!(cin >> x)) return 0;

    Solution sol;
    cout << sol.swapAdjacent2BitBlocks(x) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  swapAdjacent2BitBlocks(x) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);
  if (input.length < 1) return;

  const x = parseInt(input[0]);

  const sol = new Solution();
  console.log(sol.swapAdjacent2BitBlocks(x));
}

solve();
```
