---
problem_id: GRD_LIBRARY_MERGE_QUEUES__8135
display_id: GRD-010
slug: library-merge-queues
title: "Library Merge Queues"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Heap
  - Merge K Sorted Lists
tags:
  - greedy
  - heap
  - priority-queue
  - merge
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-010: Library Merge Queues

## Problem Statement

You have `k` sorted queues of book IDs (integers). You need to merge them into a single sorted stream with a constraint: **no book ID can appear more than twice consecutively** in the output.

If a book ID would appear for the third time in a row, skip it and move to the next available different ID. Continue this process until all queues are processed.

Return the merged stream as a list.

![Problem Illustration](../images/GRD-010/problem-illustration.png)

## Input Format

- First line: integer `k` (number of queues)
- Next `k` lines: each line starts with an integer `len` (queue length), followed by `len` sorted integers

## Output Format

- Single line with space-separated integers representing the merged stream

## Constraints

- `1 <= k <= 100`
- Total elements across all queues `<= 2*10^5`
- All queues are sorted in non-decreasing order
- Book IDs are integers in range `[1, 10^9]`

## Example

**Input:**

```
3
3 1 1 1
2 1 2
1 2
```

**Output:**

```
1 1 1 2 2
```

**Explanation:**

Queues:

- Queue 0: [1, 1, 1]
- Queue 1: [1, 2]
- Queue 2: [2]

Merge process:

1. Take 1 from queue 0 → output: [1], last two: [1]
2. Take 1 from queue 0 → output: [1, 1], last two: [1, 1]
3. Cannot take another 1 (would be third consecutive). Take 2 from queue 1 → output: [1, 1, 2]
4. Take 1 from queue 0 → output: [1, 1, 2, 1]
5. Take 2 from queue 2 → output: [1, 1, 2, 1, 2]

The constraint ensures no more than 2 consecutive identical values.

![Example Visualization](../images/GRD-010/example-1.png)

## Notes

- Use a min-heap to track the minimum value across all queue fronts
- Track the last two values added to the output
- If the next minimum would create three consecutive identical values, temporarily skip it
- Pull from a different queue/value, then resume
- Time complexity: O(N log k) where N is total elements

## Related Topics

Merge K Sorted Lists, Heap, Priority Queue, Greedy Algorithms, Constraint Handling

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> mergeQueues(List<List<Integer>> queues) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();

        List<List<Integer>> queues = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int len = sc.nextInt();
            List<Integer> queue = new ArrayList<>();
            for (int j = 0; j < len; j++) {
                queue.add(sc.nextInt());
            }
            queues.add(queue);
        }

        Solution solution = new Solution();
        List<Integer> result = solution.mergeQueues(queues);

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
from typing import List

class Solution:
    def merge_queues(self, queues: List[List[int]]) -> List[int]:
        # //Implement here
        return []

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit(0)

    iterator = iter(input_data)
    try:
        k = int(next(iterator))

        queues = []
        for _ in range(k):
            length = int(next(iterator))
            queue = []
            for _ in range(length):
                queue.append(int(next(iterator)))
            queues.append(queue)

        solution = Solution()
        result = solution.merge_queues(queues)
        print(' '.join(map(str, result)))
    except StopIteration:
        pass
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node {
    int val;
    int queueIndex;

    // Min-heap: greater value means lower priority
    bool operator>(const Node& other) const {
        return val > other.val;
    }
};

class Solution {
public:
    vector<int> mergeQueues(vector<vector<int>>& queues) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    vector<vector<int>> queues(k);
    for (int i = 0; i < k; i++) {
        int len;
        cin >> len;
        queues[i].resize(len);
        for (int j = 0; j < len; j++) {
            cin >> queues[i][j];
        }
    }

    Solution solution;
    vector<int> result = solution.mergeQueues(queues);

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
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return min;
  }
  size() {
    return this.heap.length;
  }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this.heap[idx].val >= this.heap[parentIdx].val) break;
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
      let minChildIdx = null;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < this.heap.length) minChildIdx = left;
      if (
        right < this.heap.length &&
        this.heap[right].val < this.heap[left].val
      ) {
        minChildIdx = right;
      }
      if (
        minChildIdx === null ||
        this.heap[idx].val <= this.heap[minChildIdx].val
      )
        break;
      [this.heap[idx], this.heap[minChildIdx]] = [
        this.heap[minChildIdx],
        this.heap[idx],
      ];
      idx = minChildIdx;
    }
  }
}

class Solution {
  mergeQueues(queues) {
    //Implement here
    return [];
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

  const queues = [];
  for (let i = 0; i < k; i++) {
    const len = allNumbers[ptr++];
    const queue = [];
    for (let j = 0; j < len; j++) {
      queue.push(allNumbers[ptr++]);
    }
    queues.push(queue);
  }

  const solution = new Solution();
  const result = solution.mergeQueues(queues);
  console.log(result.join(" "));
});
```
