---
problem_id: SEG_RANGE_XOR_BASIS__8820
display_id: SEG-007
slug: range-xor-basis
title: "Range XOR Basis"
difficulty: Medium
difficulty_score: 56
topics:
  - Segment Tree
  - Bitwise
  - Linear Basis
tags:
  - segment-tree
  - xor
  - linear-basis
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-007: Range XOR Basis

## Problem Statement

Maintain an array `a` with point updates and queries asking for the maximum XOR value obtainable from any subset of elements in `a[l..r]`.

Operations:

- `SET i x`: set `a[i] = x`
- `MAXXOR l r`: output the maximum subset XOR in `[l, r]`

![Problem Illustration](../images/SEG-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `MAXXOR`

## Output Format

- For each `MAXXOR`, print the maximum XOR value

## Constraints

- `1 <= n, q <= 100000`
- `0 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
1 2 3
MAXXOR 0 2
```

**Output:**

```
3
```

**Explanation:**

The maximum XOR from subset `{1,2}` is 3.

![Example Visualization](../images/SEG-007/example-1.png)

## Notes

- Store a linear basis in each segment tree node
- Merge bases when combining segments
- Query basis to compute max XOR
- Time per operation: O(log n * B)

## Related Topics

Linear Basis, Segment Tree, Bitwise

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
                ops.add(new String[]{op, sc.next(), sc.next()});
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
