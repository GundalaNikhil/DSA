---
problem_id: NUM_COUNT_SURJECTIVE_FUNCTIONS__7773
display_id: NUM-016
slug: count-surjective-functions
title: "Count Surjective Functions"
difficulty: Medium
difficulty_score: 55
topics:
  - Number Theory
  - Combinatorics
  - Inclusion-Exclusion
tags:
  - number-theory
  - combinatorics
  - inclusion-exclusion
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-016: Count Surjective Functions

## Problem Statement

Count the number of surjective (onto) functions from an n-element set to a k-element set. Return the result modulo `1000000007`.

![Problem Illustration](../images/NUM-016/problem-illustration.png)

## Input Format

- Single line: two integers `n` and `k`

## Output Format

- Single integer: number of surjective functions modulo `1000000007`

## Constraints

- `1 <= k <= n <= 30`

## Example

**Input:**

```
3 2
```

**Output:**

```
6
```

**Explanation:**

There are 2^3 total functions. Remove the 2 functions that map all elements to a single value.

2^3 - 2 = 6.

![Example Visualization](../images/NUM-016/example-1.png)

## Notes

- Use inclusion-exclusion: sum_{i=0..k} (-1)^i C(k,i) (k-i)^n
- Time complexity: O(k^2)
- Space complexity: O(k)

## Related Topics

Inclusion-Exclusion, Combinatorics, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countSurjections(int n, int k) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.countSurjections(n, k));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def power(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def count_surjections(n: int, k: int) -> int:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    print(count_surjections(n, k))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long countSurjections(int n, int k) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        cout << solution.countSurjections(n, k) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

const MOD = 1000000007n;

function countSurjections(n, k) {
  //Implement here
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
  console.log(countSurjections(n, k));
});
```

