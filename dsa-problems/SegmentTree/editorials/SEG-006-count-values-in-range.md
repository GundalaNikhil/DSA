---
title: Count of Values in Range
slug: count-values-in-range
difficulty: Medium
difficulty_score: 51
tags:
- Segment Tree
- Fenwick Tree
- Range Counting
problem_id: SEG_COUNT_VALUES_IN_RANGE__1637
display_id: SEG-006
topics:
- Segment Tree
- BIT
- Range Queries
---
# Count of Values in Range - Editorial

## Problem Summary

You are given an array `a`. You need to support:
1.  **SET i x**: Update `a[i] = x`.
2.  **COUNT l r x y**: Count how many elements in `a[l..r]` satisfy `x <= a[i] <= y`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x, y <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Product Inventory System**.
-   **Set**: Update the price of a specific product.
-   **Count**: A customer asks, "How many products in the 'Electronics' category (indices `l` to `r`) cost between `100 and`500?"

## Problem Exploration

### 1. 2D Range Counting
This problem can be mapped to counting points in a 2D plane.
-   Index `i` corresponds to X-coordinate.
-   Value `a[i]` corresponds to Y-coordinate.
-   **SET i x**: Remove point `(i, old_val)`, add point `(i, x)`.
-   **COUNT l r x y**: Count points in rectangle `[l, r] x [x, y]`.

### 2. Data Structures
-   **2D Segment Tree**: Supports dynamic updates and range sums. Space/Time `O(log^2 N)`.
-   **Fenwick Tree of Segment Trees**: Similar to 2D Segment Tree.
-   **Square Root Decomposition**: `O(sqrtN)` per update/query.
-   **Merge Sort Tree**: Supports query in `O(log^2 N)`, but updates are `O(N)` or `O(log^2 N)` if dynamic (using BSTs/Treaps inside nodes).

Given `N, Q <= 200,000`, `O(sqrtN)` might be too slow (`200000 x 450 ~= 9 x 10^7`, borderline). `O(log^2 N)` is preferred (`200000 x 324 ~= 6 x 10^7`).

### 3. Coordinate Compression
Values are up to `10^9`. We must coordinate compress them to range `[0, N+Q]`.

## Approaches

### Approach 1: Fenwick Tree of Dynamic Segment Trees (or BIT of BITs)
We can use a Fenwick Tree over the **indices** `0..N-1`.
Each node in the Fenwick Tree stores a data structure representing the **values** in that range.
Since we need to count values in range `[x, y]`, the inner structure should support `add(val, +1)` and `query(val)`.
A Fenwick Tree inside a Fenwick Tree works!
-   Outer BIT: Index `i`.
-   Inner BIT: Value `v`.
-   **Update**: `update(i, val, delta)`:
    -   For `i` in outer BIT: `inner_bit[i].add(val, delta)`.
-   **Query**: `query(i, val)`:
    -   For `i` in outer BIT: `sum += inner_bit[i].query(val)`.
    -   Result is `query(r, y) - query(l-1, y) - query(r, x-1) + query(l-1, x-1)`.

**Complexity**: `O(log N * log (max_val))`. With coordinate compression, `O(log^2 N)`.

### Approach 2: Square Root Decomposition
Divide into blocks. Maintain sorted values in each block.
-   **Update**: Remove old, insert new (maintain sorted). `O(sqrtN)`.
-   **Query**: Binary search in full blocks, brute force partials. `O(sqrtN log N)`.
This is easier to implement but slower. Given 2 seconds, it might pass.

Let's stick to the **BIT of BITs** (or BIT of Segment Trees) approach for optimal performance.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int n;
    private int maxVal;
    // We use a Map for the inner BITs to save space, or coordinate compress.
    // Coordinate compression is better.
    
    public List<Integer> process(int[] arr, List<String[]> ops) {
        n = arr.length;
        
        // Coordinate Compression
        Set<Integer> values = new HashSet<>();
        for (int x : arr) values.add(x);
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                values.add(Integer.parseInt(op[2]));
            } else {
                values.add(Integer.parseInt(op[3])); // x
                values.add(Integer.parseInt(op[4])); // y
            }
        }
        List<Integer> sortedVals = new ArrayList<>(values);
        Collections.sort(sortedVals);
        Map<Integer, Integer> valMap = new HashMap<>();
        for (int i = 0; i < sortedVals.size(); i++) {
            valMap.put(sortedVals.get(i), i + 1); // 1-based for BIT
        }
        maxVal = sortedVals.size();
        
        // Initialize BIT of BITs
        // Outer BIT size N, Inner BIT size maxVal
        // To save space, we can use dynamic allocation or just arrays if N*maxVal fits?
        // N=200k, maxVal=400k. 200k * 400k is too big.
        // We need dynamic nodes or Map<Integer, Integer> for inner BITs.
        // Or simpler: Use Square Root Decomposition for implementation simplicity and memory safety.
        // Given constraints and typical interview setting, SQRT is often accepted.
        // However, let's try to implement a memory-efficient BIT of BITs using HashMap for inner nodes.
        
        // For dynamic, "BIT of dynamic Segment Trees" is standard.
        // Let's use SQRT Decomposition for code clarity and safety against OOM.
        
        return sqrtDecomposition(arr, ops);
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

public class Main {
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
    n = len(arr)
    block_size = int((n * 0.5) ** 0.5) + 1
    if block_size < 50: block_size = 50
    
    blocks = []
    for i in range(0, n, block_size):
        chunk = arr[i : i + block_size]
        blocks.append(sorted(chunk))
        
    results = []
    
    for op in ops:
        if op[0] == "SET":
            idx = int(op[1])
            val = int(op[2])
            old_val = arr[idx]
            arr[idx] = val
            
            b_idx = idx // block_size
            block = blocks[b_idx]
            
            # Remove old_val (one instance)
            # bisect doesn't remove. list.remove is O(B)
            # We can use bisect to find index to remove faster?
            # list.pop(index) is O(B).
            idx_in_block = bisect.bisect_left(block, old_val)
            block.pop(idx_in_block)
            
            # Insert val
            bisect.insort(block, val)
            
        else:
            l = int(op[1])
            r = int(op[2])
            x = int(op[3])
            y = int(op[4])
            
            count = 0
            start_block = l // block_size
            end_block = r // block_size
            
            if start_block == end_block:
                for i in range(l, r + 1):
                    if x <= arr[i] <= y:
                        count += 1
            else:
                # Left partial
                for i in range(l, (start_block + 1) * block_size):
                    if x <= arr[i] <= y:
                        count += 1
                
                # Full blocks
                for i in range(start_block + 1, end_block):
                    b = blocks[i]
                    # Count in [x, y]
                    # bisect_right(y) - bisect_left(x)
                    upper = bisect.bisect_right(b, y)
                    lower = bisect.bisect_left(b, x)
                    count += (upper - lower)
                    
                # Right partial
                for i in range(end_block * block_size, r + 1):
                    if x <= arr[i] <= y:
                        count += 1
                        
            results.append(count)
            
    return results

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
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
        vector<int> arr = inputArr;
        int n = arr.size();
        int blockSize = sqrt(n * log2(n + 1)) + 1;
        if (blockSize < 50) blockSize = 50;
        
        int numBlocks = (n + blockSize - 1) / blockSize;
        vector<vector<int>> blocks(numBlocks);
        
        for (int i = 0; i < n; i++) {
            blocks[i / blockSize].push_back(arr[i]);
        }
        for (auto& b : blocks) sort(b.begin(), b.end());
        
        vector<int> results;
        
        for (const auto& op : ops) {
            if (op[0] == "SET") {
                int idx = stoi(op[1]);
                int val = stoi(op[2]);
                int oldVal = arr[idx];
                arr[idx] = val;
                
                auto& block = blocks[idx / blockSize];
                auto it = lower_bound(block.begin(), block.end(), oldVal);
                block.erase(it);
                auto it2 = upper_bound(block.begin(), block.end(), val);
                block.insert(it2, val);
                
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                int x = stoi(op[3]);
                int y = stoi(op[4]);
                
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
                        const auto& b = blocks[i];
                        auto upper = upper_bound(b.begin(), b.end(), y);
                        auto lower = lower_bound(b.begin(), b.end(), x);
                        count += distance(lower, upper);
                    }
                    for (int i = endBlock * blockSize; i <= r; i++) {
                        if (arr[i] >= x && arr[i] <= y) count++;
                    }
                }
                results.push_back(count);
            }
        }
        return results;
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
    const n = arr.length;
    const blockSize = Math.floor(Math.sqrt(n * Math.log2(n + 1))) + 1;
    const safeBlockSize = blockSize < 50 ? 50 : blockSize;
    
    const blocks = [];
    for (let i = 0; i < n; i += safeBlockSize) {
      const chunk = arr.slice(i, i + safeBlockSize);
      chunk.sort((a, b) => a - b);
      blocks.push(chunk);
    }
    
    const results = [];
    
    const lowerBound = (list, val) => {
      let l = 0, r = list.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (list[mid] >= val) r = mid;
        else l = mid + 1;
      }
      return l;
    };
    
    const upperBound = (list, val) => {
      let l = 0, r = list.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (list[mid] > val) r = mid;
        else l = mid + 1;
      }
      return l;
    };

    for (const op of ops) {
      if (op[0] === "SET") {
        const idx = parseInt(op[1], 10);
        const val = parseInt(op[2], 10);
        const oldVal = arr[idx];
        arr[idx] = val;
        
        const bIdx = Math.floor(idx / safeBlockSize);
        const block = blocks[bIdx];
        
        const removePos = lowerBound(block, oldVal);
        block.splice(removePos, 1);
        
        const insertPos = upperBound(block, val);
        block.splice(insertPos, 0, val);
        
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const x = parseInt(op[3], 10);
        const y = parseInt(op[4], 10);
        
        let count = 0;
        const startBlock = Math.floor(l / safeBlockSize);
        const endBlock = Math.floor(r / safeBlockSize);
        
        if (startBlock === endBlock) {
          for (let i = l; i <= r; i++) {
            if (arr[i] >= x && arr[i] <= y) count++;
          }
        } else {
          for (let i = l; i < (startBlock + 1) * safeBlockSize; i++) {
            if (arr[i] >= x && arr[i] <= y) count++;
          }
          for (let i = startBlock + 1; i < endBlock; i++) {
            const b = blocks[i];
            const upper = upperBound(b, y);
            const lower = lowerBound(b, x);
            count += (upper - lower);
          }
          for (let i = endBlock * safeBlockSize; i <= r; i++) {
            if (arr[i] >= x && arr[i] <= y) count++;
          }
        }
        results.push(count);
      }
    }
    return results;
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

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 1`
`1 5 2`
`COUNT 0 2 2 5`

1.  **Initial**: `[1, 5, 2]`.
2.  **Query**: `l=0, r=2, x=2, y=5`.
    -   Check `a[0]=1`: `1 notin [2, 5]`.
    -   Check `a[1]=5`: `5 in [2, 5]`. Count = 1.
    -   Check `a[2]=2`: `2 in [2, 5]`. Count = 2.
3.  **Result**: 2.

## Proof of Correctness

-   **Square Root Decomposition**: Correctly splits range into full blocks and partial blocks.
-   **Full Blocks**: Sorted property allows binary search to count elements in range `[x, y]` in `O(log B)`.
-   **Partial Blocks**: Brute force check is correct.
-   **Updates**: Maintaining sorted order ensures future queries are correct.

## Interview Extensions

1.  **2D Range Sum?**
    -   This is effectively 2D range count. 2D Range Sum is similar but sums values instead of counting.
2.  **Range Updates?**
    -   If we had `ADD l r v`, we'd need lazy propagation on blocks. For sorted blocks, adding `v` shifts the range `[x, y]` to `[x-v, y-v]`.

### Common Mistakes

-   **Block Indices**: Careful with `startBlock` and `endBlock` logic.
-   **Binary Search**: Ensure `upperBound` and `lowerBound` are implemented correctly for the range `[x, y]`.
    -   Count is `upperBound(y) - lowerBound(x)`.
