---
problem_id: ARR_SEAT_GAP_REMOVALS__6037
display_id: ARR-015
slug: seat-gap-after-removals
title: "Seat Gap After Removals"
difficulty: Medium
difficulty_score: 33
topics:
  - Arrays
  - Simulation
  - Greedy
tags:
  - arrays
  - simulation
  - greedy
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-015: Seat Gap After Removals

## Problem Statement

You are given sorted seat positions and a list of indices to remove (indices refer to the original array). After removals, compute the maximum gap between remaining consecutive seats.

![Problem Illustration](../images/ARR-015/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers seats[i] (sorted)
- Third line: integer r, the number of removals
- Fourth line: r space-separated indices to remove

## Output Format

Print the maximum gap between remaining consecutive seats.

## Constraints

- `2 <= n <= 200000`
- `0 <= seats[i] <= 1000000000`
- `1 <= r <= n - 2`

## Example

**Input:**

```
4
2 5 9 10
1
1
```

**Output:**

```
7
```

**Explanation:**

Seat at index 1 (value 5) is removed. Remaining seats are [2, 9, 10], so the
maximum gap is 7.

![Example Visualization](../images/ARR-015/example-1.png)

## Notes

- Removal indices refer to the original array positions.
- At least two seats remain after removals.

## Related Topics

Simulation, Greedy, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int maxSeatGap(int n, int[] seats, int r, HashSet<Integer> removals) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] seats = new int[n];
        String sLine = br.readLine();
        if (sLine != null) {
            String[] parts = sLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                seats[i] = Integer.parseInt(parts[i]);
            }
        }

        String rLine = br.readLine();
        if (rLine == null) return;
        int r = Integer.parseInt(rLine.trim());

        HashSet<Integer> removals = new HashSet<>();
        String remLine = br.readLine();
        if (remLine != null && r > 0) {
            String[] parts = remLine.trim().split("\\s+");
            for (String p : parts) {
                removals.add(Integer.parseInt(p));
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.maxSeatGap(n, seats, r, removals));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_seat_gap(self, n, seats, r, removals):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    seats = list(map(int, input_data[1:n+1]))
    r = int(input_data[n+1])
    removals = set()
    for i in range(r):
        removals.add(int(input_data[n+2+i]))

    sol = Solution()
    print(sol.max_seat_gap(n, seats, r, removals))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxSeatGap(int n, vector<int>& seats, int r, unordered_set<int>& removals) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> seats(n);
    for (int i = 0; i < n; i++) {
        cin >> seats[i];
    }

    int r;
    cin >> r;

    unordered_set<int> removals;
    for (int i = 0; i < r; i++) {
        int idx;
        cin >> idx;
        removals.insert(idx);
    }

    Solution sol;
    cout << sol.maxSeatGap(n, seats, r, removals) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxSeatGap(n, seats, r, removals) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const seats = [];
  for (let i = 0; i < n; i++) seats.push(readInt());

  const r = readInt();
  const removals = new Set();
  for (let i = 0; i < r; i++) removals.add(readInt());

  const sol = new Solution();
  console.log(sol.maxSeatGap(n, seats, r, removals));
}

solve();
```
