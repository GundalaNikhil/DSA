---
problem_id: STK_WORKSHOP_NEXT_TALLER_WIDTH__8156
display_id: STK-005
slug: workshop-next-taller-width
title: "Workshop Next Taller with Width"
difficulty: Medium
difficulty_score: 45
topics:
  - Stack
  - Monotonic Stack
  - Arrays
tags:
  - stack
  - monotonic
  - next-greater
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-005: Workshop Next Taller with Width

## Problem Statement

For each height `h[i]`, find the next taller height to its right within distance at most `w`. If no taller height exists within `w`, output `-1` for that position.

![Problem Illustration](../images/STK-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `w`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers, the next taller heights or `-1`

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i] <= 10^9`
- `1 <= w <= n`

## Example

**Input:**

```
5 2
1 7 3 4 2
```

**Output:**

```
7 -1 4 -1 -1
```

**Explanation:**

For index 0, the next taller within distance 2 is 7. For index 2, 4 is taller and within width.

![Example Visualization](../images/STK-005/example-1.png)

## Notes

- Use a monotonic decreasing stack of indices
- Remove indices that are more than `w` away
- Pop while current height is taller to resolve answers
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Next Greater Element, Sliding Window

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] nextTallerWithin(int[] h, int w) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int w = sc.nextInt();
        int[] h = new int[n];
        for (int i = 0; i < n; i++) h[i] = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.nextTallerWithin(h, w);
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
def next_taller_within(h: list[int], w: int) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    w = int(next(it))
    h = [int(next(it)) for _ in range(n)]

    result = next_taller_within(h, w)
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
    vector<int> nextTallerWithin(const vector<int>& h, int w) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w;
    if (!(cin >> n >> w)) return 0;
    vector<int> h(n);
    for (int i = 0; i < n; i++) cin >> h[i];

    Solution solution;
    vector<int> result = solution.nextTallerWithin(h, w);
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
  nextTallerWithin(h, w) {
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
  const w = parseInt(data[idx++], 10);
  const h = [];
  for (let i = 0; i < n; i++) h.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.nextTallerWithin(h, w);
  console.log(result.join(" "));
});
```
