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
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[] gain, cost;

            // If we have exactly 2n values
            if (remaining.size() == 2 * n) {
                gain = new int[n];
                cost = new int[n];
                for (int i = 0; i < n; i++) {
                    gain[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    cost[i] = remaining.get(n + i);
                }
            } else if (remaining.size() == n) {
                // Only n values - use as gain, create default cost of 1s
                gain = new int[n];
                cost = new int[n];
                for (int i = 0; i < n; i++) {
                    gain[i] = remaining.get(i);
                    cost[i] = 1;
                }
            } else {
                // Fallback
                int gainLen = Math.min(n, remaining.size());
                gain = new int[gainLen];
                cost = new int[gainLen];

                for (int i = 0; i < gainLen; i++) {
                    gain[i] = remaining.get(i);
                    if (i < remaining.size() - n) {
                        cost[i] = remaining.get(n + i);
                    } else {
                        cost[i] = 1;
                    }
                }
            }

            Solution solution = new Solution();
            System.out.println(solution.findStart(gain, cost));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

def find_start(gain: List[int], cost: List[int]) -> int:
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        remaining = list(iterator)

        # If we have exactly 2n values, split them in half
        if len(remaining) == 2 * n:
            gain = [int(x) for x in remaining[:n]]
            cost = [int(x) for x in remaining[n:]]
        # If we have exactly n values, use as gain, create cost array
        elif len(remaining) == n:
            gain = [int(x) for x in remaining]
            cost = [1] * n  # Default cost
        # Otherwise try to split as much as possible
        else:
            gain = [int(x) for x in remaining[:n]]
            cost = [int(x) for x in remaining[n:]] if len(remaining) > n else [1] * n

        result = find_start(gain, cost)
        print(result)
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findStart(vector<int>& gain, const vector<int>& cost) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<int> gain, cost;

        // If we have exactly 2n values
        if ((int)remaining.size() == 2 * n) {
            gain.assign(remaining.begin(), remaining.begin() + n);
            cost.assign(remaining.begin() + n, remaining.end());
        } else if ((int)remaining.size() == n) {
            // Only n values - use as gain, create default cost of 1s
            gain.assign(remaining.begin(), remaining.end());
            cost.assign(n, 1);
        } else {
            // Fallback
            gain.assign(remaining.begin(), remaining.begin() + min(n, (int)remaining.size()));
            if ((int)remaining.size() > n) {
                cost.assign(remaining.begin() + n, remaining.end());
            }
            // Pad with 1s if needed
            while ((int)cost.size() < n) {
                cost.push_back(1);
            }
        }

        Solution solution;
        cout << solution.findStart(gain, cost) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findStart(gain, cost) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let gain, cost;

  // If we have exactly 2n values, first n are gain, second n are cost
  if (remaining.length === 2 * n) {
    gain = remaining.slice(0, n).map(x => parseInt(x, 10));
    cost = remaining.slice(n, 2 * n).map(x => parseInt(x, 10));
  } else if (remaining.length === n) {
    // Only n values provided - use as gain, create default cost array
    gain = remaining.map(x => parseInt(x, 10));
    cost = Array(n).fill(1);
  } else {
    // Fallback: first n values as gain, rest as cost (or default)
    gain = remaining.slice(0, n).map(x => parseInt(x, 10));
    cost = remaining.length > n ? remaining.slice(n).map(x => parseInt(x, 10)) : Array(n).fill(1);
    // Pad cost if needed
    while (cost.length < n) {
      cost.push(1);
    }
  }

  const solution = new Solution();
  console.log(solution.findStart(gain, cost));
});
```

