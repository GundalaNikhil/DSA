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
    static class Block {
        long[] sorted;
        long lazy;
        
        Block(int size) {
            sorted = new long[size];
            lazy = 0;
        }
    }
    
    private long[] arr;
    private Block[] blocks;
    private int blockSize;
    private int n;

    public List<Long> process(long[] inputArr, List<String[]> ops) {
        return null;
    }
    
    private void update(int l, int r, long x) {
    }
    
    private void partialUpdate(int bIdx, int l, int r, long x) {
    }
    
    private long query(int l, int r, int k) {
        return 0;
    }
    
    private int countLessEqual(int l, int r, long val) {
        return 0;
    }
    
    private int upperBound(long[] arr, long val) {
        return 0;
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
                if (type.equals("ADD")) {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next()});
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
from bisect import bisect_right

def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    return []
def main():
    import sys
    def input_gen():
        return 0

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
        if type == "ADD":
            ops.append([type, next(it), next(it), next(it)])
        else:
            ops.append([type, next(it), next(it), next(it)])
    
    results = process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

struct Block {
    vector<long long> sorted;
    long long lazy;
};

class Solution {
    vector<long long> arr;
    vector<Block> blocks;
    int blockSize;
    int n;

    void update(int l, int r, long long x) {
    }

    void partialUpdate(int bIdx, int l, int r, long long x) {
    }

    int countLessEqual(int l, int r, long long val) {
        return 0;
    }

public:
    vector<long long> process(const vector<long long>& inputArr, const vector<vector<string>>& ops) {
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
        string a, b, c;
        cin >> a >> b >> c;
        ops[i] = {type, a, b, c};
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
class Solution {
  process(arr, ops) {
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
  const ops = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    ops.push([type, data[idx++], data[idx++], data[idx++]]);
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```

