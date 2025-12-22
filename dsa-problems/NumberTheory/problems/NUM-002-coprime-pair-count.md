---
problem_id: NUM_COPRIME_PAIR_COUNT__7194
display_id: NUM-002
slug: coprime-pair-count
title: "Coprime Pair Count Up To N"
difficulty: Medium
difficulty_score: 48
topics:
  - Number Theory
  - Euler Totient
  - Counting
tags:
  - number-theory
  - totient
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-002: Coprime Pair Count Up To N

## Problem Statement

Given an integer `N`, count the number of ordered pairs `(i, j)` such that `1 <= i < j <= N` and `gcd(i, j) = 1`.

![Problem Illustration](../images/NUM-002/problem-illustration.png)

## Input Format

- Single line: integer `N`

## Output Format

- Single integer: number of coprime pairs

## Constraints

- `1 <= N <= 100000`

## Example

**Input:**

```
5
```

**Output:**

```
7
```

**Explanation:**

The coprime pairs are:

(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4)

Total = 7.

![Example Visualization](../images/NUM-002/example-1.png)

## Notes

- The answer equals sum_{k=2..N} phi(k)
- Compute phi for all k with a sieve
- Time complexity: O(N log log N)
- Space complexity: O(N)

## Related Topics

Euler Totient, Counting, GCD

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countCoprimePairs(int N) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countCoprimePairs(N));
        sc.close();
    }
}
```

### Python

```python
def count_coprime_pairs(N: int) -> int:
    # Your implementation here
    return 0

def main():
    N = int(input())
    print(count_coprime_pairs(N))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    long long countCoprimePairs(int N) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    Solution solution;
    cout << solution.countCoprimePairs(N) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function countCoprimePairs(N) {
  // Your implementation here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const N = parseInt(data[0], 10);
  console.log(countCoprimePairs(N));
});
```
