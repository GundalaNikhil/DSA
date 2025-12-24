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
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.secondMinimums(values, k);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
from typing import List

def second_minimums(values: List[int], k: int) -> List[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    values = [int(next(it)) for _ in range(n)]

    result = second_minimums(values, k)
    sys.stdout.write(" ".join(str(x) for x in result))

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
    vector<int> secondMinimums(const vector<int>& values, int k) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    Solution solution;
    vector<int> result = solution.secondMinimums(values, k);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  secondMinimums(values, k) {
    // Your implementation here
    return [];
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
  const k = parseInt(data[idx++], 10);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.secondMinimums(values, k);
  console.log(result.join(" "));
});
```
