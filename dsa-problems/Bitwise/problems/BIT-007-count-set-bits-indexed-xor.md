---
problem_id: BIT_COUNT_SETBITS_INDEXED_XOR__8407
display_id: BIT-007
slug: count-set-bits-indexed-xor
title: "Count Set Bits Of Indexed XOR"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - XOR
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - popcount
  - mathematics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-007: Count Set Bits Of Indexed XOR

## Problem Statement

Let b[i] = i XOR a[i] for i from 0 to n-1. Compute the total number of set bits across all values in b.

![Problem Illustration](../images/BIT-007/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the total count of set bits in b.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**
```
2
0 2
```

**Output:**
```
2
```

**Explanation:**

b = [0 XOR 0, 1 XOR 2] = [0, 3]. The popcounts are 0 and 2, totaling 2.

![Example Visualization](../images/BIT-007/example-1.png)

## Notes

- Indices are 0-based.
- Use 64-bit arithmetic for the total.

## Related Topics

Bitwise Operations, Counting Bits

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countSetBitsIndexedXor(int[] a) {
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

        Solution solution = new Solution();
        System.out.println(solution.countSetBitsIndexedXor(a));
        sc.close();
    }
}
```

### Python

```python
import sys

def count_set_bits_indexed_xor(a: list[int]) -> int:
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
    
    result = count_set_bits_indexed_xor(a)
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
    long long countSetBitsIndexedXor(vector<int>& a) {
        long long total = 0;
        for (int i = 0; i < a.size(); i++) {
            // __builtin_popcount is a GCC/Clang intrinsic.
            // For standard C++20, use <bit> std::popcount
            total += __builtin_popcount(i ^ a[i]);
        }
        return total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    cout << solution.countSetBitsIndexedXor(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countSetBitsIndexedXor(a) {
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
    
    const solution = new Solution();
    console.log(solution.countSetBitsIndexedXor(a));
});
```

