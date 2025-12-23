---
title: Range Sum with Point Updates and Undo
slug: range-sum-point-updates-undo
difficulty: Medium
difficulty_score: 52
tags:
- Segment Tree
- Fenwick Tree
- Rollback
problem_id: SEG_RANGE_SUM_POINT_UPDATES_UNDO__5472
display_id: SEG-001
topics:
- Segment Tree
- Fenwick Tree
- Rollback
---
# Range Sum with Point Updates and Undo - Editorial

## Problem Summary

You are given an array of integers and need to support three operations:
1.  **UPDATE**: Change the value at a specific index.
2.  **QUERY**: Calculate the sum of elements in a range `[L, R]` modulo `M`.
3.  **UNDO**: Revert the last `k` updates.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= M <= 10^9+7`
- `0 <= k <= 100`
## Real-World Scenario

Imagine a **Financial Ledger System**.
-   **Update**: A transaction modifies an account balance.
-   **Query**: An auditor checks the total assets across a range of accounts.
-   **Undo**: A batch of erroneous transactions needs to be rolled back quickly.

## Problem Exploration

### 1. Operations Analysis
-   **Point Update**: Standard operation supported by Segment Trees or Fenwick Trees in `O(log N)`.
-   **Range Sum**: Standard operation supported by Segment Trees or Fenwick Trees in `O(log N)`.
-   **Undo**: This is the tricky part. We need to revert the state of the array to what it was before the last `k` updates.

### 2. Handling Undo
Since we need to undo *updates*, we must store the history of changes.
For every `UPDATE i x`, we should record:
-   The index `i`.
-   The *previous* value at `a[i]` (so we can restore it).

When we receive `UNDO k`, we pop the last `k` updates from our history stack and apply the reverse operation: set `a[i] = prev_value`.

### 3. Data Structures
-   **Fenwick Tree (Binary Indexed Tree)**: Easier to implement for point updates and prefix sums. Range sum `[L, R]` is `query(R) - query(L-1)`.
-   **Segment Tree**: Also works, slightly more code but more flexible if operations get complex (e.g., range max). Since we only need sum, Fenwick is sufficient and faster.

## Approaches

### Approach 1: Fenwick Tree with History Stack
1.  Build a Fenwick Tree from the initial array.
2.  Maintain a stack `history` storing tuples `(index, old_value)`.
3.  **UPDATE i x**:
    -   Get current value `old_val = a[i]`.
    -   Update Fenwick Tree: `add(i, x - old_val)`.
    -   Update array: `a[i] = x`.
    -   Push `(i, old_val)` to `history`.
4.  **QUERY l r**:
    -   Return `(query(r) - query(l-1)) % M`. Handle negative results by adding `M`.
5.  **UNDO k**:
    -   Repeat `k` times:
        -   Pop `(idx, val)` from `history`.
        -   Current value is `a[idx]`.
        -   Update Fenwick: `add(idx, val - a[idx])`.
        -   Restore array: `a[idx] = val`.

**Complexity**:
-   Update: `O(log N)`
-   Query: `O(log N)`
-   Undo: `O(k log N)`
-   Total: `O((N + Q) log N)` since total undos are bounded or proportional to updates.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private long[] bit;
    private int n;
    private long mod;

    public List<Long> process(int[] arr, long mod, List<String[]> ops) {
        this.n = arr.length;
        this.mod = mod;
        this.bit = new long[n + 1];
        
        // Build BIT
        for (int i = 0; i < n; i++) {
            add(i + 1, arr[i]);
        }

        // Current state of array to track values for updates
        long[] currentArr = new long[n];
        for(int i=0; i<n; i++) currentArr[i] = arr[i];

        // History stack: stores {index, oldValue}
        Stack<long[]> history = new Stack<>();
        List<Long> results = new ArrayList<>();

        for (String[] op : ops) {
            String type = op[0];
            if (type.equals("UPDATE")) {
                int idx = Integer.parseInt(op[1]); // 0-based from input?
                // Problem statement usually implies 0-based or 1-based. 
                // Example: UPDATE 2 10. Array 1 2 3 4 5.
                // If 0-based, index 2 is 3. 
                // Let's assume 0-based based on "QUERY 0 4".
                long val = Long.parseLong(op[2]);
                
                long oldVal = currentArr[idx];
                history.push(new long[]{idx, oldVal});
                
                long diff = (val - oldVal) % mod;
                if (diff < 0) diff += mod;
                
                add(idx + 1, diff);
                currentArr[idx] = val;

            } else if (type.equals("QUERY")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                long res = (query(r + 1) - query(l)) % mod;
                if (res < 0) res += mod;
                results.add(res);

            } else if (type.equals("UNDO")) {
                int k = Integer.parseInt(op[1]);
                while (k > 0 && !history.isEmpty()) {
                    long[] last = history.pop();
                    int idx = (int) last[0];
                    long oldVal = last[1];
                    
                    long currentVal = currentArr[idx];
                    long diff = (oldVal - currentVal) % mod;
                    if (diff < 0) diff += mod;
                    
                    add(idx + 1, diff);
                    currentArr[idx] = oldVal;
                    k--;
                }
            }
        }
        return results;
    }

    private void add(int idx, long val) {
        for (; idx <= n; idx += idx & -idx) {
            bit[idx] = (bit[idx] + val) % mod;
        }
    }

    private long query(int idx) {
        long sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum = (sum + bit[idx]) % mod;
        }
        return sum;
    }
}
```

### Python

```python
def process(arr: list[int], mod: int, ops: list[list[str]]) -> list[int]:
    n = len(arr)
    bit = [0] * (n + 1)
    
    def add(idx, val):
        idx += 1  # 1-based
        while idx <= n:
            bit[idx] = (bit[idx] + val) % mod
            idx += idx & (-idx)
            
    def query(idx):
        idx += 1
        s = 0
        while idx > 0:
            s = (s + bit[idx]) % mod
            idx -= idx & (-idx)
        return s

    # Build BIT
    for i, x in enumerate(arr):
        add(i, x)
        
    current_arr = list(arr)
    history = [] # Stack of (index, old_value)
    results = []
    
    for op in ops:
        type = op[0]
        if type == "UPDATE":
            idx = int(op[1])
            val = int(op[2])
            
            old_val = current_arr[idx]
            history.append((idx, old_val))
            
            diff = (val - old_val) % mod
            add(idx, diff)
            current_arr[idx] = val
            
        elif type == "QUERY":
            l = int(op[1])
            r = int(op[2])
            # Sum [l, r] is query(r) - query(l-1)
            # My query function is inclusive 0..idx
            # So query(r) returns sum 0..r
            # query(l-1) returns sum 0..l-1
            res = (query(r) - query(l - 1)) % mod
            results.append(res)
            
        elif type == "UNDO":
            k = int(op[1])
            while k > 0 and history:
                idx, old_val = history.pop()
                current_val = current_arr[idx]
                
                diff = (old_val - current_val) % mod
                add(idx, diff)
                current_arr[idx] = old_val
                k -= 1
                
    return results
```

### C++

```cpp
#include <vector>
#include <string>
#include <stack>

using namespace std;

class Solution {
    vector<long long> bit;
    int n;
    long long mod;

    void add(int idx, long long val) {
        idx++; // 1-based
        for (; idx <= n; idx += idx & -idx) {
            bit[idx] = (bit[idx] + val) % mod;
            if (bit[idx] < 0) bit[idx] += mod;
        }
    }

    long long query(int idx) {
        idx++;
        long long sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum = (sum + bit[idx]) % mod;
        }
        return sum;
    }

public:
    vector<long long> process(const vector<int>& arr, long long mod, const vector<vector<string>>& ops) {
        this->n = arr.size();
        this->mod = mod;
        bit.assign(n + 1, 0);

        // Build BIT
        for (int i = 0; i < n; i++) {
            add(i, arr[i]);
        }

        vector<long long> currentArr(arr.begin(), arr.end());
        stack<pair<int, long long>> history;
        vector<long long> results;

        for (const auto& op : ops) {
            if (op[0] == "UPDATE") {
                int idx = stoi(op[1]);
                long long val = stoll(op[2]);

                long long oldVal = currentArr[idx];
                history.push({idx, oldVal});

                long long diff = (val - oldVal) % mod;
                if (diff < 0) diff += mod;

                add(idx, diff);
                currentArr[idx] = val;

            } else if (op[0] == "QUERY") {
                int l = stoi(op[1]);
                int r = stoi(op[2]);

                long long res = (query(r) - query(l - 1)) % mod;
                if (res < 0) res += mod;
                results.push_back(res);

            } else if (op[0] == "UNDO") {
                int k = stoi(op[1]);
                while (k > 0 && !history.empty()) {
                    auto last = history.top();
                    history.pop();
                    int idx = last.first;
                    long long oldVal = last.second;

                    long long currentVal = currentArr[idx];
                    long long diff = (oldVal - currentVal) % mod;
                    if (diff < 0) diff += mod;

                    add(idx, diff);
                    currentArr[idx] = oldVal;
                    k--;
                }
            }
        }
        return results;
    }
};
```

### JavaScript

```javascript
class Solution {
  process(arr, mod, ops) {
    const n = arr.length;
    const bit = new Array(n + 1).fill(0n);
    const bigMod = BigInt(mod);

    const add = (idx, val) => {
      idx++; // 1-based
      while (idx <= n) {
        bit[idx] = (bit[idx] + val) % bigMod;
        if (bit[idx] < 0n) bit[idx] += bigMod;
        idx += idx & -idx;
      }
    };

    const query = (idx) => {
      idx++;
      let sum = 0n;
      while (idx > 0) {
        sum = (sum + bit[idx]) % bigMod;
        idx -= idx & -idx;
      }
      return sum;
    };

    // Build BIT
    for (let i = 0; i < n; i++) {
      add(i, BigInt(arr[i]));
    }

    const currentArr = arr.map(BigInt);
    const history = []; // Stack
    const results = [];

    for (const op of ops) {
      const type = op[0];
      if (type === "UPDATE") {
        const idx = parseInt(op[1], 10);
        const val = BigInt(op[2]);

        const oldVal = currentArr[idx];
        history.push({ idx, oldVal });

        let diff = (val - oldVal) % bigMod;
        if (diff < 0n) diff += bigMod;

        add(idx, diff);
        currentArr[idx] = val;

      } else if (type === "QUERY") {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);

        let res = (query(r) - query(l - 1)) % bigMod;
        if (res < 0n) res += bigMod;
        results.push(Number(res)); // Convert back to number for output

      } else if (type === "UNDO") {
        let k = parseInt(op[1], 10);
        while (k > 0 && history.length > 0) {
          const { idx, oldVal } = history.pop();
          const currentVal = currentArr[idx];

          let diff = (oldVal - currentVal) % bigMod;
          if (diff < 0n) diff += bigMod;

          add(idx, diff);
          currentArr[idx] = oldVal;
          k--;
        }
      }
    }
    return results;
  }
}
```

## Test Case Walkthrough

**Input:**
`5 5 1000`
`1 2 3 4 5`
1.  `QUERY 1 3`: Sum indices 1, 2, 3 (values 2, 3, 4). Sum = 9. Output 9.
2.  `UPDATE 2 10`: `a[2]` changes from 3 to 10. History: `[(2, 3)]`. Array: `1 2 10 4 5`.
3.  `QUERY 0 4`: Sum all. `1+2+10+4+5 = 22`. Output 22.
4.  `UNDO 1`: Pop `(2, 3)`. Restore `a[2]` to 3. Array: `1 2 3 4 5`.
5.  `QUERY 0 4`: Sum all. `1+2+3+4+5 = 15`. Output 15.

**Output:**
9
22
15

## Proof of Correctness

-   **Fenwick Tree**: Correctly maintains prefix sums under point updates.
-   **Undo Logic**: By storing the exact previous value, we can compute the difference `old_val - current_val` and apply it to the Fenwick Tree, effectively reversing the update. Since updates are processed sequentially, a stack correctly reverses the order.
-   **Modulo Arithmetic**: All additions and subtractions are modulo `M`, handling negative results correctly.

## Interview Extensions

1.  **Range Updates?**
    -   If we had Range Updates and Point Queries, we could use a BIT on the difference array.
    -   If Range Updates and Range Queries, we need Segment Tree with Lazy Propagation. Undo becomes more complex (store old node states or reverse operations).
2.  **Persistent Segment Tree?**
    -   We could use a Persistent Segment Tree to access *any* previous version, not just undoing the last `k`. This would be `O(log N)` per update/query but use `O(Q log N)` space.

### Common Mistakes

-   **0-based vs 1-based Indexing**: Fenwick Trees are naturally 1-based. Input is usually 0-based. Be careful with conversions.
-   **Modulo Negative Numbers**: In languages like Java/C++, `%` can return negative numbers. Always add `mod` before taking modulo again.
-   **History Stack**: Ensure you push *before* updating the array.
