---
problem_id: QUE_LAB_WINDOW_INSTABILITY__3951
display_id: QUE-007
slug: lab-window-instability
title: "Lab Window Instability"
difficulty: Medium
difficulty_score: 50
topics:
  - Sliding Window
  - Queue
  - Heaps
tags:
  - sliding-window
  - deque
  - median
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-007: Lab Window Instability

## Problem Statement

A lab monitors sensor readings in a sliding window. For each window of size `k`, compute:

```
instability = floor((max - min) / median)
```

The median is the lower median when `k` is even. If the median is `0`, output `0` for that window.

![Problem Illustration](../images/QUE-007/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` space-separated integers (readings)

## Output Format

- Single line: `n - k + 1` integers, each the instability of a window

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- Readings fit in 32-bit signed integer

## Example

**Input:**

```
5 3
5 1 4 6 2
```

**Output:**

```
1 1 1
```

**Explanation:**

Windows:

- [5, 1, 4] -> min=1, max=5, median=4, (5-1)/4=1
- [1, 4, 6] -> min=1, max=6, median=4, (6-1)/4=1
- [4, 6, 2] -> min=2, max=6, median=4, (6-2)/4=1

![Example Visualization](../images/QUE-007/example-1.png)

## Notes

- Use deques for max and min in O(1) amortized time
- Use two heaps with lazy deletion for the median
- Keep the lower heap size equal to or one more than the upper heap
- Total time complexity should be O(n log k)

## Related Topics

Sliding Window, Deque, Median Maintenance

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] windowInstability(int[] values, int k) {
        //Implement here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[] values;
            int k = n / 2;  // Default

            // If we have exactly n values
            if (remaining.size() == n) {
                values = new int[n];
                for (int i = 0; i < n; i++) {
                    values[i] = remaining.get(i);
                }
                k = n / 2;
            } else if (remaining.size() == n + 1) {
                // First is k, rest are values
                k = remaining.get(0);
                values = new int[n];
                for (int i = 0; i < n; i++) {
                    values[i] = remaining.get(i + 1);
                }
            } else {
                // Fallback
                k = !remaining.isEmpty() ? remaining.get(0) : n / 2;
                values = new int[Math.min(n, remaining.size() - 1)];
                for (int i = 0; i < values.length; i++) {
                    values[i] = remaining.get(i + 1);
                }
            }

            Solution solution = new Solution();
            long[] result = solution.windowInstability(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
from collections import deque
import heapq
import sys

class MedianFinder:
    def __init__(self):
        self.small = [] # Max heap (negative values)
        self.large = [] # Min heap
        self.delayed = {} # Lazy removal
        self.small_size = 0
        self.large_size = 0

    def add(self, num: int):
        # Add to small
        heapq.heappush(self.small, -num)
        # Move to large
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        self.large_size += 1
        
        # Rebalance: small needs to be size k or k+1
        if self.small_size < self.large_size:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1

    def remove(self, num: int):
        self.delayed[num] = self.delayed.get(num, 0) + 1
        
        # Determine which heap it effectively belongs to
        # small.peek is the median (or close to it)
        # If num <= small.peek(), it's in small
        small_top = -self.small[0] if self.small else float('-inf')
        
        if num <= small_top:
            self.small_size -= 1
        else:
            self.large_size -= 1
            
        # Prune dead roots
        self.prune()
        
        # Rebalance sizes
        if self.small_size < self.large_size:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1
        elif self.small_size > self.large_size + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.small_size -= 1
            self.large_size += 1
            
        self.prune()

    def prune(self):
        while self.small and self.delayed.get(-self.small[0], 0) > 0:
            val = -heapq.heappop(self.small)
            self.delayed[val] -= 1
        while self.large and self.delayed.get(self.large[0], 0) > 0:
            val = heapq.heappop(self.large)
            self.delayed[val] -= 1

    def get_median(self) -> int:
        return -self.small[0]

def window_instability(values: List[int], k: int) -> List[int]:
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        # Read all remaining values as they might be just the array
        remaining = list(iterator)

        # If we have exactly n remaining, they're the array and k should be guessed
        if len(remaining) == n:
            values = [int(x) for x in remaining]
            k = n // 2  # Default window size
        # If we have n+1 remaining, first is k, rest are array
        elif len(remaining) == n + 1:
            k = int(remaining[0])
            values = [int(x) for x in remaining[1:]]
        else:
            # Try to parse as many as possible
            k = int(remaining[0]) if remaining else n // 2
            values = [int(x) for x in remaining[1:n+1]]

        if len(values) == n:
            result = window_instability(values, k)
            if result:
                print(" ".join(map(str, result)))
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <set>

using namespace std;

class Solution {
public:
    vector<long long> windowInstability(const vector<int>& values, int k) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<int> values;
        int k = n / 2;  // Default

        // If we have exactly n values, use as values and k = n // 2
        if ((int)remaining.size() == n) {
            values.assign(remaining.begin(), remaining.end());
            k = n / 2;
        } else if ((int)remaining.size() == n + 1) {
            // First is k, rest are values
            k = remaining[0];
            values.assign(remaining.begin() + 1, remaining.begin() + n + 1);
        } else {
            // Try to parse k and values
            k = !remaining.empty() ? remaining[0] : n / 2;
            for (int i = 1; i <= n && i < (int)remaining.size(); i++) {
                values.push_back(remaining[i]);
            }
        }

        Solution solution;
        vector<long long> result = solution.windowInstability(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

// Simple MinPriorityQueue / MaxPriorityQueue polyfill for JS environment
// Or use a sorted array with binary search insertion (O(K) insertion)
// Since K can be large, O(K) is bad.
// However, JS doesn't have built-in Heap or TreeMap.
// For competitive programming in JS without libraries, implementing a Heap is standard.
// Here, we'll implement a basic Heap.

class Heap {
  constructor(compare) {
    this.data = [];
    this.compare = compare; // (a, b) => boolean (true if a should be above b)
  }
  size() { return this.data.length; }
  peek() { return this.data[0]; }
  push(val) {
    this.data.push(val);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    const top = this.data[0];
    const bottom = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.compare(this.data[idx], this.data[p])) {
        [this.data[idx], this.data[p]] = [this.data[p], this.data[idx]];
        idx = p;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = idx;
      if (left < this.data.length && this.compare(this.data[left], this.data[swap])) swap = left;
      if (right < this.data.length && this.compare(this.data[right], this.data[swap])) swap = right;
      if (swap !== idx) {
        [this.data[idx], this.data[swap]] = [this.data[swap], this.data[idx]];
        idx = swap;
      } else break;
    }
  }
}

class MedianFinder {
  constructor() {
    this.small = new Heap((a, b) => a > b); // Max Heap
    this.large = new Heap((a, b) => a < b); // Min Heap
    this.delayed = new Map();
    this.smallSize = 0;
    this.largeSize = 0;
  }
  add(val) {
    this.small.push(val);
    const maxSmall = this.small.pop();
    this.large.push(maxSmall);
    this.largeSize++;
    
    if (this.smallSize < this.largeSize) {
      this.small.push(this.large.pop());
      this.largeSize--;
      this.smallSize++;
    }
  }
  remove(val) {
    this.delayed.set(val, (this.delayed.get(val) || 0) + 1);
    const smallTop = this.small.size() > 0 ? this.small.peek() : -Infinity;
    if (val <= smallTop) this.smallSize--;
    else this.largeSize--;
    
    this.prune();
    
    if (this.smallSize < this.largeSize) {
      this.small.push(this.large.pop());
      this.largeSize--;
      this.smallSize++;
    } else if (this.smallSize > this.largeSize + 1) {
      this.large.push(this.small.pop());
      this.smallSize--;
      this.largeSize++;
    }
    this.prune();
  }
  prune() {
    while (this.small.size() > 0 && (this.delayed.get(this.small.peek()) || 0) > 0) {
      const val = this.small.pop();
      this.delayed.set(val, this.delayed.get(val) - 1);
    }
    while (this.large.size() > 0 && (this.delayed.get(this.large.peek()) || 0) > 0) {
      const val = this.large.pop();
      this.delayed.set(val, this.delayed.get(val) - 1);
    }
  }
  getMedian() {
    return this.small.peek();
  }
}

class Solution {
  windowInstability(values, k) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let k, values;
  if (remaining.length === n) {
    // Only values, no k -> k = n // 2
    values = remaining.map(x => parseInt(x, 10));
    k = Math.floor(n / 2);
  } else if (remaining.length === n + 1) {
    // First is k, rest are values
    k = parseInt(remaining[0], 10);
    values = remaining.slice(1, n + 1).map(x => parseInt(x, 10));
  } else {
    // Default case: try to parse k and n values
    k = parseInt(remaining[0], 10) || Math.floor(n / 2);
    values = remaining.slice(1, n + 1).map(x => parseInt(x, 10));
  }

  if (values.length === n) {
    const solution = new Solution();
    const result = solution.windowInstability(values, k);
    if (result.length > 0) {
      console.log(result.join(" "));
    }
  }
});
```

