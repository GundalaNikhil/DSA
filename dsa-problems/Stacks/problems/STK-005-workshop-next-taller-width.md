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
    public int[] nextTallerWithWidth(int n, int w, int[] h) {
        // Implement here
        return new int[n];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int w = sc.nextInt();
            int[] h = new int[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) h[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] res = sol.nextTallerWithWidth(n, w, h);
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
    def next_taller_with_width(self, n: int, w: int, h: list) -> list:
        # Implement here
        return [-1] * n

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    w = int(input_data[1])
    h = [int(x) for x in input_data[2:]]
    sol = Solution()
    res = sol.next_taller_with_width(n, w, h)
    print(*(res))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> nextTallerWithWidth(int n, int w, const vector<int>& h) {
        // Implement here
        return vector<int>(n, -1);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, w;
    if (cin >> n >> w) {
        vector<int> h(n);
        for (int i = 0; i < n; i++) {
            cin >> h[i];
        }
        Solution sol;
        vector<int> res = sol.nextTallerWithWidth(n, w, h);
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
  nextTallerWithWidth(n, w, h) {
    // Implement here
    return new Array(n).fill(-1);
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
  const [n, w] = input[0].split(/\s+/).map(Number);
  const h = input[1].split(/\s+/).map(Number);
  const sol = new Solution();
  const res = sol.nextTallerWithWidth(n, w, h);
  console.log(res.join(" "));
});
```
