---
problem_id: SEG_RANGE_ADD_KTH_ORDER__8059
display_id: SEG-012
slug: range-add-kth-order
title: "Range Add, K-th Order"
difficulty: Hard
difficulty_score: 70
topics:
  - Segment Tree
  - Order Statistics
  - Range Updates
tags:
  - segment-tree
  - kth-statistic
  - range-add
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-012: Range Add, K-th Order

## Problem Statement

Maintain an array under range-add updates and k-th order statistic queries on subarrays.

Operations:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `KTH l r k`: output the k-th smallest value in `a[l..r]`

![Problem Illustration](../images/SEG-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `ADD` or `KTH`

## Output Format

- For each `KTH`, print the k-th smallest value

## Constraints

- `1 <= n, q <= 100000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= k <= r - l + 1`

## Example

**Input:**

```
3 2
1 2 3
ADD 0 2 1
KTH 0 2 2
```

**Output:**

```
3
```

**Explanation:**

After adding 1, the array is `[2,3,4]`, so the 2nd smallest in `[0,2]` is 3.

![Example Visualization](../images/SEG-012/example-1.png)

## Notes

- This requires advanced data structures to support order statistics under updates
- Solutions may use sqrt decomposition or offline processing
- Correctness is more important than a specific technique
- Ensure output uses 64-bit values

## Related Topics

Order Statistics, Segment Tree, Range Updates

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<Long> process(long[] arr, List<String[]> ops) {
        // Your implementation here
        return new ArrayList<>();
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
            if (op.equals("ADD")) {
                ops.add(new String[]{op, sc.next(), sc.next(), sc.next()});
            } else {
                ops.add(new String[]{op, sc.next(), sc.next(), sc.next()});
            }
        }

        Solution solution = new Solution();
        List<Long> out = solution.process(arr, ops);
        for (long v : out) System.out.println(v);
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
        if op == "ADD":
            ops.append([op, next(it), next(it), next(it)])
        else:
            ops.append([op, next(it), next(it), next(it)])

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
    vector<long long> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
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
        if (op == "ADD") {
            string l, r, x;
            cin >> l >> r >> x;
            ops.push_back({op, l, r, x});
        } else {
            string l, r, k;
            cin >> l >> r >> k;
            ops.push_back({op, l, r, k});
        }
    }

    Solution solution;
    vector<long long> out = solution.process(arr, ops);
    for (long long v : out) cout << v << "\n";
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
    if (op === "ADD") {
      ops.push([op, data[idx++], data[idx++], data[idx++]]);
    } else {
      ops.push([op, data[idx++], data[idx++], data[idx++]]);
    }
  }

  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```
