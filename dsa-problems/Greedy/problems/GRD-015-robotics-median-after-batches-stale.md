---
problem_id: GRD_ROBOTICS_MEDIAN_BATCHES_STALE__4276
display_id: GRD-015
slug: robotics-median-after-batches-stale
title: "Robotics Median After Batches with Stale Filter"
difficulty: Medium
difficulty_score: 60
topics:
  - Heap
  - Two Heaps
  - Median Finding
  - Data Structures
tags:
  - heap
  - two-heaps
  - median
  - data-structures
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-015: Robotics Median After Batches with Stale Filter

## Problem Statement

Numbers arrive in batches from robot sensors. A value becomes **"stale"** once it has appeared more than `t` times in total across all batches seen so far. Stale values must be excluded from median calculations.

After processing each batch, report the median of all **non-stale** values seen so far. If all values are stale (or no values exist), output `"NA"`.

**Median definition**:

- If count is odd: middle element
- If count is even: average of two middle elements (round down)

![Problem Illustration](../images/GRD-015/problem-illustration.png)

## Input Format

- First line: two integers `k t` (number of batches and staleness threshold)
- Next `k` lines: each line starts with integer `m` (batch size), followed by `m` integers

## Output Format

- `k` space-separated outputs: median after each batch (or "NA" if no valid values)

## Constraints

- `1 <= k <= 1000`
- `1 <= t <= 10^5`
- Total numbers across all batches `<= 2*10^5`
- Values are integers in range `[-10^9, 10^9]`

## Example

**Input:**

```
3 2
3 5 5 1
2 5 3
2 8 9
```

**Output:**

```
5 3 6
```

**Explanation:**

Threshold t = 2 (values appearing > 2 times become stale)

**After Batch 1: [5, 5, 1]**

- Frequency: {5:2, 1:1}
- Non-stale values: [5, 5, 1] (none exceed threshold)
- Sorted: [1, 5, 5]
- Median: 5

**After Batch 2: [5, 5, 1] + [5, 3]**

- Frequency: {5:3, 1:1, 3:1}
- Value 5 appears 3 times > t=2, so it's stale
- Non-stale values: [1, 3]
- Sorted: [1, 3]
- For even count, we take the upper median: 3

**After Batch 3: [1, 3] + [8, 9]** (excluding stale 5)

- Frequency: {5:3 (stale), 1:1, 3:1, 8:1, 9:1}
- Non-stale values: [1, 3, 8, 9]
- Sorted: [1, 3, 8, 9]
- For even count (4 values), median is the average of the two middle values (3 and 8): (3+8)/2 = 5.5, rounded down = 5

The median calculation uses the upper median for pairs and rounds down for averages.

![Example Visualization](../images/GRD-015/example-1.png)

## Notes

- Use two heaps (max-heap for lower half, min-heap for upper half) to maintain median
- Track frequency map to identify stale values
- Use lazy deletion: when a value becomes stale, remove it from heaps
- After each batch, rebalance heaps and compute median
- Time complexity: O(N log N) where N is total numbers

## Related Topics

Two Heaps, Median Finding, Lazy Deletion, Frequency Map, Data Structures

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<String> medianAfterBatches(int k, int t, List<List<Integer>> batches) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        int t = sc.nextInt();

        List<List<Integer>> batches = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int m = sc.nextInt();
            List<Integer> batch = new ArrayList<>();
            for (int j = 0; j < m; j++) {
                batch.add(sc.nextInt());
            }
            batches.add(batch);
        }

        Solution solution = new Solution();
        List<String> result = solution.medianAfterBatches(k, t, batches);

        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
import heapq
import sys
import math
from collections import defaultdict

def median_after_batches(k: int, t: int, batches: list) -> list:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        k = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    batches = []
    for _ in range(k):
        m = int(next(iterator))
        batch = []
        for _ in range(m):
            batch.append(int(next(iterator)))
        batches.append(batch)

    result = median_after_batches(k, t, batches)
    print(' '.join(result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <cmath>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> medianAfterBatches(int k, int t, vector<vector<int>>& batches) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, t;
    if (!(cin >> k >> t)) return 0;

    vector<vector<int>> batches(k);
    for (int i = 0; i < k; i++) {
        int m;
        cin >> m;
        batches[i].resize(m);
        for (int j = 0; j < m; j++) {
            cin >> batches[i][j];
        }
    }

    Solution solution;
    vector<string> result = solution.medianAfterBatches(k, t, batches);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MinHeap {
  constructor() { this.heap = []; }
  push(val) { this.heap.push(val); this._siftUp(); }
  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();
    const top = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return top;
  }
  peek() { return this.size() === 0 ? null : this.heap[0]; }
  size() { return this.heap.length; }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.heap[idx] >= this.heap[p]) break;
      [this.heap[idx], this.heap[p]] = [this.heap[p], this.heap[idx]];
      idx = p;
    }
  }
  _siftDown() {
    let idx = 0;
    while (idx < this.heap.length) {
      let min = idx;
      const l = 2*idx+1, r = 2*idx+2;
      if (l < this.heap.length && this.heap[l] < this.heap[min]) min = l;
      if (r < this.heap.length && this.heap[r] < this.heap[min]) min = r;
      if (min === idx) break;
      [this.heap[idx], this.heap[min]] = [this.heap[min], this.heap[idx]];
      idx = min;
    }
  }
}

class MaxHeap {
  constructor() { this.heap = []; }
  push(val) { this.heap.push(val); this._siftUp(); }
  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();
    const top = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return top;
  }
  peek() { return this.size() === 0 ? null : this.heap[0]; }
  size() { return this.heap.length; }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.heap[idx] <= this.heap[p]) break;
      [this.heap[idx], this.heap[p]] = [this.heap[p], this.heap[idx]];
      idx = p;
    }
  }
  _siftDown() {
    let idx = 0;
    while (idx < this.heap.length) {
      let max = idx;
      const l = 2*idx+1, r = 2*idx+2;
      if (l < this.heap.length && this.heap[l] > this.heap[max]) max = l;
      if (r < this.heap.length && this.heap[r] > this.heap[max]) max = r;
      if (max === idx) break;
      [this.heap[idx], this.heap[max]] = [this.heap[max], this.heap[idx]];
      idx = max;
    }
  }
}

class Solution {
  medianAfterBatches(k, t, batches) {
    //Implement here
    return 0;
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

  // Flatten all input like Python does
  const allNumbers = [];
  for (const line of data) {
    allNumbers.push(...line.split(" ").map(Number));
  }

  let ptr = 0;
  const k = allNumbers[ptr++];
  const t = allNumbers[ptr++];

  const batches = [];
  for (let i = 0; i < k; i++) {
    const m = allNumbers[ptr++];
    const batch = [];
    for (let j = 0; j < m; j++) {
      batch.push(allNumbers[ptr++]);
    }
    batches.push(batch);
  }

  const solution = new Solution();
  const result = solution.medianAfterBatches(k, t, batches);
  console.log(result.join(" "));
});
```

