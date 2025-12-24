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
    public long swapAdjacent2BitBlocks(int x) {
        // Your implementation here
        return 0L;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.swapAdjacent2BitBlocks(x);
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
    x = int(input())

    result = swap_adjacent_2bit_blocks(x)
    print(result)

if __name__ == "__main__":
    main()
```


### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <tuple>
using namespace std;


class Solution {
public:
    long long swapAdjacent2BitBlocks(int x) {
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
    long long result = solution.swapAdjacent2BitBlocks(x);
    cout << result << "\n";
    return 0;
}
```


### JavaScript

```javascript
const fs = require("fs");
const data = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (data.length === 1 && data[0] === "") {
  process.exit(0);
}

class Solution {
  swapAdjacent2BitBlocks(x) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const x = Number(data[idx++]);

const solution = new Solution();
const result = solution.swapAdjacent2BitBlocks(x);
console.log(String(result));
```

