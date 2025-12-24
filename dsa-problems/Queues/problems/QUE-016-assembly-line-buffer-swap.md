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
        // Your implementation here
        return new int[0][0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] q1 = new int[n];
        int[] q2 = new int[n];
        for (int i = 0; i < n; i++) {
            q1[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            q2[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[][] result = solution.swapQueues(q1, q2);
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        for (int i = 0; i < result[0].length; i++) {
            if (i > 0) sb1.append(' ');
            sb1.append(result[0][i]);
        }
        for (int i = 0; i < result[1].length; i++) {
            if (i > 0) sb2.append(' ');
            sb2.append(result[1][i]);
        }
        System.out.println(sb1.toString());
        System.out.println(sb2.toString());
        sc.close();
    }
}
```

### Python

```python
from typing import List

def swap_queues(q1: List[int], q2: List[int]) -> List[List[int]]:
    # Your implementation here
    return [[], []]

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q1 = [int(next(it)) for _ in range(n)]
    q2 = [int(next(it)) for _ in range(n)]

    result = swap_queues(q1, q2)
    print(" ".join(str(x) for x in result[0]))
    print(" ".join(str(x) for x in result[1]))

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
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> q1(n), q2(n);
    for (int i = 0; i < n; i++) {
        cin >> q1[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> q2[i];
    }

    Solution solution;
    vector<vector<int>> result = solution.swapQueues(q1, q2);
    for (int i = 0; i < (int)result[0].size(); i++) {
        if (i) cout << ' ';
        cout << result[0][i];
    }
    cout << "\n";
    for (int i = 0; i < (int)result[1].size(); i++) {
        if (i) cout << ' ';
        cout << result[1][i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  swapQueues(q1, q2) {
    // Your implementation here
    return [[], []];
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
  const q1 = [];
  const q2 = [];
  for (let i = 0; i < n; i++) {
    q1.push(parseInt(data[idx++], 10));
  }
  for (let i = 0; i < n; i++) {
    q2.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.swapQueues(q1, q2);
  console.log(result[0].join(" "));
  console.log(result[1].join(" "));
});
```
