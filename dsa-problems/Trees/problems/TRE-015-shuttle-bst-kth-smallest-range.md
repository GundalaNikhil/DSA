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
        // Your implementation here
        return -1L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] values = new long[n];
        for (int i = 0; i < n; i++) values[i] = sc.nextLong();
        long L = sc.nextLong();
        long R = sc.nextLong();
        int k = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.kthInRange(values, L, R, k));
        sc.close();
    }
}
```

### Python

```python
def kth_in_range(values: list[int], L: int, R: int, k: int) -> int:
    # Your implementation here
    return -1

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [int(data[idx + i]) for i in range(n)]
    idx += n
    L = int(data[idx]); idx += 1
    R = int(data[idx]); idx += 1
    k = int(data[idx]) if idx < len(data) else 1
    print(kth_in_range(values, L, R, k))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long kthInRange(const vector<long long>& values, long long L, long long R, int k) {
        // Your implementation here
        return -1LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> values(n);
    for (int i = 0; i < n; i++) cin >> values[i];
    long long L, R;
    cin >> L >> R;
    int k;
    cin >> k;

    Solution solution;
    cout << solution.kthInRange(values, L, R, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  kthInRange(values, L, R, k) {
    // Your implementation here
    return -1;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = new Array(n);
  for (let i = 0; i < n; i++) values[i] = parseInt(data[idx++], 10);
  const L = parseInt(data[idx++], 10);
  const R = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);

  const solution = new Solution();
  console.log(solution.kthInRange(values, L, R, k).toString());
});
```
