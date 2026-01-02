---
problem_id: SEG_RANGE_SUM_MULTIPLE_POWERS__4175
display_id: SEG-013
slug: range-sum-multiple-powers
title: "Range Sum of Multiple Powers"
difficulty: Medium
difficulty_score: 55
topics:
  - Segment Tree
  - Modular Arithmetic
  - Range Sum
tags:
  - segment-tree
  - range-sum
  - modular
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-013: Range Sum of Multiple Powers

## Problem Statement

Maintain an array `a` with point updates and queries asking for the sum of powers in a range.

Operations:

- `SET i x`: set `a[i] = x`
- `SUM l r p`: output `sum(a[i]^p)` for `i` in `[l,r]` where `p` is 1, 2, or 3

All answers are modulo `MOD = 1000000007`.

![Problem Illustration](../images/SEG-013/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `SUM`

## Output Format

- For each `SUM`, print the sum modulo `MOD`

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `p` is in `{1,2,3}`

## Example

**Input:**

```
2 2
2 3
SUM 0 1 2
SUM 0 1 3
```

**Output:**

```
13
35
```

**Explanation:**

`2^2 + 3^2 = 13` and `2^3 + 3^3 = 35`.

![Example Visualization](../images/SEG-013/example-1.png)

## Notes

- Store sums of powers 1, 2, and 3 per segment
- Recompute these values on point updates
- Use modular arithmetic for all sums
- Each operation is O(log n)

## Related Topics

Segment Tree, Modular Arithmetic, Range Sum

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Long> process(long[] arr, List<String[]> ops) {
        // Implementation here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                if (type.equals("SET")) {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Long> results = sol.process(arr, ops);
            for (long res : results) {
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

class Solution:
    def process(self, arr: list[int], ops: list[list[str]]) -> list[int]:
        # Implementation here
        return []

def main():
    import sys
    sys.setrecursionlimit(300000)
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    ops = []
    for _ in range(q):
        type = next(it)
        if type == "SET":
            ops.append([type, next(it), next(it)])
        else:
            ops.append([type, next(it), next(it), next(it)])
    
    sol = Solution()
    results = sol.process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<long long> process(const vector<long long>& inputArr, const vector<vector<string>>& ops) {
        // Implementation here
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
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "SET") {
            string a, b;
            cin >> a >> b;
            ops[i] = {type, a, b};
        } else {
            string a, b, c;
            cin >> a >> b >> c;
            ops[i] = {type, a, b, c};
        }
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  process(arr, ops) {
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
  const ops = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "SET") {
      ops.push([type, data[idx++], data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```
