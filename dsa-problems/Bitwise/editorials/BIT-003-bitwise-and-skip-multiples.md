---
problem_id: BIT_AND_SKIP_MULTIPLES__8403
display_id: BIT-003
slug: bitwise-and-skip-multiples
title: "Bitwise AND Skipping Multiples"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - AND
  - Number Theory
  - Mathematics
tags:
  - bitwise
  - and-operation
  - number-theory
  - medium
premium: true
subscription_tier: basic
---

# BIT-003: Bitwise AND Skipping Multiples

## 📋 Problem Summary

Compute the Bitwise AND of all integers in the range `[L, R]` that are **not** divisible by `m`. If no such numbers exist, return -1.

## 🌍 Real-World Scenario

**Scenario Title:** The Secure Channel Hopping

You are configuring a frequency hopping spread spectrum system.
- **Spectrum**: Channels are numbered `L` to `R`.
- **Interference**: Some channels are blocked by a strong 50Hz hum harmonic (multiples of `m`).
- **Configuration**: You need to set a "Master Mask" that defines the bits that are *always* 1 across all valid hops. This helps the receiver synchronize.
- **Goal**: Calculate the AND of all valid channel IDs to find the stable bits.

**Why This Problem Matters:**

- **Range Queries**: Efficiently aggregating properties over large intervals.
- **Sparse Data**: Dealing with data that has regular "holes".
- **Bitwise Logic**: Understanding how `AND` converges to the common prefix.

![Real-World Application](../images/BIT-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Skipping Pattern
```
L=10, R=15, m=3
Range: 10, 11, 12, 13, 14, 15
Skip multiples of 3: 12, 15.

Valid Numbers:
10: 1 0 1 0
11: 1 0 1 1
13: 1 1 0 1
14: 1 1 1 0

AND Calculation:
Col 3 (8s): 1, 1, 1, 1 -> 1
Col 2 (4s): 0, 0, 1, 1 -> 0
Col 1 (2s): 1, 1, 0, 1 -> 0
Col 0 (1s): 0, 1, 1, 0 -> 0

Result: 1 0 0 0 (8)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **L, R**: 64-bit integers.
- **m**: Integer up to 1,000,000.
- **-1**: If `[L, R]` has no valid numbers (e.g. `L=3, R=3, m=3`), return -1.

Common interpretation mistake:

- ❌ Using `(L & R)` or standard range AND shortcut immediately.
- ✅ realizing that skipping numbers *might* keep some bits as 1 that would otherwise become 0 (e.g., if we skip all even numbers).

### Core Concept: Convergence of AND

The bitwise AND of a continuous range `[L, R]` is determined by the common high-order bits of `L` and `R`. The lower bits become 0 quickly because the range usually includes numbers with 0 and 1 at those positions.
Skipping multiples of `m` preserves this property unless `m` is related to bit positions (e.g., `m=2` removes all even numbers, forcing bit 0 to stay 1).

### Why Naive Approach is too slow

Looping `L` to `R` takes O(R-L). Since `R-L` can be `10^12`, this TLEs.
However, `m` is small. The pattern of multiples repeats every `m`. The bitwise AND converges very fast.

## Naive Approach (Linear Scan)

### Intuition

Loop through all valid numbers and AND them.

### Algorithm

1. `ans = -1` (All 1s).
2. `found = false`
3. loop `i` from `L` to `R`:
   - if `i % m != 0`:
     - `ans &= i`
     - `found = true`
4. Return `found ? ans : -1`

### Time Complexity

- **O(R - L)**. Good if range is small, unused if large.

### Space Complexity

- **O(1)**.

## Optimal Approach (Hybrid)

### Key Insight

1. **Small Range**: If `R - L` is small (e.g., `< 2*10^6`), use the naive scan. It's fast enough.
2. **Large Range**: If `R - L` is huge, the range contains many full cycles of `m`.
   - The result is simply the **Standard Range AND** of `[L, R]`, with one exception.
   - **Exception**: If `m=2`, we remove all even numbers. Valid numbers are all Odd. Bit 0 will be 1.
   - For all `m > 2`, we retain enough variation in parity and bit positions that the result matches the Standard Range AND (Common Prefix followed by 0s).

### Algorithm

1. **Constraint Check**: `limit = 5 * m` (or fixed `2*10^6`).
2. If `R - L <= limit`:
   - Run Naive Loop.
3. Else:
   - Calculate Standard Range AND:
     - Find MSB where `L` and `R` differ.
     - Mask out all bits below that MSB.
     - `RangeAND = L & Mask`.
   - If `m == 2`: `RangeAND |= 1`.
   - Return `RangeAND`.

Note: The threshold `limit` ensures we don't miss edge cases where specific bit patterns align with multiples. Since AND reduces bits, once the range is large, the "Standard AND" zeros dominate.

### Time Complexity

- **O(min(R-L, m))**. Worst case O(m).

### Space Complexity

- **O(1)**.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long bitwiseAndSkipMultiples(long L, long R, int m) {
        // If range is manageable, iterate.
        // Threshold: 3 million ops is trivial (~10ms)
        if (R - L <= 3000000) {
            long ans = -1;
            boolean found = false;
            for (long i = L; i <= R; i++) {
                if (i % m != 0) {
                    ans &= i;
                    found = true;
                }
            }
            return found ? ans : -1;
        }

        // Large Range Logic
        // 1. Compute Standard Range AND
        // Logic: Keep common prefix of L and R, rest 0.
        // Efficient way: while L < R, R &= (R-1) ? No, standard algo:
        /*
           shift = 0
           while (L != R) { L >>=1; R >>=1; shift++; }
           res = L << shift
        */
        // Or cleaner: bits where L and R match prefix.
        
        // However, R - L is HUGE. So L and R differ at a high bit.
        // We can just find the highest diff bit.
        // Or simply:
        
        long diff = L ^ R;
        // Highest Set Bit of diff
        if (diff == 0) return (L % m != 0) ? L : -1; 
        
        // Mask out everything below the MSB of diff
        // msb(x) can be found by Long.highestOneBit(diff)
        // If diff has bit K set, then bits 0..K must become 0.
        // Mask = ~((highestOneBit(diff) << 1) - 1) ?
        // Simpler loop:
        
        long lTemp = L;
        long rTemp = R;
        int shift = 0;
        while (lTemp != rTemp) {
            lTemp >>= 1;
            rTemp >>= 1;
            shift++;
        }
        long standardAnd = lTemp << shift;
        
        // Special Case: m=2 means we skipped all evens. 
        // Odd & Odd ... always has bit 0 set.
        if (m == 2) {
            standardAnd |= 1;
        }
        
        return standardAnd;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long L = sc.nextLong();
        long R = sc.nextLong();
        int m = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.bitwiseAndSkipMultiples(L, R, m);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
import sys

def bitwise_and_skip_multiples(L: int, R: int, m: int) -> int:
    # Small range optimization
    if R - L <= 2000000:
        ans = -1
        found = False
        for i in range(L, R + 1):
            if i % m != 0:
                ans &= i
                found = True
        return ans if found else -1

    # Large range: Use Common Prefix logic
    shift = 0
    l_temp = L
    r_temp = R
    
    while l_temp != r_temp:
        l_temp >>= 1
        r_temp >>= 1
        shift += 1
        
    standard_and = l_temp << shift
    
    # Correction for m=2 (skipping evens)
    if m == 2:
        standard_and |= 1
        
    return standard_and

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    L = int(data[0])
    R = int(data[1])
    m = int(data[2])
    
    result = bitwise_and_skip_multiples(L, R, m)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    long long bitwiseAndSkipMultiples(long long L, long long R, int m) {
        // Threshold: 2e6 is safe given 2s time limit (usually ~10^8 ops allowed)
        if (R - L <= 2000000) {
            long long ans = -1;
            bool found = false;
            for (long long i = L; i <= R; i++) {
                if (i % m != 0) {
                    ans &= i;
                    found = true;
                }
            }
            return found ? ans : -1;
        }
        
        long long lTemp = L;
        long long rTemp = R;
        int shift = 0;
        while (lTemp != rTemp) {
            lTemp >>= 1;
            rTemp >>= 1;
            shift++;
        }
        
        long long standardAnd = lTemp << shift;
        
        if (m == 2) {
            standardAnd |= 1;
        }
        
        return standardAnd;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    int m;
    if (!(cin >> L >> R >> m)) return 0;

    Solution solution;
    cout << solution.bitwiseAndSkipMultiples(L, R, m) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bitwiseAndSkipMultiples(L, R, m) {
    // BigInt operations required
    const diff = R - L;
    
    if (diff <= 2000000n) {
      let ans = -1n;
      let found = false;
      for (let i = L; i <= R; i++) {
        if (i % m !== 0n) {
          if (!found) ans = i;
          else ans &= i;
          found = true;
        }
      }
      return found ? ans : -1n;
    }
    
    let lTemp = L;
    let rTemp = R;
    let shift = 0n;
    
    while (lTemp !== rTemp) {
      lTemp >>= 1n;
      rTemp >>= 1n;
      shift++;
    }
    
    let standardAnd = lTemp << shift;
    
    if (m === 2n) {
      standardAnd |= 1n;
    }
    
    return standardAnd;
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
    const m = BigInt(tokens[2]);
    
    const solution = new Solution();
    console.log(solution.bitwiseAndSkipMultiples(L, R, m).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `L=10, R=15, m=3`.
Range Small (`5 <= 2e6`). Run Loop.
- 10: `1010` (Valid). Ans=1010.
- 11: `1011` (Valid). Ans = 1010 & 1011 = `1010`.
- 12: Skip.
- 13: `1101` (Valid). Ans = 1010 & 1101 = `1000`.
- 14: `1110` (Valid). Ans = 1000 & 1110 = `1000`.
- 15: Skip.
Result: 8. Matches Example.

**Large Case**: `L=16 (10000), R=31 (11111), m=2`.
Loop huge? No, here small.
Common Prefix of 16, 31: `0` (diff at bit 4). Shifted 5 times -> 0.
`m=2` -> Result `0 | 1 = 1`.
Is `1` correct?
Valid: 17, 19, 21, ..., 31.
All have bit 0 set.
AND(17, ..., 31) -> 17 is `10001`, 31 `11111`.
Prefix diffs at 16 vs 31?
17: `10001`. 19: `10011`.
Lowest bit 1 is common.
Other bits will flip.
So 1 is correct.

## ✅ Proof of Correctness

### Invariant

For range `[L, R]`, bits below the common prefix cycle through `0` and `1`. Deleting sparse numbers (multiples of `m > 2`) cannot prevent us from seeing at least one `0` in every bit position below the prefix, provided the range is large enough (`> m`).
Case `m=2` is the only dense deletion pattern that systematically removes `0`s from bit 0.

## 💡 Interview Extensions (High-Value Add-ons)

- **Range OR**: Logic is symmetric (find common prefix, rest 1s).
- **Count Set Bits**: Population count in usage.

## Common Mistakes to Avoid

1. **Off-by-one**:
   - ❌ `i < R` loop.
   - ✅ `i <= R`.
2. **Infinite Loop**:
   - ❌ `while (l != r)` with regular Ints could overflow if not careful (but right shift converges).

