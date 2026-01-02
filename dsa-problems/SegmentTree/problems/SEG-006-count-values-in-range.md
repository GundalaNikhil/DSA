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
    private int n;
    private int maxVal;
    // We use a Map for the inner BITs to save space, or coordinate compress.
    // Coordinate compression is better.
    
    public List<Integer> process(int[] arr, List<String[]> ops) {
        return null;
    }
    
    private List<Integer> sqrtDecomposition(int[] arr, List<String[]> ops) {
        int blockSize = (int) Math.sqrt(n * Math.log(n + 1) / Math.log(2)) + 1;
        List<List<Integer>> blocks = new ArrayList<>();
        int numBlocks = (n + blockSize - 1) / blockSize;
        
        for (int i = 0; i < numBlocks; i++) blocks.add(new ArrayList<>());
        for (int i = 0; i < n; i++) blocks.get(i / blockSize).add(arr[i]);
        for (List<Integer> b : blocks) Collections.sort(b);
        
        List<Integer> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                int val = Integer.parseInt(op[2]);
                int oldVal = arr[idx];
                arr[idx] = val;
                
                List<Integer> block = blocks.get(idx / blockSize);
                // Remove oldVal
                int pos = Collections.binarySearch(block, oldVal);
                if (pos < 0) pos = -pos - 1; // Should exist
                // Handle duplicates: binarySearch finds arbitrary. We just remove one.
                // But we must ensure we remove *a* instance.
                // If binarySearch returns index, it is present.
                block.remove(pos);
                
                // Add val
                int ins = Collections.binarySearch(block, val);
                if (ins < 0) ins = -ins - 1;
                block.add(ins, val);
                
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                int x = Integer.parseInt(op[3]);
                int y = Integer.parseInt(op[4]);
                
                int count = 0;
                int startBlock = l / blockSize;
                int endBlock = r / blockSize;
                
                if (startBlock == endBlock) {
                    for (int i = l; i <= r; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                } else {
                    for (int i = l; i < (startBlock + 1) * blockSize; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                    for (int i = startBlock + 1; i < endBlock; i++) {
                        List<Integer> b = blocks.get(i);
                        // Count elements in [x, y]
                        // upper_bound(y) - lower_bound(x)
                        int upper = upperBound(b, y);
                        int lower = lowerBound(b, x);
                        count += (upper - lower);
                    }
                    for (int i = endBlock * blockSize; i <= r; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                }
                results.add(count);
            }
        }
        return results;
    }
    
    private int lowerBound(List<Integer> list, int val) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) >= val) r = mid;
            else l = mid + 1;
        }
        return l;
    }
    
    private int upperBound(List<Integer> list, int val) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) > val) r = mid;
            else l = mid + 1;
        }
        return l;
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
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                if (type.equals("SET")) {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Integer> results = sol.process(arr, ops);
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
import bisect

def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    return []
def main():
    import sys
    def input_gen():
        return 0
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
            ops.append([type, next(it), next(it), next(it), next(it)])
    
    results = process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> process(const vector<int>& inputArr, const vector<vector<string>>& ops) {
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
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "SET") {
            string i_str, x_str;
            cin >> i_str >> x_str;
            ops[i] = {type, i_str, x_str};
        } else {
            string l_str, r_str, x_str, y_str;
            cin >> l_str >> r_str >> x_str >> y_str;
            ops[i] = {type, l_str, r_str, x_str, y_str};
        }
    }
    Solution sol;
    vector<int> results = sol.process(arr, ops);
    for (int res : results) {
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
    if (type === "SET") {
      ops.push([type, data[idx++], data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++], data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
```

