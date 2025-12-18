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

Given an array `a` of size `n`, compute the total number of set bits across all elements of the sequence `b[i] = i XOR a[i]` for `i` from `0` to `n-1`.

In other words, calculate: `popcount(0 XOR a[0]) + popcount(1 XOR a[1]) + ... + popcount((n-1) XOR a[n-1])`

```
ASCII Diagram: Indexed XOR Process
===================================
Index i:  0   1   2   3   ...
Array a:  a0  a1  a2  a3  ...

Compute:  0^a0  1^a1  2^a2  3^a3  ...
          ↓     ↓     ↓     ↓
Count     c0    c1    c2    c3    ...
set bits

Total = c0 + c1 + c2 + ... + c(n-1)
```

## Input Format

- First line: Integer `n` - array size
- Second line: `n` space-separated integers representing array `a`

## Output Format

A single integer representing the total count of set bits

## Constraints

- `1 <= n <= 2 * 10^5`
- `0 <= a[i] <= 10^9`

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

```
Index-by-Index Calculation:
===========================
i = 0: b[0] = 0 XOR a[0] = 0 XOR 0 = 0
       Binary: 000
       Set bits: 0

i = 1: b[1] = 1 XOR a[1] = 1 XOR 2 = 3
       Binary: 011
       Set bits: 2

Total set bits = 0 + 2 = 2
```

```
Detailed XOR Calculation:
=========================
i=0, a[0]=0:
  0: 000
^ 0: 000
  --------
  0: 000  → popcount = 0

i=1, a[1]=2:
  1: 001
^ 2: 010
  --------
  3: 011  → popcount = 2 (two 1s)

Sum = 0 + 2 = 2
```

## Notes

- The sequence b[i] is not stored; we only need the total count
- Process each bit position independently for optimization
- XOR property: bit k in (i XOR a[i]) is set if bit k differs between i and a[i]
- For bit k, count how many indices have bit k set vs unset
- Total set bits at position k = ones_in_indices[k] × zeros_in_array[k] + zeros_in_indices[k] × ones_in_array[k]

## Related Topics

XOR Properties, Bit Counting, Hamming Weight, Mathematical Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countSetBitsIndexedXOR(int[] a) {
        // Your implementation here
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
        long result = solution.countSetBitsIndexedXOR(a);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def count_set_bits_indexed_xor(a: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))

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
    long long countSetBitsIndexedXOR(vector<int>& a) {
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
    cout << solution.countSetBitsIndexedXOR(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countSetBitsIndexedXOR(a) {
    // Your implementation here
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
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const a = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.countSetBitsIndexedXOR(a));
});
```
