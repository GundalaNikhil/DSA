---
problem_id: HEP_TOP_K_FREQUENT_DECAY__5829
display_id: HEP-003
slug: top-k-frequent-decay
title: "Top K Frequent with Decay"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Lazy Updates
  - Time Decay
tags:
  - heaps
  - decay
  - frequency
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-003: Top K Frequent with Decay

## Problem Statement

You receive events with timestamps. Each event adds 1 to the count of a key. Every `d` seconds, counts decay by half. At query time `t`, the effective count for a key is:

```
count * 0.5^(floor((t - last_update) / d))
```

Return the top `k` keys by effective count at each query. Break ties by lexicographic order. If fewer than `k` keys exist, return all. If no keys exist, output `EMPTY`.

![Problem Illustration](../images/HEP-003/problem-illustration.png)

## Input Format

- First line: three integers `q`, `d`, and `k`
- Next `q` lines:
  - `ADD key t`
  - `QUERY t`

## Output Format

- For each `QUERY`, output one line with up to `k` keys separated by spaces, or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= d <= 10^9`
- `1 <= k <= 100000`
- `0 <= t <= 10^9`
- `1 <= |key| <= 20` (lowercase letters)

## Example

**Input:**

```
4 5 1
ADD a 0
ADD a 5
ADD b 5
QUERY 10
```

**Output:**

```
a
```

**Explanation:**

At t=10:

- a was updated at t=5 with count 1.5, then decays once -> 0.75
- b was updated at t=5 with count 1, then decays once -> 0.5

Top 1 key is a.

![Example Visualization](../images/HEP-003/example-1.png)

## Notes

- Store last update time and current count per key
- Apply decay lazily when a key is accessed
- Use a max-heap for retrieving top k keys per query
- Time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Heaps, Time Decay, Lazy Updates, Streaming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class State {
        double count;
        int last_update;
        int version;
    }

    static class Entry {
        double count;
        String key;
        int version;

        Entry(double count, String key, int version) {
            this.count = count;
            this.key = key;
            this.version = version;
        }
    }

    public List<String> processOperations(int d, int k, List<String[]> operations) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            int d = sc.nextInt();
            int k = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("ADD")) {
                    String key = sc.next();
                    String t = sc.next();
                    operations.add(new String[]{op, key, t});
                } else {
                    String t = sc.next();
                    operations.add(new String[]{op, t});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(d, k, operations);
            for (String s : result) System.out.println(s);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import math
import heapq

class Solution:
    def process_operations(self, d: int, k: int, operations: list) -> list:
        return []
def process_operations(d: int, k: int, operations: list) -> list:
    return []
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        d = int(next(it))
        k = int(next(it))
        operations = []
        for _ in range(q):
            try:
                op = next(it)
            except StopIteration:
                break
                
            if op == "ADD":
                key = next(it)
                t = next(it)
                operations.append([op, key, t])
            else:
                t = next(it)
                operations.append([op, t])
        
        result = process_operations(d, k, operations)
        print("\n".join(result))
    except StopIteration:
        # Fallback if initial params or arguments fail
        if 'operations' in locals() and operations:
             result = process_operations(d, k, operations)
             print("\n".join(result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

struct State {
    double count;
    int last_update;
    int version;
};

struct Entry {
    double count;
    string key;
    int version;
};

struct Cmp {
    bool operator()(const Entry& a, const Entry& b) const {
        if (abs(a.count - b.count) > 1e-9) {
            return a.count < b.count; // Max heap by count
        }
        return a.key > b.key; // Lexicographically smaller key
    }
};

class Solution {
public:
    vector<string> processOperations(int d, int k, const vector<vector<string>>& operations) {
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q, d, k;
    if (cin >> q >> d >> k) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "ADD") {
                string key, t;
                cin >> key >> t;
                operations.push_back({op, key, t});
            } else {
                string t;
                cin >> t;
                operations.push_back({op, t});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(d, k, operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MaxHeap {
  constructor() {
    this.data = [];
  }
  isEmpty() {
    return this.data.length === 0;
  }
  better(a, b) {
    // a is "better" if it should be higher in heap
    // Higher count = better
    // Equal count = lexicographically smaller key = better
    if (Math.abs(a.count - b.count) > 1e-9) return a.count > b.count;
    return a.key < b.key;
  }
  push(item) {
    this.data.push(item);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    if (this.data.length === 0) return null;
    const top = this.data[0];
    const last = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = last;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.better(this.data[idx], this.data[pIdx])) {
        [this.data[idx], this.data[pIdx]] = [this.data[pIdx], this.data[idx]];
        idx = pIdx;
      } else {
        break;
      }
    }
  }
  bubbleDown(idx) {
    const n = this.data.length;
    while (true) {
      let best = idx;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < n && this.better(this.data[left], this.data[best])) best = left;
      if (right < n && this.better(this.data[right], this.data[best])) best = right;
      if (best === idx) break;
      [this.data[idx], this.data[best]] = [this.data[best], this.data[idx]];
      idx = best;
    }
  }
}

class Solution {
  processOperations(d, k, operations) {
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
  const d = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "ADD") {
      const key = data[idx++];
      const t = data[idx++];
      operations.push([op, key, t]);
    } else {
      const t = data[idx++];
      operations.push([op, t]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(d, k, operations);
  console.log(result.join("\n"));
});
```

