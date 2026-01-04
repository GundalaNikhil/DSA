---
problem_id: SEG_RANGE_ADD_KTH_ORDER__8059
display_id: SEG-012
slug: range-add-kth-order
title: "Range Add, K-th Order"
difficulty: Hard
difficulty_score: 70
topics:
  - Segment Tree
  - Order Statistics
  - Range Updates
tags:
  - segment-tree
  - kth-statistic
  - range-add
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-012: Range Add, K-th Order

## Problem Statement

Maintain an array under range-add updates and k-th order statistic queries on subarrays.

Operations:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `KTH l r k`: output the k-th smallest value in `a[l..r]`

![Problem Illustration](../images/SEG-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `ADD` or `KTH`

## Output Format

- For each `KTH`, print the k-th smallest value

## Constraints

- `1 <= n, q <= 100000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= k <= r - l + 1`

## Example

**Input:**

```
3 2
1 2 3
ADD 0 2 1
KTH 0 2 2
```

**Output:**

```
3
```

**Explanation:**

After adding 1, the array is `[2,3,4]`, so the 2nd smallest in `[0,2]` is 3.

![Example Visualization](../images/SEG-012/example-1.png)

## Notes

- This requires advanced data structures to support order statistics under updates
- Solutions may use sqrt decomposition or offline processing
- Correctness is more important than a specific technique
- Ensure output uses 64-bit values

## Related Topics

Order Statistics, Segment Tree, Range Updates

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processOperations(int n, int q, long[] a, List<String> ops) {
        // Implement here
        // For each KTH, print the k-th smallest value
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
        # For each KTH, print the k-th smallest value
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
        // For each KTH, cout << result << endl;
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
    // For each KTH, console.log(result.toString());
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
