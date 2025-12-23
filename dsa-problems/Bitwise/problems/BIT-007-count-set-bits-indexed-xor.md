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
        long result = solution.countSetBitsIndexedXor(a);
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
#include <unordered_set>
#include <tuple>
using namespace std;


class Solution {
public:
    long long countSetBitsIndexedXor(vector<int>& a) {
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
    long long result = solution.countSetBitsIndexedXor(a);
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
  countSetBitsIndexedXor(a) {
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
const result = solution.countSetBitsIndexedXor(a);
console.log(String(result));
```

