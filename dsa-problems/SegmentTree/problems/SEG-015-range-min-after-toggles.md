---
problem_id: SEG_RANGE_MIN_AFTER_TOGGLES__5728
display_id: SEG-015
slug: range-min-after-toggles
title: "Range Min After Additive Toggles"
difficulty: Medium
difficulty_score: 60
topics:
  - Segment Tree
  - Lazy Propagation
  - Range Queries
tags:
  - segment-tree
  - range-min
  - toggles
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-015: Range Min After Additive Toggles

## Problem Statement

Maintain an array with two update types and range minimum queries:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `FLIP l r`: multiply all elements in `a[l..r]` by `-1`
- `MIN l r`: output the minimum value in `a[l..r]`

![Problem Illustration](../images/SEG-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `ADD`, `FLIP`, or `MIN`

## Output Format

- For each `MIN`, print the minimum value

## Constraints

- `1 <= n, q <= 100000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
3 3
1 -2 3
FLIP 0 2
ADD 1 2 1
MIN 0 2
```

**Output:**

```
-2
```

**Explanation:**

After flip: `[-1, 2, -3]`, after add: `[-1, 3, -2]`, minimum is -2.

![Example Visualization](../images/SEG-015/example-1.png)

## Notes

- Track both min and max to handle sign flips
- Lazy tags include pending add and pending flip
- Apply flip by swapping min/max and negating
- Each operation runs in O(log n)

## Related Topics

Segment Tree, Lazy Propagation, Range Minimum

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processOperations(int n, int q, long[] a, List<String> ops) {
        // Implement here
        // For each MIN, print the minimum value
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
        # For each MIN, print the minimum value
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
#include <algorithm>

using namespace std;

class Solution {
public:
    void processOperations(int n, int q, vector<long long>& a, const vector<string>& ops) {
        // Implement here
        // For each MIN, cout << min_val << endl;
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
    // For each MIN, console.log(min_val.toString());
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
