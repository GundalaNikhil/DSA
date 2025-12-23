---
problem_id: HEP_MEDIAN_TWO_HEAPS_MERGE__4476
display_id: HEP-015
slug: median-two-heaps-merge
title: "Median of Two Heaps After Merge"
difficulty: Medium
difficulty_score: 50
topics:
  - Heaps
  - Median
  - Data Structures
tags:
  - heaps
  - median
  - merge
  - medium
premium: true
subscription_tier: basic
---

# HEP-015: Median of Two Heaps After Merge

## 📋 Problem Summary

You are given two arrays representing the contents of a Max-Heap and a Min-Heap.
Merge all elements into a single collection.
Find the median of the merged collection.
- If total size is odd, return the middle element.
- If total size is even, return the average of the two middle elements.

## 🌍 Real-World Scenario

**Scenario Title:** Merging Sensor Data Streams

Two sensors collect temperature data.
- Sensor A keeps track of the lower half of temperatures (Max-Heap logic).
- Sensor B keeps track of the upper half (Min-Heap logic).
- Due to a network partition, they operated independently and their sizes can be unbalanced.
- You need to merge their logs to find the true median temperature of the entire period.

![Real-World Application](../images/HEP-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Rebalancing

Input:
Max-Heap (A): `[10, 5, 3]` (Size 3)
Min-Heap (B): `[2, 8]` (Size 2)

Merged: `[2, 3, 5, 8, 10]`.
Median: 5.

Process:
1. Combine all elements: `10, 5, 3, 2, 8`.
2. Sort: `2, 3, 5, 8, 10`.
3. Pick middle.

### Key Concept: Two Heaps for Median

The standard "Find Median from Data Stream" uses two heaps:
- `Left` (Max-Heap): Stores smaller half.
- `Right` (Min-Heap): Stores larger half.
- Invariant: `Left.size() == Right.size()` or `Left.size() == Right.size() + 1`.
- Also: `Left.max() <= Right.min()`.

Here, we are given two arrays. We can treat them as raw data.
We simply need to build the Two-Heap structure from scratch using all elements.
Since we have all data at once, we can just sort everything?
Constraints: `N, M <= 200,000`.
Sorting takes `O((N+M) log (N+M))`. This is acceptable.
Is there a faster way using the heap property?
- The input arrays are "contents of a heap".
- A heap array is NOT sorted. It's just a valid heap.
- So we can't assume order.
- We must process all elements.
- Sorting is the most straightforward optimal solution.
- Can we do `O(N+M)`? (Selection algorithm).
- Yes, `QuickSelect` (or `std::nth_element`) can find the median in linear time.
- The problem is tagged "Heaps", so we can use the heap property or the Two-Heap pattern.
- But given the input is just "contents", and heap contents are not fully sorted, we effectively have unsorted arrays.
- So `QuickSelect` is `O(N+M)` average.
- Sorting is `O((N+M) log (N+M))`.
- Both are fine for `4 * 10^5`.
- We will implement the Sorting approach for simplicity and stability, or the Two-Heap rebalancing if we want to simulate the "Stream" aspect.
- Using Two Heaps explicitly:
  - Push all to `Left` (Max-Heap).
  - Move half to `Right` (Min-Heap).
  - Balance.
  - This is `O((N+M) log (N+M))` anyway.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Two arrays.
- **Output:** Float/Double.
- **Constraints:** Values can be negative.
- **Empty Input:** Handle `N=0, M=0`. (Though constraints say `N, M >= 0`, usually at least 1 element total for median).

## Naive Approach

### Intuition

Combine arrays, sort, pick middle.

### Time Complexity

- **O((N+M) log (N+M))**.

## Optimal Approach

### Key Insight

Since we need the exact median, and `N+M` fits in memory, sorting is efficient enough.
For interview bonus, mention `QuickSelect` (`O(N+M)`).

### Algorithm (Sorting)

1. Create a list `all_elements`.
2. Add elements from `maxHeap` and `minHeap`.
3. Sort `all_elements`.
4. If size `S` is odd: return `all_elements[S/2]`.
5. If size `S` is even: return `(all_elements[S/2 - 1] + all_elements[S/2]) / 2.0`.

### Algorithm (Two Heaps - Educational)

1. Create `left` (Max-Heap) and `right` (Min-Heap).
2. Insert all numbers into `left`.
3. Move half (`total/2`) elements from `left` to `right`.
   - Pop max from `left`, push to `right`.
4. Ensure balance:
   - If `left` has more than `right` + 1, move to `right`.
   - If `right` has more than `left`, move to `left`.
5. Calculate median from tops.

We will implement the **Sorting** approach as it is robust and standard for this problem size.

### Time Complexity

- **O(K log K)** where `K = N+M`.

### Space Complexity

- **O(K)**.

![Algorithm Visualization](../images/HEP-015/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double findMedian(int[] maxHeap, int[] minHeap) {
        int n = maxHeap.length;
        int m = minHeap.length;
        int[] all = new int[n + m];
        
        System.arraycopy(maxHeap, 0, all, 0, n);
        System.arraycopy(minHeap, 0, all, n, m);
        
        Arrays.sort(all);
        
        int total = n + m;
        if (total == 0) return 0.0;
        
        if (total % 2 == 1) {
            return (double) all[total / 2];
        } else {
            long sum = (long) all[total / 2 - 1] + all[total / 2];
            return sum / 2.0;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] maxHeap = new int[n];
            int[] minHeap = new int[m];
            for (int i = 0; i < n; i++) maxHeap[i] = sc.nextInt();
            for (int i = 0; i < m; i++) minHeap[i] = sc.nextInt();
            
            Solution solution = new Solution();
            System.out.println(solution.findMedian(maxHeap, minHeap));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_median(self, max_heap: list, min_heap: list) -> float:
        combined = max_heap + min_heap
        combined.sort()
        
        n = len(combined)
        if n == 0:
            return 0.0
            
        if n % 2 == 1:
            return float(combined[n // 2])
        else:
            mid1 = combined[n // 2 - 1]
            mid2 = combined[n // 2]
            return (mid1 + mid2) / 2.0

def find_median(max_heap: list, min_heap: list) -> float:
    solver = Solution()
    return solver.find_median(max_heap, min_heap)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        max_heap = []
        for _ in range(n):
            max_heap.append(int(next(it)))
        min_heap = []
        for _ in range(m):
            min_heap.append(int(next(it)))
            
        print(find_median(max_heap, min_heap))
    except StopIteration:
        pass

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
    double findMedian(const vector<int>& maxHeap, const vector<int>& minHeap) {
        vector<int> all;
        all.reserve(maxHeap.size() + minHeap.size());
        all.insert(all.end(), maxHeap.begin(), maxHeap.end());
        all.insert(all.end(), minHeap.begin(), minHeap.end());
        
        if (all.empty()) return 0.0;
        
        // Use nth_element for O(N) performance
        int n = all.size();
        if (n % 2 == 1) {
            auto mid = all.begin() + n / 2;
            nth_element(all.begin(), mid, all.end());
            return (double)*mid;
        } else {
            auto mid1 = all.begin() + n / 2 - 1;
            auto mid2 = all.begin() + n / 2;
            nth_element(all.begin(), mid2, all.end()); // Fixes mid2
            // Now find max of first half for mid1
            int val2 = *mid2;
            int val1 = *max_element(all.begin(), mid2);
            return (double)((long long)val1 + val2) / 2.0;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<int> maxHeap(n), minHeap(m);
        for (int i = 0; i < n; i++) cin >> maxHeap[i];
        for (int i = 0; i < m; i++) cin >> minHeap[i];
        
        Solution solution;
        cout << solution.findMedian(maxHeap, minHeap) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findMedian(maxHeap, minHeap) {
    const all = maxHeap.concat(minHeap);
    all.sort((a, b) => a - b);
    
    const n = all.length;
    if (n === 0) return 0.0;
    
    if (n % 2 === 1) {
      return all[Math.floor(n / 2)];
    } else {
      const mid1 = all[n / 2 - 1];
      const mid2 = all[n / 2];
      return (mid1 + mid2) / 2.0;
    }
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++]);
  const m = parseInt(data[idx++]);
  const maxHeap = [];
  const minHeap = [];
  for (let i = 0; i < n; i++) maxHeap.push(parseInt(data[idx++]));
  for (let i = 0; i < m; i++) minHeap.push(parseInt(data[idx++]));
  
  const solution = new Solution();
  console.log(solution.findMedian(maxHeap, minHeap));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `2 2`. `1 3`, `2 4`.
1. Combine: `[1, 3, 2, 4]`.
2. Sort: `[1, 2, 3, 4]`.
3. Size 4 (Even).
4. Mids: `2` and `3`.
5. Avg: `2.5`.

## ✅ Proof of Correctness

### Invariant
- The median of a set is independent of the initial structure (heaps).
- Sorting or QuickSelect correctly identifies the rank-based median.

## 💡 Interview Extensions

- **Extension 1:** What if arrays are sorted?
  - *Answer:* Use binary search (`O(log (min(N, M)))`).
- **Extension 2:** Stream?
  - *Answer:* Two Heaps (`O(log K)` per insert).

### Common Mistakes to Avoid

1. **Integer Division**
   - ❌ Wrong: `(mid1 + mid2) / 2`.
   - ✅ Correct: `(mid1 + mid2) / 2.0`.
2. **Overflow**
   - ❌ Wrong: `mid1 + mid2` can overflow int.
   - ✅ Correct: Cast to long/double before adding.

## Related Concepts

- **QuickSelect:** O(N) selection.
- **Merge Sort:** O(N log N).
