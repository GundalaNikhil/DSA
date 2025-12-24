---
problem_id: QUE_CAFETERIA_QUEUE_ROTATION__9067
display_id: QUE-003
slug: cafeteria-queue-rotation
title: "Cafeteria Queue Rotation"
difficulty: Easy
difficulty_score: 20
topics:
  - Queue
  - Array Manipulation
  - Simulation
tags:
  - queue
  - rotation
  - easy
  - arrays
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-003: Cafeteria Queue Rotation

## Problem Statement

A cafeteria line is represented as a queue of student IDs. The manager rotates the line by moving the first `k` students to the back of the line in the same order.

Given the initial queue and `k`, output the resulting order after the left rotation. If `k` is larger than the queue length, use `k % n` rotations.

![Problem Illustration](../images/QUE-003/problem-illustration.png)

## Input Format

- First line: integer `n` (number of students)
- Second line: `n` space-separated integers (queue order, front to back)
- Third line: integer `k` (number of left rotations)

## Output Format

- Single line with the rotated queue values, space-separated
- If `n = 0`, print an empty line

## Constraints

- `1 <= n <= 100000`
- `0 <= k <= 10^9`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
4
4 9 1 7
3
```

**Output:**

```
7 4 9 1
```

**Explanation:**

Rotate left by `3`:

- Move 4 -> back
- Move 9 -> back
- Move 1 -> back

Queue becomes `[7, 4, 9, 1]`.

![Example Visualization](../images/QUE-003/example-1.png)

## Notes

- Normalize `k` with `k % n` to avoid extra work
- You can simulate by dequeuing and enqueuing `k` times
- Time complexity: O(n)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Rotation, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] rotateQueue(int[] values, long k) {
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
        long k = sc.nextLong();

        Solution solution = new Solution();
        int[] result = solution.rotateQueue(values, k);
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

def rotate_queue(values: List[int], k: int) -> List[int]:
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

    result = rotate_queue(values, k)
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
    vector<int> rotateQueue(const vector<int>& values, long long k) {
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
    long long k;
    cin >> k;

    Solution solution;
    vector<int> result = solution.rotateQueue(values, k);
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
  rotateQueue(values, k) {
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
  const result = solution.rotateQueue(values, k);
  console.log(result.join(" "));
});
```
