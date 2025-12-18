---
problem_id: BIT_SMALLEST_ABSENT_XOR__8409
display_id: BIT-009
slug: smallest-absent-xor
title: "Smallest Absent XOR"
difficulty: Medium
difficulty_score: 60
topics:
  - Bitwise Operations
  - XOR
  - XOR Basis
  - Linear Algebra
tags:
  - bitwise
  - xor
  - xor-basis
  - hard
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-009: Smallest Absent XOR

## Problem Statement

Given an array `a`, find the smallest non-negative integer `x` such that NO pair `(i, j)` exists where `a[i] XOR a[j] = x`.

```
ASCII Diagram: XOR Pairs
=========================
Array: [1, 2, 3]

All possible XOR values:
1 XOR 1 = 0
1 XOR 2 = 3
1 XOR 3 = 2
2 XOR 1 = 3
2 XOR 2 = 0
2 XOR 3 = 1
3 XOR 1 = 2
3 XOR 2 = 1
3 XOR 3 = 0

Reachable XORs: {0, 1, 2, 3}
Smallest absent: 4
```

## Input Format

- First line: Integer `n`
- Second line: `n` space-separated integers

## Output Format

Single integer representing smallest absent XOR

## Constraints

- `1 <= n <= 2 * 10^5`
- `0 <= a[i] <= 10^9`

## Example

**Input:**

```
3
1 2 3
```

**Output:**

```
4
```

**Explanation:**

Possible XOR values from pairs: {0, 1, 2, 3}
Smallest missing: 4

## Notes

- Use XOR basis to find reachable XORs
- MEX (minimal excludant) problem variant

## Related Topics

XOR Basis, Linear Algebra, Gaussian Elimination, MEX

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int smallestAbsentXOR(int[] a) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.smallestAbsentXOR(a));
        sc.close();
    }
}
```

### Python

```python
def smallest_absent_xor(a: list[int]) -> int:
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(smallest_absent_xor(a))

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
    int smallestAbsentXOR(vector<int>& a) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    Solution solution;
    cout << solution.smallestAbsentXOR(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  smallestAbsentXOR(a) {
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
  const n = parseInt(data[0]);
  const a = data[1].split(" ").map(Number);
  const solution = new Solution();
  console.log(solution.smallestAbsentXOR(a));
});
```
