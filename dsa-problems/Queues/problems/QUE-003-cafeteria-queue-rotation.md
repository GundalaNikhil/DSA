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
    public void rotateQueue(int n, int[] students, long k) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] students = new int[n];
        for (int i = 0; i < n; i++) students[i] = sc.nextInt();
        long k = sc.nextLong();
        Solution sol = new Solution();
        sol.rotateQueue(n, students, k);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def rotate_queue(self, n, students, k):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    students = [int(x) for x in input_data[1:n+1]]
    k = int(input_data[n+1])
    sol = Solution()
    sol.rotate_queue(n, students, k)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void rotateQueue(int n, vector<int>& students, long long k) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> students(n);
    for (int i = 0; i < n; i++) cin >> students[i];
    long long k;
    cin >> k;
    Solution sol;
    sol.rotateQueue(n, students, k);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  rotateQueue(n, students, k) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const students = [];
  for (let i = 0; i < n; i++) students.push(parseInt(input[1 + i]));
  const k = BigInt(input[1 + n]);
  const sol = new Solution();
  sol.rotateQueue(n, students, k);
}

solve();
```
