---
problem_id: ARR_WEIGHTED_BALANCE_POINT__7742
display_id: ARR-005
slug: weighted-balance-point
title: "Weighted Balance Point"
difficulty: Medium
difficulty_score: 44
topics:
  - Arrays
  - Prefix Sum
  - Math
tags:
  - arrays
  - prefix-sum
  - math
  - medium
premium: true
subscription_tier: basic
---

# ARR-005: Weighted Balance Point

## 📋 Problem Summary

Find the smallest pivot index `i` such that the weighted sum of elements on the left (multiplied by `L`) equals the weighted sum of elements on the right (multiplied by `R`).

## 🌍 Real-World Scenario

**Scenario Title:** The Crane Stabilization

You are designing a control system for a large construction crane. The crane has a long horizontal boom with various counterweights distributed along it.
To lift a heavy load safely, the operator must position the fulcrum (the lifting point) at a specific location `i` where the torque is balanced.
- The "Left Arm" has a mechanical leverage factor `L`.
- The "Right Arm" has a mechanical leverage factor `R`.

If the torques (`TotalLeftWeight * L` and `TotalRightWeight * R`) are not equal, the crane could tip over! You need to scan the beam and find the first perfectly stable lifting point.

**Why This Problem Matters:**

- **Equilibrium Finding**: Common in physics engines and game development.
- **Prefix/Suffix Sums**: Standard technique for range query optimization.
- **Linear Scan**: Essential pattern for optimizing naive quadratic solutions.

![Real-World Application](../images/ARR-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Balance Beam
```
Weights:   [2]   [3]   [-1]   [3]   [2]
Indices:    0     1      2     3     4
                         ^
                       Pivot

Left Side: [2, 3] sum = 5
Right Side: [3, 2] sum = 5

Factors: L=2, R=2 (Example where L=R)
Check: 5*2 == 5*2 -> 10 == 10 (Balanced!)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Pivot Exclusion**: The element at index `i` itself is the pivot/fulcrum and is **excluded** from both left and right sums.
- **Smallest Index**: If multiple indices satisfy the condition, return the smallest one.
- **Factor Application**: `L` applies to the SUM of the left side, not individual elements. (Same for `R`).

Common interpretation mistake:

- ❌ Including `arr[i]` in either the left or right sum.
- ❌ Computing `(arr[0]*L + arr[1]*L ...)` individually (mathematically same, but computationally slower if not careful).
- ✅ Correctly maintaining `LeftSum` and deriving `RightSum` from `TotalSum`.

### Core Concept: Total Sum subtraction

Instead of re-summing the right side loop every time, we can know the Right Sum instantly if we know the Total Sum and the Left Sum.
`RightSum = TotalSum - LeftSum - PivotValue`

### Why Naive Approach is too slow

Calculating the sum of the left subarray and right subarray for every index `i` takes O(N) work per index. Done for N indices, this is O(N²).
For N=200,000, 40 billion operations is unacceptable (Time Limit Exceeded).

## Naive Approach

### Intuition

Check every index `i` from 0 to `n-1`. Loop left to sum, loop right to sum. Compare.

### Algorithm

1. Loop `i` from 0 to `n-1`.
2. `l_sum = 0`, `r_sum = 0`.
3. Loop `j` from 0 to `i-1`: `l_sum += arr[j]`.
4. Loop `k` from `i+1` to `n-1`: `r_sum += arr[k]`.
5. If `l_sum * L == r_sum * R`, return `i`.
6. If loop ends, return -1.

### Time Complexity

- **O(N²)**: Nested loops.

### Space Complexity

- **O(1)**: No extra space.

## Optimal Approach (Prefix Sum / Running Sum)

### Key Insight

As we move the pivot `i` from left to right, `LeftSum` only grows by `arr[i-1]`. `RightSum` shrinks by `arr[i+1]`.
Even simpler: We can compute `TotalSum` once. Then, at any `i`:
`RightSum = TotalSum - LeftSum - arr[i]`.

### Algorithm

1. Calculate `total_sum` of the entire array.
2. Initialize `left_sum = 0`.
3. Iterate `i` from 0 to `n-1`:
   - `pivot_val = arr[i]`
   - `right_sum = total_sum - left_sum - pivot_val`
   - Check condition: `left_sum * L == right_sum * R`
   - If true, return `i`.
   - Update `left_sum += pivot_val` (prepare for next iteration).
4. Return -1.

### Time Complexity

- **O(N)**: Two passes (one for total sum, one for scan).

### Space Complexity

- **O(1)**: Only a few variables needed.

### Why This Is Optimal

We visit each element a constant number of times (2 times). We cannot do better than linear time as we must read the input.

![Algorithm Visualization](../images/ARR-005/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-005/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int weightedBalancePoint(int[] a, int L, int R) {
        long totalSum = 0;
        for (int x : a) {
            totalSum += x;
        }
        
        long leftSum = 0;
        long L_long = L; // Use long for multiplication
        long R_long = R;

        for (int i = 0; i < a.length; i++) {
            // Right sum is total minus (left part + current element)
            long rightSum = totalSum - leftSum - a[i];
            
            if (leftSum * L_long == rightSum * R_long) {
                return i;
            }
            
            leftSum += a[i];
        }
        
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        
        int L = sc.nextInt();
        int R = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.weightedBalancePoint(a, L, R));
        sc.close();
    }
}
```

### Python

```python
import sys

def weighted_balance_point(a: list[int], L: int, R: int) -> int:
    """
    Find smallest index i where L * sum(left) == R * sum(right).
    """
    total_sum = sum(a)
    left_sum = 0
    
    for i, x in enumerate(a):
        # right_sum excludes current element x
        right_sum = total_sum - left_sum - x
        
        if left_sum * L == right_sum * R:
            return i
            
        left_sum += x
        
    return -1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
        
    L = int(data[ptr]); ptr += 1
    R = int(data[ptr]); ptr += 1
    
    result = weighted_balance_point(a, L, R)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int weightedBalancePoint(vector<int>& a, int L, int R) {
        long long totalSum = 0;
        for (int x : a) totalSum += x;
        
        long long leftSum = 0;
        long long LL = L;
        long long RR = R;
        
        for (int i = 0; i < a.size(); i++) {
            long long rightSum = totalSum - leftSum - a[i];
            
            if (leftSum * LL == rightSum * RR) {
                return i;
            }
            
            leftSum += a[i];
        }
        
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    
    int L, R;
    cin >> L >> R;

    Solution solution;
    cout << solution.weightedBalancePoint(a, L, R) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  weightedBalancePoint(a, L, R) {
    let totalSum = 0n;
    for (const x of a) {
      totalSum += BigInt(x);
    }
    
    let leftSum = 0n;
    const bigL = BigInt(L);
    const bigR = BigInt(R);
    
    for (let i = 0; i < a.length; i++) {
      const val = BigInt(a[i]);
      const rightSum = totalSum - leftSum - val;
      
      if (leftSum * bigL === rightSum * bigR) {
        return i;
      }
      
      leftSum += val;
    }
    
    return -1;
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
    
    const L = Number(tokens[ptr++]);
    const R = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.weightedBalancePoint(a, L, R));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `a=[2, 3, -1, 3, 2]`, `L=2, R=1`

Total Sum = `2+3-1+3+2 = 9`.

1. **i=0**: `val=2`.
   - `Left=0`. `Right = 9 - 0 - 2 = 7`.
   - `0*2 == 7*1`? 0 != 7.
   - `Left += 2` -> 2.

2. **i=1**: `val=3`.
   - `Left=2`. `Right = 9 - 2 - 3 = 4`.
   - `2*2 == 4*1`? **4 == 4. TRUE!**
   - Return 1? Wait, example says output is 2.
   - Let's check calculation again.
   - Input example: `2 3 -1 3 2`.
   - Example Explanation: "At i=2, left sum is 5 and right sum is 8."
   - Left of i=2 is `2, 3`. Sum=5.
   - Right of i=2 is `3, 2`. Sum=5. Wait, 3+2=5.
   - Explanation says Right Sum is 8. WHY?
   - Input: `2 3 -1 3 2`.
   - Elements at i=2 is `-1`.
   - Right elements: `3, 2`. Sum = 5.
   - Is my mental arithmetic wrong or the example explanation?
   - "At i = 2, left sum is 5 and right sum is 8. 5 * 2 == 8 * 1".
   - `10 == 8`. False. 4!=4?
   - Wait, my walkthough `i=1` check: `Left=2`. `Right=4`. `2*2 == 4*1`. Correct.
   - So my logic found i=1.
   - Let's check value at i=1 (`3`).
   - Left: `[2]`. Sum=2.
   - Right: `[-1, 3, 2]`. Sum=4.
   - `2*2 == 4*1`. `4=4`. Balanced.
   - Why does example say 2?
   - Maybe constraints/indices distinct?
   - Constraints: `2 1` (L, R).
   - Input: `2 3 -1 3 2`.
   - Let's check i=2 again.
   - Left: `2 + 3 = 5`.
   - Right: `3 + 2 = 5`.
   - `5*2 = 10`. `5*1 = 5`. `10 != 5`.
   - Maybe example input `2 3 -1 3 2`... explanation says `Right sum is 8`.
   - For Right Sum to be 8, elements `3, 2` must sum to 8? No.
   - Maybe `3 + 2 + ?`.
   - Or maybe `L=2, R=1` was `L=1, R=1`?
   - No, explanation explicitly says `5 * 2 == 8 * 1`.
   - Where did 8 come from?
   - Maybe the element `-1` is somehow 8? No.
   - Is it possible the input array in explanation is DIFFERENT? "At i=2...".
   - The example output is `2`.
   - And explanation says `5 * 2 == 8 * 1`. This equation `10 == 8` is FALSE.
   - So the example explanation text "5 * 2 == 8 * 1, so the answer is 2" contains a mathematical error claiming 10 equals 8?
   - OR, I am misreading.
   - `5 * 2 = 10`. `8 * 1 = 8`.
   - Is it possible `L` and `R` are swapped in explanation? `5*1 == ?`. No.
   - Conclusion: The example in the problem description is chaotic/broken.
   - `Right Sum 8` implies `3+2` isn't `3+2`? Or `a[3]=6`? If `a[3]=6`, sum is `6+2=8`.
   - If array was `2 3 -1 6 2`.
   - Left (i=2): `2+3=5`. Right: `6+2=8`.
   - `5*L == 8*R`. `5*2 = 10`. `8*1=8`. Still not equal.

   - Let's stick to the Correct Logic:
     - My `i=1` check worked (`2*2 == 4*1`).
     - So for `2 3 -1 3 2` with `L=2, R=1`, index 1 is a valid balance point.
     - Why does example say 2?
     - Maybe 1-based indexing?
     - If index 2 is actually the 2nd element (index 1), then it matches my result. "Print the smallest index i (0-based)".
     - If output `2` means index 2 (0-based), then result is index 2 (`-1`).
     - But we proved index 2 fails.
     - So either 1-based indexing in example output, OR broken example.
     - Given `(0-based)` in output format description, and output `2`, it likely implies index 2.
     - Which is weird.

   - I will implement the 0-based index logic in the editorial and assume the problem statement example has a typo (or my manual trace is missing a subtlety).
   - Actually, wait. `2 3 -1 3 2`.
   - i=0: L=0, R=7. 0 != 7.
   - i=1: L=2, R=4. 2*2 = 4. 4*1=4. Match. Index 1.
   - i=2: L=5, R=5. 5*2=10. 5*1=5. No.
   - i=3: L=4, R=2. 4*2=8. 2*1=2. No.
   - i=4: L=7, R=0. 14 != 0.

   - Okay, sticking to my guns. The algorithm is correct. The example might be flawed. I will present the correct algorithm.

## ✅ Proof of Correctness

### Invariant

At index `i`, `left_sum` contains `sum(a[0...i-1])` and `right_sum` correctly derived as `Total - left_sum - a[i]`. `L*LS == R*RS` correctly checks the condition.

## 💡 Interview Extensions (High-Value Add-ons)

- **Search Space**: Can we use binary search? (A: Only if weights are all positive, function `L*LS - R*RS` is monotonic. With negative numbers, monotonic property is lost, must use linear scan).
- **Floating Point**: Dealing with precision if L/R were floats.

## Common Mistakes to Avoid

1. **Including Pivot**:
   - ❌ Adding `arr[i]` to Left Sum before comparison.
   - ✅ Compare first, then add to Left Sum.

2. **Overflow**:
   - ❌ Using `int` for weighted sums. Sum can be `N * MaxVal * L` ≈ `2e5 * 1e9 * 1e6` ≈ `2e20`. Need `long long` (64-bit).

## Related Concepts

- **Equilibrium Index**: This is the weighted version of the classic Equilibrium Index problem.
