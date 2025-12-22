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
    public int[] spans(int[] counts) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] counts = new int[n];
        for (int i = 0; i < n; i++) counts[i] = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.spans(counts);
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
def spans(counts: list[int]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    counts = [int(x) for x in data[1:1+n]]

    result = spans(counts)
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
    vector<int> spans(const vector<int>& counts) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> counts(n);
    for (int i = 0; i < n; i++) cin >> counts[i];

    Solution solution;
    vector<int> result = solution.spans(counts);
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
  spans(counts) {
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
  const counts = [];
  for (let i = 0; i < n; i++) counts.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.spans(counts);
  console.log(result.join(" "));
});
```
