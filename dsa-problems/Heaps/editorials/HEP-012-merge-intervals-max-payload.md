---
problem_id: HEP_MERGE_INTERVALS_MAX_PAYLOAD__6043
display_id: HEP-012
slug: merge-intervals-max-payload
title: "Merge Intervals With Max Payload"
difficulty: Medium
difficulty_score: 48
topics:
  - Heaps
  - Intervals
  - Sorting
tags:
  - heaps
  - intervals
  - sorting
  - medium
premium: true
subscription_tier: basic
---

# HEP-012: Merge Intervals With Max Payload

## 📋 Problem Summary

You have `n` intervals `[start, end]` with a `payload`.
Merge overlapping intervals into one.
The new interval spans from the minimum start to the maximum end of the overlapping group.
The new payload is the **maximum** payload of any interval in the group.
Return the merged intervals sorted by start time.

## 🌍 Real-World Scenario

**Scenario Title:** Cargo Shipment Consolidation

A logistics company receives shipment requests.
- Each request occupies a time slot `[start, end]` on the loading dock.
- Each shipment has a "priority" or "value" (payload).
- If shipments overlap in time, they must be processed together as a single batch.
- The "value" of the batch is determined by the highest-value item in it (e.g., for insurance or security level).
- You need to output the schedule of batches and their required security levels.

![Real-World Application](../images/HEP-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Merging Process

Intervals:
A: `[1, 3]`, P=5
B: `[2, 4]`, P=7
C: `[5, 6]`, P=2

Sorted by Start: A, B, C.

1. Process A `[1, 3]`, P=5. Current merged: `[1, 3]`, MaxP=5.
2. Process B `[2, 4]`, P=7.
   - Overlap? Yes (`2 <= 3`).
   - Merge: New End = `max(3, 4) = 4`. New MaxP = `max(5, 7) = 7`.
   - Current merged: `[1, 4]`, MaxP=7.
3. Process C `[5, 6]`, P=2.
   - Overlap? No (`5 > 4`).
   - Push `[1, 4, 7]`.
   - Start new merged: `[5, 6]`, MaxP=2.

Result: `[1, 4, 7]`, `[5, 6, 2]`.

### Key Concept: Sorting + Linear Scan

This is a classic "Merge Intervals" problem with a twist (payload).
1. **Sort** intervals by `start` time.
2. Iterate through sorted intervals.
3. Maintain a `current` interval `[currStart, currEnd]` and `currPayload`.
4. For next interval `next`:
   - If `next.start <= currEnd`: **Overlap**.
     - `currEnd = max(currEnd, next.end)`.
     - `currPayload = max(currPayload, next.payload)`.
   - Else: **No Overlap**.
     - Add `current` to results.
     - Update `current = next`.

### Why Heaps?

The problem is tagged "Heaps", but sorting is sufficient (`O(N log N)`).
A heap can be used to sort (`O(N log N)`), or to merge k sorted lists of intervals.
Given the constraints and problem type, standard sorting is the optimal approach.
However, if the intervals were arriving in a stream, a Heap/BST would be needed (Interval Tree).
Here, we stick to the sorting approach as it's standard for static input.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n`, list of `[start, end, payload]`.
- **Output:** Count `m`, list of merged intervals.
- **Constraints:** `N <= 10^5`. Coordinates up to `10^9`.
- **Overlap:** `[1, 2]` and `[2, 3]` overlap at 2. Merge them.

## Naive Approach

### Intuition

Compare every pair. Merge. Repeat until no overlaps.

### Time Complexity

- **O(N^2)**: Too slow.

## Optimal Approach

### Key Insight

Sorting by start time brings potentially overlapping intervals next to each other.

### Algorithm

1. Sort intervals by `start` ascending.
2. Initialize `results` list.
3. If empty, return empty.
4. `curr = intervals[0]`.
5. Loop `i` from 1 to `n-1`:
   - `next = intervals[i]`.
   - If `next.start <= curr.end`:
     - `curr.end = max(curr.end, next.end)`.
     - `curr.payload = max(curr.payload, next.payload)`.
   - Else:
     - Add `curr` to `results`.
     - `curr = next`.
6. Add final `curr` to `results`.
7. Return `results`.

### Time Complexity

- **O(N log N)** due to sorting.

### Space Complexity

- **O(N)** for sorting/output.

![Algorithm Visualization](../images/HEP-012/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[][] mergeIntervals(int[][] intervals) {
        if (intervals.length == 0) return new int[0][0];
        
        // Sort by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];
        
        for (int i = 1; i < intervals.length; i++) {
            int[] next = intervals[i];
            
            // Check overlap
            if (next[0] <= current[1]) {
                // Merge
                current[1] = Math.max(current[1], next[1]);
                current[2] = Math.max(current[2], next[2]);
            } else {
                // No overlap, push current and start new
                merged.add(current);
                current = next;
            }
        }
        merged.add(current);
        
        return merged.toArray(new int[merged.size()][]);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[][] intervals = new int[n][3];
            for (int i = 0; i < n; i++) {
                intervals[i][0] = sc.nextInt();
                intervals[i][1] = sc.nextInt();
                intervals[i][2] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            int[][] result = solution.mergeIntervals(intervals);
            System.out.println(result.length);
            for (int[] row : result) {
                System.out.println(row[0] + " " + row[1] + " " + row[2]);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def merge_intervals(self, intervals: list) -> list:
        if not intervals:
            return []
            
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        current = intervals[0]
        
        for i in range(1, len(intervals)):
            next_int = intervals[i]
            
            if next_int[0] <= current[1]:
                # Merge
                current[1] = max(current[1], next_int[1])
                current[2] = max(current[2], next_int[2])
            else:
                merged.append(current)
                current = next_int
                
        merged.append(current)
        return merged

def merge_intervals(intervals: list) -> list:
    solver = Solution()
    return solver.merge_intervals(intervals)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        intervals = []
        for _ in range(n):
            start = int(next(it))
            end = int(next(it))
            payload = int(next(it))
            intervals.append([start, end, payload])
            
        result = merge_intervals(intervals)
        print(len(result))
        for row in result:
            print(f"{row[0]} {row[1]} {row[2]}")
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
    vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        
        // Sort by start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<vector<int>> merged;
        vector<int> current = intervals[0];
        
        for (size_t i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] <= current[1]) {
                current[1] = max(current[1], intervals[i][1]);
                current[2] = max(current[2], intervals[i][2]);
            } else {
                merged.push_back(current);
                current = intervals[i];
            }
        }
        merged.push_back(current);
        
        return merged;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<vector<int>> intervals(n, vector<int>(3));
        for (int i = 0; i < n; i++) {
            cin >> intervals[i][0] >> intervals[i][1] >> intervals[i][2];
        }
        
        Solution solution;
        vector<vector<int>> result = solution.mergeIntervals(intervals);
        cout << result.size() << "\n";
        for (const auto& row : result) {
            cout << row[0] << " " << row[1] << " " << row[2] << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mergeIntervals(intervals) {
    if (intervals.length === 0) return [];
    
    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);
    
    const merged = [];
    let current = intervals[0];
    
    for (let i = 1; i < intervals.length; i++) {
      const next = intervals[i];
      
      if (next[0] <= current[1]) {
        current[1] = Math.max(current[1], next[1]);
        current[2] = Math.max(current[2], next[2]);
      } else {
        merged.push(current);
        current = next;
      }
    }
    merged.push(current);
    
    return merged;
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
  const intervals = [];
  for (let i = 0; i < n; i++) {
    const start = parseInt(data[idx++]);
    const end = parseInt(data[idx++]);
    const payload = parseInt(data[idx++]);
    intervals.push([start, end, payload]);
  }
  
  const solution = new Solution();
  const result = solution.mergeIntervals(intervals);
  console.log(result.length);
  for (const row of result) {
    console.log(row[0] + " " + row[1] + " " + row[2]);
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `2`. `[1, 3, 5]`, `[2, 4, 7]`.
1. Sort: `[1, 3, 5]`, `[2, 4, 7]`.
2. `curr = [1, 3, 5]`.
3. `next = [2, 4, 7]`.
   - `2 <= 3`. Overlap.
   - `curr[1] = max(3, 4) = 4`.
   - `curr[2] = max(5, 7) = 7`.
   - `curr` is now `[1, 4, 7]`.
4. End loop. Push `[1, 4, 7]`.
5. Output: `1`, `1 4 7`.

## ✅ Proof of Correctness

### Invariant
- `current` always represents the merged interval of all processed overlapping intervals so far.
- Sorting ensures we encounter intervals in the order they start, so we only need to check overlap with the immediately preceding merged interval.

## 💡 Interview Extensions

- **Extension 1:** Sum of payloads instead of max?
  - *Answer:* `curr[2] += next[2]`.
- **Extension 2:** Stream of intervals?
  - *Answer:* Use Interval Tree or TreeMap to merge dynamically (`O(log N)`).

### Common Mistakes to Avoid

1. **Unsorted Input**
   - ❌ Wrong: Assuming input is sorted.
   - ✅ Correct: Always sort first.
2. **Edge Cases**
   - ❌ Wrong: `next.start < curr.end` (strict inequality).
   - ✅ Correct: `next.start <= curr.end` (touching intervals merge).

## Related Concepts

- **Sweep Line:** General technique for interval problems.
- **Union-Find:** Can also be used but overkill.
