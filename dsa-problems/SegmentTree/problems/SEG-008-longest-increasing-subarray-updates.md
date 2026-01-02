---
problem_id: SEG_LONGEST_INCREASING_SUBARRAY_UPDATES__2654
display_id: SEG-008
slug: longest-increasing-subarray-updates
title: "Longest Increasing Subarray After Updates"
difficulty: Medium
difficulty_score: 55
topics:
  - Segment Tree
  - Dynamic Arrays
  - Monotonicity
tags:
  - segment-tree
  - increasing
  - updates
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-008: Longest Increasing Subarray After Updates

## Problem Statement

Given an array `a`, you must handle point updates. After each update, output the length of the longest strictly increasing contiguous subarray.

Operation:

- `SET i x`: set `a[i] = x`

![Problem Illustration](../images/SEG-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET i x`

## Output Format

- For each update, print the current longest increasing subarray length

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
3 1
1 2 1
SET 2 3
```

**Output:**

```
3
```

**Explanation:**

After the update the array becomes `[1, 2, 3]`, which is strictly increasing.

![Example Visualization](../images/SEG-008/example-1.png)

## Notes

- Store prefix and suffix increasing lengths per segment
- Merge using boundary comparisons between segments
- Update affects only O(log n) nodes
- The answer is the max length stored at the root

## Related Topics

Segment Tree, Range Merge, Dynamic Updates

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] process(int[] arr, int[][] updates) {
        // Implementation here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int[][] updates = new int[q][2];
            for (int i = 0; i < q; i++) {
                String type = sc.next(); // SET
                updates[i][0] = sc.nextInt();
                updates[i][1] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] results = sol.process(arr, updates);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def process(arr: list[int], updates: list[tuple[int, int]]) -> list[int]:
    # Implementation here
    return []

def main():
    import sys
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    updates = []
    for _ in range(q):
        type = next(it) # SET
        updates.append((int(next(it)), int(next(it))))
    
    results = process(arr, updates)
    for res in results:
        print(res)

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
    vector<int> process(const vector<int>& inputArr, const vector<pair<int,int>>& updates) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<pair<int, int>> updates(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // SET
        cin >> updates[i].first >> updates[i].second;
    }
    Solution sol;
    vector<int> results = sol.process(arr, updates);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  process(arr, updates) {
    // Implementation here
    return null;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const updates = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++]; // SET
    updates.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.process(arr, updates);
  console.log(out.join("\n"));
});
```
