---
problem_id: QUE_DEQUE_BALANCE_REARRANGE__5142
display_id: QUE-014
slug: deque-balance-rearrange
title: "Deque Balance Rearrange"
difficulty: Medium
difficulty_score: 41
topics:
  - Deque
  - Two Pointers
  - Simulation
tags:
  - deque
  - two-pointers
  - rearrangement
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-014: Deque Balance Rearrange

## Problem Statement

You are given an array of values. Build a new deque by alternately taking from the front and back of the array, starting with the front. Output the deque from front to back.

For example, `[2, 4, 6, 8]` becomes `[2, 8, 4, 6]`.

![Problem Illustration](../images/QUE-014/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single line: deque contents from front to back, space-separated

## Constraints

- `1 <= n <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
4
2 4 6 8
```

**Output:**

```
2 8 4 6
```

**Explanation:**

Take alternately from the ends:

- Take front 2
- Take back 8
- Take front 4
- Take back 6

![Example Visualization](../images/QUE-014/example-1.png)

## Notes

- Use two pointers `l` and `r`
- Append elements to the output in the chosen order
- Time complexity: O(n)
- Space complexity: O(n) for the output

## Related Topics

Deque, Two Pointers, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] buildDeque(int[] values) {
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

            Solution sol = new Solution();
            int[] result = sol.buildDeque(values);
            for (int i = 0; i < result.length; i++) {
                if (i > 0) System.out.print(" ");
                System.out.print(result[i]);
            }
            System.out.println();
        }
    }
}
```

### Python

```python
from typing import List
import sys

def build_deque(values: List[int]) -> List[int]:
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

        result = build_deque(values)
        print(" ".join(map(str, result)))
    except (StopIteration, ValueError):
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
    vector<int> buildDeque(const vector<int>& values) {
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
        for (int i = 0; i < n; i++) cin >> values[i];

        Solution sol;
        vector<int> result = sol.buildDeque(values);
        for (int i = 0; i < (int)result.size(); i++) {
            cout << (i ? " " : "") << result[i];
        }
        cout << endl;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  buildDeque(values) {
    //Implement here
    return 0;
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
  const result = solution.buildDeque(values);
  console.log(result.join(" "));
});
```
