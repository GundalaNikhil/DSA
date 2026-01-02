---
problem_id: HEP_RUNNING_MEDIAN_DELETE_THRESHOLD__4217
display_id: HEP-001
slug: running-median-with-delete-threshold
title: "Running Median with Delete and Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Median
  - Data Streams
tags:
  - heaps
  - median
  - lazy-deletion
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-001: Running Median with Delete and Threshold

## Problem Statement

Maintain a multiset of integers under three operations:

- `ADD x`: insert `x` into the multiset
- `DEL x`: remove one occurrence of `x` if it exists
- `MEDIAN`: report the median (lower middle if size is even)

If the multiset is empty, output `EMPTY`. If the multiset size is less than a given threshold `T`, output `NA` instead of the median.

![Problem Illustration](../images/HEP-001/problem-illustration.png)

## Input Format

- First line: two integers `q` and `T` (number of operations and threshold)
- Next `q` lines: one operation (`ADD x`, `DEL x`, or `MEDIAN`)

## Output Format

- For each `MEDIAN` operation, output one line:
  - `EMPTY` if the multiset is empty
  - `NA` if size < `T`
  - Otherwise the median value (lower middle)

## Constraints

- `1 <= q <= 100000`
- `-10^9 <= x <= 10^9`
- `0 <= T <= 100000`

## Example

**Input:**

```
4 2
ADD 1
ADD 5
DEL 1
MEDIAN
```

**Output:**

```
NA
```

**Explanation:**

Operations:

- ADD 1 -> multiset {1}
- ADD 5 -> multiset {1, 5}
- DEL 1 -> multiset {5}
- MEDIAN -> size is 1 < T (2), so output NA

![Example Visualization](../images/HEP-001/example-1.png)

## Notes

- Use two heaps to track lower and upper halves
- Apply lazy deletion to handle `DEL` efficiently
- Each operation can be processed in O(log n)
- Space complexity: O(n)

## Related Topics

Heaps, Median Maintenance, Lazy Deletion, Data Streams

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private PriorityQueue<Integer> left; // Max heap
    private PriorityQueue<Integer> right; // Min heap
    private Map<Integer, Integer> leftDebt;
    private Map<Integer, Integer> rightDebt;
    private Map<Integer, Integer> globalCounts;
    private int validLeft, validRight;

    public List<String> processOperations(int T, List<String[]> operations) {
        return null;
    }
    
    private void add(int x) {
    }
    
    private void del(int x) {
    }
    
    private String getMedian(int T) {
        return "";
    }
    
    private void rebalance() {
    }
    
    private void cleanLeft() {
    }

    private void cleanRight() {
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            int T = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("ADD") || op.equals("DEL")) {
                    String x = sc.next();
                    operations.add(new String[]{op, x});
                } else {
                    operations.add(new String[]{op});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(T, operations);
            for (String s : result) System.out.println(s);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq
from collections import defaultdict

class Solution:
    def process_operations(self, T: int, operations: list) -> list:
        return []
def process_operations(T: int, operations: list) -> list:
    return []
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    q_str = next(it, None)
    if q_str is None: return
    q = int(q_str)
    t_str = next(it, None)
    if t_str is None: return
    T = int(t_str)
    
    operations = []
    for _ in range(q):
        op = next(it)
        if op in ("ADD", "DEL"):
            x = next(it)
            operations.append([op, x])
        else:
            operations.append([op])
    
    result = process_operations(T, operations)
    print("\n".join(result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>

using namespace std;

class Solution {
    priority_queue<int> left; // Max heap
    priority_queue<int, vector<int>, greater<int>> right; // Min heap
    unordered_map<int, int> leftDebt;
    unordered_map<int, int> rightDebt;
    unordered_map<int, int> global_counts;
    int validLeft = 0;
    int validRight = 0;

    void cleanLeft() {
    }

    void cleanRight() {
    }

    void rebalance() {
    }

public:
    vector<string> processOperations(int T, const vector<vector<string>>& operations) {
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q, T;
    if (cin >> q >> T) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "ADD" || op == "DEL") {
                string x;
                cin >> x;
                operations.push_back({op, x});
            } else {
                operations.push_back({op});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(T, operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.heap = [];
    this.compare = compare;
  }
  size() { return this.heap.length; }
  isEmpty() { return this.heap.length === 0; }
  peek() { return this.heap[0]; }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.size() > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.compare(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = null;
      if (left < this.size() && this.compare(this.heap[left], this.heap[idx]) < 0) swap = left;
      if (right < this.size() && this.compare(this.heap[right], swap === null ? this.heap[idx] : this.heap[swap]) < 0) swap = right;
      if (swap === null) break;
      [this.heap[idx], this.heap[swap]] = [this.heap[swap], this.heap[idx]];
      idx = swap;
    }
  }
}

class Solution {
  processOperations(T, operations) {
    return 0;
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
  const q = parseInt(data[idx++]);
  const T = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "ADD" || op === "DEL") {
      const x = data[idx++];
      operations.push([op, x]);
    } else {
      operations.push([op]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(T, operations);
  console.log(result.join("\n"));
});
```

