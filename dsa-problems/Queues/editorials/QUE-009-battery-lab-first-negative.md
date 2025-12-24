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
    public int[] firstNegatives(int[] values, int k) {
        int n = values.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> queue = new ArrayDeque<>(); // Stores indices
        
        int idx = 0;
        for (int i = 0; i < n; i++) {
            // Add new element if negative
            if (values[i] < 0) {
                queue.offerLast(i);
            }
            
            // Remove expired from front
            if (!queue.isEmpty() && queue.peekFirst() <= i - k) {
                queue.pollFirst();
            }
            
            // Record result if window is full size
            if (i >= k - 1) {
                if (queue.isEmpty()) {
                    result[idx++] = 0;
                } else {
                    result[idx++] = values[queue.peekFirst()];
                }
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            int[] result = solution.firstNegatives(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
from collections import deque
import sys

def first_negatives(values: List[int], k: int) -> List[int]:
    n = len(values)
    result = []
    queue = deque() # Stores indices
    
    for i in range(n):
        if values[i] < 0:
            queue.append(i)
            
        # Remove expired
        if queue and queue[0] <= i - k:
            queue.popleft()
            
        if i >= k - 1:
            if not queue:
                result.append(0)
            else:
                result.append(values[queue[0]])
                
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        
        result = first_negatives(values, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> firstNegatives(const vector<int>& values, int k) {
        int n = values.size();
        vector<int> result;
        deque<int> q; // Stores indices
        
        for (int i = 0; i < n; i++) {
            if (values[i] < 0) {
                q.push_back(i);
            }
            
            if (!q.empty() && q.front() <= i - k) {
                q.pop_front();
            }
            
            if (i >= k - 1) {
                if (q.empty()) {
                    result.push_back(0);
                } else {
                    result.push_back(values[q.front()]);
                }
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }
    
        Solution solution;
        vector<int> result = solution.firstNegatives(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  firstNegatives(values, k) {
    const result = [];
    // Using array as queue. For strict O(N), use pointer or linked list.
    // shift() is O(N) in worst case (queue size N).
    // But queue size is bounded by K. Total time O(N*K) worst case if using shift.
    // Let's use pointer for O(1) dequeue.
    
    const queue = []; // Stores indices
    let head = 0;
    
    for (let i = 0; i < values.length; i++) {
      if (values[i] < 0) {
        queue.push(i);
      }
      
      // Remove expired
      if (head < queue.length && queue[head] <= i - k) {
        head++;
      }
      
      if (i >= k - 1) {
        if (head >= queue.length) {
          result.push(0);
        } else {
          result.push(values[queue[head]]);
        }
      }
    }
    return result;
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
  const k = parseInt(data[idx++], 10);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.firstNegatives(values, k);
  console.log(result.join(" "));
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
