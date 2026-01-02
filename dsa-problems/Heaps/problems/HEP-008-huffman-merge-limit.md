---
problem_id: HEP_HUFFMAN_MERGE_LIMIT__1584
display_id: HEP-008
slug: huffman-merge-limit
title: "Huffman with Merge Limit"
difficulty: Medium
difficulty_score: 50
topics:
  - Heaps
  - Huffman Coding
  - Greedy
tags:
  - heaps
  - huffman
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-008: Huffman with Merge Limit

## Problem Statement

Given `n` frequencies, build a Huffman-like tree where you may merge at most `m` nodes at a time (`2 <= m <= 5`). The cost of each merge is the sum of merged values, and that sum is pushed back into the pool. The total cost is the sum of all merge costs.

If `(n - 1) % (m - 1) != 0`, pad the list with zeros until it satisfies the condition.

Return the total cost.

![Problem Illustration](../images/HEP-008/problem-illustration.png)

## Input Format

- First line: two integers `n` and `m`
- Second line: `n` space-separated frequencies

## Output Format

- Single integer: total merge cost

## Constraints

- `1 <= n <= 100000`
- `2 <= m <= 5`
- `0 <= frequency <= 10^9`

## Example

**Input:**

```
3 2
5 7 10
```

**Output:**

```
34
```

**Explanation:**

Binary merges:

- Merge 5 and 7 -> cost 12
- Merge 10 and 12 -> cost 22

Total cost = 12 + 22 = 34.

![Example Visualization](../images/HEP-008/example-1.png)

## Notes

- Use a min-heap to repeatedly extract the smallest `m` values
- Pad with zeros so the final tree is valid
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Heaps, Huffman Coding, Greedy Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long huffmanCost(int[] freq, int m) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] freq = new int[n];
            for (int i = 0; i < n; i++) {
                freq[i] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.huffmanCost(freq, m));
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

class Solution:
    def huffman_cost(self, freq: list, m: int) -> int:
        return 0
def huffman_cost(freq: list, m: int) -> int:
    return 0
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        freq = []
        for _ in range(n):
            freq.append(int(next(it)))
            
        print(huffman_cost(freq, m))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

class Solution {
public:
    long long huffmanCost(const vector<int>& freq, int m) {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        for (int f : freq) {
            pq.push((long long)f);
        }
        
        while ((pq.size() - 1) % (m - 1) != 0) {
            pq.push(0);
        }
        
        long long totalCost = 0;
        
        while (pq.size() > 1) {
            long long sum = 0;
            for (int i = 0; i < m; i++) {
                sum += pq.top();
                pq.pop();
            }
            totalCost += sum;
            pq.push(sum);
        }
        
        return totalCost;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<int> freq(n);
        for (int i = 0; i < n; i++) cin >> freq[i];
        
        Solution solution;
        cout << solution.huffmanCost(freq, m) << "\n";
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
  huffmanCost(freq, m) {
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
  const n = parseInt(data[idx++]);
  const m = parseInt(data[idx++]);
  const freq = [];
  for (let i = 0; i < n; i++) {
    freq.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.huffmanCost(freq, m));
});
```

