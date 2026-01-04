---
problem_id: STK_CANTEEN_TOKEN_CLIMB_SPAN__6180
display_id: STK-008
slug: canteen-token-climb-span
title: "Canteen Token Climb Span"
difficulty: Medium
difficulty_score: 50
topics:
  - Stack
  - Monotonic Stack
  - Spans
tags:
  - stack
  - spans
  - monotonic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-008: Canteen Token Climb Span

## Problem Statement

For each day, compute how many consecutive prior days had demand strictly lower than today's demand. If any prior day equals today's demand, the span resets to 0 at that day.

Return the span counts (not including today).

![Problem Illustration](../images/STK-008/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (demands)

## Output Format

- Single line: `n` integers of spans

## Constraints

- `1 <= n <= 100000`
- `0 <= demand[i] <= 10^9`

## Example

**Input:**

```
5
3 1 2 2 5
```

**Output:**

```
0 0 1 0 4
```

**Explanation:**

Day 4 (value 5) has four prior days with smaller demand; day 3 equals 2 so its span is 0.

![Example Visualization](../images/STK-008/example-1.png)

## Notes

- Use a strictly increasing stack of (value, index)
- Pop while values are strictly lower
- If the top equals current, span is 0
- Time complexity: O(n)

## Related Topics

Stock Span, Monotonic Stack, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] computeSpans(int n, int[] demands) {
        // Implement here
        return new int[n];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] demands = new int[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) demands[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] res = sol.computeSpans(n, demands);
            for (int i = 0; i < n; i++) {
                System.out.print(res[i] + (i == n - 1 ? "" : " "));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def compute_spans(self, n: int, demands: list) -> list:
        # Implement here
        return [0] * n

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    demands = [int(x) for x in input_data[1:]]
    sol = Solution()
    res = sol.compute_spans(n, demands)
    print(*(res))

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
    vector<int> computeSpans(int n, const vector<int>& demands) {
        // Implement here
        return vector<int>(n, 0);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> demands(n);
        for (int i = 0; i < n; i++) {
            cin >> demands[i];
        }
        Solution sol;
        vector<int> res = sol.computeSpans(n, demands);
        for (int i = 0; i < n; i++) {
            cout << res[i] << (i == n - 1 ? "" : " ");
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
  computeSpans(n, demands) {
    // Implement here
    return new Array(n).fill(0);
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
  const demands = input[1].split(/\s+/).map(Number);
  const sol = new Solution();
  const res = sol.computeSpans(n, demands);
  console.log(res.join(" "));
});
```
