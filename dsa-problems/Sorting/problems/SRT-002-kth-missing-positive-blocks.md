---
problem_id: SRT_KTH_MISSING_POSITIVE_BLOCKS__4179
display_id: SRT-002
slug: kth-missing-positive-blocks
title: "Kth Missing Positive with Blocks"
difficulty: Easy
difficulty_score: 33
topics:
  - Sorting
  - Binary Search
  - Prefix Counts
tags:
  - sorting
  - binary-search
  - missing-number
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-002: Kth Missing Positive with Blocks

## Problem Statement

You are given a sorted array of unique positive integers. Define the list of missing positive integers in increasing order. A query provides `(k, blockSize)` and asks for the last number in the k-th block of size `blockSize` in that missing list.

Equivalently, the answer is the `(k * blockSize)`-th missing positive integer.

![Problem Illustration](../images/SRT-002/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated sorted positive integers
- Next `q` lines: two integers `k` and `blockSize`

## Output Format

- For each query, print the requested missing number

## Constraints

- `1 <= n, q <= 100000`
- `1 <= a[i] <= 10^9`
- `1 <= k, blockSize <= 10^9`

## Example

**Input:**

```
3 1
2 3 7
3 2
```

**Output:**

```
9
```

**Explanation:**

Missing positives are `1,4,5,6,8,9,...`. The 3rd block of size 2 ends at the 6th missing number, which is 9.

![Example Visualization](../images/SRT-002/example-1.png)

## Notes

- Precompute how many positives are missing up to each array value
- Use binary search to find the position of the m-th missing number
- m can be large (`k * blockSize`)
- Time per query: O(log n)

## Related Topics

Binary Search, Missing Number, Prefix Counts

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public long[] solve(int[] arr, long[][] queries) {
        //Implement here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        long[][] queries = new long[q][2];
        for (int i = 0; i < q; i++) {
            queries[i][0] = sc.nextLong();
            queries[i][1] = sc.nextLong();
        }
        Solution solution = new Solution();
        long[] results = solution.solve(arr, queries);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < results.length; i++) {
            if (i > 0) sb.append('\n');
            sb.append(results[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def solve(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    # //Implement here
    return 0

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        k, b = map(int, input().split())
        queries.append((k, b))

    results = solve(arr, queries)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<long long> solve(const vector<int>& arr, const vector<pair<long long,long long>>& queries) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    vector<pair<long long, long long>> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        long long k, b;
        cin >> k >> b;
        queries.push_back({k, b});
    }
    Solution solution;
    vector<long long> results = solution.solve(arr, queries);
    for (long long v : results) {
        cout << v << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  solve(arr, queries) {
    //Implement here
    return 0;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const q = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const queries = [];
for (let i = 0; i < q; i++) {
  const k = data[idx++];
  const b = data[idx++];
  queries.push([k, b]);
}
const solution = new Solution();
const results = solution.solve(arr, queries);
console.log(results.join("\n"));
```

