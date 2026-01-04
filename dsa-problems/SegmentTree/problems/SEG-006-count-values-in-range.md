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
    public void processOperations(int n, int q, long[] a, List<String> ops) {
        // Implement here
        // For each COUNT, print the number of values in range
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
        # For each COUNT, print the number of values in range
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
        // For each COUNT, cout << count << endl;
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
    // For each COUNT, console.log(count);
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
