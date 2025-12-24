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
    public long countBitwisePalindromesBalancedOnes(long L, long R) {
        // Your implementation here
        return 0L;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long L = sc.nextLong();
        long R = sc.nextLong();

        Solution solution = new Solution();
        long result = solution.countBitwisePalindromesBalancedOnes(L, R);
        System.out.println(result);
        sc.close();
    }
}
```


### Python

```python
def count_bitwise_palindromes_balanced_ones(L: int, R: int) -> int:
    # Your implementation here
    return 0

def main():
    L, R = map(int, input().split())

    result = count_bitwise_palindromes_balanced_ones(L, R)
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
    long long countBitwisePalindromesBalancedOnes(long long L, long long R) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    cin >> L >> R;

    Solution solution;
    long long result = solution.countBitwisePalindromesBalancedOnes(L, R);
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
  countBitwisePalindromesBalancedOnes(L, R) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const L = BigInt(data[idx++]);
const R = BigInt(data[idx++]);

const solution = new Solution();
const result = solution.countBitwisePalindromesBalancedOnes(L, R);
console.log(String(result));
```

