---
problem_id: STK_ASSEMBLY_LINE_SPAN_RESET__3846
display_id: STK-016
slug: assembly-line-span-reset
title: "Assembly Line Span Reset"
difficulty: Medium
difficulty_score: 45
topics:
  - Stack
  - Spans
  - Arrays
tags:
  - stack
  - spans
  - arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-016: Assembly Line Span Reset

## Problem Statement

Given daily production counts, compute for each day the span of consecutive prior days with counts strictly less than today's count. The span includes today as 1.

Return the span counts.

![Problem Illustration](../images/STK-016/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers of spans

## Constraints

- `1 <= n <= 100000`
- `0 <= count[i] <= 10^9`

## Example

**Input:**

```
5
2 1 3 2 5
```

**Output:**

```
1 1 3 1 5
```

**Explanation:**

Day 3 (value 3) covers days 1..3, and day 5 covers all prior days.

![Example Visualization](../images/STK-016/example-1.png)

## Notes

- Use a monotonic decreasing stack of (value, span)
- Pop while top value is strictly less than current
- Add spans as you pop
- Time complexity: O(n)

## Related Topics

Stock Span, Monotonic Stack, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] computeSpans(int n, int[] counts) {
        // Implement here
        return new int[n];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] counts = new int[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) counts[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] res = sol.computeSpans(n, counts);
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
    def compute_spans(self, n: int, counts: list) -> list:
        # Implement here
        return [0] * n

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    counts = [int(x) for x in input_data[1:]]
    sol = Solution()
    res = sol.compute_spans(n, counts)
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
    vector<int> computeSpans(int n, const vector<int>& counts) {
        // Implement here
        return vector<int>(n, 0);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> counts(n);
        for (int i = 0; i < n; i++) {
            cin >> counts[i];
        }
        Solution sol;
        vector<int> res = sol.computeSpans(n, counts);
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
  computeSpans(n, counts) {
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
  const counts = input[1].split(/\s+/).map(Number);
  const sol = new Solution();
  const res = sol.computeSpans(n, counts);
  console.log(res.join(" "));
});
```
