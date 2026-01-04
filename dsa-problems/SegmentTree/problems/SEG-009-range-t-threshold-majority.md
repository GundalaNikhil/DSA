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
- Time complexity is around O(log n \* K)

## Related Topics

Segment Tree, Majority, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processQueries(int n, int q, long[] a, int[] ls, int[] rs, int[] ts) {
        // Implement here
        // For each query, print the selected value or -1
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextLong();
            int[] ls = new int[q];
            int[] rs = new int[q];
            int[] ts = new int[q];
            for (int i = 0; i < q; i++) {
                String cmd = sc.next();
                ls[i] = sc.nextInt();
                rs[i] = sc.nextInt();
                ts[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            sol.processQueries(n, q, a, ls, rs, ts);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def process_queries(self, n, q, a, queries):
        # Implement here
        # For each query, print the selected value or -1
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    a = [int(x) for x in input_data[2:2+n]]
    queries = []
    ptr = 2 + n
    for _ in range(q):
        cmd = input_data[ptr]
        l = int(input_data[ptr+1])
        r = int(input_data[ptr+2])
        t = int(input_data[ptr+3])
        queries.append((l, r, t))
        ptr += 4

    sol = Solution()
    sol.process_queries(n, q, a, queries)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void processQueries(int n, int q, const vector<long long>& a, const vector<vector<int>>& queries) {
        // Implement here
        // For each query, cout << val << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (cin >> n >> q) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        vector<vector<int>> queries(q, vector<int>(3));
        for (int i = 0; i < q; i++) {
            string cmd;
            cin >> cmd >> queries[i][0] >> queries[i][1] >> queries[i][2];
        }

        Solution sol;
        sol.processQueries(n, q, a, queries);
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processQueries(n, q, a, queries) {
    // Implement here
    // For each query, console.log(Number(val));
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const q = parseInt(input[1]);
  const a = input.slice(2, 2 + n).map(BigInt);
  const queries = [];
  let ptr = 2 + n;
  for (let i = 0; i < q; i++) {
    const l = parseInt(input[ptr + 1]);
    const r = parseInt(input[ptr + 2]);
    const t = parseInt(input[ptr + 3]);
    queries.push({ l, r, t });
    ptr += 4;
  }

  const sol = new Solution();
  sol.processQueries(n, q, a, queries);
});
```
