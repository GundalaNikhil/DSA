---
problem_id: ARR_POWER_WINDOW_DROP__2879
display_id: ARR-016
slug: power-window-with-drop
title: "Power Window With Drop"
difficulty: Medium
difficulty_score: 49
topics:
  - Arrays
  - Sliding Window
  - Greedy
tags:
  - arrays
  - sliding-window
  - greedy
  - medium
premium: true
subscription_tier: basic
---

# ARR-016: Power Window With Drop

## 📋 Problem Summary

Find the maximum sum of a sliding window of size `k`. You are allowed to optionally drop (remove) one element from the window to improve the sum. Since all input elements are positive, this optional drop is never strictly beneficial for maximization, simplifying the problem to finding the maximum sum of any subarray of length `k`.

## 🌍 Real-World Scenario

**Scenario Title:** The Solar Panel Output

You have a strip of solar cells. You want to connect a contiguous block of `k` cells to a battery.
- **Defective Bypass**: The system allows you to bypass exactly one cell in the block if it's defective (e.g., negative output/drain).
- **Positive Output**: In this specific batch, all cells are functioning and producing positive energy.
- **Goal**: Choosing the best `k` block. Since all cells add power, bypassing any cell would just waste valid energy. You simply want the `k` block with the highest total generation.

**Why This Problem Matters:**

- **Constraint Analysis**: Recognizing when a "feature" (dropping an element) is redundant due to data properties (positivity).
- **Sliding Window**: Efficiently computing sums of moving intervals.
- **Greedy Logic**: Realizing `Sum > Sum - Positive_Value`.

![Real-World Application](../images/ARR-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: To Drop or Not?
```
Arr:  [2]  [1]  [5]  [3]  [2]
k = 3

Window 1: [2, 1, 5]
  Sum = 8
  Drop Min(1) -> 7
  Max = 8 (Keep all)

Window 2: [1, 5, 3]
  Sum = 9
  Drop Min(1) -> 8
  Max = 9 (Keep all)

Window 3: [5, 3, 2]
  Sum = 10
  Drop Min(2) -> 8
  Max = 10 (Keep all)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: all `arr[i] >= 1`.
- **Option**: You *can* drop one, but you aren't forced to.
- **Strategy**: Since `x > 0`, `Sum > Sum - x`. Therefore, never drop anything.

Common interpretation mistake:

- ❌ Implementing a Monotonic Deque to find the minimum in the window.
- ✅ realizing that step is unnecessary given the constraints, reducing the problem to a standard sliding window sum.

### Core Concept: Sliding Window Sum

We maintain a running sum of `k` elements.
As we slide the window one step right (from index `i` to `i+1`):
`CurrentSum = PreviousSum - arr[exiting] + arr[entering]`.
We track the maximum `CurrentSum` seen.

### Why Naive Approach is too slow

Recomputing sum for every window is O(N*K). Sliding window is O(N).

## Naive Approach (Re-summing)

### Intuition

For each starting position, loop `k` times to sum.

### Algorithm

1. Loop `i` from 0 to `n-k`:
   - `sum = 0`
   - Loop `j` from 0 to `k-1`: `sum += arr[i+j]`
   - `max_sum = max(max_sum, sum)`
2. Return `max_sum`.

### Time Complexity

- **O(N * K)**.

### Space Complexity

- **O(1)**.

## Optimal Approach (Sliding Window)

### Key Insight

The sum of window `i+1` shares `k-1` elements with window `i`. We can update the sum in O(1).

### Algorithm

1. `current_sum = sum(arr[0...k-1])`.
2. `max_total = current_sum`.
3. Loop `i` from `k` to `n-1`:
   - `current_sum += arr[i]`.
   - `current_sum -= arr[i-k]`.
   - `max_total = max(max_total, current_sum)`.
4. Return `max_total`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(1)**.

### Why This Is Optimal

We touch every element constant times.

![Algorithm Visualization](../images/ARR-016/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-016/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long maxWindowSumWithDrop(int[] arr, int k) {
        int n = arr.length;
        if (n < k) return 0;

        long currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += arr[i];
        }

        long maxTotal = currentSum;

        for (int i = k; i < n; i++) {
            currentSum += arr[i];
            currentSum -= arr[i - k];
            if (currentSum > maxTotal) {
                maxTotal = currentSum;
            }
        }

        return maxTotal;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        
        int k = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.maxWindowSumWithDrop(arr, k);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
import sys

def max_window_sum_with_drop(arr: list[int], k: int) -> int:
    n = len(arr)
    if n < k: return 0
    
    current_sum = sum(arr[:k])
    max_total = current_sum
    
    for i in range(k, n):
        current_sum += arr[i]
        current_sum -= arr[i-k]
        if current_sum > max_total:
            max_total = current_sum
            
    return max_total

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    result = max_window_sum_with_drop(arr, k)
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
    long long maxWindowSumWithDrop(vector<int>& arr, int k) {
        int n = arr.size();
        if (n < k) return 0;
        
        long long currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += arr[i];
        }
        
        long long maxTotal = currentSum;
        
        for (int i = k; i < n; i++) {
            currentSum += arr[i];
            currentSum -= arr[i - k];
            maxTotal = max(maxTotal, currentSum);
        }
        
        return maxTotal;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    
    int k;
    cin >> k;

    Solution solution;
    cout << solution.maxWindowSumWithDrop(arr, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxWindowSumWithDrop(arr, k) {
    const n = arr.length;
    if (n < k) return 0;
    
    let currentSum = 0n;
    for (let i = 0; i < k; i++) {
      currentSum += BigInt(arr[i]);
    }
    
    let maxTotal = currentSum;
    
    for (let i = k; i < n; i++) {
      currentSum += BigInt(arr[i]);
      currentSum -= BigInt(arr[i - k]);
      if (currentSum > maxTotal) {
        maxTotal = currentSum;
      }
    }
    
    return maxTotal.toString();
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
    const arr = [];
    for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));
    
    const k = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maxWindowSumWithDrop(arr, k));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `[2, 1, 5, 3, 2]`, `k=3`.

1. **Init**: Sum `[2, 1, 5]` = 8. Max = 8.
2. **Slide** (i=3): Add 3, Drop 2. Sum = `8 + 3 - 2 = 9`. Max = 9.
3. **Slide** (i=4): Add 2, Drop 1. Sum = `9 + 2 - 1 = 10`. Max = 10.

**Result**: 10. Matches Example.

![Example Visualization](../images/ARR-016/example-1.png)

## ✅ Proof of Correctness

### Invariant

`currentSum` accurately reflects the sum of the subarray `arr[i-k+1...i]`. Since all elements are positive, any dropped element would decrease the sum, so keeping all elements is always optimal.

### Why the approach is correct

Reduces to standard Max Sliding Window Sum.

## 💡 Interview Extensions (High-Value Add-ons)

- **Negative numbers**: If negatives allowed, we must track the minimum element in the window using a **Monotonic Deque** (O(N)). The answer would be `max(sum, sum - min_element_in_window)`.
- **Variable K**: Kadane's Algorithm.

## Common Mistakes to Avoid

1. **Over-engineering**:
   - ❌ Implementing Deque when not needed.
   - ✅ Checking constraints first.

2. **Overflow**:
   - ❌ `int` for sums.
   - ✅ `long/BigInt`.

## Related Concepts

- **Given Sum Subarray**: Two Pointers.
- **Maximum Sum Subarray**: Kadane's.
