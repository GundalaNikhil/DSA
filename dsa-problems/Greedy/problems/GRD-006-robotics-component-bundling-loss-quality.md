---
problem_id: GRD_ROBOTICS_COMPONENT_BUNDLING__7259
display_id: GRD-006
slug: robotics-component-bundling-loss-quality
title: "Robotics Component Bundling with Loss and Quality Score"
difficulty: Medium
difficulty_score: 60
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
  - Simulation
tags:
  - greedy
  - heap
  - priority-queue
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-006: Robotics Component Bundling with Loss and Quality Score

## Problem Statement

You have `n` robot parts, where each part `i` has:

- Weight `w[i]`
- Quality score `q[i]`

You can bundle two parts together using the following rules:

- **Weight calculation**: When bundling parts with weights `w_big` and `w_small` (where `w_big >= w_small`), the new weight is: `w_big + w_small - floor(0.1 × w_small)`
  - This represents a 10% material loss from the smaller part
- **Quality calculation**: When bundling parts with qualities `q[i]` and `q[j]`, the new quality is: `min(q[i], q[j]) - 1`
  - Quality degrades by 1 due to the bundling process

**Constraint**: All intermediate bundles must maintain quality >= T (threshold), otherwise they become unusable.

Your goal is to bundle all parts into a single component while maximizing the final weight. Return the maximum achievable weight, or `-1` if no valid bundling sequence exists.

![Problem Illustration](../images/GRD-006/problem-illustration.png)

## Input Format

- First line: two integers `n T` (number of parts and quality threshold)
- Second line: `n` space-separated integers representing weights `w[0], w[1], ..., w[n-1]`
- Third line: `n` space-separated integers representing qualities `q[0], q[1], ..., q[n-1]`

## Output Format

- Single integer: maximum final weight achievable, or `-1` if impossible

## Constraints

- `1 <= n <= 2*10^5`
- `1 <= w[i] <= 10^9`
- `1 <= q[i] <= 100`
- `1 <= T <= 100`

## Example

**Input:**

```
3 5
4 3 2
10 8 6
```

**Output:**

```
8
```

**Explanation:**

Parts: weights [4, 3, 2], qualities [10, 8, 6]
Threshold: T = 5

Valid bundling sequence:

1. Bundle parts with weights 3 and 2, qualities 8 and 6:

   - New weight: 3 + 2 - floor(0.1 × 2) = 5 - 0 = 5
   - New quality: min(8, 6) - 1 = 5 (meets threshold!)
   - Now have: [4, 5] with qualities [10, 5]

2. Bundle parts with weights 4 and 3, qualities 10 and 8:

   - Weight: 4 + 3 - floor(0.1 × 3) = 7 - 0 = 7
   - Quality: min(10, 8) - 1 = 7

3. Bundle the result (weight 7, quality 7) with the part (weight 2, quality 6):
   - Weight: 7 + 2 - floor(0.1 × 2) = 9 - 0 = 9
   - Quality: min(7, 6) - 1 = 5

Final weight = 9, quality maintained at 5.

![Example Visualization](../images/GRD-006/example-1.png)

## Notes

- Use a max-heap to track (weight, quality) pairs
- Always try to bundle pairs that maintain quality >= T
- The 10% loss applies to the smaller weight
- Greedy strategy: prioritize maintaining quality while maximizing weight
- Time complexity: O(n log n) for heap operations

## Related Topics

Greedy Algorithms, Heap, Priority Queue, Simulation, Constraint Satisfaction

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxBundleWeight(int n, int T, int[] weights, int[] qualities) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;

        int n = sc.nextInt();
        int T = sc.nextInt();

        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            weights[i] = sc.nextInt();
        }

        int[] qualities = new int[n];
        for (int i = 0; i < n; i++) {
            qualities[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxBundleWeight(n, T, weights, qualities));
        sc.close();
    }
}
```

### Python

```python
import heapq
import math
import sys

class Solution:
    def max_bundle_weight(self, n: int, T: int, weights: list[int], qualities: list[int]) -> int:
        # //Implement here
        return 0

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit(0)

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        T = int(next(iterator))

        weights = []
        for _ in range(n):
            weights.append(int(next(iterator)))

        qualities = []
        for _ in range(n):
            qualities.append(int(next(iterator)))

        solution = Solution()
        print(solution.max_bundle_weight(n, T, weights, qualities))
    except StopIteration:
        pass
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

struct Part {
    long long w;
    int q;

    // For priority_queue, we want max quality at top, then min weight if tied.
    // Default is max-heap, so operator< should return true if 'this' is smaller than 'other'.
    bool operator<(const Part& other) const {
        if (q != other.q) return q < other.q;
        return w > other.w;  // If quality is equal, prefer smaller weight (min-heap on weight)
    }
};

class Solution {
public:
    long long maxBundleWeight(int n, int T, vector<int>& weights, vector<int>& qualities) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, T;
    if (!(cin >> n >> T)) return 0;

    vector<int> weights(n), qualities(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> qualities[i];
    }

    Solution solution;
    cout << solution.maxBundleWeight(n, T, weights, qualities) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MaxHeap {
  constructor() {
    this.heap = [];
  }
  push(val) {
    this.heap.push(val);
    this._siftUp();
  }
  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();
    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return max;
  }
  size() {
    return this.heap.length;
  }
  _compare(a, b) {
    // Compare by quality first (max), then by weight if tied (min)
    if (a.q !== b.q) return a.q > b.q ? 1 : -1;
    return a.w < b.w ? 1 : -1;
  }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this._compare(this.heap[idx], this.heap[parentIdx]) <= 0) break;
      [this.heap[idx], this.heap[parentIdx]] = [
        this.heap[parentIdx],
        this.heap[idx],
      ];
      idx = parentIdx;
    }
  }
  _siftDown() {
    let idx = 0;
    while (idx < this.heap.length) {
      let maxChildIdx = null;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < this.heap.length) maxChildIdx = left;
      if (
        right < this.heap.length &&
        this._compare(this.heap[right], this.heap[left]) > 0
      ) {
        maxChildIdx = right;
      }
      if (
        maxChildIdx === null ||
        this._compare(this.heap[idx], this.heap[maxChildIdx]) >= 0
      )
        break;
      [this.heap[idx], this.heap[maxChildIdx]] = [
        this.heap[maxChildIdx],
        this.heap[idx],
      ];
      idx = maxChildIdx;
    }
  }
}

class Solution {
  maxBundleWeight(n, T, weights, qualities) {
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

  let ptr = 0;
  const [n, T] = data[ptr++].split(" ").map(Number);
  const weights = data[ptr++].split(" ").map(Number);
  const qualities = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.maxBundleWeight(n, T, weights, qualities));
});
```
