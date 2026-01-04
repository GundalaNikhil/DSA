---
problem_id: HEP_HUFFMAN_MERGE_LIMIT__1584
display_id: HEP-008
slug: huffman-merge-limit
title: "Huffman with Merge Limit"
difficulty: Medium
difficulty_score: 50
topics:
  - Heaps
  - Huffman Coding
  - Greedy
tags:
  - heaps
  - huffman
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-008: Huffman with Merge Limit

## Problem Statement

Given `n` frequencies, build a Huffman-like tree where you may merge at most `m` nodes at a time (`2 <= m <= 5`). The cost of each merge is the sum of merged values, and that sum is pushed back into the pool. The total cost is the sum of all merge costs.

If `(n - 1) % (m - 1) != 0`, pad the list with zeros until it satisfies the condition.

Return the total cost.

![Problem Illustration](../images/HEP-008/problem-illustration.png)

## Input Format

- First line: two integers `n` and `m`
- Second line: `n` space-separated frequencies

## Output Format

- Single integer: total merge cost

## Constraints

- `1 <= n <= 100000`
- `2 <= m <= 5`
- `0 <= frequency <= 10^9`

## Example

**Input:**

```
3 2
5 7 10
```

**Output:**

```
34
```

**Explanation:**

Binary merges:

- Merge 5 and 7 -> cost 12
- Merge 10 and 12 -> cost 22

Total cost = 12 + 22 = 34.

![Example Visualization](../images/HEP-008/example-1.png)

## Notes

- Use a min-heap to repeatedly extract the smallest `m` values
- Pad with zeros so the final tree is valid
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Heaps, Huffman Coding, Greedy Algorithms

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minMergeCost(int n, int m, long[] frequencies) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);

        long[] frequencies = new long[n];
        String[] vals = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) {
            frequencies[i] = Long.parseLong(vals[i]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minMergeCost(n, m, frequencies));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_merge_cost(self, n, m, frequencies):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    frequencies = list(map(int, input_data[2:2+n]))

    sol = Solution()
    print(sol.min_merge_cost(n, m, frequencies))

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
    long long minMergeCost(int n, int m, vector<long long>& frequencies) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> frequencies(n);
    for (int i = 0; i < n; i++) cin >> frequencies[i];

    Solution sol;
    cout << sol.minMergeCost(n, m, frequencies) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minMergeCost(n, m, frequencies) {
    // Implement here
    return 0n;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);
  const frequencies = [];
  for (let i = 0; i < n; i++) {
    frequencies.push(BigInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.minMergeCost(n, m, frequencies).toString());
}

solve();
```
