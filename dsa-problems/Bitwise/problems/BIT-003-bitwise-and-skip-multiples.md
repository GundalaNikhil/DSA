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
time_limit: 2000
memory_limit: 256
---

# BIT-003: Bitwise AND Skipping Multiples

## Problem Statement

Given L, R, and m, compute the bitwise AND of all numbers in [L, R] that are not divisible by m. If no numbers remain, return -1.

![Problem Illustration](../images/BIT-003/problem-illustration.png)

## Input Format

- Single line: integers L R m

## Output Format

Print the bitwise AND of all numbers in [L, R] not divisible by m, or -1.

## Constraints

- `0 <= L <= R <= 1000000000000`
- `1 <= m <= 1000000`

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

The numbers 10, 11, 13, 14, 15 are not divisible by 3, and their AND is 8.

![Example Visualization](../images/BIT-003/example-1.png)

## Notes

- If every number in [L, R] is divisible by m, output -1.
- Use 64-bit integers for L, R, and the result.

## Related Topics

Bitwise Operations, Math

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long bitwiseAndSkipMultiples(long L, long R, int m) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long L = sc.nextLong();
        long R = sc.nextLong();
        int m = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.bitwiseAndSkipMultiples(L, R, m);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
import sys

def bitwise_and_skip_multiples(L: int, R: int, m: int) -> int:
    # Implementation here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    L = int(data[0])
    R = int(data[1])
    m = int(data[2])
    
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
    long bitwiseAndSkipMultiples(long long L, long long R, int m) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    int m;
    if (!(cin >> L >> R >> m)) return 0;

    Solution solution;
    cout << solution.bitwiseAndSkipMultiples(L, R, m) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bitwiseAndSkipMultiples(L, R, m) {
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
    
    const L = BigInt(tokens[0]);
    const R = BigInt(tokens[1]);
    const m = BigInt(tokens[2]);
    
    const solution = new Solution();
    console.log(solution.bitwiseAndSkipMultiples(L, R, m).toString());
});
```
