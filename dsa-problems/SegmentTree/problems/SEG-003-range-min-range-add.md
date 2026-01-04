---
problem_id: SEG_RANGE_MIN_RANGE_ADD__3915
display_id: SEG-003
slug: range-min-range-add
title: "Range Minimum with Range Add"
difficulty: Medium
difficulty_score: 48
topics:
  - Segment Tree
  - Lazy Propagation
  - Range Updates
tags:
  - segment-tree
  - range-min
  - lazy-propagation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-003: Range Minimum with Range Add

## Problem Statement

Given an array `a`, support two operations:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `MIN l r`: output the minimum value in `a[l..r]`

![Problem Illustration](../images/SEG-003/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: operations `ADD` or `MIN`

## Output Format

- For each `MIN`, print the minimum value

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 2
3 1 4
ADD 0 2 2
MIN 1 2
```

**Output:**

```
3
```

**Explanation:**

After adding 2 to all elements, the array becomes `[5, 3, 6]`, and the minimum in `[1,2]` is 3.

![Example Visualization](../images/SEG-003/example-1.png)

## Notes

- Store the minimum in each segment tree node
- Use lazy propagation to defer range adds
- Each operation runs in O(log n)
- Use 64-bit integers if needed

## Related Topics

Segment Tree, Range Minimum Query, Lazy Propagation

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
