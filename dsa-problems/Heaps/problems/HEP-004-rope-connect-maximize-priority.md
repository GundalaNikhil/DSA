---
problem_id: HEP_ROPE_CONNECT_MAXIMIZE_PRIORITY__6742
display_id: HEP-004
slug: rope-connect-maximize-priority
title: "Rope Connection Maximize Strength with Priority Classes"
difficulty: Medium
difficulty_score: 57
topics:
  - Heaps
  - Greedy
  - Priority Classes
tags:
  - heaps
  - greedy
  - priority
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-004: Rope Connection Maximize Strength with Priority Classes

## Problem Statement

You are given `n` ropes. Each rope has a strength and a priority class:

- Class 1: critical
- Class 2: standard
- Class 3: spare

You may repeatedly connect two ropes into one. The new strength is:

```
strength = s1 + s2 - penalty
```

Penalty rules:

- 0 if both ropes are in the same class
- 1 if classes differ by 1 (1 with 2, or 2 with 3)
- 2 if classes are 1 and 3

The new rope inherits the higher priority class (smaller class number). Continue until one rope remains. Maximize the final rope strength.

![Problem Illustration](../images/HEP-004/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` integers for strengths
- Third line: `n` integers for priority classes (each in {1,2,3})

## Output Format

- Single integer: maximum possible final rope strength

## Constraints

- `1 <= n <= 100000`
- `1 <= strength <= 10^9`
- Priority class is 1, 2, or 3

## Example

**Input:**

```
3
6 5 4
1 2 3
```

**Output:**

```
13
```

**Explanation:**

One optimal sequence:

- Connect strengths 5 (class 2) and 4 (class 3)
  - Penalty = 1, new strength = 5 + 4 - 1 = 8, new class = 2
- Connect strengths 8 (class 2) and 6 (class 1)
  - Penalty = 1, new strength = 8 + 6 - 1 = 13

Final strength = 13.

![Example Visualization](../images/HEP-004/example-1.png)

## Notes

- Keep max-heaps for each class to pick strong candidates
- Prefer same-class merges to avoid penalties when possible
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Heaps, Greedy, Priority Scheduling, Merging

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maximizeStrength(int n, long[] strengths, int[] classes) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        int n = Integer.parseInt(firstLine.trim());

        long[] strengths = new long[n];
        String[] sVals = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) {
            strengths[i] = Long.parseLong(sVals[i]);
        }

        int[] classes = new int[n];
        String[] cVals = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) {
            classes[i] = Integer.parseInt(cVals[i]);
        }

        Solution sol = new Solution();
        System.out.println(sol.maximizeStrength(n, strengths, classes));
    }
}
```

### Python

```python
import sys

class Solution:
    def maximize_strength(self, n, strengths, classes):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    strengths = list(map(int, input_data[1:n+1]))
    classes = list(map(int, input_data[n+1:2*n+1]))

    sol = Solution()
    print(sol.maximize_strength(n, strengths, classes))

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
    long long maximizeStrength(int n, vector<long long>& strengths, vector<int>& classes) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> strengths(n);
    for (int i = 0; i < n; i++) cin >> strengths[i];

    vector<int> classes(n);
    for (int i = 0; i < n; i++) cin >> classes[i];

    Solution sol;
    cout << sol.maximizeStrength(n, strengths, classes) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maximizeStrength(n, strengths, classes) {
    // Implement here
    return 0n;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const strengths = [];
  for (let i = 0; i < n; i++) {
    strengths.push(BigInt(input[idx++]));
  }
  const classes = [];
  for (let i = 0; i < n; i++) {
    classes.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.maximizeStrength(n, strengths, classes).toString());
}

solve();
```
