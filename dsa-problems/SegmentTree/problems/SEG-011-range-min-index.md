---
problem_id: SEG_RANGE_MIN_INDEX__3926
display_id: SEG-011
slug: range-min-index
title: "Range Minimum Index"
difficulty: Medium
difficulty_score: 45
topics:
  - Segment Tree
  - Range Queries
  - Tie Breaking
tags:
  - segment-tree
  - range-min
  - index
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-011: Range Minimum Index

## Problem Statement

Given an array `a`, answer queries for the index of the minimum value in a range. If multiple indices have the same minimum value, return the smallest index.

Operations:

- `SET i x`: set `a[i] = x`
- `MINIDX l r`: output the index of the minimum in `a[l..r]`

![Problem Illustration](../images/SEG-011/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `MINIDX`

## Output Format

- For each `MINIDX`, print the index

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
4 2 2
MINIDX 0 2
```

**Output:**

```
1
```

**Explanation:**

The minimum value is 2 at indices 1 and 2, so return the smaller index 1.

![Example Visualization](../images/SEG-011/example-1.png)

## Notes

- Store (value, index) pairs in the segment tree
- Merge by comparing values, then indices
- Each operation runs in O(log n)
- Use 64-bit for values if needed

## Related Topics

Segment Tree, Range Minimum Query, Tie Breaking

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] process(long[] arr, List<String[]> ops) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
        List<String[]> ops = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            String op = sc.next();
            if (op.equals("SET")) {
                ops.add(new String[]{op, sc.next(), sc.next()});
            } else {
                ops.add(new String[]{op, sc.next(), sc.next()});
            }
        }

        Solution solution = new Solution();
        int[] out = solution.process(arr, ops);
        for (int v : out) System.out.println(v);
        sc.close();
    }
}
```

### Python

```python
def process(arr: list[int], ops: list[list[str]]) -> list[int]:
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
    ops = []
    for _ in range(q):
        op = next(it)
        ops.append([op, next(it), next(it)])

    out = process(arr, ops)
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
    vector<int> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<string>> ops;
    ops.reserve(q);
    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        string a, b;
        cin >> a >> b;
        ops.push_back({op, a, b});
    }

    Solution solution;
    vector<int> out = solution.process(arr, ops);
    for (int v : out) cout << v << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  process(arr, ops) {
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
  const ops = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    ops.push([op, data[idx++], data[idx++]]);
  }

  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```
