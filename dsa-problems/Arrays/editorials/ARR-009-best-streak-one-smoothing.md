---
problem_id: ARR_BEST_STREAK_SMOOTH__2467
display_id: ARR-009
slug: best-streak-one-smoothing
title: "Best Streak With One Smoothing"
difficulty: Medium
difficulty_score: 54
topics:
  - Arrays
  - Dynamic Programming
  - Kadane
tags:
  - arrays
  - dynamic-programming
  - kadane
  - medium
premium: true
subscription_tier: basic
---

# ARR-009: Best Streak With One Smoothing

## 📋 Problem Summary

Find the maximum subarray sum possible after replacing exactly one element `arr[i]` with the average of itself and its neighbors (`floor((arr[i-1] + arr[i] + arr[i+1]) / 3)`). You can choose any valid `i` (index 1 to n-2) to perform this operation.

## 🌍 Real-World Scenario

**Scenario Title:** The Signal Smoothing

You are analyzing a noisy radio signal for a burst of high energy (maximum sum of consecutive readings).
However, simple noise can spike or dip the readings erroneously.
Your signal processor has a "smoothing filter" that can be applied to exactly one point in the stream to correct an outlier by averaging it with its neighbors.
You want to know: *If we apply the filter optimally at the best possible spot, what is the strongest energy burst we can detect?*

**Why This Problem Matters:**

- **Signal Processing**: Filtering noise while preserving significant features.
- **DP on Arrays**: A variation of the "Maximum Subarray Sum" (Kadane's) problem, common in interviews (e.g., "Max Sum with one deletion").
- **State Management**: Handling "before", "during", and "after" states in linear scans.

![Real-World Application](../images/ARR-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: To Smooth or Not to Smooth?
```
Arr:  [-2]  [3]  [-4]  [5]
Idx:    0    1     2    3

Candidate 1: Smooth index 1 (val 3)
Values: -2, 3, -4 -> (-2+3-4)/3 = -1
Arr becomes: [-2, -1, -4, 5]
Max Sum: 5 (subarray [5])

Candidate 2: Smooth index 2 (val -4)
Values: 3, -4, 5 -> (3-4+5)/3 = 1
Arr becomes: [-2, 3, 1, 5]
Max Sum: 3+1+5 = 9

Best: 9
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **One Operation**: You *must* choose exactly one `i` to smooth.
- **Neighbors**: Since you need `i-1` and `i+1`, valid indices are `1` to `n-2`.
- **Global Max**: The result can be a subarray including the smoothed element OR a subarray completely separate from it (though typically we smooth to improve the sum).

Common interpretation mistake:

- ❌ Only considering subarrays that *include* the smoothed element.
- ✅ Considering that smoothing `arr[i]` might create a localized high sum, OR it might just be a harmless operation while the true max sum lies elsewhere unchanged.

### Core Concept: Precomputed Kadane's

To evaluate the effect of smoothing at `i` in O(1) time, we need to know:
1. Max suffix sum ending at `i-1`.
2. Max prefix sum starting at `i+1`.
3. Max subarray sum fully within `0...i-1` (to handle the "separate subarray" case).
4. Max subarray sum fully within `i+1...n-1`.

### Why Naive Approach is too slow

Trying every index `i`, applying the change, and running Kadane's Algorithm takes O(N) per index. Total O(N²).
With N=200,000, we need O(N).

## Naive Approach

### Intuition

Loop `i` from 1 to `n-2`. Modify `arr`. Run Kadane. Revert `arr`. Track max.

### Algorithm

1. `global_max = -infinity`
2. For `i` from 1 to `n-2`:
   - `save = arr[i]`
   - `arr[i] = (arr[i-1] + arr[i] + arr[i+1]) / 3`
   - `current_max = Kadane(arr)`
   - `global_max = max(global_max, current_max)`
   - `arr[i] = save`
3. Return `global_max`.

### Time Complexity

- **O(N²)**.

### Space Complexity

- **O(1)** (if modifying in-place) or O(N) (copy).

## Optimal Approach (DP / Precomputation)

### Key Insight

For a fixed split point `i`, the best subarray sum is either:
A. The best subarray strictly to the left of `i`.
B. The best subarray strictly to the right of `i`.
C. A subarray passing *through* `i`. This is `(MaxSuffixSum[i-1]) + NewVal[i] + (MaxPrefixSum[i+1])`. Note: `MaxSuffixSum` should be clamped at 0 if negative (i.e., we can choose an empty left/right part).

### Algorithm

1. **Precompute Arrays**:
   - `MaxEndingAt[k]`: Max subarray sum ending at index `k`. (Standard Kadane step).
   - `MaxStartingAt[k]`: Max subarray sum starting at index `k`. (Reverse Kadane step).
   - `GlobalMaxIn[0...k]`: Max subarray sum found anywhere in partition `0...k`.
   - `GlobalMaxIn[k...n-1]`: Max subarray sum found anywhere in partition `k...n-1`.

2. **Iterate** `i` from 1 to `n-2`:
   - `smoothed_val = floor((a[i-1] + a[i] + a[i+1]) / 3)`
   - `cross_sum = max(0, MaxEndingAt[i-1]) + smoothed_val + max(0, MaxStartingAt[i+1])`
   - `left_max = GlobalMaxIn[i-1]`
   - `right_max = GlobalMaxIn[i+1]`
   - `current_best = max(cross_sum, left_max, right_max)`
   - Update `answer`.

### Time Complexity

- **O(N)**: 4 precomputation passes (linear) + 1 partial scan (linear).

### Space Complexity

- **O(N)**: To store the auxiliary arrays.

### Why This Is Optimal

We inspect the "change" at each index in O(1) time.

![Algorithm Visualization](../images/ARR-009/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-009/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long bestStreakWithSmoothing(int[] a) {
        int n = a.length;
        if (n < 3) return 0; // Should not happen per constraints

        long[] maxEndingAt = new long[n];
        long[] globalMaxPrefix = new long[n];
        
        // Forward Pass
        maxEndingAt[0] = a[0];
        globalMaxPrefix[0] = a[0];
        for (int i = 1; i < n; i++) {
            maxEndingAt[i] = Math.max(a[i], maxEndingAt[i - 1] + a[i]);
            globalMaxPrefix[i] = Math.max(globalMaxPrefix[i - 1], maxEndingAt[i]);
        }

        long[] maxStartingAt = new long[n];
        long[] globalMaxSuffix = new long[n];
        
        // Backward Pass
        maxStartingAt[n - 1] = a[n - 1];
        globalMaxSuffix[n - 1] = a[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            maxStartingAt[i] = Math.max(a[i], maxStartingAt[i + 1] + a[i]);
            globalMaxSuffix[i] = Math.max(globalMaxSuffix[i + 1], maxStartingAt[i]);
        }

        long ans = Long.MIN_VALUE;

        // Try smoothing each valid i
        for (int i = 1; i <= n - 2; i++) {
            long smoothedVal = (long)Math.floor((double)(a[i - 1] + a[i] + a[i + 1]) / 3.0);
            
            // 1. Check pass-through sum
            long leftPart = Math.max(0, maxEndingAt[i - 1]);
            long rightPart = Math.max(0, maxStartingAt[i + 1]);
            long crossSum = leftPart + smoothedVal + rightPart;
            
            // 2. Check disjoint sums
            long globalLeft = globalMaxPrefix[i - 1];
            long globalRight = globalMaxSuffix[i + 1];
            
            long currentBest = Math.max(crossSum, Math.max(globalLeft, globalRight));
            ans = Math.max(ans, currentBest);
        }

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.bestStreakWithSmoothing(a);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
import sys
import math

def best_streak_with_smoothing(a: list[int]) -> int:
    n = len(a)
    if n < 3: return 0

    max_ending_at = [0] * n
    global_max_prefix = [0] * n
    
    # Forward
    max_ending_at[0] = a[0]
    global_max_prefix[0] = a[0]
    for i in range(1, n):
        max_ending_at[i] = max(a[i], max_ending_at[i-1] + a[i])
        global_max_prefix[i] = max(global_max_prefix[i-1], max_ending_at[i])
        
    max_starting_at = [0] * n
    global_max_suffix = [0] * n
    
    # Backward
    max_starting_at[n-1] = a[n-1]
    global_max_suffix[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        max_starting_at[i] = max(a[i], max_starting_at[i+1] + a[i])
        global_max_suffix[i] = max(global_max_suffix[i+1], max_starting_at[i])
        
    ans = -float('inf')
    
    for i in range(1, n-1):
        smoothed_val = math.floor((a[i-1] + a[i] + a[i+1]) / 3)
        
        left_part = max(0, max_ending_at[i-1])
        right_part = max(0, max_starting_at[i+1])
        cross_sum = left_part + smoothed_val + right_part
        
        global_left = global_max_prefix[i-1]
        global_right = global_max_suffix[i+1]
        
        current_best = max(cross_sum, global_left, global_right)
        ans = max(ans, current_best)
        
    return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
        
    result = best_streak_with_smoothing(a)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
using namespace std;

class Solution {
public:
    long long bestStreakWithSmoothing(vector<int>& a) {
        int n = a.size();
        if (n < 3) return 0;

        vector<long long> maxEndingAt(n);
        vector<long long> globalMaxPrefix(n);
        
        maxEndingAt[0] = a[0];
        globalMaxPrefix[0] = a[0];
        for (int i = 1; i < n; i++) {
            maxEndingAt[i] = max((long long)a[i], maxEndingAt[i - 1] + a[i]);
            globalMaxPrefix[i] = max(globalMaxPrefix[i - 1], maxEndingAt[i]);
        }

        vector<long long> maxStartingAt(n);
        vector<long long> globalMaxSuffix(n);
        
        maxStartingAt[n - 1] = a[n - 1];
        globalMaxSuffix[n - 1] = a[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            maxStartingAt[i] = max((long long)a[i], maxStartingAt[i + 1] + a[i]);
            globalMaxSuffix[i] = max(globalMaxSuffix[i + 1], maxStartingAt[i]);
        }

        long long ans = LLONG_MIN;

        for (int i = 1; i < n - 1; i++) {
            long long smoothedVal = floor((double)(a[i - 1] + a[i] + a[i + 1]) / 3.0);
            
            long long leftPart = max(0LL, maxEndingAt[i - 1]);
            long long rightPart = max(0LL, maxStartingAt[i + 1]);
            long long crossSum = leftPart + smoothedVal + rightPart;
            
            long long globalLeft = globalMaxPrefix[i - 1];
            long long globalRight = globalMaxSuffix[i + 1];
            
            long long currentBest = max({crossSum, globalLeft, globalRight});
            ans = max(ans, currentBest);
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    cout << solution.bestStreakWithSmoothing(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bestStreakWithSmoothing(a) {
    const n = a.length;
    if (n < 3) return 0;

    const maxEndingAt = new Array(n).fill(0);
    const globalMaxPrefix = new Array(n).fill(0);
    
    maxEndingAt[0] = a[0];
    globalMaxPrefix[0] = a[0];
    for (let i = 1; i < n; i++) {
      maxEndingAt[i] = Math.max(a[i], maxEndingAt[i - 1] + a[i]);
      globalMaxPrefix[i] = Math.max(globalMaxPrefix[i - 1], maxEndingAt[i]);
    }

    const maxStartingAt = new Array(n).fill(0);
    const globalMaxSuffix = new Array(n).fill(0);
    
    maxStartingAt[n - 1] = a[n - 1];
    globalMaxSuffix[n - 1] = a[n - 1];
    for (let i = n - 2; i >= 0; i--) {
      maxStartingAt[i] = Math.max(a[i], maxStartingAt[i + 1] + a[i]);
      globalMaxSuffix[i] = Math.max(globalMaxSuffix[i + 1], maxStartingAt[i]);
    }

    let ans = Number.MIN_SAFE_INTEGER;

    for (let i = 1; i < n - 1; i++) {
      const smoothedVal = Math.floor((a[i - 1] + a[i] + a[i + 1]) / 3);
      
      const leftPart = Math.max(0, maxEndingAt[i - 1]);
      const rightPart = Math.max(0, maxStartingAt[i + 1]);
      const crossSum = leftPart + smoothedVal + rightPart;
      
      const globalLeft = globalMaxPrefix[i - 1];
      const globalRight = globalMaxSuffix[i + 1];
      
      const currentBest = Math.max(crossSum, globalLeft, globalRight);
      ans = Math.max(ans, currentBest);
    }
    return ans;
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
    
    const solution = new Solution();
    console.log(String(solution.bestStreakWithSmoothing(a)));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `[-2, 3, -4, 5]`
Precomputation:
- `maxEndingAt`: `[-2, 3, -1, 5]`
- `globalMaxPrefix`: `[-2, 3, 3, 5]`
- `maxStartingAt`: `[2, 4, 1, 5]` (Wait: 3+-4+5=4, -4+5=1). Backwards:
  - `i=3`: 5
  - `i=2`: max(-4, 5-4=1) -> 1
  - `i=1`: max(3, 1+3=4) -> 4
  - `i=0`: max(-2, 4-2=2) -> 2. Correct.
- `globalMaxSuffix`: `[5, 5, 5, 5]`

Loop i=1 (Val 3):
- Smooth: `floor((-2+3-4)/3) = -1`.
- `CrossSum` = `max(0, -2) + (-1) + max(0, 1)` = `0 - 1 + 1` = `0`.
- `GlobalLeft`: -2. `GlobalRight`: 5.
- `Best`: `max(0, -2, 5)` = 5.

Loop i=2 (Val -4):
- Smooth: `floor((3-4+5)/3) = 1`.
- `CrossSum` = `max(0, 3) + 1 + max(0, 5) ` (Wait `maxStartingAt[3]=5`. Yes.)
- `CrossSum` = `3 + 1 + 5 = 9`.
- `GlobalLeft`: 3. `GlobalRight`: 5.
- `Best`: `9`.

Ans = 9. Matches Example.

![Example Visualization](../images/ARR-009/example-1.png)

## ✅ Proof of Correctness

### Invariant

`MaxEndingAt` and `MaxStartingAt` correctly capture optimal subarray sums adjacent to `i`. The algorithm exhaustively checks every possible operation, ensuring no better configuration is missed.

### Why the approach is correct

Since we modify exactly one index `i`, the optimal answer must strictly fall into one of three categories relative to `i`: completely left, completely right, or crossing `i`. We handle each case.

## 💡 Interview Extensions (High-Value Add-ons)

- **K Smoothings**: What if you can smooth `k` times? (A: Heavy DP).
- **Max Sum with 1 Deletion**: Similar problem, just skip `i` instead of averaging.

## Common Mistakes to Avoid

1. **Missing Disjoint Cases**:
   - ❌ Forgetting `GlobalLeft` and `GlobalRight`. The smoothing might lower the sum locally, and the best answer might be far away.
2. **Bounds**:
   - ❌ Smooth `i=0` or `n-1`. Not enough neighbors.
3. **Empty Subarray**:
   - ❌ `max(0, ...)` logic handles empty prefix/suffix extending the cross sum.

## Related Concepts

- **Kadane's Algorithm**: Base pattern.
- **Prefix/Suffix arrays**: Common in array manipulation.
