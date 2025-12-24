---
problem_id: QUE_LAB_PRINTER_REVERSAL__6429
display_id: QUE-005
slug: lab-printer-reversal
title: "Lab Printer Reversal"
difficulty: Easy
difficulty_score: 26
topics:
  - Queue
  - Stack
  - Simulation
tags:
  - queue
  - stack
  - reversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-005: Lab Printer Reversal

## Problem Statement

A lab printer processes jobs in a queue. The technician wants to reverse the first `k` jobs while preserving the order of the remaining jobs.

Given the queue and `k`, output the new queue order.

![Problem Illustration](../images/QUE-005/problem-illustration.png)

## Input Format

- First line: integer `n` (number of jobs)
- Second line: `n` space-separated integers (queue order, front to back)
- Third line: integer `k` (number of jobs to reverse from the front)

## Output Format

- Single line: updated queue values, space-separated

## Constraints

- `1 <= n <= 100000`
- `1 <= k <= n`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
5
2 4 6 8 10
4
```

**Output:**

```
8 6 4 2 10
```

**Explanation:**

Reverse the first 4 jobs:

- Original: `[2, 4, 6, 8, 10]`
- After reversal of first 4: `[8, 6, 4, 2, 10]`

![Example Visualization](../images/QUE-005/example-1.png)

## Notes

- Use a stack to reverse the first `k` elements
- Append the remaining `n - k` elements in their original order
- Time complexity: O(n)
- Space complexity: O(k)

## Related Topics

Queue, Stack, Reversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] reverseFirstK(int[] values, int k) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
        }
        int k = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.reverseFirstK(values, k);
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

def reverse_first_k(values: List[int], k: int) -> List[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    values = [int(next(it)) for _ in range(n)]
    k = int(next(it))

    result = reverse_first_k(values, k)
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
    vector<int> reverseFirstK(const vector<int>& values, int k) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }
    int k;
    cin >> k;

    Solution solution;
    vector<int> result = solution.reverseFirstK(values, k);
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
  reverseFirstK(values, k) {
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
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }
  const k = parseInt(data[idx++], 10);

  const solution = new Solution();
  const result = solution.reverseFirstK(values, k);
  console.log(result.join(" "));
});
```
