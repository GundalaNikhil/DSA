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
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int[][] queries = new int[q][3];
        for (int i = 0; i < q; i++) {
            sc.next();
            queries[i][0] = sc.nextInt();
            queries[i][1] = sc.nextInt();
            queries[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] out = solution.process(arr, queries);
        for (int v : out) System.out.println(v);
        sc.close();
    }
}
```

### Python

```python
def process(arr: list[int], queries: list[tuple[int, int, int]]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    queries = []
    for _ in range(q):
        _ = next(it)
        l = int(next(it))
        r = int(next(it))
        t = int(next(it))
        queries.append((l, r, t))

    out = process(arr, queries)
    sys.stdout.write("\n".join(str(x) for x in out))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <array>
using namespace std;

class Solution {
public:
    vector<int> process(const vector<int>& arr, const vector<array<int,3>>& queries) {
        // Your implementation here
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
    vector<array<int,3>> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        int l, r, t;
        cin >> l >> r >> t;
        queries.push_back({l, r, t});
    }

    Solution solution;
    vector<int> out = solution.process(arr, queries);
    for (int v : out) cout << v << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  process(arr, queries) {
    // Your implementation here
    return [];
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
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const queries = [];
  for (let i = 0; i < q; i++) {
    idx++;
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    const t = parseInt(data[idx++], 10);
    queries.push([l, r, t]);
  }

  const solution = new Solution();
  const out = solution.process(arr, queries);
  console.log(out.join("\n"));
});
```
