---
problem_id: NUM_MODULAR_INVERSE_EXISTENCE__3507
display_id: NUM-003
slug: modular-inverse-existence
title: "Modular Inverse Existence"
difficulty: Easy
difficulty_score: 22
topics:
  - Number Theory
  - GCD
  - Modular Arithmetic
tags:
  - number-theory
  - gcd
  - modular
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-003: Modular Inverse Existence

## Problem Statement

For each query `(a, m)`, determine whether `a` has a modular inverse modulo `m`. An inverse exists if and only if `gcd(a, m) = 1`.

![Problem Illustration](../images/NUM-003/problem-illustration.png)

## Input Format

- First line: integer `q`
- Next `q` lines: two integers `a` and `m`

## Output Format

- For each query, print `true` if an inverse exists, otherwise `false`

## Constraints

- `1 <= q <= 100000`
- `1 <= a, m <= 10^9`

## Example

**Input:**

```
1
4 7
```

**Output:**

```
true
```

**Explanation:**

`gcd(4, 7) = 1`, so the inverse exists.

![Example Visualization](../images/NUM-003/example-1.png)

## Notes

- Use the Euclidean algorithm for gcd
- Time complexity: O(q log max(a,m))
- Space complexity: O(1)

## Related Topics

Modular Arithmetic, GCD, Euclid Algorithm

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean hasInverse(long a, long m) {
        //Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            Solution solution = new Solution();
            for (int i = 0; i < q; i++) {
                long a = sc.nextLong();
                long m = sc.nextLong();
                System.out.println(solution.hasInverse(a, m) ? "true" : "false");
            }
        }
        sc.close();
    }
}
```

### Python

```python
import math

def has_inverse(a: int, m: int) -> bool:
    # //Implement here
    return 0

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data: return
    q = int(input_data[0])
    idx = 1
    results = []
    for _ in range(q):
        a = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        results.append("true" if has_inverse(a, m) else "false")
    print("\n".join(results))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <numeric>

using namespace std;

class Solution {
public:
    bool hasInverse(long long a, long long m) {
        //Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (cin >> q) {
        Solution solution;
        for (int i = 0; i < q; i++) {
            long long a, m;
            cin >> a >> m;
            cout << (solution.hasInverse(a, m) ? "true" : "false") << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function hasInverse(a, m) {
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
  let idx = 0;
  const q = parseInt(data[idx++], 10);
  const out = [];
  for (let i = 0; i < q; i++) {
    const a = parseInt(data[idx++], 10);
    const m = parseInt(data[idx++], 10);
    out.push(hasInverse(a, m) ? "true" : "false");
  }
  console.log(out.join("\n"));
});
```

