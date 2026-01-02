---
problem_id: QUE_EVENT_REGISTRATION_MERGE__6205
display_id: QUE-011
slug: event-registration-merge
title: "Event Registration Merge"
difficulty: Easy
difficulty_score: 22
topics:
  - Queue
  - Merge
  - Two Pointers
tags:
  - queue
  - merge
  - two-pointers
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-011: Event Registration Merge

## Problem Statement

Two event registration lines are already sorted by registration ID. Merge the two queues into one sorted queue while preserving the order of equal IDs.

![Problem Illustration](../images/QUE-011/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first queue)
- Second line: `n` space-separated integers (first queue)
- Third line: integer `m` (length of second queue)
- Fourth line: `m` space-separated integers (second queue)

## Output Format

- Single line: merged queue values in nondecreasing order
- If both queues are empty, print an empty line

## Constraints

- `0 <= n, m <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
3
3 5 9
3
1 4 10
```

**Output:**

```
1 3 4 5 9 10
```

**Explanation:**

Merge by repeatedly taking the smaller front value:

- 1 (from second)
- 3 (from first)
- 4 (from second)
- 5 (from first)
- 9 (from first)
- 10 (from second)

![Example Visualization](../images/QUE-011/example-1.png)

## Notes

- This is the queue version of merge in merge sort
- Always compare fronts of both queues
- Time complexity: O(n + m)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Merge, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] mergeQueues(int[] a, int[] b) {
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

            int[] a, b;

            // If we have exactly 2n values, split them in half
            if (remaining.size() == 2 * n) {
                a = new int[n];
                b = new int[n];
                for (int i = 0; i < n; i++) {
                    a[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    b[i] = remaining.get(n + i);
                }
            } else if (remaining.size() == n) {
                // Only n values - use as a, create empty b
                a = new int[n];
                b = new int[0];
                for (int i = 0; i < n; i++) {
                    a[i] = remaining.get(i);
                }
            } else if (remaining.size() > n) {
                // First value is m (size of b), rest split
                int m = remaining.get(0);
                if (remaining.size() >= n + m) {
                    a = new int[n];
                    b = new int[m];
                    for (int i = 0; i < n; i++) {
                        a[i] = remaining.get(i + 1);
                    }
                    for (int i = 0; i < m; i++) {
                        b[i] = remaining.get(n + 1 + i);
                    }
                } else {
                    int aLen = Math.min(n, remaining.size() - 1);
                    a = new int[aLen];
                    b = new int[remaining.size() - 1 - aLen];
                    for (int i = 0; i < aLen; i++) {
                        a[i] = remaining.get(i + 1);
                    }
                    for (int i = 0; i < b.length; i++) {
                        b[i] = remaining.get(aLen + 1 + i);
                    }
                }
            } else {
                // Fallback
                a = new int[remaining.size()];
                b = new int[0];
                for (int i = 0; i < a.length; i++) {
                    a[i] = remaining.get(i);
                }
            }

            Solution solution = new Solution();
            int[] result = solution.mergeQueues(a, b);
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

def merge_queues(a: List[int], b: List[int]) -> List[int]:
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
            a = [int(x) for x in remaining[:n]]
            b = [int(x) for x in remaining[n:]]
        # If we have n values, use as array a, create empty b
        elif len(remaining) == n:
            a = [int(x) for x in remaining]
            b = []
        # If we have n + m + 1 values, first is m, rest split
        elif len(remaining) > n:
            m = int(remaining[0]) if remaining else n
            if len(remaining) >= n + m:
                a = [int(x) for x in remaining[1:n+1]]
                b = [int(x) for x in remaining[n+1:n+1+m]]
            else:
                a = [int(x) for x in remaining[1:n+1]]
                b = [int(x) for x in remaining[n+1:]]
        else:
            a = [int(x) for x in remaining]
            b = []

        result = merge_queues(a, b)
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

using namespace std;

class Solution {
public:
    vector<int> mergeQueues(const vector<int>& a, const vector<int>& b) {
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

        vector<int> a, b;

        // If we have exactly 2n values, split them in half
        if ((int)remaining.size() == 2 * n) {
            a.assign(remaining.begin(), remaining.begin() + n);
            b.assign(remaining.begin() + n, remaining.end());
        } else if ((int)remaining.size() == n) {
            // Only n values - use as a, create empty b
            a.assign(remaining.begin(), remaining.end());
            b.clear();
        } else if ((int)remaining.size() > n) {
            // First value is m (size of b), rest split
            int m = remaining[0];
            if ((int)remaining.size() >= n + m) {
                a.assign(remaining.begin() + 1, remaining.begin() + n + 1);
                b.assign(remaining.begin() + n + 1, remaining.begin() + n + 1 + m);
            } else {
                a.assign(remaining.begin() + 1, remaining.begin() + min(n + 1, (int)remaining.size()));
                b.assign(remaining.begin() + min(n + 1, (int)remaining.size()), remaining.end());
            }
        } else {
            // Fallback
            a.assign(remaining.begin(), remaining.end());
            b.clear();
        }

        Solution solution;
        vector<int> result = solution.mergeQueues(a, b);
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
  mergeQueues(a, b) {
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
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(data[idx++], 10));
  }
  const m = parseInt(data[idx++], 10);
  const b = [];
  for (let i = 0; i < m; i++) {
    b.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.mergeQueues(a, b);
  console.log(result.join(" "));
});
```

