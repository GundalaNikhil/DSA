---
problem_id: BIT_SWAP_ADJACENT_2BIT_BLOCKS__8415
display_id: BIT-015
slug: swap-adjacent-2bit-blocks
title: "Swap Adjacent 2-Bit Blocks"
difficulty: Easy-Medium
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

class Solution {
    public long swapAdjacent2BitBlocks(long x) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.swapAdjacent2BitBlocks(x));
        sc.close();
    }
}
```

### Python

```
// No template available
```

### C++

```cpp
#include <iostream>

using namespace std;

class Solution {
public:
    long swapAdjacent2BitBlocks(int x) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned int x;
    if (!(cin >> x)) return 0;

    Solution solution;
    cout << solution.swapAdjacent2BitBlocks((int)x) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  swapAdjacent2BitBlocks(x) {
    // Implementation here
    return null;
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
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    const x = Number(tokens[0]);
    
    const solution = new Solution();
    console.log(solution.swapAdjacent2BitBlocks(x));
});
```
