---
problem_id: QUE_LAB_WINDOW_INSTABILITY__3951
display_id: QUE-007
slug: lab-window-instability
title: "Lab Window Instability"
difficulty: Medium
difficulty_score: 50
topics:
  - Sliding Window
  - Queue
  - Heaps
tags:
  - sliding-window
  - deque
  - median
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-007: Lab Window Instability

## Problem Statement

A lab monitors sensor readings in a sliding window. For each window of size `k`, compute:

```
instability = floor((max - min) / median)
```

The median is the lower median when `k` is even. If the median is `0`, output `0` for that window.

![Problem Illustration](../images/QUE-007/problem-illustration.png)

## Input Format

- First line: two integers `n` and `k`
- Second line: `n` space-separated integers (readings)

## Output Format

- Single line: `n - k + 1` integers, each the instability of a window

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`
- Readings fit in 32-bit signed integer

## Example

**Input:**

```
5 3
5 1 4 6 2
```

**Output:**

```
1 1 1
```

**Explanation:**

Windows:

- [5, 1, 4] -> min=1, max=5, median=4, (5-1)/4=1
- [1, 4, 6] -> min=1, max=6, median=4, (6-1)/4=1
- [4, 6, 2] -> min=2, max=6, median=4, (6-2)/4=1

![Example Visualization](../images/QUE-007/example-1.png)

## Notes

- Use deques for max and min in O(1) amortized time
- Use two heaps with lazy deletion for the median
- Keep the lower heap size equal to or one more than the upper heap
- Total time complexity should be O(n log k)

## Related Topics

Sliding Window, Deque, Median Maintenance

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] windowInstability(int[] values, int k) {
        // Your implementation here
        return new long[0];
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
        long[] result = solution.windowInstability(values, k);
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

def window_instability(values: List[int], k: int) -> List[int]:
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

    result = window_instability(values, k)
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
    vector<long long> windowInstability(const vector<int>& values, int k) {
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
    vector<long long> result = solution.windowInstability(values, k);
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
  windowInstability(values, k) {
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
  const result = solution.windowInstability(values, k);
  console.log(result.join(" "));
});
```
