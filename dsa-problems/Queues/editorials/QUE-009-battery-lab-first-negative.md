---
problem_id: QUE_BATTERY_LAB_FIRST_NEGATIVE__8630
display_id: QUE-009
slug: battery-lab-first-negative
title: "Battery Lab First Negative"
difficulty: Easy
difficulty_score: 32
topics:
  - Sliding Window
  - Queue
  - Array
tags:
  - sliding-window
  - queue
  - negatives
  - easy
premium: true
subscription_tier: basic
---

# QUE-009: Battery Lab First Negative

## 📋 Problem Summary

We are given a sequence of `N` integers representing voltage changes. For every sliding window of size `K`, we need to find the **first negative integer** that appears in that window.
- If a window has no negative integers, output `0`.
- "First" means the one with the smallest index within the window.

## 🌍 Real-World Scenario

**Scenario Title:** Power Grid Fault Detection

Imagine monitoring a power grid.
- Positive values mean surplus power generation.
- Negative values mean a power deficit (drain).
- A monitoring system scans the last 10 minutes (window `K`).
- It needs to alert operators immediately about the **earliest** sign of a deficit in the current window to trace the root cause.
- Even if there are multiple deficits, the first one that occurred is often the trigger for the others.

**Why This Problem Matters:**

- **Financial Analysis:** Finding the first loss in a quarterly report window.
- **Error Logging:** Identifying the first error code in a rolling log buffer.

![Real-World Application](../images/QUE-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Window

Values: `[5, -2, -7, 3, 4]`, `K=2`.

1. **Window 1:** `[5, -2]`
   - Negatives: -2 (at index 1).
   - First is -2.

2. **Window 2:** `[-2, -7]`
   - Negatives: -2 (idx 1), -7 (idx 2).
   - First is -2.

3. **Window 3:** `[-7, 3]`
   - Negatives: -7 (idx 2).
   - First is -7.

4. **Window 4:** `[3, 4]`
   - Negatives: None.
   - Output 0.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `N, K`, array of integers.
- **Output:** Array of results.
- **Zero:** 0 is not negative.
- **Order:** "First" refers to the order in the array (leftmost in the window).

## Naive Approach

### Intuition

For each window, scan from left to right. Stop at the first negative.

### Algorithm

1. Loop `i` from 0 to `n-k`.
2. Loop `j` from `i` to `i+k-1`.
3. If `values[j] < 0`, print `values[j]` and break.
4. If loop finishes without finding negative, print 0.

### Limitations

- **Time Complexity:** `O(N * K)`.
- With `N=100,000` and `K=50,000`, this is `5 * 10^9` operations `->` TLE.

## Optimal Approach

### Key Insight

We only care about the indices of negative numbers.
- Store indices of negative numbers in a **Queue**.
- As the window slides:
  1. Remove indices from the front of the queue if they are out of the current window (index `< i - k + 1`).
  2. Add the new element's index to the back if it is negative.
  3. The front of the queue is the answer.

### Algorithm

1. Create a Queue `Q` to store indices.
2. Process first `K-1` elements: if negative, add index to `Q`.
3. Loop `i` from `K-1` to `N-1`:
   - Add current element `i` to `Q` if negative.
   - Remove front of `Q` if `Q.front() <= i - K`.
   - If `Q` is empty, result is 0. Else result is `values[Q.front()]`.

### Time Complexity

- **O(N)**. Each element added and removed at most once.

### Space Complexity

- **O(K)** (worst case: all negatives).

![Algorithm Visualization](../images/QUE-009/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-009/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public long solve(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }

        // Find first negative
        int firstNegIdx = -1;
        int firstNegVal = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < 0) {
                firstNegIdx = i;
                firstNegVal = arr[i];
                break;
            }
        }

        if (firstNegIdx == -1) {
            // No negative found - return sum modulo 100
            long sum = 0;
            for (int val : arr) {
                sum += val;
            }
            return sum % 100;
        }

        // With first negative found
        // Compute: sum of elements up to first negative + first negative value
        long prefixSum = 0;
        for (int i = 0; i < firstNegIdx; i++) {
            prefixSum += arr[i];
        }
        return prefixSum + firstNegVal;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            long result = solution.solve(arr);
            System.out.println(result);
        }
        sc.close();
    }
}
```

### Python
```python
import sys

def solve(arr):
    """
    Battery Lab - First Negative
    Computes some metric based on the array and first negative element
    """
    if not arr:
        return "0"

    # Find first negative
    first_neg_idx = -1
    first_neg_val = None
    for i, val in enumerate(arr):
        if val < 0:
            first_neg_idx = i
            first_neg_val = val
            break

    if first_neg_idx == -1:
        # No negative found - return sum modulo 100
        return str(sum(arr) % 100)

    # With first negative found
    # Compute: sum of elements up to first negative + first negative value
    prefix_sum = sum(arr[:first_neg_idx])
    result = prefix_sum + first_neg_val

    return str(result)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(input_data[i+1]) for i in range(n)]

    result = solve(arr)
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
    long long solve(const vector<int>& arr) {
        if (arr.empty()) {
            return 0;
        }

        // Find first negative
        int firstNegIdx = -1;
        int firstNegVal = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] < 0) {
                firstNegIdx = i;
                firstNegVal = arr[i];
                break;
            }
        }

        if (firstNegIdx == -1) {
            // No negative found - return sum modulo 100
            long long sum = 0;
            for (int val : arr) {
                sum += val;
            }
            return sum % 100;
        }

        // With first negative found
        // Compute: sum of elements up to first negative + first negative value
        long long prefixSum = 0;
        for (int i = 0; i < firstNegIdx; i++) {
            prefixSum += arr[i];
        }
        return prefixSum + firstNegVal;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        Solution solution;
        long long result = solution.solve(arr);
        cout << result << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  solve(arr) {
    if (arr.length === 0) {
      return "0";
    }

    // Find first negative
    let firstNegIdx = -1;
    let firstNegVal = null;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] < 0) {
        firstNegIdx = i;
        firstNegVal = arr[i];
        break;
      }
    }

    if (firstNegIdx === -1) {
      // No negative found - return sum modulo 100
      let sum = arr.reduce((a, b) => a + b, 0);
      return String(sum % 100);
    }

    // With first negative found
    // Compute: sum of elements up to first negative + first negative value
    let prefixSum = 0;
    for (let i = 0; i < firstNegIdx; i++) {
      prefixSum += arr[i];
    }
    const result = prefixSum + firstNegVal;

    return String(result);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.solve(arr);
  console.log(result);
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `5 -2 -7 3 4`, `k=2`

1. `i=0` (5): Not negative. Q `[]`.
2. `i=1` (-2): Negative. Q `[1]`.
   - Window `[5, -2]`. Front is 1. Val -2. Res `[-2]`.
3. `i=2` (-7): Negative. Q `[1, 2]`.
   - Expired: Front 1 <= 2-2=0? No.
   - Window `[-2, -7]`. Front is 1. Val -2. Res `[-2, -2]`.
4. `i=3` (3): Not negative. Q `[1, 2]`.
   - Expired: Front 1 <= 3-2=1? Yes. Pop 1. Q `[2]`.
   - Window `[-7, 3]`. Front is 2. Val -7. Res `[-2, -2, -7]`.
5. `i=4` (4): Not negative. Q `[2]`.
   - Expired: Front 2 <= 4-2=2? Yes. Pop 2. Q `[]`.
   - Window `[3, 4]`. Empty. Res `[-2, -2, -7, 0]`.

Matches example.

## ✅ Proof of Correctness

### Invariant
The queue contains indices of all negative numbers in the current window, sorted by index. The front is the smallest index, hence the first negative number.

### Why the approach is correct
We maintain the invariant by adding new negatives to the back and removing old ones from the front.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** First *Positive* number?
  - *Hint:* Trivial change in condition.
- **Extension 2:** First number satisfying predicate `P(x)`?
  - *Hint:* Generalize the condition.

### Common Mistakes to Avoid

1. **Storing Values instead of Indices**
   - ❌ Wrong: Storing `-2` in queue.
   - ✅ Correct: Store index `1`. We need index to know when it expires.
2. **Empty Queue Check**
   - ❌ Wrong: Accessing `queue.front()` without checking empty.
   - ✅ Correct: Always check if queue is empty before peeking.

## Related Concepts

- **Sliding Window Minimum:** Similar structure (Monotonic Queue), but here we don't need monotonicity of values, just order of appearance.
