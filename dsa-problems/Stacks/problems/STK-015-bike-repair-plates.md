---
problem_id: STK_BIKE_REPAIR_PLATES__5937
display_id: STK-015
slug: bike-repair-plates
title: "Bike Repair Plates"
difficulty: Medium
difficulty_score: 47
topics:
  - Stack
  - Monotonic Stack
  - Simulation
tags:
  - stack
  - monotonic
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-015: Bike Repair Plates

## Problem Statement

You have a stack of metal plates with diameters, listed from top to bottom. Plates are removed one by one from the top. If a plate is smaller than a plate beneath it at the moment that plate is revealed, the lower plate is marked unsafe.

Count how many plates become unsafe during the entire removal process.

![Problem Illustration](../images/STK-015/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (diameters, top to bottom)

## Output Format

- Single integer: number of unsafe plates

## Constraints

- `1 <= n <= 200000`
- `1 <= d[i] <= 10^9`

## Example

**Input:**

```
3
5 2 4
```

**Output:**

```
1
```

**Explanation:**

When the top plate 5 is removed, 2 is revealed (safe). When 2 is removed, 4 is revealed and marked unsafe because 2 < 4.

![Example Visualization](../images/STK-015/example-1.png)

## Notes

- Scan from top to bottom
- Track the last removed plate diameter
- A plate is unsafe if it is larger than the plate removed just above it
- Time complexity: O(n)

## Related Topics

Stack Simulation, Monotonic Patterns, Arrays

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int countUnsafe(int[] d) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] d = new int[n];
        for (int i = 0; i < n; i++) d[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countUnsafe(d));
        sc.close();
    }
}
```

### Python

```python
def count_unsafe(d: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    d = [int(x) for x in data[1:1+n]]

    print(count_unsafe(d))

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
    int countUnsafe(const vector<int>& d) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> d(n);
    for (int i = 0; i < n; i++) cin >> d[i];

    Solution solution;
    cout << solution.countUnsafe(d) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countUnsafe(d) {
    // Your implementation here
    return 0;
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
  const d = [];
  for (let i = 0; i < n; i++) d.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  console.log(solution.countUnsafe(d).toString());
});
```
