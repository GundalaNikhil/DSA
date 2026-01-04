---
problem_id: GRD_ROBOTICS_COMPONENT_BUNDLING__7259
display_id: GRD-006
slug: robotics-component-bundling-loss-quality
title: "Robotics Component Bundling with Loss and Quality Score"
difficulty: Medium
difficulty_score: 60
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
  - Simulation
tags:
  - greedy
  - heap
  - priority-queue
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-006: Robotics Component Bundling with Loss and Quality Score

## Problem Statement

You have `n` robot parts, where each part `i` has:

- Weight `w[i]`
- Quality score `q[i]`

You can bundle two parts together using the following rules:

- **Weight calculation**: When bundling parts with weights `w_big` and `w_small` (where `w_big >= w_small`), the new weight is: `w_big + w_small - floor(0.1 × w_small)`
  - This represents a 10% material loss from the smaller part
- **Quality calculation**: When bundling parts with qualities `q[i]` and `q[j]`, the new quality is: `min(q[i], q[j]) - 1`
  - Quality degrades by 1 due to the bundling process

**Constraint**: All intermediate bundles must maintain quality >= T (threshold), otherwise they become unusable.

Your goal is to bundle all parts into a single component while maximizing the final weight. Return the maximum achievable weight, or `-1` if no valid bundling sequence exists.

![Problem Illustration](../images/GRD-006/problem-illustration.png)

## Input Format

- First line: two integers `n T` (number of parts and quality threshold)
- Second line: `n` space-separated integers representing weights `w[0], w[1], ..., w[n-1]`
- Third line: `n` space-separated integers representing qualities `q[0], q[1], ..., q[n-1]`

## Output Format

- Single integer: maximum final weight achievable, or `-1` if impossible

## Constraints

- `1 <= n <= 2*10^5`
- `1 <= w[i] <= 10^9`
- `1 <= q[i] <= 100`
- `1 <= T <= 100`

## Example

**Input:**

```
3 5
4 3 2
10 8 6
```

**Output:**

```
8
```

**Explanation:**

Parts: weights [4, 3, 2], qualities [10, 8, 6]
Threshold: T = 5

Valid bundling sequence:

1. Bundle parts with weights 3 and 2, qualities 8 and 6:

   - New weight: 3 + 2 - floor(0.1 × 2) = 5 - 0 = 5
   - New quality: min(8, 6) - 1 = 5 (meets threshold!)
   - Now have: [4, 5] with qualities [10, 5]

2. Bundle parts with weights 4 and 3, qualities 10 and 8:

   - Weight: 4 + 3 - floor(0.1 × 3) = 7 - 0 = 7
   - Quality: min(10, 8) - 1 = 7

3. Bundle the result (weight 7, quality 7) with the part (weight 2, quality 6):
   - Weight: 7 + 2 - floor(0.1 × 2) = 9 - 0 = 9
   - Quality: min(7, 6) - 1 = 5

Final weight = 9, quality maintained at 5.

![Example Visualization](../images/GRD-006/example-1.png)

## Notes

- Use a max-heap to track (weight, quality) pairs
- Always try to bundle pairs that maintain quality >= T
- The 10% loss applies to the smaller weight
- Greedy strategy: prioritize maintaining quality while maximizing weight
- Time complexity: O(n log n) for heap operations

## Related Topics

Greedy Algorithms, Heap, Priority Queue, Simulation, Constraint Satisfaction

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxWeight(int n, int t, long[] w, int[] q) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ntLine = br.readLine();
        if (ntLine == null) return;
        String[] nt = ntLine.trim().split("\\s+");
        int n = Integer.parseInt(nt[0]);
        int t = Integer.parseInt(nt[1]);

        long[] w = new long[n];
        String[] wLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) w[i] = Long.parseLong(wLine[i]);

        int[] q = new int[n];
        String[] qLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) q[i] = Integer.parseInt(qLine[i]);

        Solution sol = new Solution();
        System.out.println(sol.maxWeight(n, t, w, q));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_weight(self, n, t, w, q):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    t = int(input_data[1])
    idx = 2
    w = list(map(int, input_data[idx:idx+n]))
    idx += n
    q = list(map(int, input_data[idx:idx+n]))

    sol = Solution()
    print(sol.max_weight(n, t, w, q))

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
    long long maxWeight(int n, int t, vector<long long>& w, vector<int>& q) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, t;
    if (!(cin >> n >> t)) return 0;

    vector<long long> w(n);
    for (int i = 0; i < n; i++) cin >> w[i];

    vector<int> q(n);
    for (int i = 0; i < n; i++) cin >> q[i];

    Solution sol;
    cout << sol.maxWeight(n, t, w, q) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxWeight(n, t, w, q) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const t = parseInt(input[idx++]);

  const w = [];
  for (let i = 0; i < n; i++) {
    w.push(BigInt(input[idx++]));
  }

  const q = [];
  for (let i = 0; i < n; i++) {
    q.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.maxWeight(n, t, w, q).toString());
}

solve();
```
