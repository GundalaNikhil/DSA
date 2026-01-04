---
problem_id: HSH_SUBARRAY_HASH_EQUALITY__6271
display_id: HSH-012
slug: subarray-hash-equality
title: "Subarray Hash Equality (Integers)"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Arrays
  - Rolling Hash
tags:
  - hashing
  - array
  - subarray
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-012: Subarray Hash Equality (Integers)

## Problem Statement

Given an integer array and queries, treat the array as a "string" where each element is a character. Build a rolling hash to support equality checks between subarrays.

Each query asks: are subarrays `a[l1..r1]` and `a[l2..r2]` equal?

![Problem Illustration](../images/HSH-012/problem-illustration.png)

## Input Format

- First line: integer `n` (array size)
- Second line: `n` space-separated integers (array elements)
- Third line: integer `q` (number of queries)
- Next `q` lines: four integers `l1 r1 l2 r2`

## Output Format

- `q` lines, each containing `true` or `false`

## Constraints

- `1 <= n <= 2*10^5`
- `1 <= q <= 2*10^5`
- `-10^9 <= a[i] <= 10^9`
- `0 <= l1 <= r1 < n`
- `0 <= l2 <= r2 < n`

## Example

**Input:**

```
4
1 2 1 2
2
0 1 2 3
0 0 2 2
```

**Output:**

```
true
true
```

**Explanation:**

Array: [1, 2, 1, 2]

Query 1: a[0..1] = [1, 2], a[2..3] = [1, 2] → equal → true
Query 2: a[0..0] = [1], a[2..2] = [1] → equal → true

![Example Visualization](../images/HSH-012/example-1.png)

## Notes

- Map integers to unique values (handle negative numbers)
- Use polynomial rolling hash
- Precompute prefix hashes
- Answer queries in O(1) after O(n) preprocessing
- Time complexity: O(n + q)
- Space complexity: O(n)

## Related Topics

Rolling Hash, Arrays, Subarray Comparison, Integer Hashing

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean[] checkSubarrayEquality(int n, int[] arr, int q, int[][] queries) {
        // Implement here
        return new boolean[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] arr = new int[n];
        String[] arrParts = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(arrParts[i]);

        String qLine = br.readLine();
        if (qLine == null) return;
        int q = Integer.parseInt(qLine.trim());

        int[][] queries = new int[q][4];
        for (int i = 0; i < q; i++) {
            String[] qParts = br.readLine().trim().split("\\s+");
            for (int j = 0; j < 4; j++) queries[i][j] = Integer.parseInt(qParts[j]);
        }

        Solution sol = new Solution();
        boolean[] result = sol.checkSubarrayEquality(n, arr, q, queries);

        PrintWriter out = new PrintWriter(System.out);
        for (boolean res : result) out.println(res);
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def check_subarray_equality(self, n, arr, q, queries):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    q = int(input_data[n+1])
    queries = []
    idx = n + 2
    for _ in range(q):
        queries.append(list(map(int, input_data[idx:idx+4])))
        idx += 4

    sol = Solution()
    result = sol.check_subarray_equality(n, arr, q, queries)
    for res in result:
        print("true" if res else "false")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<bool> checkSubarrayEquality(int n, vector<int>& arr, int q, vector<vector<int>>& queries) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    int q;
    if (!(cin >> q)) return 0;

    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++) {
        for (int j = 0; j < 4; j++) cin >> queries[i][j];
    }

    Solution sol;
    vector<bool> result = sol.checkSubarrayEquality(n, arr, q, queries);

    for (int i = 0; i < q; i++) {
        cout << (result[i] ? "true" : "false") << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  checkSubarrayEquality(n, arr, q, queries) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(input[idx++]));

  const q = parseInt(input[idx++]);
  const queries = [];
  for (let i = 0; i < q; i++) {
    queries.push([
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
    ]);
  }

  const sol = new Solution();
  const result = sol.checkSubarrayEquality(n, arr, q, queries);
  process.stdout.write(
    result.map((res) => (res ? "true" : "false")).join("\n") + "\n"
  );
}

solve();
```
