---
problem_id: BIT_AND_SKIP_MULTIPLES__8403
display_id: BIT-003
slug: bitwise-and-skip-multiples
title: "Bitwise AND Skipping Multiples"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - AND
  - Number Theory
  - Mathematics
tags:
  - bitwise
  - and-operation
  - number-theory
  - medium
premium: true
subscription_tier: basic
---

# BIT-003: Bitwise AND Skipping Multiples

## Problem Statement

Given integers L, R, and m, compute the bitwise AND of all numbers in [L, R] that are NOT divisible by m. If no valid numbers exist, return -1.

![Problem Illustration](../images/BIT-003/problem-illustration.png)

## Input Format

- Single line: Three integers `L`, `R`, and `m`

## Output Format

Single integer representing the bitwise AND result, or -1 if no valid numbers exist.

## Constraints

- 0 ≤ L ≤ R ≤ 10¹²
- 1 ≤ m ≤ 10⁶

## Example

**Input:**

```
10 15 3
```

**Output:**

```
8
```

**Explanation:**

Numbers in [10, 15]: 10, 11, 12, 13, 14, 15

Numbers NOT divisible by 3: 10, 11, 13, 14, 15 (skip 12)

Binary representation:

- 10 = 1010
- 11 = 1011
- 13 = 1101
- 14 = 1110
- 15 = 1111

Bitwise AND: 1010 & 1011 & 1101 & 1110 & 1111 = 1000 = 8

![Example Visualization](../images/BIT-003/example-1.png)

## Notes

- If all numbers in [L, R] are divisible by m, return -1
- AND operation reduces as more numbers are included
- Consider power-of-2 boundaries for optimization

## Related Topics

Bitwise Operations, AND, Number Theory, Mathematics

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long bitwiseAndSkipMultiples(long L, long R, long m) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long L = sc.nextLong();
        long R = sc.nextLong();
        long m = sc.nextLong();

        Solution solution = new Solution();
        long result = solution.bitwiseAndSkipMultiples(L, R, m);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def bitwise_and_skip_multiples(L: int, R: int, m: int) -> int:
    # Your implementation here
    pass

def main():
    L, R, m = map(int, input().split())
    result = bitwise_and_skip_multiples(L, R, m)
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
    long long bitwiseAndSkipMultiples(long long L, long long R, long long m) {
        // Your implementation here
    }
};

int main() {
    long long L, R, m;
    cin >> L >> R >> m;

    Solution solution;
    long long result = solution.bitwiseAndSkipMultiples(L, R, m);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bitwiseAndSkipMultiples(L, R, m) {
    // Your implementation here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const [L, R, m] = line.split(" ").map(Number);

  const solution = new Solution();
  const result = solution.bitwiseAndSkipMultiples(L, R, m);

  console.log(result);
  rl.close();
});
```
