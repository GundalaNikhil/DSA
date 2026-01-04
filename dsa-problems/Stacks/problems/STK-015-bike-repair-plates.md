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
    public int countUnsafePlates(int n, int[] diameters) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] diameters = new int[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) diameters[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            System.out.println(sol.countUnsafePlates(n, diameters));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_unsafe_plates(self, n: int, diameters: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    diameters = [int(x) for x in input_data[1:]]
    sol = Solution()
    print(sol.count_unsafe_plates(n, diameters))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int countUnsafePlates(int n, const vector<int>& diameters) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> diameters(n);
        for (int i = 0; i < n; i++) {
            cin >> diameters[i];
        }
        Solution sol;
        cout << sol.countUnsafePlates(n, diameters) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countUnsafePlates(n, diameters) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(line.trim());
}).on("close", () => {
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const diameters = input[1].split(/\s+/).map(Number);
  const sol = new Solution();
  console.log(sol.countUnsafePlates(n, diameters));
});
```
