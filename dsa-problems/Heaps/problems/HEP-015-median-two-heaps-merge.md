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
time_limit: 2000
memory_limit: 256
---

# HEP-015: Median of Two Heaps After Merge

## Problem Statement

You are given the contents of a max-heap and a min-heap (as arrays). Treat them as two multisets. Compute the median of all elements after merging both sets.

If the total number of elements is odd, the median is the middle element. If it is even, the median is the average of the two middle elements.

![Problem Illustration](../images/HEP-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers (max-heap contents)
- Third line: `m` integers (min-heap contents)

## Output Format

- Single number: the median (use `.5` if needed)

## Constraints

- `0 <= n, m <= 200000`
- `-10^9 <= value <= 10^9`

## Example

**Input:**

```
2 2
1 3
2 4
```

**Output:**

```
2.5
```

**Explanation:**

Merged values are [1,2,3,4]. Median is (2 + 3) / 2 = 2.5.

![Example Visualization](../images/HEP-015/example-1.png)

## Notes

- Use two heaps to balance all elements
- Keep size difference at most 1
- Time complexity: O((n+m) log(n+m))
- Space complexity: O(n+m)

## Related Topics

Heaps, Median Maintenance, Data Structures

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double findMedian(int[] maxHeap, int[] minHeap) {
        // Implementation here
        return 0.0;
    }
}

class Main {
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
            double result = solution.findMedian(maxHeap, minHeap);
            if (result == (long) result) {
                System.out.println((long) result);
            } else {
                System.out.println(result);
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
    def find_median(self, max_heap: list, min_heap: list) -> float:
        # Implementation here
        return 0

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
        // Implementation here
        return {};
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
        double res = solution.findMedian(maxHeap, minHeap);
        if (res == (long long)res) {
            cout << (long long)res << "\n";
        } else {
            cout << res << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findMedian(maxHeap, minHeap) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});
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
