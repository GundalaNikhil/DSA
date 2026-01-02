---
problem_id: QUE_CORRIDOR_WINDOW_SECOND_MINIMUM__2748
display_id: QUE-008
slug: corridor-window-second-minimum
title: "Corridor Window Second Minimum"
difficulty: Medium
difficulty_score: 48
topics:
  - Sliding Window
  - Ordered Map
  - Queue
tags:
  - sliding-window
  - multiset
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-008: Corridor Window Second Minimum

## Problem Statement

Security sensors report values along a corridor. For each sliding window of size `k`, you must output the second smallest value in that window.

If the window size is `1`, the second smallest value is defined as the only element. If the smallest value appears at least twice, the second smallest equals the smallest.

![Problem Illustration](../images/QUE-008/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` space-separated integers (sensor values)

## Output Format

- Single line: `n - k + 1` integers, each the second smallest for a window

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5 3
6 2 5 1 7
```

**Output:**

```
5 2 5
```

**Explanation:**

Windows and second minima:

- [6, 2, 5] -> sorted [2, 5, 6], second smallest = 5
- [2, 5, 1] -> sorted [1, 2, 5], second smallest = 2
- [5, 1, 7] -> sorted [1, 5, 7], second smallest = 5

![Example Visualization](../images/QUE-008/example-1.png)

## Notes

- Maintain a balanced structure with counts to track the smallest two values
- Removing outgoing elements must update counts correctly
- Time complexity: O(n log k)
- Space complexity: O(k)

## Related Topics

Sliding Window, Multiset, Ordered Map

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] secondMinimums(int[] values, int k) {
        // Implementation here
        return new int[0];
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

            int[] values;
            int k = 2;  // Default

            // If we have exactly n values
            if (remaining.size() == n) {
                values = new int[n];
                for (int i = 0; i < n; i++) {
                    values[i] = remaining.get(i);
                }
                k = 2;
            } else if (remaining.size() == n + 1) {
                // First is k, rest are values
                k = remaining.get(0);
                values = new int[n];
                for (int i = 0; i < n; i++) {
                    values[i] = remaining.get(i + 1);
                }
            } else {
                // Fallback
                k = !remaining.isEmpty() ? remaining.get(0) : 2;
                values = new int[Math.min(n, remaining.size() - 1)];
                for (int i = 0; i < values.length; i++) {
                    values[i] = remaining.get(i + 1);
                }
            }

            Solution solution = new Solution();
            int[] result = solution.secondMinimums(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys
import heapq

class Solution:
    def second_minimums(self, values: List[int], k: int) -> List[int]:
        # Implementation here
        return []

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        remaining = list(iterator)

        # If we have exactly n values, use n as window size (or default k=2)
        if len(remaining) == n:
            values = [int(x) for x in remaining]
            k = 2  # Default window size
        # If we have n+1 values, first is k, rest are values
        elif len(remaining) == n + 1:
            k = int(remaining[0])
            values = [int(x) for x in remaining[1:]]
        # If we have more than n, assume first is k, next n are values
        else:
            k = int(remaining[0]) if remaining else 2
            values = [int(x) for x in remaining[1:n+1]]

        result = second_minimums(values, k)
        print(" ".join(map(str, result)))
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> secondMinimums(const vector<int>& values, int k) {
        // Implementation here
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

        vector<int> values;
        int k = 2;  // Default

        // If we have exactly n values
        if ((int)remaining.size() == n) {
            values.assign(remaining.begin(), remaining.end());
            k = 2;
        } else if ((int)remaining.size() == n + 1) {
            // First is k, rest are values
            k = remaining[0];
            values.assign(remaining.begin() + 1, remaining.begin() + n + 1);
        } else {
            // Fallback
            k = !remaining.empty() ? remaining[0] : 2;
            for (int i = 1; i <= n && i < (int)remaining.size(); i++) {
                values.push_back(remaining[i]);
            }
        }

        Solution solution;
        vector<int> result = solution.secondMinimums(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  secondMinimums(values, k) {
    // Implementation here
    return null;
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

  let k, values;
  if (remaining.length === n) {
    // Only values, no k -> k = 2 (default)
    values = remaining.map(x => parseInt(x, 10));
    k = 2;
  } else if (remaining.length === n + 1) {
    // First is k, rest are values
    k = parseInt(remaining[0], 10);
    values = remaining.slice(1, n + 1).map(x => parseInt(x, 10));
  } else {
    // Default case: try to parse k and n values
    k = parseInt(remaining[0], 10) || 2;
    values = remaining.slice(1, n + 1).map(x => parseInt(x, 10));
  }

  const solution = new Solution();
  const result = solution.secondMinimums(values, k);
  console.log(result.join(" "));
});
```
