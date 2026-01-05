---
problem_id: GRD_FESTIVAL_STALL_PLACEMENT__7146
display_id: GRD-003
slug: festival-stall-placement
title: "Festival Stall Placement"
difficulty: Medium
difficulty_score: 45
topics:
  - Greedy Algorithms
  - Intervals
  - Activity Selection
tags:
  - greedy
  - intervals
  - scheduling
  - activity-selection
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-003: Festival Stall Placement

## Problem Statement

You are organizing a festival along a straight road and have received `n` stall placement requests. Each request specifies a start and end coordinate `[start, end]` where the vendor wants to place their stall.

However, there's a safety regulation: no two stalls can be placed within distance `d` of each other (measured by their closest points).

Your goal is to approve the maximum number of stall requests while respecting the distance constraint.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-003.jpg)

## Input Format

- First line: two integers `n d` (number of requests and minimum distance)
- Next `n` lines: two integers `start end` representing each stall's position interval

## Output Format

- Single integer: maximum number of stalls that can be placed

## Constraints

- `1 <= n <= 10^5`
- `1 <= d <= 10^9`
- `0 <= start < end <= 10^9`
- Positions are integers

## Example

**Input:**

```
3 2
0 2
1 4
5 6
```

**Output:**

```
2
```

**Explanation:**

Stall requests with minimum distance d=2:

- Stall 1: [0, 2] (ends at position 2)
- Stall 2: [1, 4] (ends at position 4)
- Stall 3: [5, 6] (ends at position 6)

Greedy approach (sort by end position, pick earliest ending):

1. Choose stall 1 ending at 2
2. Stall 2 ends at 4, but starts at 1. Distance from stall 1's end (2) to stall 2's start (1) is not valid (overlapping). Skip.
3. Stall 3 starts at 5. Distance from stall 1's end (2) to stall 3's start (5) is 3, which is >= d=2. Choose stall 3.

Total: 2 stalls

![Example Visualization](../images/GRD-003/example-1.png)

## Notes

- Sort stalls by their end position
- Greedily select stalls whose start position is at least distance `d` from the previously selected stall's end position
- This is a variant of the interval scheduling maximization problem with distance constraints
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Interval Scheduling, Activity Selection, Sorting

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int maxStalls(int n, int d, int[][] requests) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ndLine = br.readLine();
        if (ndLine == null) return;
        String[] nd = ndLine.trim().split("\\s+");
        int n = Integer.parseInt(nd[0]);
        int d = Integer.parseInt(nd[1]);

        int[][] requests = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] req = br.readLine().trim().split("\\s+");
            requests[i][0] = Integer.parseInt(req[0]);
            requests[i][1] = Integer.parseInt(req[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.maxStalls(n, d, requests));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_stalls(self, n, d, requests):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    d = int(input_data[1])
    idx = 2
    requests = []
    for _ in range(n):
        requests.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.max_stalls(n, d, requests))

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
    int maxStalls(int n, int d, vector<vector<int>>& requests) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, d;
    if (!(cin >> n >> d)) return 0;

    vector<vector<int>> requests(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> requests[i][0] >> requests[i][1];
    }

    Solution sol;
    cout << sol.maxStalls(n, d, requests) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxStalls(n, d, requests) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const d = parseInt(input[idx++]);
  const requests = [];
  for (let i = 0; i < n; i++) {
    requests.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.maxStalls(n, d, requests));
}

solve();
```
