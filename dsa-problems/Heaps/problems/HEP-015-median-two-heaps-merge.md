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
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] maxHeap = new int[n];
        int[] minHeap = new int[m];
        for (int i = 0; i < n; i++) maxHeap[i] = sc.nextInt();
        for (int i = 0; i < m; i++) minHeap[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.findMedian(maxHeap, minHeap));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def find_median(max_heap: List[int], min_heap: List[int]) -> float:
    # Your implementation here
    return 0.0

def main():
    n, m = map(int, input().split())
    max_heap = list(map(int, input().split())) if n > 0 else []
    min_heap = list(map(int, input().split())) if m > 0 else []

    result = find_median(max_heap, min_heap)
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
    double findMedian(const vector<int>& maxHeap, const vector<int>& minHeap) {
        // Your implementation here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> maxHeap(n), minHeap(m);
    for (int i = 0; i < n; i++) cin >> maxHeap[i];
    for (int i = 0; i < m; i++) cin >> minHeap[i];

    Solution solution;
    cout << solution.findMedian(maxHeap, minHeap) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findMedian(maxHeap, minHeap) {
    // Your implementation here
    return 0.0;
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
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const maxHeap = [];
  const minHeap = [];
  for (let i = 0; i < n; i++) maxHeap.push(parseInt(data[idx++], 10));
  for (let i = 0; i < m; i++) minHeap.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  console.log(solution.findMedian(maxHeap, minHeap));
});
```
