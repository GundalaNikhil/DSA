---
problem_id: GRD_AUDITORIUM_SEAT_REFUNDS__2841
display_id: GRD-013
slug: auditorium-seat-refunds
title: "Auditorium Seat Refunds"
difficulty: Medium
difficulty_score: 35
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
tags:
  - greedy
  - heap
  - priority-queue
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-013: Auditorium Seat Refunds

## Problem Statement

An auditorium has seats organized in rows numbered 1 to `r`. Initially, all rows are fully occupied with `capacity[i]` seats in row `i`.

You receive `n` refund requests, where each request specifies a seat ID that includes the row number. When processing refunds, you want to minimize the highest occupied row index remaining after all refunds.

Return the highest occupied row number after processing all refund requests.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-013.jpg)

## Input Format

- First line: two integers `r n` (number of rows and number of refund requests)
- Second line: `r` space-separated integers representing initial capacity of each row
- Next `n` lines: two integers `row seat_id` representing each refund request

## Output Format

- Single integer: highest occupied row number (1-indexed) after all refunds

## Constraints

- `1 <= r <= 10^5`
- `1 <= capacity[i] <= 10^5`
- `0 <= n <= sum(capacity[i])`
- `1 <= row <= r`

## Example

**Input:**

```
3 3
5 4 3
3 1
3 2
2 1
```

**Output:**

```
2
```

**Explanation:**

Initial state:

- Row 1: 5 seats occupied
- Row 2: 4 seats occupied
- Row 3: 3 seats occupied

Refund requests:

1. Refund seat 1 from row 3 → Row 3 now has 2 seats
2. Refund seat 2 from row 3 → Row 3 now has 1 seat
3. Refund seat 1 from row 2 → Row 2 now has 3 seats

After processing:

- Row 1: 5 seats (still occupied)
- Row 2: 3 seats (still occupied)
- Row 3: 0 seats (completely empty after processing all refunds)

Since row 3 is completely empty, the highest occupied row is row 2.

The greedy strategy processes refunds from the highest rows first to minimize the highest occupied row number after all refunds are processed.

![Example Visualization](../images/GRD-013/example-1.png)

## Notes

- Track the occupancy count for each row
- Use a max-heap to efficiently track the highest occupied row
- After each refund, decrement the row's count
- If a row becomes empty (count = 0), it's no longer occupied
- Time complexity: O(n log r) for heap operations

## Related Topics

Greedy Algorithms, Heap, Priority Queue, State Management, Optimization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int highestOccupiedRow(int r, int n, int[] capacity, int[][] refunds) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String rnLine = br.readLine();
        if (rnLine == null) return;
        String[] rn = rnLine.trim().split("\\s+");
        int r = Integer.parseInt(rn[0]);
        int n = Integer.parseInt(rn[1]);

        int[] capacity = new int[r];
        String[] capLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < r; i++) capacity[i] = Integer.parseInt(capLine[i]);

        int[][] refunds = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] refLine = br.readLine().trim().split("\\s+");
            refunds[i][0] = Integer.parseInt(refLine[0]);
            refunds[i][1] = Integer.parseInt(refLine[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.highestOccupiedRow(r, n, capacity, refunds));
    }
}
```

### Python

```python
import sys

class Solution:
    def highest_occupied_row(self, r, n, capacity, refunds):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    r = int(input_data[0])
    n = int(input_data[1])
    idx = 2
    capacity = list(map(int, input_data[idx:idx+r]))
    idx += r
    refunds = []
    for _ in range(n):
        refunds.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.highest_occupied_row(r, n, capacity, refunds))

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
    int highestOccupiedRow(int r, int n, vector<int>& capacity, vector<vector<int>>& refunds) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int r, n;
    if (!(cin >> r >> n)) return 0;

    vector<int> capacity(r);
    for (int i = 0; i < r; i++) cin >> capacity[i];

    vector<vector<int>> refunds(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> refunds[i][0] >> refunds[i][1];
    }

    Solution sol;
    cout << sol.highestOccupiedRow(r, n, capacity, refunds) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  highestOccupiedRow(r, n, capacity, refunds) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const r = parseInt(input[idx++]);
  const n = parseInt(input[idx++]);

  const capacity = [];
  for (let i = 0; i < r; i++) capacity.push(parseInt(input[idx++]));

  const refunds = [];
  for (let i = 0; i < n; i++) {
    refunds.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.highestOccupiedRow(r, n, capacity, refunds));
}

solve();
```
