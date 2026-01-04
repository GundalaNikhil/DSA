---
problem_id: PDS_MISRA_GRIES__9624
display_id: PDS-005
slug: misra-gries
title: "Frequent Items with Misra-Gries"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - Streaming
  - Frequency Estimation
tags:
  - probabilistic-ds
  - misra-gries
  - streaming
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-005: Frequent Items with Misra-Gries

## Problem Statement

Given a stream of `n` integers and a parameter `k`, run the Misra-Gries algorithm with `k-1` counters. Output the set of candidate items after processing the stream.

If no candidates remain, print an empty line.

![Problem Illustration](../images/PDS-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers (stream)

## Output Format

- Single line: candidate items in ascending order, space-separated

## Constraints

- `1 <= n <= 10^6`
- `2 <= k <= 1000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
7 3
1 2 1 3 1 2 4
```

**Output:**

```
1 2
```

**Explanation:**

Misra-Gries keeps at most 2 counters and returns {1,2} as candidates.

![Example Visualization](../images/PDS-005/example-1.png)

## Notes

- The algorithm guarantees all items with frequency > n/k appear in the candidates
- A second pass is needed to verify true frequencies (not required here)
- Time complexity: O(n * k) in the naive implementation, O(n) with hash map

## Related Topics

Heavy Hitters, Streaming Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void misraGries(int n, int k, int[] stream) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] stream = new int[n];
        for (int i = 0; i < n; i++) stream[i] = sc.nextInt();
        Solution sol = new Solution();
        sol.misraGries(n, k, stream);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def misra_gries(self, n, k, stream):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    stream = [int(x) for x in input_data[2:2+n]]
    sol = Solution()
    sol.misra_gries(n, k, stream)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
    void misraGries(int n, int k, const vector<int>& stream) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> stream(n);
    for (int i = 0; i < n; i++) cin >> stream[i];
    Solution sol;
    sol.misraGries(n, k, stream);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  misraGries(n, k, stream) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const stream = [];
  for (let i = 0; i < n; i++) stream.push(parseInt(input[2 + i]));
  const sol = new Solution();
  sol.misraGries(n, k, stream);
}

solve();
```
