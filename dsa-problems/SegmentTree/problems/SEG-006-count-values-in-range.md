---
problem_id: SEG_COUNT_VALUES_IN_RANGE__1637
display_id: SEG-006
slug: count-values-in-range
title: "Count of Values in Range"
difficulty: Medium
difficulty_score: 51
topics:
  - Segment Tree
  - BIT
  - Range Queries
tags:
  - segment-tree
  - range-count
  - fenwick
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-006: Count of Values in Range

## Problem Statement

Maintain an array `a` under point updates and range count queries. The operations are:

- `SET i x`: set `a[i] = x`
- `COUNT l r x y`: count how many `a[i]` in `[l, r]` satisfy `x <= a[i] <= y`

![Problem Illustration](../images/SEG-006/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `COUNT` operations

## Output Format

- For each `COUNT`, print the number of values in range

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x, y <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
1 5 2
COUNT 0 2 2 5
```

**Output:**

```
2
```

**Explanation:**

In `[1,5,2]`, the values in `[2,5]` are 5 and 2.

![Example Visualization](../images/SEG-006/example-1.png)

## Notes

- Coordinate-compress all values from updates and queries
- Use a segment tree of Fenwick trees or a BIT of BITs
- Each operation runs in O(log^2 n)
- Counts fit in 32-bit integer

## Related Topics

Segment Tree, Fenwick Tree, Range Counting

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<Integer> process(int[] arr, List<String[]> ops) {
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
        List<String[]> ops = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            String op = sc.next();
            if (op.equals("SET")) {
                ops.add(new String[]{op, sc.next(), sc.next()});
            } else {
                ops.add(new String[]{op, sc.next(), sc.next(), sc.next(), sc.next()});
            }
        }

        Solution solution = new Solution();
        List<Integer> out = solution.process(arr, ops);
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
        if op == "SET":
            ops.append([op, next(it), next(it)])
        else:
            ops.append([op, next(it), next(it), next(it), next(it)])

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
    vector<int> process(const vector<int>& arr, const vector<vector<string>>& ops) {
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
    vector<vector<string>> ops;
    ops.reserve(q);
    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        if (op == "SET") {
            string i1, x;
            cin >> i1 >> x;
            ops.push_back({op, i1, x});
        } else {
            string l, r, x, y;
            cin >> l >> r >> x >> y;
            ops.push_back({op, l, r, x, y});
        }
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
    if (op === "SET") {
      ops.push([op, data[idx++], data[idx++]]);
    } else {
      ops.push([op, data[idx++], data[idx++], data[idx++], data[idx++]]);
    }
  }

  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```
