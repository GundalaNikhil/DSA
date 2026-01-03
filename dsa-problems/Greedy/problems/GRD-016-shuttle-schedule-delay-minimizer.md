---
problem_id: GRD_SHUTTLE_SCHEDULE_DELAY_MINIMIZER__8457
display_id: GRD-016
slug: shuttle-schedule-delay-minimizer
title: "Shuttle Schedule Delay Minimizer"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Scheduling
  - Sorting
tags:
  - greedy
  - scheduling
  - sorting
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-016: Shuttle Schedule Delay Minimizer

## Problem Statement

You have `n` shuttle trips to schedule. Each trip `i` has:

- Planned start time `s[i]`
- Duration `d[i]`

Trips must be executed sequentially (one at a time). If a trip starts later than its planned time, it incurs a delay. This delay propagates: if trip `i` is delayed by `x` time units, all subsequent trips are also delayed by at least `x` units.

Your goal is to choose an execution order that minimizes the total accumulated delay across all trips.

**Delay calculation**: If trip `i` actually starts at time `t` but was planned for time `s[i]`, its delay is `max(0, t - s[i])`.

Return the minimum total delay.

![Problem Illustration](../images/GRD-016/problem-illustration.png)

## Input Format

- First line: integer `n` (number of trips)
- Next `n` lines: two integers `s d` representing planned start time and duration for each trip

## Output Format

- Single integer: minimum total delay

## Constraints

- `1 <= n <= 10^5`
- `0 <= s[i], d[i] <= 10^9`

## Example

**Input:**

```
2
0 3
1 2
```

**Output:**

```
2
```

**Explanation:**

Trips:

- Trip 0: planned start=0, duration=3
- Trip 1: planned start=1, duration=2

**Order 1: Execute [Trip 0, Trip 1]**

- Trip 0 starts at time 0 (planned), delay=0, ends at time 3
- Trip 1 starts at time 3 (planned for 1), delay=2, ends at time 5
- Total delay = 0 + 2 = 2

**Order 2: Execute [Trip 1, Trip 0]**

- Trip 1 starts at time 0 (planned for 1), delay=0 (early is OK, no negative delay), ends at time 2
- Trip 0 starts at time 2 (planned for 0), delay=2, ends at time 5
- Total delay = 0 + 2 = 2

Both orders give the same total delay of 2.

Output: 2

![Example Visualization](../images/GRD-016/example-1.png)

## Notes

- Sort trips by a specific criteria to minimize weighted completion time
- Use shortest processing time (SPT) rule variant
- Consider sorting by `s[i] - d[i]` or similar metric
- Greedy strategy: Execute trips in order that minimizes cumulative delay
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Scheduling Theory, Weighted Completion Time, Sorting, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minTotalDelay(int n, int[][] trips) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;

        int n = sc.nextInt();
        int[][] trips = new int[n][2];
        for (int i = 0; i < n; i++) {
            trips[i][0] = sc.nextInt();
            trips[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.minTotalDelay(n, trips));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def min_total_delay(self, n: int, trips: list[list[int]]) -> int:
        # //Implement here
        return 0

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit(0)

    iterator = iter(input_data)
    try:
        n = int(next(iterator))

        trips = []
        for _ in range(n):
            s = int(next(iterator))
            d = int(next(iterator))
            trips.append([s, d])

        solution = Solution()
        print(solution.min_total_delay(n, trips))
    except StopIteration:
        pass
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minTotalDelay(int n, vector<pair<int,int>>& trips) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<int,int>> trips(n);
    for (int i = 0; i < n; i++) {
        cin >> trips[i].first >> trips[i].second;
    }

    Solution solution;
    cout << solution.minTotalDelay(n, trips) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minTotalDelay(n, trips) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  let ptr = 0;
  const n = parseInt(data[ptr++]);

  const trips = [];
  for (let i = 0; i < n; i++) {
    const [s, d] = data[ptr++].split(" ").map(Number);
    trips.push([s, d]);
  }

  const solution = new Solution();
  console.log(solution.minTotalDelay(n, trips));
});
```
