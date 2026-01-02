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
        return null;
    }

    private long[] solveWithDualPQ(int[] values, int k) {
        int n = values.length;
        long[] result = new long[n - k + 1];
        Deque<Integer> minD = new ArrayDeque<>();
        Deque<Integer> maxD = new ArrayDeque<>();
        MedianFinder mf = new MedianFinder();

        for (int i = 0; i < n; i++) {
            // Min/Max
            while (!minD.isEmpty() && minD.peekFirst() <= i - k) minD.pollFirst();
            while (!minD.isEmpty() && values[minD.peekLast()] >= values[i]) minD.pollLast();
            minD.offerLast(i);

            while (!maxD.isEmpty() && maxD.peekFirst() <= i - k) maxD.pollFirst();
            while (!maxD.isEmpty() && values[maxD.peekLast()] <= values[i]) maxD.pollLast();
            maxD.offerLast(i);

            // Median
            mf.add(values[i]);
            if (i >= k) mf.remove(values[i - k]);

            if (i >= k - 1) {
                int minVal = values[minD.peekFirst()];
                int maxVal = values[maxD.peekFirst()];
                int median = mf.getMedian();
                if (median == 0) result[i - k + 1] = 0;
                else {
                    long diff = (long)maxVal - minVal;
                    long instability = diff / median;
                    if (diff % median != 0 && ((diff ^ median) < 0)) {
                        instability--;
                    }
                    result[i - k + 1] = instability;
                }
            }
        }
        return result;
    }

    static class MedianFinder {
        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> large = new PriorityQueue<>();
        // To handle lazy removal correctly, we track balance explicitly
        // Balance = small.size() - large.size() (considering only valid elements)
        // But since we can't know if a specific instance in heap is valid, we just track counts.
        // Let's use two TreeMaps (Multiset).
        
        // Re-implementation with TreeMap for correctness and simplicity
        TreeMap<Integer, Integer> smallMap = new TreeMap<>();
        TreeMap<Integer, Integer> largeMap = new TreeMap<>();
        int smallSize = 0;
        int largeSize = 0;

        void add(int val) {
            // Add to small first
            addMap(smallMap, val);
            smallSize++;
            
            // Move max of small to large
            int maxSmall = smallMap.lastKey();
            removeMap(smallMap, maxSmall);
            smallSize--;
            
            addMap(largeMap, maxSmall);
            largeSize++;
            
            // Rebalance: small should be >= large
            if (smallSize < largeSize) {
                int minLarge = largeMap.firstKey();
                removeMap(largeMap, minLarge);
                largeSize--;
                
                addMap(smallMap, minLarge);
                smallSize++;
            }
        }

        void remove(int val) {
            // Try to remove from small first
            if (smallMap.containsKey(val)) {
                // Check if it really belongs to small range
                // It must be <= small.lastKey()
                // Since small contains smaller elements, if val <= small.lastKey(), it's in small.
                // If val is in smallMap, we can just remove it?
                // Yes, because all elements in smallMap are <= all elements in largeMap.
                // So if val is in smallMap, it MUST be in the small partition.
                removeMap(smallMap, val);
                smallSize--;
            } else {
                removeMap(largeMap, val);
                largeSize--;
            }
            
            // Rebalance
            if (smallSize < largeSize) {
                int minLarge = largeMap.firstKey();
                removeMap(largeMap, minLarge);
                largeSize--;
                addMap(smallMap, minLarge);
                smallSize++;
            } else if (smallSize > largeSize + 1) {
                int maxSmall = smallMap.lastKey();
                removeMap(smallMap, maxSmall);
                smallSize--;
                addMap(largeMap, maxSmall);
                largeSize++;
            }
        }

        int getMedian() {
            return smallMap.lastKey();
        }

        void addMap(TreeMap<Integer, Integer> map, int val) {
            map.put(val, map.getOrDefault(val, 0) + 1);
        }

        void removeMap(TreeMap<Integer, Integer> map, int val) {
            int count = map.get(val);
            if (count == 1) map.remove(val);
            else map.put(val, count - 1);
        }
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
        return 0
    def add(self, num: int):
        return 0
    def remove(self, num: int):
        return 0
    def prune(self):
        return 0
    def get_median(self) -> int:
        return 0
def window_instability(values: List[int], k: int) -> List[int]:
    return []
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
        int n = values.size();
        vector<long long> result;
        deque<int> minD, maxD;
        
        // Use multiset for median (simplest in C++ as it supports deletion)
        // Two multisets: small (max), large (min)
        multiset<int> small, large;
        
        auto balance = [&]() {
            while (small.size() > large.size() + 1) {
                large.insert(*small.rbegin());
                small.erase(prev(small.end()));
            }
            while (large.size() > small.size()) {
                small.insert(*large.begin());
                large.erase(large.begin());
            }
        };
        
        auto add = [&](int val) {
            small.insert(val);
            large.insert(*small.rbegin());
            small.erase(prev(small.end()));
            balance();
        };
        
        auto remove = [&](int val) {
            auto it = small.find(val);
            if (it != small.end()) {
                small.erase(it);
            } else {
                large.erase(large.find(val));
            }
            balance();
        };
        
        for (int i = 0; i < n; i++) {
            // Min/Max Deques
            while (!minD.empty() && minD.front() <= i - k) minD.pop_front();
            while (!minD.empty() && values[minD.back()] >= values[i]) minD.pop_back();
            minD.push_back(i);
            
            while (!maxD.empty() && maxD.front() <= i - k) maxD.pop_front();
            while (!maxD.empty() && values[maxD.back()] <= values[i]) maxD.pop_back();
            maxD.push_back(i);
            
            // Median
            add(values[i]);
            if (i >= k) remove(values[i - k]);
            
            if (i >= k - 1) {
                int minVal = values[minD.front()];
                int maxVal = values[maxD.front()];
                int med = *small.rbegin();
                if (med == 0) result.push_back(0);
                else {
                    long long diff = (long long)maxVal - minVal;
                    long long instability = diff / med;
                    if (diff % med != 0 && ((diff ^ med) < 0)) {
                        instability--;
                    }
                    result.push_back(instability);
                }
            }
        }
        return result;
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

