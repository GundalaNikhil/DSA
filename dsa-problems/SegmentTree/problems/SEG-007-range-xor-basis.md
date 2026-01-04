---
problem_id: SEG_RANGE_XOR_BASIS__8820
display_id: SEG-007
slug: range-xor-basis
title: "Range XOR Basis"
difficulty: Medium
difficulty_score: 56
topics:
  - Segment Tree
  - Bitwise
  - Linear Basis
tags:
  - segment-tree
  - xor
  - linear-basis
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-007: Range XOR Basis

## Problem Statement

Maintain an array `a` with point updates and queries asking for the maximum XOR value obtainable from any subset of elements in `a[l..r]`.

Operations:

- `SET i x`: set `a[i] = x`
- `MAXXOR l r`: output the maximum subset XOR in `[l, r]`

![Problem Illustration](../images/SEG-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `MAXXOR`

## Output Format

- For each `MAXXOR`, print the maximum XOR value

## Constraints

- `1 <= n, q <= 100000`
- `0 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
1 2 3
MAXXOR 0 2
```

**Output:**

```
3
```

**Explanation:**

The maximum XOR from subset `{1,2}` is 3.

![Example Visualization](../images/SEG-007/example-1.png)

## Notes

- Store a linear basis in each segment tree node
- Merge bases when combining segments
- Query basis to compute max XOR
- Time per operation: O(log n \* B)

## Related Topics

Linear Basis, Segment Tree, Bitwise

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processOperations(int n, int q, long[] a, List<String> ops) {
        // Implement here
        // For each MAXXOR, print the maximum XOR value
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
            sc.nextLine(); // consume newline
            List<String> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                ops.add(sc.nextLine());
            }
            Solution sol = new Solution();
            sol.processOperations(n, q, a, ops);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def process_operations(self, n, q, a, ops):
        # Implement here
        # For each MAXXOR, print the maximum XOR value
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    first_line = list(map(int, input_data[0].split()))
    n, q = first_line[0], first_line[1]
    a = list(map(int, input_data[1].split()))
    ops = input_data[2:2+q]

    sol = Solution()
    sol.process_operations(n, q, a, ops)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void processOperations(int n, int q, vector<long long>& a, const vector<string>& ops) {
        // Implement here
        // For each MAXXOR, cout << max_xor << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (cin >> n >> q) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        string dummy;
        getline(cin, dummy); // consume newline
        vector<string> ops(q);
        for (int i = 0; i < q; i++) {
            getline(cin, ops[i]);
        }

        Solution sol;
        sol.processOperations(n, q, a, ops);
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processOperations(n, q, a, ops) {
    // Implement here
    // For each MAXXOR, console.log(max_xor.toString());
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
  const [n, q] = input[0].split(/\s+/).map(Number);
  const a = input[1].split(/\s+/).map(BigInt);
  const ops = input.slice(2, 2 + q);

  const sol = new Solution();
  sol.processOperations(n, q, a, ops);
});
```
