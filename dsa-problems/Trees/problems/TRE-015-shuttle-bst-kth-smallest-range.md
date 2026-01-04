---
problem_id: TRE_SHUTTLE_BST_KTH_SMALLEST_RANGE__4916
display_id: TRE-015
slug: shuttle-bst-kth-smallest-range
title: "Shuttle BST Kth Smallest in Range"
difficulty: Medium
difficulty_score: 52
topics:
  - Trees
  - BST
  - Traversal
tags:
  - trees
  - bst
  - kth-smallest
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-015: Shuttle BST Kth Smallest in Range

## Problem Statement

Build a BST by inserting values in the given order. Given a range `[L, R]` and an integer `k`, return the k-th smallest value within the range (1-indexed among in-range values).

If fewer than `k` values fall in the range, output `-1`.

![Problem Illustration](../images/TRE-015/problem-illustration.png)

## Input Format

- First line: integer `n`, number of values to insert
- Second line: `n` integers, the insertion order
- Third line: integers `L` and `R`
- Fourth line: integer `k`

Duplicates, if any, must be inserted into the right subtree.

## Output Format

- Single integer: the k-th smallest value in `[L, R]`, or `-1` if not enough values

## Constraints

- `1 <= n <= 100000`
- Values fit in 64-bit signed integers
- `1 <= k <= n`

## Example

**Input:**

```
5
2 4 5 7 9
4 8
2
```

**Output:**

```
5
```

**Explanation:**

Values in the range `[4, 8]` are `[4, 5, 7]`. The 2nd smallest is 5.

![Example Visualization](../images/TRE-015/example-1.png)

## Notes

- Use inorder traversal and skip values outside the range.
- Stop early once `k` elements are counted.
- If `n=0`, output `-1`.

## Related Topics

BST, Inorder Traversal, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long kthInRange(long[] values, long L, long R, int k) {
        // Implement here
        return -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] values = new long[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextLong();
        }
        long L = sc.hasNextLong() ? sc.nextLong() : 0;
        long R = sc.hasNextLong() ? sc.nextLong() : 0;
        int k = sc.hasNextInt() ? sc.nextInt() : 0;

        Solution solution = new Solution();
        System.out.println(solution.kthInRange(values, L, R, k));
        sc.close();
    }
}
```

### Python

```python
import sys
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def kth_in_range(self, values: List[int], L: int, R: int, k: int) -> int:
        # Implement here
        return -1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = []
        for _ in range(n):
            values.append(int(next(iterator)))

        L = int(next(iterator))
        R = int(next(iterator))
        k = int(next(iterator))

        solution = Solution()
        print(solution.kth_in_range(values, L, R, k))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long kthInRange(const vector<long long>& values, long long L, long long R, int k) {
        // Implement here
        return -1;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }
    long long L, R;
    int k;
    cin >> L >> R >> k;

    Solution solution;
    cout << solution.kthInRange(values, L, R, k) << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  kthInRange(values, L, R, k) {
    // Implement here
    return -1;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  let idx = 0;
  const n = parseInt(tokens[idx++]);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(BigInt(tokens[idx++]));
  }
  let L = 0n,
    R = 0n,
    k = 0;
  if (idx < tokens.length) L = BigInt(tokens[idx++]);
  if (idx < tokens.length) R = BigInt(tokens[idx++]);
  if (idx < tokens.length) k = parseInt(tokens[idx++]);

  const solution = new Solution();
  console.log(solution.kthInRange(values, L, R, k).toString());
});
```
