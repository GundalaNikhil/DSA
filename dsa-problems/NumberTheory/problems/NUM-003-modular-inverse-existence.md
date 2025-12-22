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
        // Your implementation here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        Solution solution = new Solution();
        for (int i = 0; i < q; i++) {
            long a = sc.nextLong();
            long m = sc.nextLong();
            System.out.println(solution.hasInverse(a, m) ? "true" : "false");
        }
        sc.close();
    }
}
```

### Python

```python
def has_inverse(a: int, m: int) -> bool:
    # Your implementation here
    return False

def main():
    q = int(input())
    for _ in range(q):
        a, m = map(int, input().split())
        print("true" if has_inverse(a, m) else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    bool hasInverse(long long a, long long m) {
        // Your implementation here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    Solution solution;
    for (int i = 0; i < q; i++) {
        long long a, m;
        cin >> a >> m;
        cout << (solution.hasInverse(a, m) ? "true" : "false") << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function hasInverse(a, m) {
  // Your implementation here
  return false;
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
