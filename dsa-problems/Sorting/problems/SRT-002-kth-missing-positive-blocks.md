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
    public long findKthMissing(int n, long[] a, long k, long blockSize) {
        // Implement here
        return 0;
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

            Solution sol = new Solution();
            for (int i = 0; i < q; i++) {
                long k = sc.nextLong();
                long blockSize = sc.nextLong();
                System.out.println(sol.findKthMissing(n, a, k, blockSize));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_kth_missing(self, n: int, a: list, k: int, block_size: int) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    a = [int(x) for x in input_data[2:2+n]]

    sol = Solution()
    ptr = 2+n
    for _ in range(q):
        k = int(input_data[ptr])
        block_size = int(input_data[ptr+1])
        print(sol.find_kth_missing(n, a, k, block_size))
        ptr += 2

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
    long long findKthMissing(int n, const vector<long long>& a, long long k, long long blockSize) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (cin >> n >> q) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution sol;
        while (q--) {
            long long k, blockSize;
            cin >> k >> blockSize;
            cout << sol.findKthMissing(n, a, k, blockSize) << "\n";
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findKthMissing(n, a, k, blockSize) {
    // Implement here
    return 0n;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const q = parseInt(input[1]);
  const a = input.slice(2, 2 + n).map(BigInt);

  const sol = new Solution();
  let ptr = 2 + n;
  for (let i = 0; i < q; i++) {
    const k = BigInt(input[ptr]);
    const blockSize = BigInt(input[ptr + 1]);
    console.log(sol.findKthMissing(n, a, k, blockSize).toString());
    ptr += 2;
  }
});
```
