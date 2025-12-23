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
---

# BIT-001: Odd After Bit Salt

## 📋 Problem Summary

You are given an array of numbers and a `salt` value. Every number `x` in the array is transformed into `x ^ salt`. In this new transformed list, exactly one number appears an odd number of times. Find that number.

## 🌍 Real-World Scenario

**Scenario Title:** The Secure Token Replay

You are investigating a log of authentication tokens.
- **Protocol**: Every time a user initiates a session, a "Start" token is logged. When they finish, an identical "End" token is logged.
- **Encryption**: To secure the logs, every token value is XORed with a daily secret key (`salt`) before writing to disk.
- **Anomaly**: One session crashed and never logged its "End" token.
- **Goal**: Find the ID of the crashed session. You have the list of all encrypted logs. Since every completed session has two entries (Even count), and the crashed one has only one (Odd count), you can find it by processing the stream.

**Why This Problem Matters:**

- **XOR Cancellation**: The property `A ^ A = 0` is the cornerstone of many efficient algorithms (like RAID parity).
- **Stream Processing**: Solving problems in O(1) space without storing frequency maps.
- **Data Transformation**: Handling data that has been masked or salted without needing to unmask everything first.

![Real-World Application](../images/BIT-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: XOR Cancellation
```
Input: [4, 1, 2, 1, 2]
Salt: 3

Transformed Values:
4 ^ 3 = 7
1 ^ 3 = 2
2 ^ 3 = 1
1 ^ 3 = 2
2 ^ 3 = 1

Transformed Array: [7, 2, 1, 2, 1]
Pairs: (2, 2) cancels out. (1, 1) cancels out.
Remaining: 7.
Result: 7.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Integer array `a` and integer `salt`.
- **Output**: The single value that appears odd times *after* XORing with salt.
- **Constraint**: `N` will always be odd (implied, since sum of even counts + 1 odd count = odd).

Common interpretation mistake:

- ❌ Finding the original value that appears odd times (result 4) instead of the transformed value (result 7).
- ✅ The question asks for the value *in the transformed multiset*.

### Core Concept: XOR Properties

XOR (exclusive OR) has two useful properties:
1.  **Inverse**: `x ^ x = 0`. Any value appearing an even number of times will XOR with itself to become 0.
2.  **Identity**: `x ^ 0 = x`.
3.  **Associative/Commutative**: Order doesn't matter.

If we XOR all elements in the transformed array, the result will be the single element that appears an odd number of times.

### Why Naive Approach is too slow

Using a HashMap to count frequencies takes O(N) time but also **O(N) space**. In embedded systems or very large streams, O(N) space might be too expensive. We want O(1) space.

## Naive Approach (Frequency Map)

### Intuition

Generate all `x ^ salt` values, count their frequencies, and return the one with odd count.

### Algorithm

1. `counts = {}`
2. For `x` in `a`:
   - `val = x ^ salt`
   - `counts[val]++`
3. For `val, count` in `counts`:
   - If `count % 2 != 0`: return `val`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**.

## Optimal Approach (XOR Aggregation)

### Key Insight

Instead of storing counts, just maintain a running XOR sum.
`RunningSum = (a[0]^salt) ^ (a[1]^salt) ^ ...`
Since pairs cancel out, `RunningSum` will equal the unique odd-occurrence value.

### Algorithm

1. `ans = 0`
2. For multiple `x` in `a`:
   - `ans ^= (x ^ salt)`
3. Return `ans`.

Alternatively, due to associativity:
`ans = (a[0] ^ a[1] ^ ...) ^ (salt ^ salt ^ ...)`
If N is odd, `salt` XORed `N` times is just `salt`.
So `ans = (XOR sum of original array) ^ salt`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(1)**.

### Why This Is Optimal

We inspect every element once and use no extra memory.

![Algorithm Visualization](../images/BIT-001/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-001/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long oddAfterBitSalt(int[] a, int salt) {
        long result = 0;
        // In Java, XOR works fine on ints.
        // We accumulate the XOR of (a[i] ^ salt)
        for (int x : a) {
            result ^= (x ^ salt);
        }
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
    result = 0
    for x in a:
        result ^= (x ^ salt)
    return result

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
        long long result = 0;
        for (int x : a) {
            result ^= (x ^ salt);
        }
        return result;
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
    let result = 0;
    for (const x of a) {
      result ^= (x ^ salt);
    }
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
    
    const salt = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(String(solution.oddAfterBitSalt(a, salt)));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `a = [4, 1, 2, 1, 2]`, `salt = 3`.
**Target Answer**: The number appearing once is `4`. Transformed answer should be `4 ^ 3 = 7`.

1. `result = 0`
2. `x = 4`: `result ^= (4 ^ 3) = 0 ^ 7 = 7`.
3. `x = 1`: `result ^= (1 ^ 3) = 7 ^ 2 = 5`.
4. `x = 2`: `result ^= (2 ^ 3) = 5 ^ 1 = 4`.
5. `x = 1`: `result ^= (1 ^ 3) = 4 ^ 2 = 6`.
6. `x = 2`: `result ^= (2 ^ 3) = 6 ^ 1 = 7`.

**Final Result**: 7.
Matches expectation.

![Example Visualization](../images/BIT-001/example-1.png)

## ✅ Proof of Correctness

### Invariant

`result` always stores the XOR sum of all transformed elements processed so far.
At end, `result = T_1 ^ T_2 ... ^ T_n`.
Since XOR is commutative, we can group equal values.
`result = (A^A) ^ (B^B) ^ ... ^ Unique`.
`result = 0 ^ 0 ^ ... ^ Unique = Unique`.

### Why the approach is correct

The algorithm directly implements the mathematical property of XOR cancellation.

## 💡 Interview Extensions (High-Value Add-ons)

- **Two Missing Numbers**: What if *two* numbers appear once? (A: Use XOR sum + rightmost set bit to partition).
- **Three Missing**: General System of Equations.

## Common Mistakes to Avoid

1. **Forgetting Transformation**:
   - ❌ XORing only the original array `a` and returning that.
   - ✅ Check requirement: return transformed value.

2. **Overflow**:
   - ❌ Not an issue for XOR, but generally good to be aware of data types.

## Related Concepts

- **Single Number (LeetCode 136)**: Classic variation.
- **Nim Game**: XOR sum governs winning strategy.
