---
problem_id: SEG_INVERSION_COUNT_UPDATES__5048
display_id: SEG-004
slug: inversion-count-updates
title: "Inversion Count Updates"
difficulty: Medium
difficulty_score: 58
topics:
  - Segment Tree
  - Fenwick Tree
  - Inversions
tags:
  - inversion-count
  - segment-tree
  - fenwick
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-004: Inversion Count Updates

## Problem Statement

You are given an array `a`. An inversion is a pair `(i, j)` with `i < j` and `a[i] > a[j]`.

Process point updates `SET i x`. After each update, output the current inversion count of the whole array.

![Problem Illustration](../images/SEG-004/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET i x`

## Output Format

- Print one line after each update: the inversion count

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
3 1 2
SET 1 4
```

**Output:**

```
2
```

**Explanation:**

After setting `a[1]=4`, the array is `[3,4,2]` with inversions `(3,2)` and `(4,2)`.

![Example Visualization](../images/SEG-004/example-1.png)

## Notes

- Coordinate-compress values to a compact range
- Use a BIT or segment tree to count inversions
- Updating a position affects pairs with its left and right sides
- Output fits in 64-bit signed integer

## Related Topics

Inversion Count, Fenwick Tree, Segment Tree

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<Long> process(int[] arr, List<int[]> updates) {
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
        List<int[]> updates = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            sc.next();
            int idx = sc.nextInt();
            int val = sc.nextInt();
            updates.add(new int[]{idx, val});
        }

        Solution solution = new Solution();
        List<Long> out = solution.process(arr, updates);
        for (long v : out) System.out.println(v);
        sc.close();
    }
}
```

### Python

```python
def process(arr: list[int], updates: list[tuple[int, int]]) -> list[int]:
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
    updates = []
    for _ in range(q):
        _ = next(it)
        idx = int(next(it))
        val = int(next(it))
        updates.append((idx, val))

    out = process(arr, updates)
    sys.stdout.write("\n".join(str(x) for x in out))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<long long> process(const vector<int>& arr, const vector<pair<int,int>>& updates) {
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
    vector<pair<int,int>> updates;
    updates.reserve(q);
    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        int idx, val;
        cin >> idx >> val;
        updates.push_back({idx, val});
    }

    Solution solution;
    vector<long long> out = solution.process(arr, updates);
    for (long long v : out) cout << v << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  process(arr, updates) {
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
  const updates = [];
  for (let i = 0; i < q; i++) {
    idx++; // skip op
    const pos = parseInt(data[idx++], 10);
    const val = parseInt(data[idx++], 10);
    updates.push([pos, val]);
  }

  const solution = new Solution();
  const out = solution.process(arr, updates);
  console.log(out.join("\n"));
});
```
