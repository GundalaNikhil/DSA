---
problem_id: PDS_COUNT_SKETCH_HEAVY_HITTERS__3405
display_id: PDS-010
slug: count-sketch-heavy-hitters
title: "Heavy Hitters with Count Sketch"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Count Sketch
  - Streaming
tags:
  - probabilistic-ds
  - count-sketch
  - heavy-hitters
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-010: Heavy Hitters with Count Sketch

## Problem Statement

Given the Count Sketch signed estimates for a single item across `d` rows, compute its frequency estimate as the median of the signed counts.

Each row provides:

- `count`: the bucket count
- `sign`: either `+1` or `-1`

The signed value is `count * sign`.

![Problem Illustration](../images/PDS-010/problem-illustration.png)

## Input Format

- First line: integer `d` (odd)
- Next `d` lines: `count` and `sign`

## Output Format

- Single integer: the median of signed counts

## Constraints

- `1 <= d <= 101`, `d` is odd
- `count` fits in 32-bit signed integer
- `sign` is either -1 or 1

## Example

**Input:**

```
3
10 1
9 -1
11 1
```

**Output:**

```
10
```

**Explanation:**

Signed counts are [10, -9, 11]. Median is 10.

![Example Visualization](../images/PDS-010/example-1.png)

## Notes

- For odd `d`, the median is the middle after sorting
- Time complexity: O(d log d)
- Space complexity: O(d)

## Related Topics

Count Sketch, Heavy Hitters, Streaming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int estimateFrequency(int d, int[] counts, int[] signs) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int d = sc.nextInt();
        int[] counts = new int[d];
        int[] signs = new int[d];
        for (int i = 0; i < d; i++) {
            counts[i] = sc.nextInt();
            signs[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.estimateFrequency(d, counts, signs));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def estimate_frequency(self, d, counts, signs):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    d = int(input_data[0])
    counts = []
    signs = []
    for i in range(d):
        counts.append(int(input_data[1 + 2 * i]))
        signs.append(int(input_data[2 + 2 * i]))
    sol = Solution()
    print(sol.estimate_frequency(d, counts, signs))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int estimateFrequency(int d, const vector<int>& counts, const vector<int>& signs) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int d;
    if (!(cin >> d)) return 0;
    vector<int> counts(d), signs(d);
    for (int i = 0; i < d; i++) {
        cin >> counts[i] >> signs[i];
    }
    Solution sol;
    cout << sol.estimateFrequency(d, counts, signs) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  estimateFrequency(d, counts, signs) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const d = parseInt(input[0]);
  const counts = [];
  const signs = [];
  for (let i = 0; i < d; i++) {
    counts.push(parseInt(input[1 + 2 * i]));
    signs.push(parseInt(input[2 + 2 * i]));
  }
  const sol = new Solution();
  console.log(sol.estimateFrequency(d, counts, signs));
}

solve();
```
