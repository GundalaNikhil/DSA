---
problem_id: ARR_PREFIX_AVG__4252
display_id: ARR-001
slug: snack-restock-snapshot
title: "Snack Restock Snapshot"
difficulty: Easy
difficulty_score: 18
topics:
  - Arrays
  - Prefix Sum
  - Math
tags:
  - arrays
  - prefix-sum
  - math
  - easy
premium: true
subscription_tier: basic
---

# ARR-001: Snack Restock Snapshot

## 📋 Problem Summary

Given an array representing daily inventory values, compute the prefix average (rounded down) for each position.

## 🌍 Real-World Scenario

**Scenario Title:** Campus Snack Shop Manager

Imagine you manage a college snack shop. Every evening, you count the inventory:

- Day 1: 4 items
- Day 2: 6 items
- Day 3: 6 items
- Day 4: 0 items (forgot to restock!)

Your boss asks: "What's been the **average inventory** from opening day until each day?"

This is exactly what prefix averages solve! It helps identify trends:

- Is inventory improving or declining?
- Do we need to order more frequently?
- Are we maintaining sufficient stock?

**Why This Problem Matters:**

- **Data Analysis**: Prefix averages smooth out daily fluctuations to show long-term trends.
- **Resource Planning**: Helps in deciding when to restock based on average consumption.
- **Performance Monitoring**: Used in systems to track average response times over a session.

![Real-World Application](../images/ARR-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Prefix Average Concept
```
Day:    0     1     2     3
Items: [4]   [6]   [6]   [0]
        |     |     |     |
        v     v     v     v
Sums:   4    10    16    16
        |     |     |     |
       ÷1    ÷2    ÷3    ÷4
        |     |     |     |
        v     v     v     v
Avgs:   4     5     5     4

Legend:
[ ] = daily items
 |  = flow of data
 v  = calculation step
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Rounding**: You must use **floor** division (integer division). `7 / 2 = 3`, not `3.5`.
- **Data Types**: The sum of elements can grow large. Even if individual elements fit in `int`, the sum might overflow `int`. Use `long` (Java/C++) or Python's arbitrary precision integers.
- **Constraints**: `n` up to 100,000 means an O(n^2) solution will time out. You need O(n).

Common interpretation mistake:

- ❌ Calculating the average of the *current* window of size k.
- ✅ Calculating the average of *everything* from index 0 to current index i.

### Core Concept: Running Sum

The fundamental approach is to maintain a cumulative sum as we iterate through the array. This avoids re-adding elements we've already seen.

### Why Naive Approach is too slow

Recalculating the sum from index 0 every single time involves a nested loop structure.
- Summing `i` elements takes `i` steps.
- Doing this for `n` elements takes `1 + 2 + ... + n` steps.
This is O(n^2). For n = 100,000, n^2 = 10,000,000,000 operations, which far exceeds the typical 10^8 operations per second limit.

## Naive Approach

### Intuition

For each day `i`, just loop from the start (day 0) to day `i`, sum up the numbers, and divide by `i + 1`.

### Algorithm

1. Loop `i` from 0 to `n-1`.
2. Inside, initialize `current_sum = 0`.
3. Loop `j` from 0 to `i`.
4. Add `arr[j]` to `current_sum`.
5. Calculate average and store it.

### Time Complexity

- **O(n²)**: The nested loops sum up to n(n+1)/2 operations.

### Space Complexity

- **O(1)**: No extra space used besides the input and output.

### Why This Works

It correctly implements the definition of prefix average by summing from scratch each time.

### Limitations

- **Too Slow**: Will Time Limit Exceed (TLE) for large inputs (n > 5000).

## Optimal Approach

### Key Insight

Notice that `Sum(0 to i) = Sum(0 to i-1) + arr[i]`.
We don't need to sum from 0 again! We can just add the new element to the sum we already have.

### Algorithm

1. Initialize `running_sum = 0`.
2. Create an empty `result` array.
3. Iterate `i` from 0 to `n-1`.
4. Update `running_sum += arr[i]`.
5. Calculate `average = running_sum / (i + 1)` (using integer division).
6. Append `average` to `result`.

### Time Complexity

- **O(n)**: We perform constant time operations (addition, division) for each of the `n` elements.

### Space Complexity

- **O(1)**: We only store `running_sum`, which takes constant extra space (ignoring the output array).

### Why This Is Optimal

We touch every element exactly once. It's impossible to do better than O(n) because we must read the input and write the output.

![Algorithm Visualization](../images/ARR-001/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-001/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] prefixAverages(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        long sum = 0;  // Use long to prevent overflow

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            result[i] = (int)(sum / (i + 1));  // Integer division
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.prefixAverages(arr);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
```

### Python

```python
import sys

def prefix_averages(arr: list[int]) -> list[int]:
    """
    Calculate prefix averages for each position.
    """
    n = len(arr)
    result = []
    running_sum = 0

    for i in range(n):
        running_sum += arr[i]
        # Integer division //
        result.append(running_sum // (i + 1))

    return result

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    arr = [int(x) for x in data[1:]]

    result = prefix_averages(arr)
    print(" ".join(map(str, result)))

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
    vector<int> prefixAverages(vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n);
        long long sum = 0;  // Use long long to prevent overflow

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            result[i] = sum / (i + 1);  // Integer division by default
        }

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    vector<int> result = solution.prefixAverages(arr);
    
    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  prefixAverages(arr) {
    const n = arr.length;
    const result = new Array(n);
    let sum = 0;

    for (let i = 0; i < n; i++) {
      sum += arr[i];
      // Math.floor for integer division
      result[i] = Math.floor(sum / (i + 1));
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
  
  // Flatten data in case multiple lines
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(Number(tokens[ptr++]));
  }

  const solution = new Solution();
  const result = solution.prefixAverages(arr);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Use the sample:

- Input: `[4, 6, 6, 0]`
- n = 4

We maintain:

- `runningSum`: holds sum of elements seen so far
- `result`: array to store averages

Initialize:

- `runningSum = 0`
- `result = []`

Now iterate:

| Step (i) | Value (`arr[i]`) | Running Sum (`prev + val`) | Calculation | Stored |
| ---: | :----: | -----: | ----------- | -----: |
|    0 | 4  |  0 + 4 = 4 | 4 / 1 = 4 | 4 |
|    1 | 6  |  4 + 6 = 10 | 10 / 2 = 5 | 5 |
|    2 | 6  |  10 + 6 = 16 | 16 / 3 = 5.33.. | 5 |
|    3 | 0  |  16 + 0 = 16 | 16 / 4 = 4 | 4 |

Answer is `[4, 5, 5, 4]`.

![Example Visualization](../images/ARR-001/example-1.png)

## ✅ Proof of Correctness

### Invariant

At the end of iteration `i`, `runningSum` correctly contains the sum of `arr[0]...arr[i]`.

### Why the approach is correct

Base case: At `i=0`, `runningSum` adds `arr[0]`, which is correct.
Inductive step: Assume `runningSum` is correct for `i-1`. In step `i`, we add `arr[i]`. Thus `runningSum` becomes sum of `0...i-1` plus `arr[i]`, which is exactly sum of `0...i`.
The division `runningSum / (i+1)` therefore correctly computes the average of the first `i+1` elements.

## 💡 Interview Extensions (High-Value Add-ons)

- **Streaming Input:** How would you handle it if numbers come one by one and you need to print the average immediately? (A: Same approach, maintain sum and count).
- **Floating Point:** What if we needed precise averages? (A: Use double/float, be careful of precision).
- **Sliding Window:** What if we need average of *last k* elements? (A: Use sliding window approach, maintain sum of last k).

## Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Using `int` for sum when `n * max_val` exceeds 2^31-1.
   - ✅ Use `long` (Java/C++) or Python.

2. **Division Type**
   - ❌ Using floating point division or not flooring results.
   - ✅ Use integer division (`//` in Python, `/` in Java/C++ for integers).

3. **Off-by-One Error**
   - ❌ Dividing by `i` instead of `i+1`.
   - ✅ Remember indices are 0-based, count is `i+1`.

4. **Recalculating Sum**
   - ❌ Summing from 0 every time (O(n^2)).
   - ✅ Maintaining a running sum (O(n)).

5. **Wrong Output Format**
   - ❌ Printing floating point numbers.
   - ✅ Printing integers.

## Related Concepts

- **Prefix Sum**: This is a direct application of prefix sums.
- **Running Average**: A statistical concept used in time series.
- **Sliding Window**: Related technique for fixed-size windows.
