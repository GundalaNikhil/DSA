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
    public int[] spans(int[] demand) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] demand = new int[n];
        for (int i = 0; i < n; i++) demand[i] = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.spans(demand);
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
def spans(demand: list[int]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    demand = [int(x) for x in data[1:1+n]]

    result = spans(demand)
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
    vector<int> spans(const vector<int>& demand) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> demand(n);
    for (int i = 0; i < n; i++) cin >> demand[i];

    Solution solution;
    vector<int> result = solution.spans(demand);
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
  spans(demand) {
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
  const demand = [];
  for (let i = 0; i < n; i++) demand.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.spans(demand);
  console.log(result.join(" "));
});
```
