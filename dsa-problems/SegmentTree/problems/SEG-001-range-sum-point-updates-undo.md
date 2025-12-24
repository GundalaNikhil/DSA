---
problem_id: SEG_RANGE_SUM_POINT_UPDATES_UNDO__5472
display_id: SEG-001
slug: range-sum-point-updates-undo
title: "Range Sum with Point Updates and Undo"
difficulty: Medium
difficulty_score: 52
topics:
  - Segment Tree
  - Fenwick Tree
  - Rollback
tags:
  - segment-tree
  - fenwick
  - rollback
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-001: Range Sum with Point Updates and Undo
## Problem Statement
You maintain an array `a` under three operations:
- `UPDATE i x`: set `a[i] = x`
- `QUERY l r`: output the sum of `a[l..r]` modulo `M`
- `UNDO k`: revert the last `k` update operations (queries do not count)
Process all operations in order and output answers for each `QUERY`.
![Problem Illustration](../images/SEG-001/problem-illustration.png)
## Input Format
- First line: integers `n`, `q`, and `M`
- Second line: `n` space-separated integers (initial array)
- Next `q` lines: one operation (`UPDATE`, `QUERY`, or `UNDO`)
## Output Format
- For each `QUERY`, print one line with the sum modulo `M`
## Constraints
- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= M <= 10^9+7`
- `0 <= k <= 100`
## Example
**Input:**
```
5 5 1000
1 2 3 4 5
QUERY 1 3
UPDATE 2 10
QUERY 0 4
UNDO 1
QUERY 0 4
```
**Output:**
```
9
22
15
```
**Explanation:**
Sums are computed modulo 1000, and `UNDO 1` restores `a[2]` from 10 back to 3.
![Example Visualization](../images/SEG-001/example-1.png)
## Notes
- Keep a history stack of point updates to undo
- Segment tree or Fenwick tree supports point updates and range sums
- Each `UNDO` replays at most 100 updates
- Total time: O((n + q) log n)
## Related Topics
Segment Tree, Fenwick Tree, Rollback
---
## Solution Template
### Java
```java
import java.util.*;
class Solution {
    public List<Long> process(int[] arr, long mod, List<String[]> ops) {
        // Your implementation here
        return new ArrayList<>();
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        long mod = sc.nextLong();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        List<String[]> ops = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            String op = sc.next();
            if (op.equals("UPDATE")) {
                ops.add(new String[]{op, sc.next(), sc.next()});
            } else if (op.equals("QUERY")) {
                ops.add(new String[]{op, sc.next(), sc.next()});
            } else {
                ops.add(new String[]{op, sc.next()});
            }
        }
        Solution solution = new Solution();
        List<Long> out = solution.process(arr, mod, ops);
        for (long v : out) System.out.println(v);
        sc.close();
    }
}
```
### Python
```python
def process(arr: list[int], mod: int, ops: list[list[str]]) -> list[int]:
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
    mod = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    ops = []
    for _ in range(q):
        op = next(it)
        if op == "UPDATE":
            ops.append([op, next(it), next(it)])
        elif op == "QUERY":
            ops.append([op, next(it), next(it)])
        else:
            ops.append([op, next(it)])
    out = process(arr, mod, ops)
    sys.stdout.write("\n".join(str(x) for x in out))
if __name__ == "__main__":
    main()
```
### C++
```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    vector<long long> process(const vector<int>& arr, long long mod, const vector<vector<string>>& ops) {
        // Your implementation here
        return {};
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    long long mod;
    if (!(cin >> n >> q >> mod)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<string>> ops;
    ops.reserve(q);
    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        if (op == "UPDATE") {
            string i1, x;
            cin >> i1 >> x;
            ops.push_back({op, i1, x});
        } else if (op == "QUERY") {
            string l, r;
            cin >> l >> r;
            ops.push_back({op, l, r});
        } else {
            string k;
            cin >> k;
            ops.push_back({op, k});
        }
    }
    Solution solution;
    vector<long long> out = solution.process(arr, mod, ops);
    for (long long v : out) cout << v << "\n";
    return 0;
}
```
### JavaScript
```javascript
const readline = require("readline");
class Solution {
  process(arr, mod, ops) {
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
  const mod = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const ops = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "UPDATE") {
      ops.push([op, data[idx++], data[idx++]]);
    } else if (op === "QUERY") {
      ops.push([op, data[idx++], data[idx++]]);
    } else {
      ops.push([op, data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, mod, ops);
  console.log(out.join("\n"));
});
```
