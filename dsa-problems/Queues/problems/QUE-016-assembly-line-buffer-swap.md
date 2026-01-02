---
problem_id: QUE_ASSEMBLY_LINE_BUFFER_SWAP__9053
display_id: QUE-016
slug: assembly-line-buffer-swap
title: "Assembly Line Buffer Swap"
difficulty: Easy
difficulty_score: 29
topics:
  - Queue
  - Simulation
  - In-Place
tags:
  - queue
  - swap
  - simulation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-016: Assembly Line Buffer Swap

## Problem Statement

An assembly line has two buffers, each represented by a queue of equal length. Swap their contents using only queue operations.

Given the two queues, output their contents after the swap.

![Problem Illustration](../images/QUE-016/problem-illustration.png)

## Input Format

- First line: integer `n` (length of each queue)
- Second line: `n` space-separated integers (Queue 1, front to back)
- Third line: `n` space-separated integers (Queue 2, front to back)

## Output Format

- First line: Queue 1 after the swap
- Second line: Queue 2 after the swap

## Constraints

- `1 <= n <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
2
4 5
7 8
```

**Output:**

```
7 8
4 5
```

**Explanation:**

After swapping, the entire contents of the queues are exchanged.

![Example Visualization](../images/QUE-016/example-1.png)

## Notes

- The queues have equal length
- Use only enqueue and dequeue operations conceptually
- Time complexity: O(n)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Simulation, In-Place Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[][] swapQueues(int[] q1, int[] q2) {
        return null;
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

            int[] q1, q2;

            // If we have exactly 2n values
            if (remaining.size() == 2 * n) {
                q1 = new int[n];
                q2 = new int[n];
                for (int i = 0; i < n; i++) {
                    q1[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    q2[i] = remaining.get(n + i);
                }
            } else if (remaining.size() == n) {
                // Only n values - use as q1, create default q2
                q1 = new int[n];
                q2 = new int[n];
                for (int i = 0; i < n; i++) {
                    q1[i] = remaining.get(i);
                    q2[i] = 0;
                }
            } else {
                // Fallback
                int q1Len = Math.min(n, remaining.size());
                q1 = new int[q1Len];
                q2 = new int[q1Len];

                for (int i = 0; i < q1Len; i++) {
                    q1[i] = remaining.get(i);
                    if (i < remaining.size() - n) {
                        q2[i] = remaining.get(n + i);
                    } else {
                        q2[i] = 0;
                    }
                }
            }

            Solution sol = new Solution();
            int[][] result = sol.swapQueues(q1, q2);
            for (int j = 0; j < 2; j++) {
                for (int i = 0; i < result[j].length; i++) {
                    if (i > 0) System.out.print(" ");
                    System.out.print(result[j][i]);
                }
                System.out.println();
            }
        }
    }
}
```

### Python

```python
from typing import List
import sys

def swap_queues(q1: List[int], q2: List[int]) -> List[List[int]]:
    return []
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
            q1 = [int(x) for x in remaining[:n]]
            q2 = [int(x) for x in remaining[n:]]
        # If we have exactly n values, use as q1, create q2
        elif len(remaining) == n:
            q1 = [int(x) for x in remaining]
            q2 = [0] * n  # Default second queue
        # Otherwise try to split as much as possible
        else:
            q1 = [int(x) for x in remaining[:n]]
            q2 = [int(x) for x in remaining[n:]] if len(remaining) > n else [0] * n

        result = swap_queues(q1, q2)
        for resArr in result:
            print(" ".join(map(str, resArr)))
    except (StopIteration, ValueError, IndexError):
        pass

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
    vector<vector<int>> swapQueues(const vector<int>& q1, const vector<int>& q2) {
        return {};
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

        vector<int> q1, q2;

        // If we have exactly 2n values
        if ((int)remaining.size() == 2 * n) {
            q1.assign(remaining.begin(), remaining.begin() + n);
            q2.assign(remaining.begin() + n, remaining.end());
        } else if ((int)remaining.size() == n) {
            // Only n values - use as q1, create default q2
            q1.assign(remaining.begin(), remaining.end());
            q2.assign(n, 0);
        } else {
            // Fallback
            q1.assign(remaining.begin(), remaining.begin() + min(n, (int)remaining.size()));
            if ((int)remaining.size() > n) {
                q2.assign(remaining.begin() + n, remaining.end());
            }
            // Pad q2 with 0s if needed
            while ((int)q2.size() < n) {
                q2.push_back(0);
            }
        }

        Solution sol;
        vector<vector<int>> result = sol.swapQueues(q1, q2);
        for (const auto& resArr : result) {
            for (int i = 0; i < (int)resArr.size(); i++) {
                cout << (i ? " " : "") << resArr[i];
            }
            cout << endl;
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  swapQueues(q1, q2) {
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

  let q1, q2;

  // If we have exactly 2n values
  if (remaining.length === 2 * n) {
    q1 = remaining.slice(0, n).map(x => parseInt(x, 10));
    q2 = remaining.slice(n, 2 * n).map(x => parseInt(x, 10));
  } else if (remaining.length === n) {
    // Only n values - use as q1, create default q2
    q1 = remaining.map(x => parseInt(x, 10));
    q2 = Array(n).fill(0);
  } else {
    // Fallback
    q1 = remaining.slice(0, n).map(x => parseInt(x, 10));
    q2 = remaining.length > n ? remaining.slice(n).map(x => parseInt(x, 10)) : Array(n).fill(0);
    // Pad q2 if needed
    while (q2.length < n) {
      q2.push(0);
    }
  }

  const solution = new Solution();
  const result = solution.swapQueues(q1, q2);
  result.forEach((resArr) => {
    console.log(resArr.join(" "));
  });
});
```

