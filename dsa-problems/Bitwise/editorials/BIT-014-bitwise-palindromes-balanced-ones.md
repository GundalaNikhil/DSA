---
problem_id: BIT_PALINDROMES_BALANCED_ONES__8414
display_id: BIT-014
slug: bitwise-palindromes-balanced-ones
title: "Bitwise Palindromes With Balanced Ones"
difficulty: Medium
difficulty_score: 62
topics:
  - Bitwise Operations
  - Palindrome
  - Bit Counting
  - Number Theory
tags:
  - bitwise
  - palindrome
  - popcount
  - number-generation
  - medium
premium: true
subscription_tier: basic
---

# BIT-014: Bitwise Palindromes With Balanced Ones

## 📋 Problem Summary

Count the integers in the range `[L, R]` that satisfy two conditions:

1. Their binary representation is a palindrome (reads same forwards and backwards).
2. The total number of set bits (1s) is even.

## 🌍 Real-World Scenario

**Scenario Title:** The Symmetric Verification Code

You are designing a secure optical recognition system.

- **Markers**: The system uses binary markers printed on objects.
- **Robustness**: To ensure the marker is read correctly regardless of orientation (left-to-right or right-to-left), the codes must be **palindromes**.
- **Error Checking**: To detect single-bit flip errors (dirt/damage), the codes must have a fast parity check (Even Parity - even number of 1s).
- **Task**: You need to calculate how many valid codes exist within a specific numeric range `[L, R]` to see if the ID space is large enough.

**Why This Problem Matters:**

- **Constructive Counting**: Instead of iterating $10^{12}$ numbers, we construct valid numbers directly.
- **Symmetry Properties**: Leveraging palindrome structure to halve the search space.
- **Parity Constraints**: Combining structural constraints with arithmetic ones.

![Real-World Application](../images/BIT-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Palindrome Construction

```
Length 5 (Odd):
Structure: [A B C B A]
Pairs: (A, A), (B, B). Middle: C.
Popcount = 2*weight(A) + 2*weight(B) + weight(C).
Since 2*k is always even, Popcount parity depends ONLY on C.
For Even Popcount -> Middle bit C must be 0.

Length 4 (Even):
Structure: [A B B A]
Pairs: (A, A), (B, B).
Popcount = 2*weight(A) + 2*weight(B).
Always Even!
Condition is automatically satisfied for all even-length palindromes.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Range `[L, R]`.
- **Leading Zeros**: Not allowed. This implies the Most Significant Bit (MSB) is 1. Consequently, the Least Significant Bit (LSB) must also be 1.
- **Constraints**: Up to $10^{12}$. $O(\sqrt{N})$ or $O(N)$ is too slow. $O(\log N)$ required.

Common interpretation mistake:

- ❌ Iterating from L to R.
- ✅ Counting valid numbers $\le X$ and computing `Solve(R) - Solve(L-1)`.

### Core Concept: Constructing Palindromes

A binary palindrome of length `k` is fully determined by its first $\lceil k/2 \rceil$ bits.
Let `H = ceil(k/2)`.
Value `V` is an integer of `H` bits (where MSB is 1).
We can "unfold" `V` to create the palindrome.

**Parity Check**:

1. **Even Length k**: Every bit in the first half is mirrored. Total 1s is even. **All** even-length palindromes are valid.
2. **Odd Length k**: The middle bit is unique. The rest are mirrored (contribute even 1s). For total 1s to be even, the **middle bit must be 0**. In the "first half" representation, this corresponds to the LSB of `V` being 0.

## Naive Approach (Iterate)

### Intuition

Check every number.

### Algorithm

1. Loop `i` from `L` to `R`.
2. Convert to binary string.
3. Check palindrome + count bits.

### Time Complexity

- **O(R - L)**. TLE for large ranges.

### Space Complexity

- **O(log R)**.

## Optimal Approach (digit DP / Construction)

### Key Insight

Calculate `count(N)`: number of valid integers in `[0, N]`.
Sum valid counts for all lengths `len < BitLen(N)`.
Then specifically count valid numbers of length `BitLen(N)` that are $\le N$.

### Algorithm for `count(N)`

1. If `N < 0` return 0. Base count = 1 (for 0).
2. Let `L` = bit length of `N`.
3. **Phase 1: Smaller Lengths**:
   - Loop `len` from 1 to `L-1`.
   - `half_len = (len + 1) / 2`.
   - Number of choices for "half":
     - Basic count is $2^{\text{half\_len} - 1}$ (MSB fixed to 1).
     - If `len` even: Use full count.
     - If `len` odd: Half must end in 0. So we fix MSB=1, LSB=0. Free bits: `half_len - 2`. Count $2^{\text{half\_len} - 2}$. (If `half_len < 2`, count is determined).
   - Add to total.
4. **Phase 2: Same Length**:
   - Construct the "target half" from the first `ceil(L/2)` bits of `N`. Let this be `limit_prefix`.
   - Iterate valid prefixes from `10...0` up to `limit_prefix`.
   - Note: We can calculate how many are strictly less than `limit_prefix` mathematically.
   - **Boundary Check**: For `limit_prefix` itself, construct the full palindrome. If `palindrome <= N`, count it.
   - Constraint Logic:
     - If `L` even: `limit_prefix` is valid. All values `< limit_prefix` valid.
     - If `L` odd: `limit_prefix` must have LSB 0. We count multiples of 2 in range `[LB, limit_prefix)`.

### Time Complexity

- **O(log N)** (proportional to number of bits).

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-014/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-014/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private long makePalindrome(long half, int len) {
        long res = half;
        int bitsToMirror = len / 2;
        // If len is 5 (10101), half has 3 bits. We mirror non-middle.
        // If len is 4 (1001), half has 2 bits. We mirror all.
        // General: We mirror 'len - ceil(len/2)' bits.
        // Which are the lower bits of half? No, the whole half is prefix.
        // Example len=5. half=110 (6). Palindrome 11011.
        // Sequence: half (110) then append reverse of 11 (3).

        long lower = 0;
        long temp = half;
        if (len % 2 == 1) temp >>= 1; // Skip middle bit for mirroring

        for (int i = 0; i < len / 2; i++) {
            lower = (lower << 1) | (temp & 1);
            temp >>= 1;
        }
        return (res << (len / 2)) | lower;
    }

    // Counts valid palindromes <= N with exact bit length 'len'
    private long countForLen(long N, int len, boolean isLimit) {
        int halfLen = (len + 1) / 2;
        long minHalf = 1L << (halfLen - 1);
        long maxHalf = (1L << halfLen) - 1;

        if (isLimit) {
            long prefix = N >>> (len - halfLen);
            if (prefix < minHalf) return 0; // Should not happen if len matches N
            maxHalf = Math.min(maxHalf, prefix);
        }

        long count = 0;

        // If len is odd, half must be even (LSB 0) implies palindrome middle is 0.
        // If len is even, any half is valid.

        // We need numbers in [minHalf, maxHalf] satisfying condition
        // If isLimit is true and we pick maxHalf, we must verify reconstruction.
        // So standard logic: Count strictly less than maxHalf, then check maxHalf.

        long limitVal = maxHalf;

        // Count in range [minHalf, limitVal - 1]
        // If len even: count all integers.
        // If len odd: count even integers.

        long validBelow = 0;

        if (limitVal > minHalf) {
            if (len % 2 == 0) {
                validBelow = limitVal - minHalf;
            } else {
                // Count evens in [minHalf, limitVal - 1]
                // minHalf is power of 2, so it is even.
                // Range [E, X). Count evens is (X - E + 1) / 2
                validBelow = (limitVal - minHalf + 1) / 2;
            }
        }

        // Check boundary limitVal
        boolean checkBoundary = true;

        // If len odd and limitVal is odd, it's invalid
        if (len % 2 == 1 && (limitVal % 2 != 0)) checkBoundary = false;

        if (checkBoundary) {
            long p = makePalindrome(limitVal, len);
            if (!isLimit || p <= N) {
                validBelow++;
            }
        }

        return validBelow;
    }

    private long solve(long N) {
        if (N < 0) return 0;
        if (N == 0) return 1; // 0 is palindrome and even bits (0)

        // Length of N
        int L = 0;
        long temp = N;
        while (temp > 0) { L++; temp >>= 1; }

        long total = 1; // Count 0

        // Lengths strictly less than L
        for (int len = 1; len < L; len++) {
            total += countForLen(Long.MAX_VALUE, len, false);
        }

        // Length equal to L
        total += countForLen(N, L, true);

        return total;
    }

    public long countBitwisePalindromesBalancedOnes(long L, long R) {
        return solve(R) - solve(L - 1);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long L = sc.nextLong();
        long R = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.countBitwisePalindromesBalancedOnes(L, R));
        sc.close();
    }
}
```

### Python

```python
import sys

def make_palindrome(half, length):
    res = half
    temp = half
    if length % 2 == 1:
        temp >>= 1

    lower = 0
    for _ in range(length // 2):
        lower = (lower << 1) | (temp & 1)
        temp >>= 1

    return (res << (length // 2)) | lower

def count_for_len(N, length, is_limit):
    half_len = (length + 1) // 2
    min_half = 1 << (half_len - 1)
    max_half = (1 << half_len) - 1

    if is_limit:
        prefix = N >> (length - half_len)
        max_half = min(max_half, prefix)

    limit_val = max_half
    valid_below = 0

    if limit_val > min_half:
        if length % 2 == 0:
            valid_below = limit_val - min_half
        else:
            # Count evens in [min_half, limit_val - 1]
            # min_half is even
            valid_below = (limit_val - min_half + 1) // 2

    # Check boundary
    check_boundary = True
    if length % 2 == 1 and (limit_val % 2 != 0):
        check_boundary = False

    if check_boundary:
        p = make_palindrome(limit_val, length)
        # When not at limit, we can construct the full range for the given length
        # When at limit, verify the palindrome doesn't exceed N
        if not is_limit or p <= N:
            valid_below += 1

    return valid_below

def solve(N):
    if N < 0: return 0
    if N == 0: return 1

    L = N.bit_length()
    total = 1 # count 0

    for length in range(1, L):
        total += count_for_len(2**63, length, False)

    total += count_for_len(N, L, True)
    return total

def count_bitwise_palindromes_balanced_ones(L: int, R: int) -> int:
    return solve(R) - solve(L - 1)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return

    L = int(data[0])
    R = int(data[1])

    result = count_bitwise_palindromes_balanced_ones(L, R)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
    long long makePalindrome(long long half, int len) {
        long long res = half;
        long long temp = half;
        if (len % 2 == 1) temp >>= 1;

        long long lower = 0;
        for (int i = 0; i < len / 2; i++) {
            lower = (lower << 1) | (temp & 1);
            temp >>= 1;
        }
        return (res << (len / 2)) | lower;
    }

    long long countForLen(long long N, int len, bool isLimit) {
        int halfLen = (len + 1) / 2;
        long long minHalf = 1LL << (halfLen - 1);
        long long maxHalf = (1LL << halfLen) - 1;

        if (isLimit) {
            long long prefix = N >> (len - halfLen);
            if (prefix < minHalf) return 0;
            maxHalf = min(maxHalf, prefix);
        }

        long long limitVal = maxHalf;
        long long validBelow = 0;

        if (limitVal > minHalf) {
            if (len % 2 == 0) {
                validBelow = limitVal - minHalf;
            } else {
                validBelow = (limitVal - minHalf + 1) / 2;
            }
        }

        bool checkBoundary = true;
        if (len % 2 == 1 && (limitVal % 2 != 0)) checkBoundary = false;

        if (checkBoundary) {
            long long p = makePalindrome(limitVal, len);
            if (!isLimit || p <= N) {
                validBelow++;
            }
        }

        return validBelow;
    }

    long long solve(long long N) {
        if (N < 0) return 0;
        if (N == 0) return 1;

        int L = 0;
        long long temp = N;
        while (temp > 0) { L++; temp >>= 1; }

        long long total = 1;

        for (int len = 1; len < L; len++) {
            total += countForLen(-1, len, false); // -1 is all 1s, essentially infinite
        }
        total += countForLen(N, L, true);
        return total;
    }

public:
    long long countBitwisePalindromesBalancedOnes(long long L, long long R) {
        return solve(R) - solve(L - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    Solution solution;
    cout << solution.countBitwisePalindromesBalancedOnes(L, R) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  makePalindrome(half, len) {
    let res = half;
    let temp = half;
    if (len % 2 === 1) temp >>= 1n;

    let lower = 0n;
    const halfLen = BigInt(Math.floor(len / 2));
    for (let i = 0; i < halfLen; i++) {
      lower = (lower << 1n) | (temp & 1n);
      temp >>= 1n;
    }
    return (res << halfLen) | lower;
  }

  countForLen(N, len, isLimit) {
    const halfLen = Math.floor((len + 1) / 2);
    const minHalf = 1n << BigInt(halfLen - 1);
    let maxHalf = (1n << BigInt(halfLen)) - 1n;

    if (isLimit) {
      const prefix = N >> BigInt(len - halfLen);
      if (prefix < minHalf) return 0n;
      if (prefix < maxHalf) maxHalf = prefix;
    }

    let limitVal = maxHalf;
    let validBelow = 0n;

    if (limitVal > minHalf) {
      if (len % 2 === 0) {
        validBelow = limitVal - minHalf;
      } else {
        // Count evens
        validBelow = (limitVal - minHalf + 1n) / 2n;
      }
    }

    let checkBoundary = true;
    if (len % 2 === 1 && limitVal % 2n !== 0n) checkBoundary = false;

    if (checkBoundary) {
      const p = this.makePalindrome(limitVal, len);
      if (!isLimit || p <= N) {
        validBelow++;
      }
    }

    return validBelow;
  }

  solve(N) {
    if (N < 0n) return 0n;
    if (N === 0n) return 1n;

    let L = 0;
    let temp = N;
    while (temp > 0n) {
      L++;
      temp >>= 1n;
    }

    let total = 1n;

    for (let len = 1; len < L; len++) {
      // Pass a very large number for infinite limit
      total += this.countForLen(1n << 62n, len, false);
    }
    total += this.countForLen(N, L, true);
    return total;
  }

  countBitwisePalindromesBalancedOnes(L, R) {
    return this.solve(R) - this.solve(L - 1n);
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

  const L = BigInt(tokens[0]);
  const R = BigInt(tokens[1]);

  const solution = new Solution();
  console.log(solution.countBitwisePalindromesBalancedOnes(L, R).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `5, 12`. Range `[101₂, 1100₂]` = `[5, 12]` in decimal.

**Solve(12)** (Binary `1100`, length=4):

- **Len 1**: Number `1` (binary `1`). Popcount=1 (odd). Even popcount required → Invalid. Count: 0
- **Len 2**: Number `11` (binary `11` = 3). Popcount=2 (even). Valid palindrome. Count: 1

- **Len 3**: Checking `101` (5, even popcount) and `111` (7, odd popcount).

  - HalfLen=2. Min=`10₂`, Max=`11₂`
  - Range [2, 3) in decimal
  - Even count in range: 1 (value 2 → generates `101`)
  - Boundary value 3 (odd) → Invalid
  - Valid: `101` (5). Count: 1

- **Len 4**: N=`1100₂` (12). HalfLen=2. Min=`10₂`, Max=`11₂`
  - Prefix of N: `11₂`
  - Below prefix `11`: Value `10` → generates `1001₂` (9, even popcount). Valid.
  - Check boundary `11`: Palindrome `1111₂` (15). `15 > 12` → Not counted.
  - Valid from len 4: 9. Count: 1

**Total**: `0 + 1 + 1 + 1 = 3` valid numbers: **3, 5, 9**
**Solve(4)** (Binary 100).

- Len 1: 0.
- Len 2: 1 (3).
- Len 3: Limit 4 (100). Half `10`.
  - Prefix `10`. MaxHalf `10`.
  - Below `10`: Empty.
  - Check `10`: `101` (5). `5 > 4`.
  - Valid 0.
    Total `0 + 1 + 0 = 1`. (Number: 3).
    **Result**: `3 - 1 = 2`.
    Valid Numbers in `[5, 12]`: 5, 9. (3 is outside).
    Correct. Matches Example.

## ✅ Proof of Correctness

### Invariant

The construction correctly identifies the bijection between the first $\lceil L/2 \rceil$ bits and the full palindrome. The parity condition simplifies cleanly to "All even lengths valid" and "Odd lengths must have 0 middle". We effectively iterate the smaller search space of prefixes.

## 💡 Interview Extensions (High-Value Add-ons)

- **Divisibility**: Count palindromes divisible by K (much harder).
- **Base-K**: Generalize to base K palindromes.

## Common Mistakes to Avoid

1. **Length 1**:
   - ❌ `1` has odd bits.
   - ✅ My logic handles it (Odd len, must be even half -> bit 0 -> invalid for leading 1).
2. **0 Case**:
   - ❌ Skipping 0.
   - ✅ Handled explicitly.

## Related Concepts

- **Digit DP**: Thinking in terms of constructing prefixes.
- **Combinatorics**: Counting with symmetries.
