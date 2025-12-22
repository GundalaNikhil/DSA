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
        // Your implementation here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        long[][] queries = new long[q][2];
        for (int i = 0; i < q; i++) {
            queries[i][0] = sc.nextLong();
            queries[i][1] = sc.nextLong();
        }

        Solution solution = new Solution();
        long[] out = solution.solve(arr, queries);
        for (long v : out) System.out.println(v);
        sc.close();
    }
}
```

### Python

```python
def solve(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    queries = []
    for _ in range(q):
        k = int(next(it))
        block = int(next(it))
        queries.append((k, block))

    out = solve(arr, queries)
    sys.stdout.write("\n".join(str(x) for x in out))

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
    vector<long long> solve(const vector<int>& arr, const vector<pair<long long,long long>>& queries) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<pair<long long,long long>> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        long long k, b;
        cin >> k >> b;
        queries.push_back({k, b});
    }

    Solution solution;
    vector<long long> out = solution.solve(arr, queries);
    for (long long v : out) cout << v << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(arr, queries) {
    // Your implementation here
    return [];
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
  const q = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const queries = [];
  for (let i = 0; i < q; i++) {
    const k = parseInt(data[idx++], 10);
    const b = parseInt(data[idx++], 10);
    queries.push([k, b]);
  }

  const solution = new Solution();
  const out = solution.solve(arr, queries);
  console.log(out.join("\n"));
});
```
