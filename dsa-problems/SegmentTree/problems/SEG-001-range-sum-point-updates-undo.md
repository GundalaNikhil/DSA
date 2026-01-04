---
problem_id: SEG_RANGE_SUM_POINT_UPDATES_UNDO__5472
display_id: SEG-001
slug: range-sum-point-updates-undo
title: "Range Sum with Point Updates and Undo"
difficulty: Medium
difficulty_score: 52
topics:
  - Segment Tree
  - Fenwick Tree
  - Rollback
tags:
  - segment-tree
  - fenwick
  - rollback
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-001: Range Sum with Point Updates and Undo

## Problem Statement

You maintain an array `a` under three operations:

- `UPDATE i x`: set `a[i] = x`
- `QUERY l r`: output the sum of `a[l..r]` modulo `M`
- `UNDO k`: revert the last `k` update operations (queries do not count)
  Process all operations in order and output answers for each `QUERY`.
  ![Problem Illustration](../images/SEG-001/problem-illustration.png)

## Input Format

- First line: integers `n`, `q`, and `M`
- Second line: `n` space-separated integers (initial array)
- Next `q` lines: one operation (`UPDATE`, `QUERY`, or `UNDO`)

## Output Format

- For each `QUERY`, print one line with the sum modulo `M`

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= M <= 10^9+7`
- `0 <= k <= 100`

## Example

**Input:**

```
5 5 1000
1 2 3 4 5
QUERY 1 3
UPDATE 2 10
QUERY 0 4
UNDO 1
QUERY 0 4
```

**Output:**

```
9
22
15
```

**Explanation:**
Sums are computed modulo 1000, and `UNDO 1` restores `a[2]` from 10 back to 3.
![Example Visualization](../images/SEG-001/example-1.png)

## Notes

- Keep a history stack of point updates to undo
- Segment tree or Fenwick tree supports point updates and range sums
- Each `UNDO` replays at most 100 updates
- Total time: O((n + q) log n)

## Related Topics

## Segment Tree, Fenwick Tree, Rollback

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processOperations(int n, int q, int m, long[] a, List<String> ops) {
        // Implement here
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int m = sc.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextLong();
            sc.nextLine(); // consume newline
            List<String> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                ops.add(sc.nextLine());
            }
            Solution sol = new Solution();
            sol.processOperations(n, q, m, a, ops);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def process_operations(self, n, q, m, a, ops):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    first_line = list(map(int, input_data[0].split()))
    n, q, m = first_line[0], first_line[1], first_line[2]
    a = list(map(int, input_data[1].split()))
    ops = input_data[2:2+q]

    sol = Solution()
    sol.process_operations(n, q, m, a, ops)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    void processOperations(int n, int q, int m, vector<long long>& a, const vector<string>& ops) {
        // Implement here
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q, m;
    if (cin >> n >> q >> m) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        string dummy;
        getline(cin, dummy); 
        vector<string> ops(q);
        for (int i = 0; i < q; i++) {
            getline(cin, ops[i]);
        }

        Solution sol;
        sol.processOperations(n, q, m, a, ops);
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processOperations(n, q, m, a, ops) {
    // Implement here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(line.trim());
}).on("close", () => {
  if (input.length < 2) return;
  const [n, q, m] = input[0].split(/\s+/).map(Number);
  const a = input[1].split(/\s+/).map(BigInt);
  const ops = input.slice(2, 2 + q);

  const sol = new Solution();
  sol.processOperations(n, q, m, a, ops);
});
```
