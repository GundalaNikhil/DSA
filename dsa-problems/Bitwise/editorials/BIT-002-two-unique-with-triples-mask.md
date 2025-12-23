---
problem_id: BIT_TWO_UNIQUE_TRIPLES__8402
display_id: BIT-002
slug: two-unique-with-triples-mask
title: "Two Unique With Triple Others Under Mask"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - bit-manipulation
  - array
  - medium
premium: true
subscription_tier: basic
---

# BIT-002: Two Unique With Triple Others Under Mask

## 📋 Problem Summary

You have an array where two distinct numbers appear exactly once, and all other numbers appear exactly three times. You are given a mask `M` and guaranteed that the two unique numbers differ in at least one bit present in `M`. Find the two numbers.

## 🌍 Real-World Scenario

**Scenario Title:** The Radio Frequency Isolation

You are monitoring a frequency band where devices broadcast signals.

- **Protocol**: Most devices broadcast a standard "Keep-Alive" sequence exactly 3 times for redundancy (Triple Modular Redundancy).
- **Anomalies**: Two rogue devices broadcast only once.
- **Interference**: If you just listen to everything, signals overlap. Simple XORing doesn't work because triple signals don't cancel out cleanly (`A^A^A = A`).
- **Filter**: You know the rogue devices operate on different sub-channels. The mask `M` represents the channel bits. You can tune your filter to a specific channel bit to separate the rogues and identify them individually.

**Why This Problem Matters:**

- **Generalizing XOR**: Standard "Single Number" problems rely on 2-redundancy (cancellation). Dealing with 3-redundancy requires counting modulo 3.
- **Divide and Conquer**: Using a bitmask to split a hard problem into two easier sub-problems.
- **Digital Logic**: Fundamental to error correction codes.

![Real-World Application](../images/BIT-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Bit Counting Partition

```
Example Array: [5, 5, 5, 9, 9, 9, 3, 6]
Unique numbers: 3 (011₂) and 6 (110₂)
Repeating numbers: 5 (101₂) appears 3x, 9 (1001₂) appears 3x

Counting Bits Modulo 3:

Bit 0 (rightmost):
  Count: 5(1)×3 + 9(1)×3 + 3(1) + 6(0) = 3 + 3 + 1 + 0 = 7
  7 % 3 = 1 → Distinguishing bit (unique numbers differ here)

Bit 1:
  Count: 5(0)×3 + 9(0)×3 + 3(1) + 6(1) = 0 + 0 + 1 + 1 = 2
  2 % 3 = 2 → Both unique numbers have this bit set

Bit 2:
  Count: 5(1)×3 + 9(0)×3 + 3(0) + 6(1) = 3 + 0 + 0 + 1 = 4
  4 % 3 = 1 → Distinguishing bit (unique numbers differ here)

Strategy:
1. Find a distinguishing bit (count % 3 == 1)
2. Split array into two groups based on that bit
3. Each group has ONE unique number and triples
4. Apply "Single Number II" to each group
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Array `a`, Mask `M`.
- **Ordering**: Return `[min, max]`.
- **Constraint**: `M` is valid (separating bit exists).

Common interpretation mistake:

- ❌ Trying to use `XOR` sum of array. `A^A^A = A`. XOR sum becomes `U1 ^ U2 ^ (X1^X2^...)`. The repeats don't vanish.
- ✅ We must use bit counting modulo 3.

### Core Concept: Modulo 3 Counting

For any bit position `i`:
Total count of set bits `C_i`.
Since repeating numbers contribute `3` or `0` to the count:
`C_i % 3 = (u1_i + u2_i) % 3`.

Possible outcomes for `rem = C_i % 3`:

- `rem == 0`: `u1` and `u2` both 0.
- `rem == 2`: `u1` and `u2` both 1.
- `rem == 1`: One is 0, One is 1. (They differ!).

So, if `(C_i % 3) == 1`, bit `i` is a **distinguishing bit**. u1 and u2 have different values here.

### Why M is given

Strictly speaking, we could find a distinguishing bit just by checking all 32 bits. The problem gives `M` to guarantee/simplify the choice or simulate a "filter" constraint. We just need to pick `bit = M & DiffMask`.

## Naive Approach (HashMap)

### Intuition

Count all frequencies. Return keys with count 1.

### Algorithm

1. `counts = {}`.
2. Iterate `a`, update `counts`.
3. Filter `counts` for value 1.
4. Sort and return.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**.

## Optimal Approach (Partition + Bitwise Mod 3)

### Key Insight

1. Determine a distinguishing bit `k`. We iterate 0..31, sum bits mod 3. If result is 1, and `(1<<i) & M` is true, choose `k = i`.
2. Partition array into `Group0` (k-th bit 0) and `Group1` (k-th bit 1).
3. In `Group0`, `u1` is the only unique. `u2` went to Group1. All repeats went together to one group or the other (since repeats are identical).
4. Solve "Find single unique where others appear 3 times" for both groups.
   - For a group: Answer bit `j` = `(Sum of j-th bits in group) % 3`.

### Algorithm

1. **Find Split Bit**:
   - `splitBit = -1`.
   - Loop `i` from 0 to 30:
     - `cnt = 0`.
     - For `x` in `a`: `if (x >> i) & 1: cnt++`.
     - If `cnt % 3 == 1` AND `(M >> i) & 1`:
       - `splitBit = i`. Break.
2. **Solve Subproblems**:
   - `ans1 = 0`, `ans2 = 0`.
   - For each bit position `b` from 0 to 30:
     - `c1 = 0, c2 = 0` (counters for each group).
     - For each `x` in array:
       - `bitVal = (x >> b) & 1` (check if bit b is set).
       - `group = (x >> splitBit) & 1` (determine which group x belongs to).
       - If `group == 0`: `c1 += bitVal`.
       - Else: `c2 += bitVal`.
     - If `c1 % 3 == 1`: Set bit `b` in `ans1` → `ans1 |= (1 << b)`.
     - If `c2 % 3 == 1`: Set bit `b` in `ans2` → `ans2 |= (1 << b)`.
3. Return sorted `[ans1, ans2]`.

### Time Complexity

- **O(32 \* N)** which is **O(N)**. We iterate bits (outer) and array (inner) or vice versa.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-002/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-002/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] twoUniqueWithTriplesMask(int[] a, int M) {
        // Step 1: Find a differentiating bit that is also in M
        int splitBit = -1;
        for (int i = 0; i < 31; i++) {
            // Only examine bits allowed by M
            if (((M >> i) & 1) == 0) continue;

            int count = 0;
            for (int x : a) {
                if (((x >> i) & 1) == 1) {
                    count++;
                }
            }
            // If count % 3 == 1, then the two uniques differ at this bit.
            if (count % 3 == 1) {
                splitBit = i;
                break;
            }
        }

        // Step 2: Reconstruct the two numbers separately
        int num1 = 0;
        int num2 = 0;

        // We can do this bit by bit for each number
        for (int i = 0; i < 31; i++) {
            int c1 = 0;
            int c2 = 0;
            for (int x : a) {
                int bitVal = (x >> i) & 1;
                // Check which group x belongs to based on splitBit
                if (((x >> splitBit) & 1) == 0) {
                    c1 += bitVal;
                } else {
                    c2 += bitVal;
                }
            }

            if (c1 % 3 != 0) num1 |= (1 << i);
            if (c2 % 3 != 0) num2 |= (1 << i);
        }

        int[] result = new int[]{num1, num2};
        Arrays.sort(result);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int M = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.twoUniqueWithTriplesMask(a, M);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
```

### Python

```python
import sys

def two_unique_with_triples_mask(a: list[int], M: int) -> list[int]:
    # 1. Find splitting bit index
    split_bit = -1
    for i in range(31):
        if not ((M >> i) & 1):
            continue

        count = 0
        for x in a:
            if (x >> i) & 1:
                count += 1

        if count % 3 == 1:
            split_bit = i
            break

    # 2. Reconstruct
    num1, num2 = 0, 0
    for i in range(31):
        c1, c2 = 0, 0
        for x in a:
            bit_val = (x >> i) & 1
            if (x >> split_bit) & 1:
                c2 += bit_val
            else:
                c1 += bit_val

        if c1 % 3: num1 |= (1 << i)
        if c2 % 3: num2 |= (1 << i)

    return sorted([num1, num2])

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return

    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    M = int(data[ptr]); ptr += 1

    result = two_unique_with_triples_mask(a, M)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> twoUniqueWithTriplesMask(vector<int>& a, int M) {
        int splitBit = -1;

        for (int i = 0; i < 31; i++) {
            if (!((M >> i) & 1)) continue;

            int count = 0;
            for (int x : a) {
                if ((x >> i) & 1) count++;
            }

            if (count % 3 == 1) {
                splitBit = i;
                break;
            }
        }

        int num1 = 0, num2 = 0;

        for (int i = 0; i < 31; i++) {
            int c1 = 0, c2 = 0;
            for (int x : a) {
                int bitVal = (x >> i) & 1;
                if ((x >> splitBit) & 1) {
                    c2 += bitVal;
                } else {
                    c1 += bitVal;
                }
            }
            if (c1 % 3 != 0) num1 |= (1 << i);
            if (c2 % 3 != 0) num2 |= (1 << i);
        }

        vector<int> res = {num1, num2};
        sort(res.begin(), res.end());
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int M;
    cin >> M;

    Solution solution;
    vector<int> result = solution.twoUniqueWithTriplesMask(a, M);
    cout << result[0] << " " << result[1] << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  twoUniqueWithTriplesMask(a, M) {
    let splitBit = -1;

    // Step 1: Find valid split bit within Mask
    for (let i = 0; i < 31; i++) {
      if (((M >> i) & 1) === 0) continue;

      let count = 0;
      for (const x of a) {
        if ((x >> i) & 1) count++;
      }

      if (count % 3 === 1) {
        splitBit = i;
        break;
      }
    }

    let num1 = 0;
    let num2 = 0;

    // Step 2: Reconstruct using standard Single Number II logic per group
    for (let i = 0; i < 31; i++) {
      let c1 = 0;
      let c2 = 0;
      for (const x of a) {
        const bitVal = (x >> i) & 1;
        const group = (x >> splitBit) & 1;
        if (group === 1) {
          c2 += bitVal;
        } else {
          c1 += bitVal;
        }
      }
      if (c1 % 3 !== 0) num1 |= 1 << i;
      if (c2 % 3 !== 0) num2 |= 1 << i;
    }

    const result = [num1, num2];
    result.sort((x, y) => x - y);
    return result;
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
  const M = Number(tokens[ptr++]);

  const solution = new Solution();
  const result = solution.twoUniqueWithTriplesMask(a, M);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `[5, 5, 5, 9, 9, 9, 3, 6]`, `M=1`

**Binary representations**:

- `3 = 0011`
- `5 = 0101`
- `6 = 0110`
- `9 = 1001`

**Unique numbers**: `3` and `6`

### Step 1: Find Distinguishing Bit

For **Bit 0** (value 1):

- Count set bits: `3(1) + 6(0) + 5×3(1,1,1) + 9×3(1,1,1)` → Total = `1 + 0 + 3 + 3 = 7`
- `7 % 3 = 1` ✓ (Distinguishing bit found!)
- `M & 1 = 1` ✓ (Bit is in mask)
- **Split bit = 0**

**Analysis**: Bit 0 separates our unique numbers:

- `3` has bit 0 set (odd)
- `6` has bit 0 unset (even)

### Step 2: Partition and Reconstruct

**Group 0** (bit 0 = 0): `[6, ...trailing 9s and 5s with bit 0 = 0]`
**Group 1** (bit 0 = 1): `[3, 5, 5, 5, 9, 9, 9]`

For each bit position, count occurrences in each group:

**Reconstructing Group 0's unique**:

- Bit 1: Count = 1 (from 6), `1 % 3 = 1` → Set
- Bit 2: Count = 1 (from 6), `1 % 3 = 1` → Set
- Result: `0110₂ = 6` ✓

**Reconstructing Group 1's unique**:

- Bit 0: Count = 7 (all odds), `7 % 3 = 1` → Set
- Bit 1: Count = 4 (3 + 3×5s), `4 % 3 = 1` → Set
- Bit 2: Count = 0, `0 % 3 = 0` → Unset
- Result: `0011₂ = 3` ✓

**Output**: `[3, 6]`

## ✅ Proof of Correctness

### Invariant

With `count % 3`, repeating elements contribute 0 to the remainder. The remainder is purely `(u1_bit + u2_bit) % 3`.

- `1` implies `1+0` (Diff).
- `2` implies `1+1` (Same).
- `0` implies `0+0` (Same).
  Thus we correctly identify separating bits. Partitioning ensures we separate `u1` and `u2`, reducing to the solved problem of "1 unique in triples".

## 💡 Interview Extensions (High-Value Add-ons)

- **General K**: What if elements appear K times? (Use count % K).
- **No Mask**: If Mask not given, just use `count % 3 == 1` to find ANY diff bit.

## Common Mistakes to Avoid

1. **Incorrect Modulo**:
   - ❌ `count % 2`.
   - ✅ `count % 3` is required for triples.
2. **Mask Validation**:
   - ❌ Assuming `M` is always perfect.
   - ✅ Algorithm robustness depends on finding _one_ valid bit.
