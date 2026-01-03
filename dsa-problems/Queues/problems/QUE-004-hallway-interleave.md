---
problem_id: QUE_HALLWAY_INTERLEAVE__1582
display_id: QUE-004
slug: hallway-interleave
title: "Hallway Interleave"
difficulty: Easy
difficulty_score: 24
topics:
  - Queue
  - Interleaving
  - Simulation
tags:
  - queue
  - interleaving
  - easy
  - simulation
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-004: Hallway Interleave

## Problem Statement

A hallway line of students has even length. You must interleave the first half of the line with the second half while preserving the relative order inside each half.

For example, `[11, 12, 13, 14]` becomes `[11, 13, 12, 14]`.

![Problem Illustration](../images/QUE-004/problem-illustration.png)

## Input Format

- First line: even integer `n` (queue length)
- Second line: `n` space-separated integers (queue order, front to back)

## Output Format

- Single line: interleaved queue values, space-separated

## Constraints

- `2 <= n <= 100000`
- `n` is even
- Values fit in 32-bit signed integer

## Example

**Input:**

```
4
11 12 13 14
```

**Output:**

```
11 13 12 14
```

**Explanation:**

First half: `[11, 12]`
Second half: `[13, 14]`

Interleaving yields `[11, 13, 12, 14]`.

![Example Visualization](../images/QUE-004/example-1.png)

## Notes

- Use an auxiliary queue or stack to split halves
- The relative order within each half must not change
- Time complexity: O(n)
- Space complexity: O(n) for auxiliary storage

## Related Topics

Queue, Interleaving, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] interleaveQueue(int[] values) {
        //Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            int[] result = solution.interleaveQueue(values);
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

def interleave_queue(values: List[int]) -> List[int]:
    # //Implement here
    return []

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]

        result = interleave_queue(values)
        if result:  # Only print if result is non-empty
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

using namespace std;

class Solution {
public:
    vector<int> interleaveQueue(const vector<int>& values) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }

        Solution solution;
        vector<int> result = solution.interleaveQueue(values);
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
  interleaveQueue(values) {
    //Implement here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) =>
  data.push(
    ...line
      .trim()
      .split(/\s+/)
      .filter((x) => x !== "")
  )
);
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.interleaveQueue(values);
  console.log(result.join(" "));
});
```
