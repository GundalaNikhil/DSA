---
problem_id: ARR_DIFF_ARRAY__53AA
display_id: ARR-004
slug: lab-temperature-ranges
title: "Lab Temperature Offline Ranges"
difficulty: Medium
difficulty_score: 50
topics:
  - Array
  - Difference Array
  - Range Queries
tags:
  - arrays
  - difference-array
  - range-queries
  - medium
premium: true
subscription_tier: basic
---

# Lab Temperature Offline Ranges

![Problem Header](../images/ARR-004/header.png)

---

## Problem Summary

Process range addition queries and sum queries on an array efficiently.

---

## 🌍 Real-World Scenario

**Laboratory Temperature Control System**

Imagine you're managing a research laboratory with temperature sensors across different zones. The lab has specific temperature requirements for experiments:

- **Temperature Array**: Current temperatures [20°C, 22°C, 21°C, 23°C, 20°C]
- **Adjustment Queries**: Scientists request heating/cooling adjustments for specific zones
- **Monitoring Queries**: System needs to report total temperature across zones

**Example Operations**:

```
Initial temps: [20, 22, 21, 23, 20]

Query 1: "Increase zones 0-2 by +3°C" (heating for chemical reaction)
Query 2: "Decrease zones 3-4 by -2°C" (cooling for storage)
Query 3: "What's total temperature in zones 1-4?"

Naive approach: Apply each adjustment individually (SLOW!)
Optimal approach: Use difference array technique (FAST!)
```

**Why This Matters**:

- **HVAC Systems**: Adjust temperature ranges across building zones
- **IoT Sensor Networks**: Batch updates to sensor calibration values
- **Cloud Resource Allocation**: Adjust compute resources across server ranges
- **Financial Systems**: Apply interest rate changes to account ranges
- **Game Development**: Area-effect damage or buffs in grid-based games

**Key Insight**: When you have many range updates followed by queries, applying updates individually is wasteful. The **difference array** technique marks boundaries in O(1) and reconstructs the array once!

---

## Approach 1: Naive Solution

### Idea

For each "add" query, iterate through the range and update each element individually. For "sum" queries, iterate and sum.

### Complexity Analysis

**Time Complexity**: O(Q × n) where Q is number of queries

- Each "add" query: O(n) in worst case
- Each "sum" query: O(n) in worst case

**Space Complexity**: O(1) excluding output

---

## Approach 2: Optimal Solution ⭐

### Key Insight

Use **difference array technique**. For range updates, only mark endpoints instead of updating every element. Apply all updates at once when needed.

### What is a Difference Array?

A difference array stores the change at each position rather than the actual values:

- `diff[i]` = change that starts at position i
- To get actual value: compute prefix sum of difference array

### Algorithm

1. Create a difference array initialized to 0
2. For each "add" query [L, R, val]:
   - `diff[L] += val` (start of range)
   - `diff[R+1] -= val` (end of range, if R+1 < n)
3. Before processing sum queries, apply difference array:
   - Convert diff to actual values with prefix sum
   - Add to original temperatures
4. For "sum" query [L, R]:
   - Compute sum of range [L, R]

### Complexity Analysis

**Time Complexity**: O(n + Q)

- Each "add" query: O(1) - just update two positions
- Each "sum" query: O(n) for applying pending updates + O(R-L) for sum
- Total: O(n + Q)

**Space Complexity**: O(n)

- Difference array

---

## Visual Representation

### Example: Array = [0, 0, 0, 0, 0]

```
Initial: [0, 0, 0, 0, 0]

Query 1: add(1, 3, 5)
Difference array:
Index:  0  1  2  3  4  5
Diff:   0  5  0  0 -5  0
        ↑  ↑        ↑
       no +5      -5 (end+1)

Query 2: add(2, 4, 3)
Difference array:
Index:  0  1  2  3  4  5
Diff:   0  5  3  0 -5 -3
           ↑  ↑       ↑
         old +3     -3 (end+1)

Apply difference (prefix sum):
Index:  0  1  2  3  4
Value:  0  5  8  8  3

Explanation:
- Position 0: 0
- Position 1: 0+5 = 5
- Position 2: 5+3 = 8
- Position 3: 8+0 = 8
- Position 4: 8-5 = 3
```

---

## Detailed Example Walkthrough

### Initial: `temps = [10, 20, 30, 40, 50]`

**Query 1: add(1, 3, 5)**

```
Difference: [0, 5, 0, 0, -5, 0]
Applied: [10, 25, 35, 45, 50]
```

**Query 2: add(0, 2, 10)**

```
Difference: [10, 5, 0, -10, -5, 0]
Applied: [20, 35, 45, 45, 50]
```

**Query 3: sum(1, 3)**

```
Apply pending updates first
Then compute: 35 + 45 + 45 = 125
```

---

## Implementations

### Java

```java
class Solution {
    public long[] processQueries(int[] temps, String[][] queries) {
        int n = temps.length;
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = temps[i];
        }

        long[] diff = new long[n + 1];
        List<Long> results = new ArrayList<>();

        for (String[] query : queries) {
            if (query[0].equals("add")) {
                int L = Integer.parseInt(query[1]);
                int R = Integer.parseInt(query[2]);
                int val = Integer.parseInt(query[3]);
                diff[L] += val;
                if (R + 1 < n) diff[R + 1] -= val;
            } else {
                // Apply all pending updates
                long current = 0;
                for (int i = 0; i < n; i++) {
                    current += diff[i];
                    arr[i] += current;
                    diff[i] = 0;
                }
                if (n < diff.length) diff[n] = 0;

                int L = Integer.parseInt(query[1]);
                int R = Integer.parseInt(query[2]);
                long sum = 0;
                for (int i = L; i <= R; i++) {
                    sum += arr[i];
                }
                results.add(sum);
            }
        }

        return results.stream().mapToLong(Long::longValue).toArray();
    }
}
```

### Python

```python
def process_queries(temps, queries):
    n = len(temps)
    arr = [float(x) for x in temps]
    diff = [0] * (n + 1)
    results = []

    for query in queries:
        if query[0] == "add":
            L, R, val = int(query[1]), int(query[2]), int(query[3])
            diff[L] += val
            if R + 1 < n:
                diff[R + 1] -= val
        else:
            # Apply all pending updates
            current = 0
            for i in range(n):
                current += diff[i]
                arr[i] += current
                diff[i] = 0
            diff[n] = 0

            L, R = int(query[1]), int(query[2])
            total = sum(arr[L:R+1])
            results.append(int(total))

    return results
```

### C++

```cpp
class Solution {
public:
    vector<long long> processQueries(vector<int>& temps, vector<vector<string>>& queries) {
        int n = temps.size();
        vector<long long> arr(n);
        for (int i = 0; i < n; i++) {
            arr[i] = temps[i];
        }

        vector<long long> diff(n + 1, 0);
        vector<long long> results;

        for (auto& query : queries) {
            if (query[0] == "add") {
                int L = stoi(query[1]);
                int R = stoi(query[2]);
                long long val = stoll(query[3]);
                diff[L] += val;
                if (R + 1 < n) diff[R + 1] -= val;
            } else {
                // Apply all pending updates
                long long current = 0;
                for (int i = 0; i < n; i++) {
                    current += diff[i];
                    arr[i] += current;
                    diff[i] = 0;
                }
                diff[n] = 0;

                int L = stoi(query[1]);
                int R = stoi(query[2]);
                long long sum = 0;
                for (int i = L; i <= R; i++) {
                    sum += arr[i];
                }
                results.push_back(sum);
            }
        }

        return results;
    }
};
```

### JavaScript

```javascript
/**
 * @param {number[]} temps
 * @param {string[][]} queries
 * @return {number[]}
 */
var processQueries = function(temps, queries) {
    const n = temps.length;
    const arr = temps.map(BigInt);
    const diff = new Array(n + 1).fill(0n);
    const results = [];

    for (const query of queries) {
        if (query[0] === "add") {
            const L = parseInt(query[1]);
            const R = parseInt(query[2]);
            const val = BigInt(query[3]);
            diff[L] += val;
            if (R + 1 < n) diff[R + 1] -= val;
        } else {
            // Apply all pending updates
            let current = 0n;
            for (let i = 0; i < n; i++) {
                current += diff[i];
                arr[i] += current;
                diff[i] = 0n;
            }
            if (n < diff.length) diff[n] = 0n;

            const L = parseInt(query[1]);
            const R = parseInt(query[2]);
            let sum = 0n;
            for (let i = L; i <= R; i++) {
                sum += arr[i];
            }
            results.push(Number(sum));
        }
    }

    return results;
};
```

---

### C++ommon Mistakes & Pitfalls

### 1. Forgetting R+1 Boundary Check ⚠️

- ❌ Always doing `diff[R+1] -= val` without checking bounds
- ✅ Check if `R+1 < n` before accessing

### 2. Not Resetting Difference Array ⚠️

- ❌ Applying difference array multiple times without resetting
- ✅ Reset diff array after applying changes

### 3. Integer Overflow ⚠️

- ❌ Using int for cumulative sums
- ✅ Use long/long long for sums

---

## Why Difference Array Works

The key insight: For a range update [L, R], instead of updating each element:

- Mark +val at position L (start of increase)
- Mark -val at position R+1 (end of increase)
- When computing prefix sum, the +val effect continues until we hit -val

---

## Related Problems

- Range Sum Query
- Range Update Query
- Lazy Propagation

## Tags

`#arrays` `#difference-array` `#range-queries` `#medium`
