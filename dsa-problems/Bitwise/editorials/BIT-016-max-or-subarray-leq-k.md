---
problem_id: BIT_MAX_OR_SUBARRAY_LEQ_K__8416
display_id: BIT-016
slug: max-or-subarray-leq-k
title: "Max Bitwise OR Subarray <= K"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - OR
  - Sliding Window
  - Array
tags:
  - bitwise
  - or-operation
  - sliding-window
  - subarray
  - medium
premium: true
subscription_tier: basic
---

# BIT-016: Max Bitwise OR Subarray <= K

## 📋 Problem Summary

Find the length of the longest subarray `nums[i..j]` such that `nums[i] | nums[i+1] | ... | nums[j] <= K`.

## 🌍 Real-World Scenario

**Scenario Title:** The Power Surge Limiter

You are monitoring a network of power cells.
- **Power Output**: Each cell adds specific "noise frequencies" to the grid, represented by bits.
- **Combination**: When cells runs in a sequence (subarray), their noise profiles superimpose (Bitwise OR).
- **Safety Limit**: The combined noise must not exceed a safety threshold `K`.
- **Goal**: Run as many consecutive cells as possible without tripping the safety breaker.

**Why This Problem Matters:**

- **Monotonicity**: Bitwise OR is non-decreasing. Adding elements can only increase bits. Removing elements can only decrease bits. This enables **Sliding Window**.
- **Inverse Operation**: Unlike Sum (where `Sum(L+1...R) = Sum(L..R) - A[L]`), Bitwise OR has no direct inverse. We cannot simply "subtract" bits. We must maintain bit counts.

![Real-World Application](../images/BIT-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Window
```
Array: [1, 2, 4, 1]
K = 7

Window [1]: OR=1. OK. Len=1.
Window [1, 2]: OR=3. OK. Len=2.
Window [1, 2, 4]: OR=7. OK. Len=3.
Window [1, 2, 4, 1]: OR=7. OK. Len=4.

Result: 4.

If K=3:
[1]: OK.
[1, 2]: OK.
[1, 2, 4]: 7 > 3. Shrink Left.
Remove 1. Window [2, 4]. OR=6 > 3. Shrink Left.
Remove 2. Window [4]. OR=4 > 3. Shrink Left.
Remove 4. Window []. OR=0.
Expand 1 (index 3). Window [1]. OR=1 <= 3. OK.
Max Len 2.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Array `a`, Integer `K`.
- **Output**: Length.
- **Constraints**: $10^5$ elements. Values up to $10^9$.

Common interpretation mistake:

- ❌ Recomputing OR from scratch every time (O(N^2) or O(N^3)).
- ✅ Using a frequency array (bit counts) to support "remove" operation in O(30).

### Core Concept: Sliding Window with Bit Counts

Standard Sliding Window pattern: `Expand Right`, `While Invalid: Shrink Left`.
Since `A | B` is not reversible, we track the `count` of set bits at each position for the current window.
- **Add(x)**: Iterate bits of `x`, increment `counts`. Recalculate `currentOR`.
- **Remove(x)**: Iterate bits of `x`, decrement `counts`. Recalculate `currentOR`.
  - If `count[bit] > 0`, that bit remains set in `currentOR`.
  - If `count[bit] == 0`, that bit becomes 0 in `currentOR`.

## Naive Approach (Brute Force)

### Intuition

Check all subarrays.

### Algorithm

1. Loop `i` from 0 to N.
2. Loop `j` from `i` to N.
3. Compute OR. Check condition.

### Time Complexity

- **O(N^2)**.

### Space Complexity

- **O(1)**.

## Optimal Approach (Sliding Window + Bit Counting)

### Key Insight

Maintain an array `bits[32]` tracking how many numbers in the current window have the i-th bit set.
`current_or = Sum(1 << i if bits[i] > 0)`.

### Algorithm

1. `left = 0`, `ans = 0`.
2. `counts = int[32]`. `currOR = 0`.
3. Loop `right` from 0 to N-1:
   - Add `a[right]` to window:
     - Update `counts` and `currOR`.
   - While `currOR > K` and `left <= right`:
     - Remove `a[left]` from window:
       - Update `counts`. If `counts[i]` drops to 0, clear bit in `currOR`.
     - `left++`
   - If `currOR <= K`, `ans = max(ans, right - left + 1)`.
4. Return `ans`.

### Time Complexity

- **O(N * 30)**. Each element added and removed once. 30 ops per update.

### Space Complexity

- **O(1)** (Technically O(30)).

![Algorithm Visualization](../images/BIT-016/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-016/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int maxOrSubarrayLeqK(int[] a, int K) {
        int n = a.length;
        int[] bitCounts = new int[32];
        int currentOr = 0;
        int left = 0;
        int maxLen = 0;
        
        for (int right = 0; right < n; right++) {
            // Add a[right] to window
            int val = a[right];
            for (int i = 0; i < 31; i++) {
                if (((val >> i) & 1) == 1) {
                    bitCounts[i]++;
                    // If count becomes > 0, set the bit in currentOr
                    if (bitCounts[i] == 1) {
                        currentOr |= (1 << i);
                    }
                }
            }
            
            // Shrink
            while (left <= right && currentOr > K) {
                int removeVal = a[left];
                for (int i = 0; i < 31; i++) {
                    if (((removeVal >> i) & 1) == 1) {
                        bitCounts[i]--;
                        // If count drops to 0, unset the bit
                        if (bitCounts[i] == 0) {
                            currentOr &= ~(1 << i);
                        }
                    }
                }
                left++;
            }
            
            // Check valid
            if (currentOr <= K) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }
        
        return maxLen;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int K = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maxOrSubarrayLeqK(a, K));
        sc.close();
    }
}
```

### Python

```python
import sys

def max_or_subarray_leq_k(a: list[int], K: int) -> int:
    n = len(a)
    bit_counts = [0] * 32
    current_or = 0
    left = 0
    max_len = 0
    
    for right in range(n):
        val = a[right]
        # Add to window
        for i in range(31):
            if (val >> i) & 1:
                bit_counts[i] += 1
                if bit_counts[i] == 1:
                    current_or |= (1 << i)
                    
        # Shrink
        while left <= right and current_or > K:
            remove_val = a[left]
            for i in range(31):
                if (remove_val >> i) & 1:
                    bit_counts[i] -= 1
                    if bit_counts[i] == 0:
                        current_or &= ~(1 << i)
            left += 1
            
        if current_or <= K:
            max_len = max(max_len, right - left + 1)
            
    return max_len

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    K = int(data[ptr]); ptr += 1
    
    result = max_or_subarray_leq_k(a, K)
    print(result)

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
    int maxOrSubarrayLeqK(vector<int>& a, int K) {
        int n = a.size();
        vector<int> bitCounts(32, 0);
        int currentOr = 0;
        int left = 0;
        int maxLen = 0;
        
        for (int right = 0; right < n; right++) {
            int val = a[right];
            for (int i = 0; i < 31; i++) {
                if ((val >> i) & 1) {
                    bitCounts[i]++;
                    if (bitCounts[i] == 1) {
                        currentOr |= (1 << i);
                    }
                }
            }
            
            while (left <= right && currentOr > K) {
                int removeVal = a[left];
                for (int i = 0; i < 31; i++) {
                    if ((removeVal >> i) & 1) {
                        bitCounts[i]--;
                        if (bitCounts[i] == 0) {
                            currentOr &= ~(1 << i);
                        }
                    }
                }
                left++;
            }
            
            if (currentOr <= K) {
                maxLen = max(maxLen, right - left + 1);
            }
        }
        return maxLen;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int K;
    cin >> K;
    
    Solution solution;
    cout << solution.maxOrSubarrayLeqK(a, K) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxOrSubarrayLeqK(a, K) {
    const n = a.length;
    const bitCounts = new Int32Array(32);
    let currentOr = 0;
    let left = 0;
    let maxLen = 0;
    
    for (let right = 0; right < n; right++) {
      const val = a[right];
      for (let i = 0; i < 31; i++) {
        if ((val >>> i) & 1) {
          bitCounts[i]++;
          if (bitCounts[i] === 1) {
            currentOr |= (1 << i);
          }
        }
      }
      
      // Use unsigned comparison just in case but numbers are non-negative
      while (left <= right && currentOr > K) {
        const removeVal = a[left];
        for (let i = 0; i < 31; i++) {
          if ((removeVal >>> i) & 1) {
            bitCounts[i]--;
            if (bitCounts[i] === 0) {
              currentOr &= ~(1 << i);
            }
          }
        }
        left++;
      }
      
      if (currentOr <= K) {
        maxLen = Math.max(maxLen, right - left + 1);
      }
    }
    return maxLen;
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
    
    const K = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maxOrSubarrayLeqK(a, K));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `1 (001), 2 (010), 4 (100)`. `K=3`.
1. R=0. Val=1. Cnts[0]=1. OR=1 (<=3). MaxLen=1.
2. R=1. Val=2. Cnts[0]=1, Cnts[1]=1. OR=3 (<=3). MaxLen=2.
3. R=2. Val=4. Cnts[0]=1, Cnts[1]=1, Cnts[2]=1. OR=7 (>3).
   - Shrink L=0 (Val 1). Cnts[0]=0 -> Unset bit 0. OR=6.
   - 6 > 3. Shrink L=1 (Val 2). Cnts[1]=0 -> Unset bit 1. OR=4.
   - 4 > 3. Shrink L=2 (Val 4). Cnts[2]=0 -> Unset bit 2. OR=0.
   - L=3. Loop breaks.
   - OR=0 <= 3. Window empty. MaxLen still 2.

## ✅ Proof of Correctness

### Invariant

`currentOr` correctly reflects the OR sum of `a[left...right]` because counting bits ensures that a bit is 1 in `currentOr` iff at least one element in the active window has that bit set. Monotonicity of OR ensures window logic holds.

## 💡 Interview Extensions (High-Value Add-ons)

- **Max AND Subarray >= K**: Similar logic.
- **Shortest Subarray with OR >= K**: Min-sliding window.

## Common Mistakes to Avoid

1. **Recomputing OR**:
   - ❌ Loop from left to right to compute OR (O(N)).
   - ✅ Bit counts allows O(1) [or constant O(30)] updates.
2. **K < 0**:
   - ❌ Bitwise OR is always non-negative?
   - ✅ Usually yes, unless signed interpretation.

## Related Concepts

- **Sliding Window**: General technique.
- **Frequency Arrays**: Tracking state for non-invertible ops.
