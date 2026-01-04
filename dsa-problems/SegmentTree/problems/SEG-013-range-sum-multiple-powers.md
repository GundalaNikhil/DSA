---
problem_id: SEG_RANGE_SUM_MULTIPLE_POWERS__4175
display_id: SEG-013
slug: range-sum-multiple-powers
title: "Range Sum of Multiple Powers"
difficulty: Medium
difficulty_score: 55
topics:
  - Segment Tree
  - Modular Arithmetic
  - Range Sum
tags:
  - segment-tree
  - range-sum
  - modular
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-013: Range Sum of Multiple Powers

## Problem Statement

Maintain an array `a` with point updates and queries asking for the sum of powers in a range.

Operations:

- `SET i x`: set `a[i] = x`
- `SUM l r p`: output `sum(a[i]^p)` for `i` in `[l,r]` where `p` is 1, 2, or 3

All answers are modulo `MOD = 1000000007`.

![Problem Illustration](../images/SEG-013/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `SUM`

## Output Format

- For each `SUM`, print the sum modulo `MOD`

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `p` is in `{1,2,3}`

## Example

**Input:**

```
2 2
2 3
SUM 0 1 2
SUM 0 1 3
```

**Output:**

```
13
35
```

**Explanation:**

`2^2 + 3^2 = 13` and `2^3 + 3^3 = 35`.

![Example Visualization](../images/SEG-013/example-1.png)

## Notes

- Store sums of powers 1, 2, and 3 per segment
- Recompute these values on point updates
- Use modular arithmetic for all sums
- Each operation is O(log n)

## Related Topics

Segment Tree, Modular Arithmetic, Range Sum

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processOperations(int n, int q, long[] a, List<String> ops) {
        // Implement here
        // For each SUM, print the sum modulo 1000000007
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
        # For each SUM, print the sum modulo 1000000007
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
        // For each SUM, cout << result << endl;
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
    // For each SUM, console.log(result.toString());
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
