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

class Solution {
    public boolean[] checkSubarrayEquality(int[] arr, int[][] queries) {
        // Your implementation here
        return new boolean[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int q = sc.nextInt();
        int[][] queries = new int[q][4];
        for (int i = 0; i < q; i++) {
            queries[i][0] = sc.nextInt();
            queries[i][1] = sc.nextInt();
            queries[i][2] = sc.nextInt();
            queries[i][3] = sc.nextInt();
        }

        Solution solution = new Solution();
        boolean[] result = solution.checkSubarrayEquality(arr, queries);

        for (boolean ans : result) {
            System.out.println(ans);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def check_subarray_equality(arr: List[int], queries: List[List[int]]) -> List[bool]:
    # Your implementation here
    return []

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        queries.append([l1, r1, l2, r2])

    result = check_subarray_equality(arr, queries)
    for ans in result:
        print("true" if ans else "false")

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
    vector<bool> checkSubarrayEquality(vector<int>& arr, vector<vector<int>>& queries) {
        // Your implementation here
        return vector<bool>();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int q;
    cin >> q;

    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++) {
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2] >> queries[i][3];
    }

    Solution solution;
    vector<bool> result = solution.checkSubarrayEquality(arr, queries);

    for (bool ans : result) {
        cout << (ans ? "true" : "false") << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  checkSubarrayEquality(arr, queries) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const arr = data[ptr++].split(" ").map(Number);
  const q = parseInt(data[ptr++]);

  const queries = [];
  for (let i = 0; i < q; i++) {
    queries.push(data[ptr++].split(" ").map(Number));
  }

  const solution = new Solution();
  const result = solution.checkSubarrayEquality(arr, queries);

  result.forEach((ans) => console.log(ans ? "true" : "false"));
});
```
