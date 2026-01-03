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
import java.io.*;
import java.util.*;

class Solution {
    public List<Boolean> checkSubarrayEquality(long[] arr, List<int[]> queries) {
        //Implemention here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        int n = Integer.parseInt(data[idx++]);
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(data[idx++]);
        }
        int q = Integer.parseInt(data[idx++]);
        List<int[]> queries = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            int l1 = Integer.parseInt(data[idx++]);
            int r1 = Integer.parseInt(data[idx++]);
            int l2 = Integer.parseInt(data[idx++]);
            int r2 = Integer.parseInt(data[idx++]);
            queries.add(new int[]{l1, r1, l2, r2});
        }

        Solution solution = new Solution();
        List<Boolean> result = solution.checkSubarrayEquality(arr, queries);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            out.append(result.get(i) ? "true" : "false");
            if (i + 1 < result.size()) out.append('\n');
        }
        System.out.print(out.toString());
    }
}
```

### Python

```python
import sys

def check_subarray_equality(arr, queries):
    # //Implemention here
    return []

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]);
    idx += 1
    arr = []
    for _ in range(n):
        arr.append(int(data[idx]));
        idx += 1
    q = int(data[idx]);
    idx += 1
    queries = []
    for _ in range(q):
        l1 = int(data[idx]);
        r1 = int(data[idx + 1]);
        l2 = int(data[idx + 2]);
        r2 = int(data[idx + 3]);
        idx += 4
        queries.append([l1, r1, l2, r2])
    result = check_subarray_equality(arr, queries)
    out_lines = [('true' if ans else 'false') for ans in result]
    sys.stdout.write('\n'.join(out_lines))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <array>

using namespace std;

vector<bool> check_subarray_equality(const vector<long long>& arr, const vector<array<int, 4>>& queries) {
    //Implemention here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int q;
    cin >> q;
    vector<array<int, 4>> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        queries.push_back({l1, r1, l2, r2});
    }

    vector<bool> result = check_subarray_equality(arr, queries);
    for (size_t i = 0; i < result.size(); i++) {
        cout << (result[i] ? "true" : "false");
        if (i + 1 < result.size()) cout << '\n';
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function checkSubarrayEquality(arr, queries) {
  //Implemention here
  return [];
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const q = parseInt(data[idx++], 10);
const queries = [];
for (let i = 0; i < q; i++) {
  const l1 = parseInt(data[idx++], 10);
  const r1 = parseInt(data[idx++], 10);
  const l2 = parseInt(data[idx++], 10);
  const r2 = parseInt(data[idx++], 10);
  queries.push([l1, r1, l2, r2]);
}
const result = checkSubarrayEquality(arr, queries);
const out = result.map(v => (v ? 'true' : 'false')).join('\n');
process.stdout.write(out);
```

