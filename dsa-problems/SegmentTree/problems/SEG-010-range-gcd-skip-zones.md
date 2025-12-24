---
problem_id: SEG_RANGE_GCD_SKIP_ZONES__6230
display_id: SEG-010
slug: range-gcd-skip-zones
title: "Range GCD with Skip Zones"
difficulty: Medium
difficulty_score: 54
topics:
  - Segment Tree
  - GCD
  - Dynamic Sets
tags:
  - segment-tree
  - gcd
  - toggles
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-010: Range GCD with Skip Zones

## Problem Statement

You are given an array `a` and a set of forbidden indices. The GCD of a range is computed using only indices that are not forbidden.
Operations:

- `TOGGLE i`: flip whether index `i` is forbidden
- `SET i x`: set `a[i] = x`
- `GCD l r`: output the gcd of all allowed elements in `[l, r]`, or 0 if none
  ![Problem Illustration](../images/SEG-010/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Third line: integer `f` (initial forbidden count)
- Next `f` lines: forbidden indices
- Next `q` lines: operations `TOGGLE`, `SET`, or `GCD`

## Output Format

- For each `GCD`, print the gcd value

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 3
6 9 3
1
1
GCD 0 2
TOGGLE 1
GCD 0 2
```

**Output:**

```
3
3
```

**Explanation:**
Initially index 1 is forbidden, so gcd(6,3) = 3. After toggling, all indices are allowed and gcd(6,9,3) = 3.
![Example Visualization](../images/SEG-010/example-1.png)

## Notes

- Store gcd in a segment tree, but ignore forbidden indices
- You can represent forbidden indices as zeroed values
- GCD of an empty set is 0
- Use absolute values for gcd on negatives

## Related Topics

## Segment Tree, GCD, Range Queries

## Solution Template

### Java

```java
import java.util.*;
class Solution {
    public List<Integer> process(int[] arr, boolean[] forbidden, List<String[]> ops) {
        // Your implementation here
        return new ArrayList<>();
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int f = sc.nextInt();
        boolean[] forbidden = new boolean[n];
        for (int i = 0; i < f; i++) forbidden[sc.nextInt()] = true;
        List<String[]> ops = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            String op = sc.next();
            if (op.equals("TOGGLE")) {
                ops.add(new String[]{op, sc.next()});
            } else {
                ops.add(new String[]{op, sc.next(), sc.next()});
            }
        }
        Solution solution = new Solution();
        List<Integer> out = solution.process(arr, forbidden, ops);
        for (int v : out) System.out.println(v);
        sc.close();
    }
}
```

### Python

```python
def process(arr: list[int], forbidden: list[bool], ops: list[list[str]]) -> list[int]:
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
    f = int(next(it))
    forbidden = [False] * n
    for _ in range(f):
        forbidden[int(next(it))] = True
    ops = []
    for _ in range(q):
        op = next(it)
        if op == "TOGGLE":
            ops.append([op, next(it)])
        else:
            ops.append([op, next(it), next(it)])
    out = process(arr, forbidden, ops)
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
    vector<int> process(const vector<int>& arr, const vector<bool>& forbidden, const vector<vector<string>>& ops) {
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
    int f;
    cin >> f;
    vector<bool> forbidden(n, false);
    for (int i = 0; i < f; i++) {
        int idx;
        cin >> idx;
        forbidden[idx] = true;
    }
    vector<vector<string>> ops;
    ops.reserve(q);
    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        if (op == "TOGGLE") {
            string a;
            cin >> a;
            ops.push_back({op, a});
        } else {
            string a, b;
            cin >> a >> b;
            ops.push_back({op, a, b});
        }
    }
    Solution solution;
    vector<int> out = solution.process(arr, forbidden, ops);
    for (int v : out) cout << v << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
class Solution {
  process(arr, forbidden, ops) {
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
  const f = parseInt(data[idx++], 10);
  const forbidden = Array(n).fill(false);
  for (let i = 0; i < f; i++) {
    forbidden[parseInt(data[idx++], 10)] = true;
  }
  const ops = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "TOGGLE") {
      ops.push([op, data[idx++]]);
    } else {
      ops.push([op, data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, forbidden, ops);
  console.log(out.join("\n"));
});
```
