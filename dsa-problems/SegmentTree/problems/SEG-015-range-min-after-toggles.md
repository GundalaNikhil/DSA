---
problem_id: SEG_RANGE_MIN_AFTER_TOGGLES__5728
display_id: SEG-015
slug: range-min-after-toggles
title: "Range Min After Additive Toggles"
difficulty: Medium
difficulty_score: 60
topics:
  - Segment Tree
  - Lazy Propagation
  - Range Queries
tags:
  - segment-tree
  - range-min
  - toggles
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-015: Range Min After Additive Toggles

## Problem Statement

Maintain an array with two update types and range minimum queries:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `FLIP l r`: multiply all elements in `a[l..r]` by `-1`
- `MIN l r`: output the minimum value in `a[l..r]`

![Problem Illustration](../images/SEG-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `ADD`, `FLIP`, or `MIN`

## Output Format

- For each `MIN`, print the minimum value

## Constraints

- `1 <= n, q <= 100000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
3 3
1 -2 3
FLIP 0 2
ADD 1 2 1
MIN 0 2
```

**Output:**

```
-2
```

**Explanation:**

After flip: `[-1, 2, -3]`, after add: `[-1, 3, -2]`, minimum is -2.

![Example Visualization](../images/SEG-015/example-1.png)

## Notes

- Track both min and max to handle sign flips
- Lazy tags include pending add and pending flip
- Apply flip by swapping min/max and negating
- Each operation runs in O(log n)

## Related Topics

Segment Tree, Lazy Propagation, Range Minimum

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Node {
        long minVal, maxVal;
        long lazyAdd;
        boolean lazyFlip;
        
        Node(long val) {
            minVal = maxVal = val;
            lazyAdd = 0;
            lazyFlip = false;
        }
        
        Node() {
            minVal = Long.MAX_VALUE;
            maxVal = Long.MIN_VALUE;
        }
    }
    
    private Node[] tree;
    private int n;

    public List<Long> process(long[] arr, List<String[]> ops) {
        return null;
    }

    private void push(int node, int start, int end) {
    }
    
    private void applyFlip(int node) {
    }
    
    private void applyAdd(int node, long val) {
    }

    private void merge(int node) {
    }

    private void build(long[] arr, int node, int start, int end) {
    }

    private void updateAdd(int node, int start, int end, int l, int r, long val) {
    }

    private void updateFlip(int node, int start, int end, int l, int r) {
    }

    private long query(int node, int start, int end, int l, int r) {
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
                } else if (type.equals("FLIP")) {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next()});
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

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

class Solution:
    def process(self, arr: list[int], ops: list[list[str]]) -> list[int]:
        return []
def main():
    import sys
    sys.setrecursionlimit(300000)
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
        elif type == "FLIP":
            ops.append([type, next(it), next(it)])
        else:
            ops.append([type, next(it), next(it)])
    
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
#include <algorithm>
#include <climits>
#include <iostream>

using namespace std;

struct Node {
    long long minVal, maxVal;
    long long lazyAdd;
    bool lazyFlip;
};

class Solution {
    vector<Node> tree;
    int n;

    void applyFlip(int node) {
    }

    void applyAdd(int node, long long val) {
    }

    void push(int node, int start, int end) {
    }

    void merge(int node) {
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
    }

    void updateAdd(int node, int start, int end, int l, int r, long long val) {
    }

    void updateFlip(int node, int start, int end, int l, int r) {
    }

    long long query(int node, int start, int end, int l, int r) {
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
        if (type == "ADD") {
            string a, b, c;
            cin >> a >> b >> c;
            ops[i] = {type, a, b, c};
        } else {
            string a, b;
            cin >> a >> b;
            ops[i] = {type, a, b};
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
    if (type === "ADD") {
      ops.push([type, data[idx++], data[idx++], data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```

