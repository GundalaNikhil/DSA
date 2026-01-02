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
        long res = half;
        int bitsToMirror = len / 2;
        // If len is 5 (10101), half has 3 bits. We mirror non-middle.
        // If len is 4 (1001), half has 2 bits. We mirror all.
        // General: We mirror 'len - ceil(len/2)' bits.
        // Which are the lower bits of half? No, the whole half is prefix.
        // Example len=5. half=110 (6). Palindrome 11011.
        // Sequence: half (110) then append reverse of 11 (3).

        long lower = 0;
        long temp = half;
        if (len % 2 == 1) temp >>= 1; // Skip middle bit for mirroring

        for (int i = 0; i < len / 2; i++) {
            lower = (lower << 1) | (temp & 1);
            temp >>= 1;
        }
        return (res << (len / 2)) | lower;
    }

    // Counts valid palindromes <= N with exact bit length 'len'
    private long countForLen(long N, int len, boolean isLimit) {
        int halfLen = (len + 1) / 2;
        long minHalf = 1L << (halfLen - 1);
        long maxHalf = (1L << halfLen) - 1;

        if (isLimit) {
            long prefix = N >>> (len - halfLen);
            if (prefix < minHalf) return 0; // Should not happen if len matches N
            maxHalf = Math.min(maxHalf, prefix);
        }

        long count = 0;

        // If len is odd, half must be even (LSB 0) implies palindrome middle is 0.
        // If len is even, any half is valid.

        // We need numbers in [minHalf, maxHalf] satisfying condition
        // If isLimit is true and we pick maxHalf, we must verify reconstruction.
        // So standard logic: Count strictly less than maxHalf, then check maxHalf.

        long limitVal = maxHalf;

        // Count in range [minHalf, limitVal - 1]
        // If len even: count all integers.
        // If len odd: count even integers.

        long validBelow = 0;

        if (limitVal > minHalf) {
            if (len % 2 == 0) {
                validBelow = limitVal - minHalf;
            } else {
                // Count evens in [minHalf, limitVal - 1]
                // minHalf is power of 2, so it is even.
                // Range [E, X). Count evens is (X - E + 1) / 2
                validBelow = (limitVal - minHalf + 1) / 2;
            }
        }

        // Check boundary limitVal
        boolean checkBoundary = true;

        // If len odd and limitVal is odd, it's invalid
        if (len % 2 == 1 && (limitVal % 2 != 0)) checkBoundary = false;

        if (checkBoundary) {
            long p = makePalindrome(limitVal, len);
            if (!isLimit || p <= N) {
                validBelow++;
            }
        }

        return validBelow;
    }

    private long solve(long N) {
        if (N < 0) return 0;
        if (N == 0) return 1; // 0 is palindrome and even bits (0)

        // Length of N
        int L = 0;
        long temp = N;
        while (temp > 0) { L++; temp >>= 1; }

        long total = 1; // Count 0

        // Lengths strictly less than L
        for (int len = 1; len < L; len++) {
            total += countForLen(Long.MAX_VALUE, len, false);
        }

        // Length equal to L
        total += countForLen(N, L, true);

        return total;
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
        long long res = half;
        long long temp = half;
        if (len % 2 == 1) temp >>= 1;

        long long lower = 0;
        for (int i = 0; i < len / 2; i++) {
            lower = (lower << 1) | (temp & 1);
            temp >>= 1;
        }
        return (res << (len / 2)) | lower;
    }

    long long countForLen(long long N, int len, bool isLimit) {
        int halfLen = (len + 1) / 2;
        long long minHalf = 1LL << (halfLen - 1);
        long long maxHalf = (1LL << halfLen) - 1;

        if (isLimit) {
            long long prefix = N >> (len - halfLen);
            if (prefix < minHalf) return 0;
            maxHalf = min(maxHalf, prefix);
        }

        long long limitVal = maxHalf;
        long long validBelow = 0;

        if (limitVal > minHalf) {
            if (len % 2 == 0) {
                validBelow = limitVal - minHalf;
            } else {
                validBelow = (limitVal - minHalf + 1) / 2;
            }
        }

        bool checkBoundary = true;
        if (len % 2 == 1 && (limitVal % 2 != 0)) checkBoundary = false;

        if (checkBoundary) {
            long long p = makePalindrome(limitVal, len);
            if (!isLimit || p <= N) {
                validBelow++;
            }
        }

        return validBelow;
    }

    long long solve(long long N) {
        if (N < 0) return 0;
        if (N == 0) return 1;

        int L = 0;
        long long temp = N;
        while (temp > 0) { L++; temp >>= 1; }

        long long total = 1;

        for (int len = 1; len < L; len++) {
            total += countForLen(-1, len, false); // -1 is all 1s, essentially infinite
        }
        total += countForLen(N, L, true);
        return total;
    }

public:
    long long countBitwisePalindromesBalancedOnes(long long L, long long R) {
        return solve(R) - solve(L - 1);
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

