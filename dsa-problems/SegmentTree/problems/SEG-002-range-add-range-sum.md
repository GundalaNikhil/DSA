---
problem_id: SEG_RANGE_ADD_RANGE_SUM__6841
display_id: SEG-002
slug: range-add-range-sum
title: "Range Add, Range Sum"
difficulty: Medium
difficulty_score: 46
topics:
  - Segment Tree
  - Lazy Propagation
  - Range Updates
tags:
  - segment-tree
  - lazy-propagation
  - range-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-002: Range Add, Range Sum

## Problem Statement

You are given an array `a`. Support two operations:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `SUM l r`: output the sum of `a[l..r]`

Process operations in order and output answers for each `SUM`.

![Problem Illustration](../images/SEG-002/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers (initial array)
- Next `q` lines: operations `ADD` or `SUM`

## Output Format

- For each `SUM`, print the range sum

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 3
0 0 0
ADD 0 1 5
ADD 1 2 2
SUM 0 2
```

**Output:**

```
14
```

**Explanation:**

After updates, the array is `[5, 7, 2]`, so the sum over `[0,2]` is 14.

![Example Visualization](../images/SEG-002/example-1.png)

## Notes

- Use a segment tree with lazy propagation
- Each operation runs in O(log n)
- Store segment sums and pending add values
- Use 64-bit integers for sums

## Related Topics

Segment Tree, Lazy Propagation, Range Updates

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processOperations(int n, int q, long[] a, List<String> ops) {
        // Implement here
        // For each SUM, print the range sum
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
        # For each SUM, print the range sum
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
        // For each SUM, cout << sum << endl;
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
    // For each SUM, console.log(sum.toString());
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
