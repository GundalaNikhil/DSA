---
problem_id: BIT_XOR_ODD_OCCURRENCE__8401
display_id: BIT-001
slug: odd-after-bit-salt
title: "Odd After Bit Salt"
difficulty: Easy
difficulty_score: 30
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Mathematics
tags:
  - bitwise
  - xor
  - array
  - mathematics
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-001: Odd After Bit Salt

## Problem Statement

Each array element x is transformed to x XOR salt, where salt is the same for all elements. In the transformed multiset, exactly one value appears an odd number of times and all others appear an even number of times.
Find that odd-occurring value without explicitly building the transformed array.

![Problem Illustration](../images/BIT-001/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer salt

## Output Format

Print the transformed value that appears an odd number of times.

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= a[i] <= 1000000000`
- `-1000000000 <= salt <= 1000000000`

## Example

**Input:**

```
7
4 1 2 1 2 4 7
3
```

**Output:**

```
4
```

**Explanation:**

XOR all values with salt and use XOR aggregation; the odd-occurring transformed
value is 4.

![Example Visualization](../images/BIT-001/example-1.png)

## Notes

- XOR is associative and cancels even counts.
- You do not need to materialize the transformed array.

## Related Topics

Bitwise Operations, XOR, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long oddAfterBitSalt(int[] a, int salt) {
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
        int salt = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.oddAfterBitSalt(a, salt);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def odd_after_bit_salt(a: list[int], salt: int) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    salt = int(input())

    result = odd_after_bit_salt(a, salt)
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
    long long oddAfterBitSalt(vector<int>& a, int salt) {
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
    int salt;
    cin >> salt;

    Solution solution;
    long long result = solution.oddAfterBitSalt(a, salt);
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
  oddAfterBitSalt(a, salt) {
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
const salt = Number(data[idx++]);

const solution = new Solution();
const result = solution.oddAfterBitSalt(a, salt);
console.log(String(result));
```
