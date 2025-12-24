---
problem_id: NUM_COUNT_STRINGS_EXACT_VOWELS__6419
display_id: NUM-013
slug: count-strings-exact-vowels
title: "Count Strings With Exact Vowels"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Combinatorics
  - Modular Arithmetic
tags:
  - number-theory
  - combinatorics
  - modular
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-013: Count Strings With Exact Vowels

## Problem Statement

Count the number of strings of length `n` over lowercase English letters that contain exactly `k` vowels. Return the answer modulo `1000000007`.

Vowels are `a, e, i, o, u`.

![Problem Illustration](../images/NUM-013/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `k`

## Output Format

- Single integer: count modulo `1000000007`

## Constraints

- `1 <= n <= 1000000`
- `0 <= k <= n`

## Example

**Input:**

```
2 1
```

**Output:**

```
210
```

**Explanation:**

Choose 1 position for the vowel (C(2,1)=2), pick vowel (5 choices), pick consonant (21 choices):

2 * 5 * 21 = 210.

![Example Visualization](../images/NUM-013/example-1.png)

## Notes

- Count = C(n,k) * 5^k * 21^(n-k) mod M
- Precompute factorials and inverse factorials
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Combinatorics, Binomial Coefficients, Modular Arithmetic

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countStrings(int n, int k) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countStrings(n, k));
        sc.close();
    }
}
```

### Python

```python
def count_strings(n: int, k: int) -> int:
    # Your implementation here
    return 0

def main():
    n, k = map(int, input().split())
    print(count_strings(n, k))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    long long countStrings(int n, int k) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    Solution solution;
    cout << solution.countStrings(n, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function countStrings(n, k) {
  // Your implementation here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  console.log(countStrings(n, k));
});
```
