---
problem_id: BIT_PALINDROMES_BALANCED_ONES__8414
display_id: BIT-014
slug: bitwise-palindromes-balanced-ones
title: "Bitwise Palindromes With Balanced Ones"
difficulty: Medium
difficulty_score: 62
topics:
  - Bitwise Operations
  - Palindrome
  - Bit Counting
  - Number Theory
tags:
  - bitwise
  - palindrome
  - popcount
  - number-generation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-014: Bitwise Palindromes With Balanced Ones

## Problem Statement

Count numbers in [L, R] whose binary representation is a palindrome and whose number of 1 bits is even.


![Problem Illustration](../images/BIT-014/problem-illustration.png)

## Input Format

- Single line: integers L R

## Output Format

Print the count of valid numbers in [L, R].

## Constraints

- `0 <= L <= R <= 1000000000000`

## Example

**Input:**
```
5 12
```

**Output:**
```
2
```

**Explanation:**

5 (101) and 9 (1001) are palindromes with an even number of 1 bits.

![Example Visualization](../images/BIT-014/example-1.png)

## Notes

- Leading zeros are not allowed in the binary representation.
- Use 64-bit arithmetic for the count.

## Related Topics

Bitwise Operations, Combinatorics

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private long makePalindrome(long half, int len) {
        return 0;
    }

    // Counts valid palindromes <= N with exact bit length 'len'
    private long countForLen(long N, int len, boolean isLimit) {
        return 0;
    }

    private long solve(long N) {
        return 0;
    }

    public long countBitwisePalindromesBalancedOnes(long L, long R) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long L = sc.nextLong();
        long R = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.countBitwisePalindromesBalancedOnes(L, R));
        sc.close();
    }
}
```

### Python

```python
import sys

def make_palindrome(half, length):
    return 0
def count_for_len(N, length, is_limit):
    return 0
def solve(N):
    return 0
def count_bitwise_palindromes_balanced_ones(L: int, R: int) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return

    L = int(data[0])
    R = int(data[1])

    result = count_bitwise_palindromes_balanced_ones(L, R)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
    long long makePalindrome(long long half, int len) {
        return 0;
    }

    long long countForLen(long long N, int len, bool isLimit) {
        return 0;
    }

    long long solve(long long N) {
        return 0;
    }

public:
    long long countBitwisePalindromesBalancedOnes(long long L, long long R) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    Solution solution;
    cout << solution.countBitwisePalindromesBalancedOnes(L, R) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  makePalindrome(half, len) {
    return 0;
  }

  countForLen(N, len, isLimit) {
    return 0;
  }

  solve(N) {
    return 0;
  }

  countBitwisePalindromesBalancedOnes(L, R) {
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
  if (data.length === 0) return;
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  const L = BigInt(tokens[0]);
  const R = BigInt(tokens[1]);

  const solution = new Solution();
  console.log(solution.countBitwisePalindromesBalancedOnes(L, R).toString());
});
```

