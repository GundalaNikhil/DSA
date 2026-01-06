---
problem_id: MTH_MODULAR_PRODUCT_DATABASES__8128
display_id: NTB-MTH-8128
slug: modular-product-databases
title: "Modular Product Calculator for Databases"
difficulty: Medium
difficulty_score: 50
topics:
  - Math Advanced
tags:
  - advanced-math
  - algorithms
  - coding-interviews
  - cryptography
  - data-structures
  - mathadvanced
  - modular-product-databases
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Modular Product Calculator for Databases

## Problem Statement

A database system uses hash values computed as products of consecutive integers modulo a prime. Given a range `[L, R]`, compute the product:

```
Product = L * (L+1) * ... * R (mod P)
```

## Input Format

- First line: `P` (prime modulus) and `q`.
- Next `q` lines: `L` and `R`.

## Output Format

- One integer per query (the product mod P).

## Constraints

- `P` is prime, `2 <= P <= 2 * 10^9`.
- `1 <= q <= 2 * 10^5`.
- `0 <= L <= R < P`.

## Clarifying Notes

- If the range `[L, R]` contains `0`, the entire product is `0`.
- For efficiency, consider that $P$ is large and $q$ is also large.

## Example Input

```
1000000007 3
1 4
0 5
10 10
```

## Example Output

```
24
0
10
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Long> calculateProducts(int P, int q, int[][] queries) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def calculateProducts(self, P: int, q: int, queries: list[list[int]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> calculateProducts(int P, int q, vector<vector<int>>& queries) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} P
   * @param {number} q
   * @param {number[][]} queries
   * @returns {number[]}
   */
  calculateProducts(P, q, queries) {
    // Your code here
    return [];
  }
}
```
