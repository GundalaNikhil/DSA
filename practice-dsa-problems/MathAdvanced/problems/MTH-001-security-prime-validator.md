---
problem_id: MTH_SECURITY_PRIME_VALIDATOR__4741
display_id: NTB-MTH-4741
slug: security-prime-validator
title: "Security System Prime Validator"
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
  - security-prime-validator
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Security System Prime Validator

## Problem Statement

A cryptocurrency validation node receives `q` validation requests. Each request contains a number `x` that might be used as a cryptographic prime.

Your validation pipeline must follow these exact steps:

1. **Quick rejection**: If `x < 2`, immediately mark as `COMPOSITE`.
2. **Sieve gate**: Check if `x` is divisible by any prime in the range `[2, 10^6]`.
   - If divisible (and $x$ itself is not one of these primes), mark as `COMPOSITE`.
   - If $x$ is one of these primes, mark as `PRIME`.
   - If `x ≤ 10^{12}` and no small prime divides it, proceed to step 3.
3. **Deterministic witness testing**: Run Miller-Rabin primality test using exactly these witnesses in order: `{2, 3, 5, 7, 11, 13}`.
   - Stop as soon as any witness proves compositeness.
   - If all witnesses pass, the number is `PRIME`.

## Input Format

- First line: integer `q`.
- Next `q` lines: each contains a single integer `x`.

## Output Format

For each query, output:

- `PRIME k` if the number is prime.
- `COMPOSITE k` if the number is composite.

Where `k` is the number of Miller-Rabin witnesses evaluated in step 3 (0 if step 3 was never reached).

## Constraints

- `1 <= q <= 2 * 10^5`
- `0 <= x <= 10^{12}`

## Clarifying Notes

- A witness $a$ proves compositeness if $a^{x-1} \not\equiv 1 \pmod x$ and for all $r < s$, $a^{2^r \cdot d} \not\equiv -1 \pmod x$, where $x-1 = 2^s \cdot d$ and $d$ is odd.
- The witnesses must be tried in the exact order: 2, then 3, then 5, then 7, then 11, then 13.

## Example Input

```
5
1
2
49
9999999967
99999999619
```

## Example Output

```
COMPOSITE 0
PRIME 0
COMPOSITE 0
PRIME 2
COMPOSITE 1
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public static class ValidationResult {
        public String status;
        public int witnesses;
        public ValidationResult(String status, int witnesses) {
            this.status = status;
            this.witnesses = witnesses;
        }
    }

    public List<ValidationResult> validatePrimes(int q, long[] requests) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class ValidationResult:
    def __init__(self, status: str, witnesses: int):
        self.status = status
        self.witnesses = witnesses

class Solution:
    def validatePrimes(self, q: int, requests: list[int]) -> list[ValidationResult]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct ValidationResult {
    string status;
    int witnesses;
};

class Solution {
public:
    vector<ValidationResult> validatePrimes(int q, vector<long long>& requests) {
        // Your code here
        return {};
    }
};
```

```javascript
class ValidationResult {
  constructor(status, witnesses) {
    this.status = status;
    this.witnesses = witnesses;
  }
}

class Solution {
  /**
   * @param {number} q
   * @param {number[]} requests
   * @returns {ValidationResult[]}
   */
  validatePrimes(q, requests) {
    // Your code here
    return [];
  }
}
```
