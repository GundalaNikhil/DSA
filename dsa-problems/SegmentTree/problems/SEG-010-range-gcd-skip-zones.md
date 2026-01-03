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
        //Implement here
        return new ArrayList<>();
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
            int f = sc.nextInt();
            boolean[] forbidden = new boolean[n];
            for (int i = 0; i < f; i++) {
                forbidden[sc.nextInt()] = true;
            }
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                if (type.equals("TOGGLE")) {
                    ops.add(new String[]{type, sc.next()});
                } else if (type.equals("SET")) {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Integer> results = sol.process(arr, forbidden, ops);
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

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def process(arr: list[int], forbidden: list[bool], ops: list[list[str]]) -> list[int]:
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
    f_count = int(next(it))
    forbidden = [False] * n
    for _ in range(f_count):
        forbidden[int(next(it))] = True
        
    ops = []
    for _ in range(q):
        type = next(it)
        if type == "TOGGLE":
            ops.append([type, next(it)])
        elif type == "SET":
            ops.append([type, next(it), next(it)])
        else:
            ops.append([type, next(it), next(it)])
            
    results = process(arr, forbidden, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    a = abs(a); b = abs(b);
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

class Solution {
public:
    vector<int> process(const vector<int>& arr, const vector<bool>& forbidden, const vector<vector<string>>& ops) {
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
    int f;
    cin >> f;
    vector<bool> forbidden(n, false);
    for (int i = 0; i < f; i++) {
        int idx;
        cin >> idx;
        forbidden[idx] = true;
    }
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "TOGGLE") {
            string idx;
            cin >> idx;
            ops[i] = {type, idx};
        } else {
            string a, b;
            cin >> a >> b;
            ops[i] = {type, a, b};
        }
    }
    Solution sol;
    vector<int> results = sol.process(arr, forbidden, ops);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  process(arr, forbidden, ops) {
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
  const f = parseInt(data[idx++], 10);
  const forbidden = Array(n).fill(false);
  for (let i = 0; i < f; i++) forbidden[parseInt(data[idx++], 10)] = true;
  const ops = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "TOGGLE") {
      ops.push([type, data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, forbidden, ops);
  console.log(out.join("\n"));
});
```

