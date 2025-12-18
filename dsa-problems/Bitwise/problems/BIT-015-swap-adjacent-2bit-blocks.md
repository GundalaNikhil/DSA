---
problem_id: BIT_SWAP_ADJACENT_2BIT_BLOCKS__8415
display_id: BIT-015
slug: swap-adjacent-2bit-blocks
title: "Swap Adjacent 2-Bit Blocks"
difficulty: Easy
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

Treat the 32-bit representation of integer `x` as 16 pairs of 2-bit blocks. Swap each pair of adjacent 2-bit blocks and return the resulting integer.

For example, bits 0-1 swap with bits 2-3, bits 4-5 swap with bits 6-7, and so on.

```
ASCII Diagram: 2-Bit Block Swapping
====================================
Original 8-bit example (extends to 32-bit):
Bits:     7 6 | 5 4 | 3 2 | 1 0
Blocks:   [D]   [C]   [B]   [A]
                ↓  swap  ↓
Result:   [C]   [D]   [A]   [B]
Bits:     5 4 | 7 6 | 1 0 | 3 2

Example: x = 6 (0110 in 4 bits)
Blocks: [01][10]
Swap:   [10][01]
Result: 1001 = 9
```

## Input Format

- Single line: Integer `x`

## Output Format

Single integer after swapping adjacent 2-bit blocks

## Constraints

- `0 <= x <= 10^9`
- Assume unsigned 32-bit operations

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

```
x = 6 in binary:
32-bit: 00000000 00000000 00000000 00000110

Focus on lower bits:
Original: ...00 00 01 10
Blocks:       [0][0][1][2]
              ↓     ↓
After swap: ...00 00 10 01
             = 00000000 00000000 00000000 00001001
             = 9

Detailed bit positions:
Bits 0-1: 10 (value 2)
Bits 2-3: 01 (value 1)

After swap:
Bits 0-1: 01 (value 1)
Bits 2-3: 10 (value 2)

Result: 01 at positions 0-1 gives 1
        10 at positions 2-3 gives 8
        Total: 1 + 8 = 9
```

```
ASCII Step-by-Step:
===================
x = 6 = 0110

Split into 2-bit blocks (right to left):
Position: 3-2  1-0
Blocks:    01   10
           │    │
Swap:      │    │
           ↓    ↓
Result:    10   01
           │    │
Binary:   1001 = 9
```

## Notes

- Use bit masking to extract and swap blocks
- Mask patterns: 0x33333333 (01 pattern), 0xCCCCCCCC (10 pattern)
- Can be done with two masks and shifts
- Formula: `((x & 0x33333333) << 2) | ((x & 0xCCCCCCCC) >> 2)`

## Related Topics

Bit Manipulation, Masking, Bit Swapping, Shift Operations

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int swapAdjacent2BitBlocks(int x) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.swapAdjacent2BitBlocks(x);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def swap_adjacent_2bit_blocks(x: int) -> int:
    # Your implementation here
    return 0

def main():
    x = int(input().strip())
    result = swap_adjacent_2bit_blocks(x)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int swapAdjacent2BitBlocks(int x) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x;
    cin >> x;

    Solution solution;
    cout << solution.swapAdjacent2BitBlocks(x) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  swapAdjacent2BitBlocks(x) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const x = parseInt(data[0]);

  const solution = new Solution();
  console.log(solution.swapAdjacent2BitBlocks(x));
});
```
