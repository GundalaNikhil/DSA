---
title: Target Sum With Limited Negations
slug: target-sum-limited-negations
difficulty: Medium
difficulty_score: 49
tags:
- Recursion
- Backtracking
- Target Sum
problem_id: REC_TARGET_SUM_LIMITED_NEGATIONS__8206
display_id: REC-014
topics:
- Recursion
- Backtracking
- DP
---
# Target Sum With Limited Negations - Editorial

## Problem Summary

You are given an array of integers `nums`. You need to assign a sign (`+` or `-`) to each integer such that the sum of the resulting values equals `target`. However, there is a constraint: you can use the `-` sign at most `K` times. Return the number of ways to achieve the target.

## Real-World Scenario

Imagine **Budget Balancing**. You have a list of potential expenses and incomes. By default, everything is an income (+). You can choose to classify at most `K` items as expenses (-) to make your final balance exactly `target`.

## Problem Exploration

### 1. Relation to Subset Sum
Let $P$ be the set of numbers assigned `+`, and $N$ be the set of numbers assigned `-`.
Sum = $\sum P - \sum N = target$.
We also know $\sum P + \sum N = \sum_{all} nums = S$.
Adding equations: $2 \sum P = S + target$.
So $\sum P = (S + target) / 2$.
This transforms the standard Target Sum problem into finding a subset $P$ with a specific sum.
However, we have an additional constraint: $|N| \le K$.
This means we need to pick a subset $N$ (the negated numbers) such that:
1.  Sum of $N$ is $(S - target) / 2$.
2.  Size of $N$ is $\le K$.

### 2. Recursive Structure
We can stick to the original formulation for backtracking:
`solve(index, current_sum, negations_count)`
-   **Base Case**:
    -   If `index == n`: Return 1 if `current_sum == target`, else 0.
-   **Transitions**:
    -   **Add (+)**: `solve(index + 1, current_sum + nums[index], negations_count)`
    -   **Subtract (-)**: Only if `negations_count < K`. `solve(index + 1, current_sum - nums[index], negations_count + 1)`

### 3. Constraints
-   $N \le 20$: $2^{20} \approx 10^6$. This is small enough for pure recursion without memoization.
-   If $N$ were larger (e.g., 100), we would need DP: `dp[index][current_sum][negations_count]`.

## Approaches

### Approach 1: Pure Backtracking
Since $N$ is small, we explore the decision tree.
At each step, try adding `nums[i]` and subtracting `nums[i]` (if allowed).
Sum up the valid paths.

### Approach 2: Meet-in-the-middle (Optimization)
Split array into two halves. Generate all `(sum, negation_count)` pairs for both halves. Combine them. This reduces complexity to $O(2^{N/2})$. Not needed for $N=20$.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long countAssignments(int[] nums, int K, int target) {
        return backtrack(0, 0, 0, nums, K, target);
    }

    private long backtrack(int index, int currentSum, int negations, int[] nums, int K, int target) {
        if (index == nums.length) {
            return currentSum == target ? 1 : 0;
        }

        long count = 0;

        // Option 1: Assign +
        count += backtrack(index + 1, currentSum + nums[index], negations, nums, K, target);

        // Option 2: Assign - (if limit allows)
        if (negations < K) {
            count += backtrack(index + 1, currentSum - nums[index], negations + 1, nums, K, target);
        }

        return count;
    }
}
```

### Python

```python
def count_assignments(nums: list[int], K: int, target: int) -> int:
    n = len(nums)

    def backtrack(index, current_sum, negations):
        if index == n:
            return 1 if current_sum == target else 0
        
        count = 0
        
        # Option 1: +
        count += backtrack(index + 1, current_sum + nums[index], negations)
        
        # Option 2: -
        if negations < K:
            count += backtrack(index + 1, current_sum - nums[index], negations + 1)
            
        return count

    return backtrack(0, 0, 0)
```

### C++

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    long long countAssignments(const vector<int>& nums, int K, int target) {
        return backtrack(0, 0, 0, nums, K, target);
    }

private:
    long long backtrack(int index, int currentSum, int negations, const vector<int>& nums, int K, int target) {
        if (index == nums.size()) {
            return currentSum == target ? 1 : 0;
        }

        long long count = 0;

        // Option 1: +
        count += backtrack(index + 1, currentSum + nums[index], negations, nums, K, target);

        // Option 2: -
        if (negations < K) {
            count += backtrack(index + 1, currentSum - nums[index], negations + 1, nums, K, target);
        }

        return count;
    }
};
```

### JavaScript

```javascript
class Solution {
  countAssignments(nums, K, target) {
    const n = nums.length;

    const backtrack = (index, currentSum, negations) => {
      if (index === n) {
        return currentSum === target ? 1 : 0;
      }

      let count = 0;

      // Option 1: +
      count += backtrack(index + 1, currentSum + nums[index], negations);

      // Option 2: -
      if (negations < K) {
        count += backtrack(index + 1, currentSum - nums[index], negations + 1);
      }

      return count;
    };

    return backtrack(0, 0, 0);
  }
}
```

## Test Case Walkthrough

**Input:** `nums=[1, 2, 3]`, `K=1`, `target=2`

1.  `solve(0, 0, 0)`
    -   **+1**: `solve(1, 1, 0)`
        -   **+2**: `solve(2, 3, 0)`
            -   **+3**: `solve(3, 6, 0)` -> Sum 6 != 2. Return 0.
            -   **-3**: `solve(3, 0, 1)` -> Sum 0 != 2. Return 0.
        -   **-2**: `solve(2, -1, 1)`
            -   **+3**: `solve(3, 2, 1)` -> Sum 2 == 2. **Return 1**. (`+1 -2 +3`)
            -   **-3**: (Negations 1 < 1 False). Skip.
    -   **-1**: `solve(1, -1, 1)`
        -   **+2**: `solve(2, 1, 1)`
            -   **+3**: `solve(3, 4, 1)` -> Sum 4 != 2. Return 0.
            -   **-3**: Skip.
        -   **-2**: Skip.

Is there another?
Example output says 2.
Explanation says: `+1 +2 -3` (Sum 0? No. $1+2-3=0$. Target is 2. Explanation says valid assignments include `+1 +2 -3`? Wait.)
Let's check the example in problem description.
Input: `3 1 2` (n=3, K=1, target=2).
Nums: `1 2 3`.
Explanation: `+1 +2 -3` and `-1 +2 +3`.
$1+2-3 = 0$. Target is 2.
$-1+2+3 = 4$. Target is 2.
Is the example explanation wrong? Or did I misread input?
Input: `3 1 2` -> `n=3`, `K=1`, `target=2`.
Nums: `1 2 3`.
Maybe target is 0? No, input says 2.
Maybe nums are different? No.
Maybe I should check if `+1 -2 +3` = 2. Yes.
Maybe `-1 +2 -3`? $-2$.
Maybe `+1 +2 +3`? $6$.
Maybe `-1 -2 +3`? $0$.
Maybe `-1 -2 -3`? $-6$.
There is only 1 way to get 2: `+1 -2 +3`.
Why does the example output say 2?
Is it possible `K` is exact? "at most K".
Is it possible `target` is different?
Let's re-read the example text in the problem file provided in context.
```
53: 3 1 2
54: 1 2 3
...
60: 2
...
65: Valid assignments include `+1 +2 -3` and `-1 +2 +3`.
```
There is a massive contradiction in the example explanation vs math.
$1+2-3 = 0$.
$-1+2+3 = 4$.
Neither is 2.
However, `+1 -2 +3` is 2.
Is it possible the input line `3 1 2` means `n=3, K=1, target=2`? Yes.
Is it possible the numbers are `1 2 3`? Yes.
Is it possible the explanation is just hallucinated text in the problem file? Yes.
Or maybe the target is 0? If target is 0:
$1+2-3 = 0$ (1 negation). Valid.
$-1-2+3 = 0$ (2 negations). Invalid (K=1).
So if target=0, answer is 1.
If target=4:
$-1+2+3 = 4$ (1 negation). Valid.
$1+2+3 = 6$.
So answer is 1.
If target=2:
$1-2+3 = 2$ (1 negation). Valid.
Answer is 1.
Why does output say 2?
Maybe `K=2`?
If `K=2`, target=0:
$1+2-3=0$ (1 neg).
$-1-2+3=0$ (2 neg).
Total 2.
This matches the count 2.
So maybe the input `3 1 2` actually means `n=3, K=2, target=0`?
Or `n=3, K=1` is wrong?
Given the ambiguity, I will write the code that strictly follows the constraints and logic ($N \le 20$, recursion). The logic is sound. The example in the problem description might be flawed, but the algorithm `backtrack` is correct for the "Target Sum" problem.

## Proof of Correctness

The algorithm explores all $2^N$ sign combinations (pruned by K).
-   **Correctness**: It sums the terms and checks against `target`.
-   **Constraint**: It ensures `negations <= K`.

## Interview Extensions

1.  **Optimize for large N?**
    -   Use DP if sum range is small. `dp[i][current_sum][negations]`.
    -   Use Meet-in-the-middle if sum is large.

### C++ommon Mistakes

-   **Base Case**: Returning 1 only if `sum == target`.
-   **Negation Count**: Only increment when using `-`.
