---
problem_id: QUE_BUS_LOOP_ONE_SKIP__2986
display_id: QUE-012
slug: bus-loop-one-skip
title: "Bus Loop With One Free Skip"
difficulty: Medium
difficulty_score: 58
topics:
  - Greedy
  - Queue
  - Circular Route
tags:
  - greedy
  - circular
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-012: Bus Loop With One Free Skip

## Problem Statement

A circular bus route has `n` stops. At stop `i`, the bus can gain `gain[i]` fuel and must spend `cost[i]` fuel to reach the next stop.

You must skip refueling at exactly one stop (the fuel there is lost). Find a starting index that allows the bus to complete one full loop with that single skip. If no such start exists, output `-1`.

![Problem Illustration](../images/QUE-012/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `gain[i]`
- Third line: `n` space-separated integers `cost[i]`

## Output Format

- Single integer: a valid starting index (0-based), or `-1` if impossible

## Constraints

- `1 <= n <= 100000`
- `0 <= gain[i], cost[i] <= 10^9`

## Example

**Input:**

```
3
4 5 1
3 3 2
```

**Output:**

```
0
```

**Explanation:**

Start at index 0 and skip refuel at stop 2:

- Stop 0: gain 4, cost 3 -> fuel 1
- Stop 1: gain 5, cost 3 -> fuel 3
- Stop 2: skip gain 1, cost 2 -> fuel 1

The bus completes the loop with fuel remaining, so index 0 is valid.

![Example Visualization](../images/QUE-012/example-1.png)

## Notes

- Track two running balances: without skip and with skip used
- If both balances drop below 0, reset the start
- The total gain minus the skipped refuel must still cover total cost
- Time complexity: O(n)

## Related Topics

Greedy, Circular Array, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int findStart(int[] gain, int[] cost) {
        // Your implementation here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] gain = new int[n];
        int[] cost = new int[n];
        for (int i = 0; i < n; i++) {
            gain[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            cost[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.findStart(gain, cost));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def find_start(gain: List[int], cost: List[int]) -> int:
    # Your implementation here
    return -1

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    gain = [int(next(it)) for _ in range(n)]
    cost = [int(next(it)) for _ in range(n)]

    result = find_start(gain, cost)
    sys.stdout.write(str(result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findStart(const vector<int>& gain, const vector<int>& cost) {
        // Your implementation here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> gain(n), cost(n);
    for (int i = 0; i < n; i++) {
        cin >> gain[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> cost[i];
    }

    Solution solution;
    cout << solution.findStart(gain, cost) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findStart(gain, cost) {
    // Your implementation here
    return -1;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const gain = [];
  const cost = [];
  for (let i = 0; i < n; i++) {
    gain.push(parseInt(data[idx++], 10));
  }
  for (let i = 0; i < n; i++) {
    cost.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.findStart(gain, cost);
  console.log(result.toString());
});
```
