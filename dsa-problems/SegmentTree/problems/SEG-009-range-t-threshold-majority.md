---
problem_id: SEG_RANGE_T_THRESHOLD_MAJORITY__7412
display_id: SEG-009
slug: range-t-threshold-majority
title: "Range T-Threshold Majority Check"
difficulty: Medium
difficulty_score: 62
topics:
  - Segment Tree
  - Frequency Counting
  - Range Queries
tags:
  - segment-tree
  - frequency
  - range-query
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-009: Range T-Threshold Majority Check

## Problem Statement

Given an array `a`, answer queries `MAJ l r T`: determine whether there exists a value that appears at least `T` times in the subarray `a[l..r]`.

If such a value exists, output the value with the highest frequency; if multiple have the same frequency, output the smallest value. Otherwise output `-1`.

![Problem Illustration](../images/SEG-009/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `MAJ l r T`

## Output Format

- For each query, print the selected value or `-1`

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `1 <= T <= r - l + 1`

## Example

**Input:**

```
5 1
1 1 2 3 1
MAJ 0 4 3
```

**Output:**

```
1
```

**Explanation:**

Value 1 appears 3 times in the range, meeting the threshold.

![Example Visualization](../images/SEG-009/example-1.png)

## Notes

- Store a small candidate frequency map per segment
- Merge nodes by keeping top candidates only
- Verify the candidate frequency in the query range
- Time complexity is around O(log n * K)

## Related Topics

Segment Tree, Majority, Range Queries

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] process(int[] arr, int[][] queries) {
        //Implement here
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
            int[][] queries = new int[q][3];
            for (int i = 0; i < q; i++) {
                String type = sc.next(); // MAJ
                queries[i][0] = sc.nextInt();
                queries[i][1] = sc.nextInt();
                queries[i][2] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] results = sol.process(arr, queries);
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
from bisect import bisect_left, bisect_right

class Summary:
    def __init__(self):
        self.candidates = {} # val -> count
        self.K = 40
        
    def add(self, val, count):
        self.candidates[val] = self.candidates.get(val, 0) + count
        if len(self.candidates) > self.K:
            min_cnt = min(self.candidates.values())
            to_remove = []
            for k, v in self.candidates.items():
                self.candidates[k] -= min_cnt
                if self.candidates[k] <= 0:
                    to_remove.append(k)
            for k in to_remove:
                del self.candidates[k]
                
    def merge(self, other):
        for val, count in other.candidates.items():
            self.add(val, count)

def process(arr: list[int], queries: list[tuple[int, int, int]]) -> list[int]:
    # //Implement here
    return 0

def main():
    import sys
    # Increase recursion depth for deep trees
    sys.setrecursionlimit(300000)
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    queries = []
    for _ in range(q):
        type = next(it) # MAJ
        l = int(next(it))
        r = int(next(it))
        t = int(next(it))
        queries.append((l, r, t))
    
    results = process(arr, queries)
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
#include <map>
#include <string>
#include <array>

using namespace std;

struct Summary {
    vector<pair<int, int>> candidates;
    static const int K = 40;
    
    void add(int val, int count) {
        for (auto& p : candidates) {
            if (p.first == val) {
                p.second += count;
                return;
            }
        }
        candidates.push_back({val, count});
        if (candidates.size() > K) {
            int minCnt = 2e9;
            for (auto& p : candidates) minCnt = min(minCnt, p.second);
            
            vector<pair<int, int>> next;
            for (auto& p : candidates) {
                p.second -= minCnt;
                if (p.second > 0) next.push_back(p);
            }
            candidates = next;
        }
    }
    
    void merge(const Summary& other) {
        for (const auto& p : other.candidates) {
            add(p.first, p.second);
        }
    }
};

class Solution {
public:
    vector<int> process(const vector<int>& arr, const vector<array<int,3>>& queries) {
        //Implement here
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
    vector<array<int, 3>> queries(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // MAJ
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2];
    }
    Solution sol;
    vector<int> results = sol.process(arr, queries);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  process(arr, queries) {
    //Implement here
    return 0;
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
  const queries = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++]; // MAJ
    queries.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.process(arr, queries);
  console.log(out.join("\n"));
});
```

