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
    public void processOperations(int n, int q, long[] a, Set<Integer> forbidden, List<String> ops) {
        // Implement here
        // For each GCD, print the gcd value
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextLong();
            int f = sc.nextInt();
            Set<Integer> forbidden = new HashSet<>();
            for (int i = 0; i < f; i++) forbidden.add(sc.nextInt());
            sc.nextLine(); // consume newline
            List<String> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                ops.add(sc.nextLine());
            }
            Solution sol = new Solution();
            sol.processOperations(n, q, a, forbidden, ops);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def process_operations(self, n, q, a, forbidden, ops):
        # Implement here
        # For each GCD, print the gcd value
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    first_line = list(map(int, input_data[0].split()))
    n, q = first_line[0], first_line[1]
    a = list(map(int, input_data[1].split()))
    f = int(input_data[2])
    forbidden = set()
    ptr = 3
    for _ in range(f):
        forbidden.add(int(input_data[ptr]))
        ptr += 1
    ops = input_data[ptr : ptr + q]

    sol = Solution()
    sol.process_operations(n, q, a, forbidden, ops)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <numeric>

using namespace std;

class Solution {
public:
    void processOperations(int n, int q, vector<long long>& a, unordered_set<int>& forbidden, const vector<string>& ops) {
        // Implement here
        // For each GCD, cout << val << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (cin >> n >> q) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        int f;
        cin >> f;
        unordered_set<int> forbidden;
        for (int i = 0; i < f; i++) {
            int idx;
            cin >> idx;
            forbidden.insert(idx);
        }
        string dummy;
        getline(cin, dummy); // consume newline
        vector<string> ops(q);
        for (int i = 0; i < q; i++) {
            getline(cin, ops[i]);
        }

        Solution sol;
        sol.processOperations(n, q, a, forbidden, ops);
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processOperations(n, q, a, forbidden, ops) {
    // Implement here
    // For each GCD, console.log(val.toString());
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
  if (input.length < 3) return;
  const [n, q] = input[0].split(/\s+/).map(Number);
  const a = input[1].split(/\s+/).map(BigInt);
  const f = parseInt(input[2]);
  const forbidden = new Set();
  let ptr = 3;
  for (let i = 0; i < f; i++) {
    forbidden.add(parseInt(input[ptr]));
    ptr++;
  }
  const ops = input.slice(ptr, ptr + q);

  const sol = new Solution();
  sol.processOperations(n, q, a, forbidden, ops);
});
```
