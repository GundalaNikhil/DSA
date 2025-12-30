---
problem_id: ARR_PAIR_SUM_FORBIDDEN__8320
display_id: ARR-008
slug: partner-pair-sum-forbidden
title: "Partner Pair Sum With Forbidden"
difficulty: Easy-Medium
difficulty_score: 36
topics:
  - Arrays
  - Two Pointers
  - Hashing
tags:
  - arrays
  - two-pointers
  - hashing
  - easy-medium
premium: true
subscription_tier: basic
---

# ARR-008: Partner Pair Sum With Forbidden

## 📋 Problem Summary

Determine if there exists a pair of elements in a sorted array that sums to a specific target, with the constraint that neither element's index is in a "forbidden" set.

## 🌍 Real-World Scenario

**Scenario Title:** The Secure Access Protocol

You are staffing a high-security vault that requires two officers to open it simultaneously. The sophisticated lock requires their combined biometric keys (represented by integers) to sum to exactly `Target`.
However, some officers' security clearances have been temporarily revoked ("Forbidden" status) due to pending investigations.
You have a sorted list of all officers' key values and a blacklist of revoked IDs (indices). Can you find _any_ valid pair of two active officers who can open the vault?

**Why This Problem Matters:**

- **Constraint Satisfaction**: real-world logic often involves "find X such that condition Y is met AND condition Z is NOT violated."
- **Data Filtering**: Efficiently ignoring invalid data points without preprocessing the entire dataset.
- **Two Pointers**: Mastering this technique on filtered views of data.

![Real-World Application](../images/ARR-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Skipping Forbidden Indices

```
Indices:   0    1    2    3    4
Values:   [1]  [3]  [4]  [6]  [9]
Status:    OK   NO   OK   OK   NO
Target:    7

Pointers:
L=0 (OK, val 1)
R=4 (NO, val 9) -> Skip R to 3 (OK, val 6)

Check: 1 + 6 = 7. Match!
Result: True
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Forbidden Set**: Contains indices (0-based) that cannot be used.
- **Sorted Input**: Essential for the two-pointer approach.
- **Uniqueness**: Values may happen multiple times. Indices are unique.

Common interpretation mistake:

- ❌ Checking if `index` is in forbidden set inside the inner sum logic only.
- ✅ Continuously advancing pointers past forbidden indices _before_ considering their values.

### Core Concept: Filtered Two Pointers

The problem is equivalent to "Find a pair in `ValidArray` summing to target", where `ValidArray` is the original array with forbidden elements removed. Since removing elements from a sorted array preserves the sorted order of the remaining elements, standard 2-Sum Two Pointers logic applies.

### Why Naive Approach is too slow

Nested loops checking every pair would be O(N²). Even with `forbidden` checks, the O(N²) iterations dominate.
Binary search for the complement for each valid element would be O(N log N).
Two Pointers is O(N).

## Naive Approach (Nested Loops)

### Intuition

Try every pair `(i, j)`. If `i` is good and `j` is good and sum is target, return true.

### Algorithm

1. Loop `i` from 0 to `n-1`.
   - If `i` in forbidden, continue.
2. Loop `j` from `i+1` to `n-1`.
   - If `j` in forbidden, continue.
   - If `arr[i] + arr[j] == target`, return true.
3. Return false.

### Time Complexity

- **O(N²)**.

### Space Complexity

- **O(1)**.

## Optimal Approach (Two Pointers with Skip)

### Key Insight

Treat the "forbidden" indices as invisible. When `left` pointer points to a forbidden index, just increment it until it points to a valid one. Same for `right`.
Since the valid elements are still sorted, the classic "Sum < Target -> Left++" and "Sum > Target -> Right--" logic works perfectly.

### Algorithm

1. Initialize `left = 0`, `right = n - 1`.
2. Convert `forbidden` list to a Hash Set for O(1) lookups.
3. Loop while `left < right`:
   - While `left` is forbidden: `left++`.
   - While `right` is forbidden: `right--`.
   - **Safety Check**: If `left >= right`, break loop.
   - sum = `arr[left] + arr[right]`
   - If sum == target: return `true`.
   - If sum < target: `left++` (need larger sum).
   - If sum > target: `right--` (need smaller sum).
4. Return `false`.

### Time Complexity

- **O(N)**: Each element is visited at most once by `left` and once by `right`. Skipping is part of the traversal.

### Space Complexity

- **O(F)**: To store the Forbidden set (where F is number of forbidden indices).

### Why This Is Optimal

2-Sum on sorted array is O(N). We just added an O(1) check at each step.

![Algorithm Visualization](../images/ARR-008/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-008/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public boolean hasPairWithForbidden(int[] arr, int target, Set<Integer> forbidden) {
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            // Skip forbidden indices
            if (forbidden.contains(left)) {
                left++;
                continue;
            }
            if (forbidden.contains(right)) {
                right--;
                continue;
            }

            // Standard 2-Sum Logic
            long sum = (long)arr[left] + arr[right];

            if (sum == target) {
                return true;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        int target = sc.nextInt();
        int f = sc.nextInt();
        Set<Integer> forbidden = new HashSet<>();
        for (int i = 0; i < f; i++) forbidden.add(sc.nextInt());

        Solution solution = new Solution();
        boolean result = solution.hasPairWithForbidden(arr, target, forbidden);
        System.out.println(result ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys

def has_pair_with_forbidden(arr: list[int], target: int, forbidden: set[int]) -> bool:
    left = 0
    right = len(arr) - 1

    while left < right:
        # Skip forbidden indices on the left
        while left < right and left in forbidden:
            left += 1
        # Skip forbidden indices on the right
        while left < right and right in forbidden:
            right -= 1

        # Check if we still have valid pointers
        if left >= right:
            break

        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    f = int(input())
    forbidden = set(map(int, input().split())) if f > 0 else set()

    result = has_pair_with_forbidden(arr, target, forbidden)
    print("true" if result else "false")

if __name__ == "__main__":
    main()

```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool hasPairWithForbidden(vector<int>& arr, int target, unordered_set<int>& forbidden) {
        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {
            if (forbidden.count(left)) {
                left++;
                continue;
            }
            if (forbidden.count(right)) {
                right--;
                continue;
            }

            long long sum = (long long)arr[left] + arr[right];

            if (sum == target) {
                return true;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    int target, f;
    cin >> target >> f;

    unordered_set<int> forbidden;
    for (int i = 0; i < f; i++) {
        int idx;
        cin >> idx;
        forbidden.insert(idx);
    }

    Solution solution;
    cout << (solution.hasPairWithForbidden(arr, target, forbidden) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasPairWithForbidden(arr, target, forbidden) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
      if (forbidden.has(left)) {
        left++;
        continue;
      }
      if (forbidden.has(right)) {
        right--;
        continue;
      }

      const sum = arr[left] + arr[right];

      if (sum === target) {
        return true;
      } else if (sum < target) {
        left++;
      } else {
        right--;
      }
    }

    return false;
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

  const target = Number(tokens[ptr++]);
  const f = Number(tokens[ptr++]);
  const forbidden = new Set();
  for (let i = 0; i < f; i++) forbidden.add(Number(tokens[ptr++]));

  const solution = new Solution();
  console.log(
    solution.hasPairWithForbidden(arr, target, forbidden) ? "true" : "false"
  );
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `arr=[1, 4, 6, 7]`, `target=11`, `forbidden={0}`

1. `left=0` (forbidden). Skip -> `left=1` (value 4).
2. `right=3` (value 7). Not forbidden.
3. Sum = `arr[1] + arr[3] = 4 + 7 = 11`.
4. Match Target! Return `true`.

Input: `arr=[...], target=100`, no pairs.
Pointer `left` moves right, `right` moves left until `left >= right`. Return `false`.

![Example Visualization](../images/ARR-008/example-1.png)

## ✅ Proof of Correctness

### Invariant

If a valid solution `(i, j)` exists with `i < j`, then at any step, `left <= i` and `right >= j`. Skipping forbidden indices maintains this invariant because the skipped index cannot be `i` or `j`.

### Why the approach is correct

Standard 2-Sum proof: eliminating `left` (when sum too small) is safe because `arr[left]` is too small even for the largest remaining element (`arr[right]`). Symmetrically for `right`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Return Indices**: Modified to return `[left, right]`.
- **Closest Sum**: What if we need pair closest to target? (Similar logic, track min diff).
- **Unsorted Array**: Use Hash Map + Check Forbidden condition. O(N) time but O(N) space.

## Common Mistakes to Avoid

1. **Infinite Loop**:

   - ❌ Not checking `left < right` inside skip loops?
   - ✅ Always verify bounds. But simpler logic: just `continue` the outer loop if forbidden, letting the logic naturally handle it on next iteration. My implementation uses `continue` pattern which is safe against bounds if structured well (or explicit inner loops like `while (left<right && forbidden.contains(left)) left++;`).

2. **Index vs Value**:
   - ❌ Skipping if `arr[left]` is in forbidden set?
   - ✅ Problem says forbidden _Indices_.

## Related Concepts

- **2-Sum**: Core problem.
- **Filtering Iterator**: Design pattern.
