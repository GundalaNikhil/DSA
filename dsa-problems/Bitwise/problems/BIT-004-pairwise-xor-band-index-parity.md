---
problem_id: BIT_PAIRWISE_XOR_BAND_PARITY__8404
display_id: BIT-004
slug: pairwise-xor-band-index-parity
title: "Pairwise XOR in Band With Index Parity"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Array
tags:
  - bitwise
  - xor
  - trie
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-004: Pairwise XOR in Band With Index Parity

## Problem Statement

Given an array and range `[L, U]`, count the number of index pairs `(i, j)` such that `i < j`, `i + j` is even, and the XOR sum `a[i] ^ a[j]` falls within `[L, U]`.

![Problem Illustration](../images/BIT-004/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integers L and U

## Output Format

Print the number of valid pairs.

## Constraints

- `1 <= n <= 100000`
- `0 <= a[i] <= 1000000000`
- `0 <= L <= U <= 1000000000`

## Example

**Input:**

```
4
2 3 1 7
1 4
```

**Output:**

```
2
```

**Explanation:**

Valid pairs are (0,2): 2 XOR 1 = 3 and (1,3): 3 XOR 7 = 4. Both have i + j even.

![Example Visualization](../images/BIT-004/example-1.png)

## Notes

- Indices are 0-based.
- Only pairs with i + j even are counted.

## Related Topics

Bitwise Operations, XOR, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countPairwiseXorBandParity(int[] a, int L, int U) {
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
        int L = sc.nextInt();
        int U = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.countPairwiseXorBandParity(a, L, U);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def count_pairwise_xor_band_parity(a: list[int], L: int, U: int) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    L, U = map(int, input().split())

    result = count_pairwise_xor_band_parity(a, L, U)
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
    long long countPairwiseXorBandParity(vector<int>& a, int L, int U) {
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
    int L, U;
    cin >> L >> U;

    Solution solution;
    long long result = solution.countPairwiseXorBandParity(a, L, U);
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
  countPairwiseXorBandParity(a, L, U) {
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
const L = Number(data[idx++]);
const U = Number(data[idx++]);

const solution = new Solution();
const result = solution.countPairwiseXorBandParity(a, L, U);
console.log(String(result));
```
