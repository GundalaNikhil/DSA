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
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            int[] result = solution.reverseFirstK(values, k);
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
from collections import deque
import sys

def reverse_first_k(values: List[int], k: int) -> List[int]:
    return []
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]

        result = reverse_first_k(values, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> reverseFirstK(const vector<int>& values, int k) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        int k;
        cin >> k;
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }

        Solution solution;
        vector<int> result = solution.reverseFirstK(values, k);
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
  reverseFirstK(values, k) {
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
  const k = parseInt(data[idx++], 10);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.reverseFirstK(values, k);
  console.log(result.join(" "));
});
```

