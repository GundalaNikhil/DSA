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

Count numbers in the range `[L, R]` whose binary representation is a palindrome AND whose number of set bits (1s) is even.

## Input Format

- Single line: Two integers `L` and `R`

## Output Format

Single integer representing the count of valid numbers

## Constraints

- `0 <= L <= R <= 10^12`

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

Check each number in [5, 12]:

- 5 = 101 (binary): palindrome ✓, set bits = 2 (even) ✓ → COUNT
- 6 = 110: not palindrome ✗
- 7 = 111: palindrome ✓, set bits = 3 (odd) ✗
- 8 = 1000: not palindrome ✗
- 9 = 1001: palindrome ✓, set bits = 2 (even) ✓ → COUNT
- 10 = 1010: not palindrome ✗
- 11 = 1011: not palindrome ✗
- 12 = 1100: not palindrome ✗

Valid numbers: 5, 9 → Count = 2

## Notes

- Generate palindromes by mirroring
- Track popcount during generation
- Filter for even set bits

## Related Topics

Binary Palindrome, Bit Counting, Number Generation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countPalindromesBalanced(long L, long R) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long L = sc.nextLong();
        long R = sc.nextLong();
        Solution solution = new Solution();
        System.out.println(solution.countPalindromesBalanced(L, R));
        sc.close();
    }
}
```

### Python

```python
def count_palindromes_balanced(L: int, R: int) -> int:
    return 0

def main():
    L, R = map(int, input().split())
    print(count_palindromes_balanced(L, R))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int countPalindromesBalanced(long long L, long long R) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long L, R;
    cin >> L >> R;
    Solution solution;
    cout << solution.countPalindromesBalanced(L, R) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countPalindromesBalanced(L, R) {
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
  const [L, R] = data[0].split(" ").map(Number);
  const solution = new Solution();
  console.log(solution.countPalindromesBalanced(L, R));
});
```
