---
problem_id: SEG_LONGEST_INCREASING_SUBARRAY_UPDATES__2654
display_id: SEG-008
slug: longest-increasing-subarray-updates
title: "Longest Increasing Subarray After Updates"
difficulty: Medium
difficulty_score: 55
topics:
  - Segment Tree
  - Dynamic Arrays
  - Monotonicity
tags:
  - segment-tree
  - increasing
  - updates
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-008: Longest Increasing Subarray After Updates

## Problem Statement

Given an array `a`, you must handle point updates. After each update, output the length of the longest strictly increasing contiguous subarray.

Operation:

- `SET i x`: set `a[i] = x`

![Problem Illustration](../images/SEG-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET i x`

## Output Format

- For each update, print the current longest increasing subarray length

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
3 1
1 2 1
SET 2 3
```

**Output:**

```
3
```

**Explanation:**

After the update the array becomes `[1, 2, 3]`, which is strictly increasing.

![Example Visualization](../images/SEG-008/example-1.png)

## Notes

- Store prefix and suffix increasing lengths per segment
- Merge using boundary comparisons between segments
- Update affects only O(log n) nodes
- The answer is the max length stored at the root

## Related Topics

Segment Tree, Range Merge, Dynamic Updates

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void processOperations(int n, int q, long[] a, List<String> ops) {
        // Implement here
        // For each update, print the current longest increasing subarray length
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
        # For each update, print the current longest increasing subarray length
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
        // For each update, cout << max_length << endl;
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
    // For each update, console.log(max_length);
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
