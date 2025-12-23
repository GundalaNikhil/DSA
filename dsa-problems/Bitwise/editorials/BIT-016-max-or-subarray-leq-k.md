---
problem_id: BIT_MAX_OR_SUBARRAY_LEQ_K__8416
display_id: BIT-016
slug: max-or-subarray-leq-k
title: Max Bitwise OR Subarray <= K
difficulty: Medium
difficulty_score: 50
topics:
- Bitwise Operations
- Sliding Window
- Two Pointers
tags:
- bitwise
- sliding-window
- medium
premium: true
subscription_tier: basic
---

# BIT-016: Max OR Subarray Leq K

## Problem Summary

Find the maximum length of a contiguous subarray whose bitwise OR value is less than or equal to `K`.

## Real-World Scenario: Feature Combination Constraints

In software configuration management, features are represented as bitmasks. When selecting a subset of features to enable, the combined feature set (via OR operation) must not exceed a resource budget K. Finding the maximum number of consecutive features that can be enabled helps optimize system configuration.

---

## Problem Analysis

### Understanding the Problem

Given an array of `n` integers and a threshold `K`, find the maximum length of a contiguous subarray whose bitwise OR is at most `K`.

**Key Observations:**

1. OR is monotonically increasing: adding elements never decreases OR
2. Once OR exceeds K, we must shrink the window
3. Sliding window technique is applicable
4. Need to efficiently compute OR of current window

### Visual Example

```
Array: [1, 2, 4, 1], K = 7

Binary Representation:
━━━━━━━━━━━━━━━━━━━━━━━
Index | Value | Binary
━━━━━━━━━━━━━━━━━━━━━━━
  0   |   1   |  001
  1   |   2   |  010
  2   |   4   |  100
  3   |   1   |  001
━━━━━━━━━━━━━━━━━━━━━━━

Window Expansion:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Window      | OR Calculation  | OR Value | ≤K?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1]         | 001             |    1     |  ✓
[1,2]       | 001|010 = 011   |    3     |  ✓
[1,2,4]     | 011|100 = 111   |    7     |  ✓
[1,2,4,1]   | 111|001 = 111   |    7     |  ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Maximum length: 4 (entire array)
```

### OR Properties

```
Bitwise OR Properties:
═══════════════════════════════════════════
1. Monotonic: a | b | c ≥ a | b
2. Idempotent: a | a = a
3. Commutative: a | b = b | a
4. Associative: (a | b) | c = a | (b | c)

Key: OR can only SET bits, never CLEAR them
```

---

## Approach 1: Brute Force - Check All Subarrays

### Algorithm

1. For each starting position L
2. Expand window to the right, computing OR
3. Stop when OR > K
4. Track maximum valid length

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int maxORSubarray(int[] a, int K) {
        int n = a.length;
        int maxLen = 0;

        for (int L = 0; L < n; L++) {
            int orValue = 0;
            for (int R = L; R < n; R++) {
                orValue |= a[R];

                if (orValue <= K) {
                    maxLen = Math.max(maxLen, R - L + 1);
                } else {
                    break; // OR will only increase, no point continuing
                }
            }
        }

        return maxLen;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int K = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.maxORSubarray(a, K));
        sc.close();
    }
}
```

**Python:**

```python
def max_or_subarray_brute(a, K):
    n = len(a)
    max_len = 0

    for L in range(n):
        or_value = 0
        for R in range(L, n):
            or_value |= a[R]

            if or_value <= K:
                max_len = max(max_len, R - L + 1)
            else:
                break  # OR will only increase

    return max_len

# Main
n, K = map(int, input().split())
a = list(map(int, input().split()))
print(max_or_subarray_brute(a, K))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int maxORSubarray(vector<int>& a, int K) {
    int n = a.size();
    int maxLen = 0;

    for (int L = 0; L < n; L++) {
        int orValue = 0;
        for (int R = L; R < n; R++) {
            orValue |= a[R];

            if (orValue <= K) {
                maxLen = max(maxLen, R - L + 1);
            } else {
                break; // OR will only increase
            }
        }
    }

    return maxLen;
}

int main() {
    int n, K;
    cin >> n >> K;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << maxORSubarray(a, K) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function maxORSubarray(a, K) {
  const n = a.length;
  let maxLen = 0;

  for (let L = 0; L < n; L++) {
    let orValue = 0;
    for (let R = L; R < n; R++) {
      orValue |= a[R];

      if (orValue <= K) {
        maxLen = Math.max(maxLen, R - L + 1);
      } else {
        break; // OR will only increase
      }
    }
  }

  return maxLen;
}

// Main
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, K] = lines[0].split(" ").map(Number);
  const a = lines[1].split(" ").map(Number);
  console.log(maxORSubarray(a, K));
});
```

### Detailed Trace

```
Array: [1, 2, 4, 1], K = 7

L=0:
  R=0: OR = 1, valid, len=1
  R=1: OR = 1|2 = 3, valid, len=2
  R=2: OR = 3|4 = 7, valid, len=3
  R=3: OR = 7|1 = 7, valid, len=4 ← max updated!

L=1:
  R=1: OR = 2, valid, len=1
  R=2: OR = 2|4 = 6, valid, len=2
  R=3: OR = 6|1 = 7, valid, len=3

L=2:
  R=2: OR = 4, valid, len=1
  R=3: OR = 4|1 = 5, valid, len=2

L=3:
  R=3: OR = 1, valid, len=1

Answer: 4
```

### Complexity Analysis

- **Time Complexity:** O(n²)
  - Outer loop: O(n)
  - Inner loop: O(n) per start position
  - Early break optimization reduces practical runtime
- **Space Complexity:** O(1)
  - Only using constant extra space

---

## Approach 2: Sliding Window with Bit Count Array (Optimal)

### Core Insight

**Efficient Window OR Computation:**

- Maintain count of each bit position across window
- If `bitCount[i] > 0`, bit i is set in OR
- When shrinking window, decrement bit counts
- Recompute OR from bit counts

### Algorithm

```
Sliding Window with Bit Tracking:
═══════════════════════════════════════════
bitCount[30] = count of elements with bit i set

Expand window:
  - Add a[R] to window
  - Update bitCount for each bit in a[R]
  - Compute current OR from bitCount

Shrink window (if OR > K):
  - Remove a[L] from window
  - Update bitCount for each bit in a[L]
  - Recompute OR
  - Increment L
```

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int maxORSubarray(int[] a, int K) {
        int n = a.length;
        int maxLen = 0;
        int[] bitCount = new int[30]; // For up to 10^9
        int L = 0;

        for (int R = 0; R < n; R++) {
            // Add a[R] to window
            addToBitCount(bitCount, a[R]);

            // Shrink window while OR > K
            while (L <= R && computeOR(bitCount) > K) {
                removeFromBitCount(bitCount, a[L]);
                L++;
            }

            // Update maximum length
            maxLen = Math.max(maxLen, R - L + 1);
        }

        return maxLen;
    }

    private void addToBitCount(int[] bitCount, int num) {
        for (int i = 0; i < 30; i++) {
            if ((num & (1 << i)) != 0) {
                bitCount[i]++;
            }
        }
    }

    private void removeFromBitCount(int[] bitCount, int num) {
        for (int i = 0; i < 30; i++) {
            if ((num & (1 << i)) != 0) {
                bitCount[i]--;
            }
        }
    }

    private int computeOR(int[] bitCount) {
        int or = 0;
        for (int i = 0; i < 30; i++) {
            if (bitCount[i] > 0) {
                or |= (1 << i);
            }
        }
        return or;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int K = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.maxORSubarray(a, K));
        sc.close();
    }
}
```

**Python:**

```python
def max_or_subarray_sliding(a, K):
    n = len(a)
    max_len = 0
    bit_count = [0] * 30
    L = 0

    def add_to_bit_count(num):
        for i in range(30):
            if num & (1 << i):
                bit_count[i] += 1

    def remove_from_bit_count(num):
        for i in range(30):
            if num & (1 << i):
                bit_count[i] -= 1

    def compute_or():
        result = 0
        for i in range(30):
            if bit_count[i] > 0:
                result |= (1 << i)
        return result

    for R in range(n):
        # Add a[R] to window
        add_to_bit_count(a[R])

        # Shrink window while OR > K
        while L <= R and compute_or() > K:
            remove_from_bit_count(a[L])
            L += 1

        # Update maximum length
        max_len = max(max_len, R - L + 1)

    return max_len

# Main
n, K = map(int, input().split())
a = list(map(int, input().split()))
print(max_or_subarray_sliding(a, K))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    int bitCount[30];

    void addToBitCount(int num) {
        for (int i = 0; i < 30; i++) {
            if (num & (1 << i)) {
                bitCount[i]++;
            }
        }
    }

    void removeFromBitCount(int num) {
        for (int i = 0; i < 30; i++) {
            if (num & (1 << i)) {
                bitCount[i]--;
            }
        }
    }

    int computeOR() {
        int result = 0;
        for (int i = 0; i < 30; i++) {
            if (bitCount[i] > 0) {
                result |= (1 << i);
            }
        }
        return result;
    }

public:
    int maxORSubarray(vector<int>& a, int K) {
        int n = a.size();
        int maxLen = 0;
        memset(bitCount, 0, sizeof(bitCount));
        int L = 0;

        for (int R = 0; R < n; R++) {
            // Add a[R] to window
            addToBitCount(a[R]);

            // Shrink window while OR > K
            while (L <= R && computeOR() > K) {
                removeFromBitCount(a[L]);
                L++;
            }

            // Update maximum length
            maxLen = max(maxLen, R - L + 1);
        }

        return maxLen;
    }
};

int main() {
    int n, K;
    cin >> n >> K;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    Solution sol;
    cout << sol.maxORSubarray(a, K) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function maxORSubarray(a, K) {
  const n = a.length;
  let maxLen = 0;
  const bitCount = new Array(30).fill(0);
  let L = 0;

  function addToBitCount(num) {
    for (let i = 0; i < 30; i++) {
      if (num & (1 << i)) {
        bitCount[i]++;
      }
    }
  }

  function removeFromBitCount(num) {
    for (let i = 0; i < 30; i++) {
      if (num & (1 << i)) {
        bitCount[i]--;
      }
    }
  }

  function computeOR() {
    let result = 0;
    for (let i = 0; i < 30; i++) {
      if (bitCount[i] > 0) {
        result |= 1 << i;
      }
    }
    return result;
  }

  for (let R = 0; R < n; R++) {
    // Add a[R] to window
    addToBitCount(a[R]);

    // Shrink window while OR > K
    while (L <= R && computeOR() > K) {
      removeFromBitCount(a[L]);
      L++;
    }

    // Update maximum length
    maxLen = Math.max(maxLen, R - L + 1);
  }

  return maxLen;
}

// Main
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, K] = lines[0].split(" ").map(Number);
  const a = lines[1].split(" ").map(Number);
  console.log(maxORSubarray(a, K));
});
```

### Detailed Trace

```
Array: [1, 2, 4, 1], K = 7

Initial: L=0, bitCount=[0,0,...,0]

R=0 (add 1=001):
  bitCount[0]=1
  OR = 001 = 1 ≤ 7 ✓
  len = 1

R=1 (add 2=010):
  bitCount[0]=1, bitCount[1]=1
  OR = 011 = 3 ≤ 7 ✓
  len = 2

R=2 (add 4=100):
  bitCount[0]=1, bitCount[1]=1, bitCount[2]=1
  OR = 111 = 7 ≤ 7 ✓
  len = 3

R=3 (add 1=001):
  bitCount[0]=2, bitCount[1]=1, bitCount[2]=1
  OR = 111 = 7 ≤ 7 ✓
  len = 4 ← Maximum!

Answer: 4
```

### Complexity Analysis

- **Time Complexity:** O(n × 30) = O(n)
  - Each element added/removed once
  - Bit operations are O(30) = O(1)
- **Space Complexity:** O(30) = O(1)
  - Bit count array

---

## Edge Cases

### Case 1: K = 0

```
Only subarrays containing only 0s are valid.
Array: [0, 1, 0, 0, 2]
Valid: [0] (len 1), [0] (len 1), [0,0] (len 2)
Answer: 2
```

### Case 2: All Elements > K

```
Array: [10, 20, 30], K = 5
No valid subarrays longer than 0.
Answer: 0
```

### Case 3: Entire Array Valid

```
Array: [1, 2, 3], K = 100
OR = 1|2|3 = 3 ≤ 100
Answer: 3 (entire array)
```

### Case 4: Single Element

```
Array: [5], K = 10
Answer: 1
```

---

### Common Mistakes

### Mistake 1: Forgetting OR is Monotonic

```java
// Wrong: checking smaller windows after OR > K
if (orValue > K) {
    // Still checking smaller R values... unnecessary!
}
```

### Mistake 2: Incorrect Bit Count Update

```python
# Wrong: not handling bit removal correctly
bitCount[i] -= 1
if bitCount[i] < 0:  # This should never happen!
    bitCount[i] = 0
```

### Mistake 3: Not Handling Empty Subarrays

```cpp
// Edge case: all elements > K
// Should return 0, not -1 or error
```

---

## Interview Extensions

### Extension 1: Minimum Length with OR >= K

Find shortest subarray with OR at least K.

**Approach:** Similar sliding window, but shrink while OR >= K.

### Extension 2: Count Subarrays with OR <= K

Count all subarrays satisfying the condition.

**Approach:** For each R, count valid L positions.

### Extension 3: Maximum OR with Length <= L

Find maximum OR among subarrays of length at most L.

---

## Practice Problems

1. **Longest Subarray with Sum <= K** - Similar sliding window
2. **Minimum Window Substring** - Classic sliding window
3. **Subarrays with Bounded Maximum** - Similar monotonic property
4. **Longest Substring with At Most K Distinct Characters** - Window technique
5. **Maximum AND Subarray** - Similar but with AND operation

---

## Summary Table

| Approach       | Time  | Space | Best For               |
| -------------- | ----- | ----- | ---------------------- |
| Brute Force    | O(n²) | O(1)  | Understanding, small n |
| Sliding Window | O(n)  | O(1)  | Optimal, all cases     |

---

## Key Takeaways

1. **OR is monotonic** - key property for optimization
2. **Sliding window** perfect for contiguous subarray problems
3. **Bit count tracking** enables efficient OR computation
4. **Two pointers** maintain valid window efficiently
5. **Early breaking** improves brute force performance

This problem teaches:

- Sliding window technique
- Bitwise OR properties
- Efficient bit manipulation
- Monotonic property exploitation

Essential for technical interviews and competitive programming!
