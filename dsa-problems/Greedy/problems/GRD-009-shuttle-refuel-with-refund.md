---
problem_id: GRD_SHUTTLE_REFUEL_WITH_REFUND__6724
display_id: GRD-009
slug: shuttle-refuel-with-refund
title: "Shuttle Refuel with Refund"
difficulty: Medium
difficulty_score: 55
topics:
  - Greedy Algorithms
  - Circular Array
  - Kadane's Algorithm
tags:
  - greedy
  - circular-array
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-009: Shuttle Refuel with Refund

## Problem Statement

A shuttle travels a circular route with `n` stops. At each stop `i`:

- You can refuel and gain `gain[i]` units of fuel
- Traveling to the next stop costs `cost[i]` units of fuel

You have a special coupon that can refund the fuel cost for exactly one segment (one `cost[i]` value). This means for that segment, you travel without consuming any fuel.

Find a starting stop index where you can complete the entire loop using the coupon optimally, or return `-1` if it's impossible even with the coupon.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-009.jpg)

## Input Format

- First line: integer `n` (number of stops)
- Second line: `n` space-separated integers representing `gain[0], gain[1], ..., gain[n-1]`
- Third line: `n` space-separated integers representing `cost[0], cost[1], ..., cost[n-1]`

## Output Format

- Single integer: starting stop index (0-indexed), or `-1` if impossible

## Constraints

- `1 <= n <= 10^5`
- `0 <= gain[i], cost[i] <= 10^9`

## Example

**Input:**

```
3
1 4 2
3 2 3
```

**Output:**

```
1
```

**Explanation:**

Stops with gain and cost:

- Stop 0: gain=1, cost to next=3
- Stop 1: gain=4, cost to next=2
- Stop 2: gain=2, cost to next=3

Starting from stop 1 (index 1):

- At stop 1: fuel = 0 + 4 = 4, travel to stop 2 costs 2 → fuel = 2
- At stop 2: fuel = 2 + 2 = 4, travel to stop 0 costs 3 → fuel = 1
- At stop 0: fuel = 1 + 1 = 2, travel to stop 1 costs 3 → fuel = -1 (FAIL without coupon)

Using coupon on the segment from stop 0 to stop 1 (cost=3):

- At stop 0: fuel = 1 + 1 = 2, travel to stop 1 with coupon → fuel = 2 (no cost)
- Successfully complete the loop!

Output: 1

![Example Visualization](../images/GRD-009/example-1.png)

## Notes

- Similar to the classic gas station problem but with a refund coupon
- Check if total gain >= total cost (necessary but not sufficient)
- Track surplus at each point and identify the segment with maximum deficit
- Apply the coupon to the most expensive segment where you'd run low on fuel
- Try each starting position and simulate with optimal coupon usage
- Time complexity: O(n²) for trying each start, or O(n) with optimization

## Related Topics

Greedy Algorithms, Circular Array, Prefix Sum, Kadane's Algorithm, Optimization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int findStartingStop(int n, long[] gain, long[] cost) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[] gain = new long[n];
        String[] gainLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) gain[i] = Long.parseLong(gainLine[i]);

        long[] cost = new long[n];
        String[] costLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < n; i++) cost[i] = Long.parseLong(costLine[i]);

        Solution sol = new Solution();
        System.out.println(sol.findStartingStop(n, gain, cost));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_starting_stop(self, n, gain, cost):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    gain = list(map(int, input_data[1:1+n]))
    cost = list(map(int, input_data[1+n:1+2*n]))

    sol = Solution()
    print(sol.find_starting_stop(n, gain, cost))

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
    int findStartingStop(int n, vector<long long>& gain, vector<long long>& cost) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> gain(n);
    for (int i = 0; i < n; i++) cin >> gain[i];

    vector<long long> cost(n);
    for (int i = 0; i < n; i++) cin >> cost[i];

    Solution sol;
    cout << sol.findStartingStop(n, gain, cost) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findStartingStop(n, gain, cost) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const gain = [];
  for (let i = 0; i < n; i++) gain.push(BigInt(input[idx++]));
  const cost = [];
  for (let i = 0; i < n; i++) cost.push(BigInt(input[idx++]));

  const sol = new Solution();
  console.log(sol.findStartingStop(n, gain, cost));
}

solve();
```
