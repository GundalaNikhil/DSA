---
problem_id: STK_ROOFTOP_SUNSET_COUNT__2974
display_id: STK-004
slug: rooftop-sunset-count
title: "Rooftop Sunset Count"
difficulty: Easy
difficulty_score: 32
topics:
  - Stack
  - Monotonic Stack
  - Arrays
tags:
  - stack
  - monotonic
  - arrays
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-004: Rooftop Sunset Count

## Problem Statement

Given building heights from west to east, a building can see the sunset if there is no taller building to its left. Count how many buildings can see the sunset.

![Problem Illustration](../images/STK-004/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (heights)

## Output Format

- Single integer: number of buildings with sunset view

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i] <= 10^9`

## Example

**Input:**

```
5
2 5 2 6 1
```

**Output:**

```
3
```

**Explanation:**

Buildings with sunset view are heights 2, 5, and 6.

![Example Visualization](../images/STK-004/example-1.png)

## Notes

- Use a monotonic decreasing stack
- Pop while current height is greater than or equal to stack top
- Count remaining stack size at the end
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Visibility, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countSunsetViews(int[] heights) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] heights = new int[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) heights[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            System.out.println(sol.countSunsetViews(heights));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_sunset_views(self, heights: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    heights = [int(x) for x in input_data[1:]]
    sol = Solution()
    print(sol.count_sunset_views(heights))

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
    int countSunsetViews(const vector<int>& heights) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> heights(n);
        for (int i = 0; i < n; i++) {
            cin >> heights[i];
        }
        Solution sol;
        cout << sol.countSunsetViews(heights) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countSunsetViews(heights) {
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
  const heights = input[1].split(/\s+/).map(Number);
  const sol = new Solution();
  console.log(sol.countSunsetViews(heights));
});
```
