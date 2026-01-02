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
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int salt = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.oddAfterBitSalt(a, salt));
        sc.close();
    }
}
```

### Python

```python
import sys

def odd_after_bit_salt(a: list[int], salt: int) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    salt = int(data[ptr]); ptr += 1
    
    result = odd_after_bit_salt(a, salt)
    print(result)

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
    long long oddAfterBitSalt(vector<int>& a, int salt) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int salt;
    cin >> salt;
    
    Solution solution;
    cout << solution.oddAfterBitSalt(a, salt) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  oddAfterBitSalt(a, salt) {
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
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    
    const salt = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(String(solution.oddAfterBitSalt(a, salt)));
});
```

