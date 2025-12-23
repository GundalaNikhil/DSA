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

Find the smallest non-negative integer x that cannot be represented as the XOR of any subset of the array (including the empty subset).

![Problem Illustration](../images/BIT-009/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the smallest absent XOR value.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

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

The reachable subset XOR values are {0, 1, 2, 3}. The smallest non-negative integer
not in the set is 4.

![Example Visualization](../images/BIT-009/example-1.png)

## Notes

- The empty subset is allowed and contributes XOR 0.
- Use a linear basis to characterize reachable XOR values.

## Related Topics

Bitwise Operations, Linear Basis

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long smallestAbsentXor(int[] a) {
        // Your implementation here
        return 0L;
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
        long result = solution.smallestAbsentXor(a);
        System.out.println(result);
        sc.close();
    }
}
```


### Python

```python
def smallest_absent_xor(a: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = smallest_absent_xor(a)
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
    long long smallestAbsentXor(vector<int>& a) {
        // Your implementation here
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
    long long result = solution.smallestAbsentXor(a);
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
  smallestAbsentXor(a) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const n = Number(data[idx++]);
const a = [];
for (let i = 0; i < n; i++) {
  a.push(Number(data[idx++]));
}

const solution = new Solution();
const result = solution.smallestAbsentXor(a);
console.log(String(result));
```

