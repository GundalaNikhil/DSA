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
    public int countVisible(int[] h) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] h = new int[n];
        for (int i = 0; i < n; i++) h[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countVisible(h));
        sc.close();
    }
}
```

### Python

```python
def count_visible(h: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    h = [int(x) for x in data[1:1+n]]
    print(count_visible(h))

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
    int countVisible(const vector<int>& h) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> h(n);
    for (int i = 0; i < n; i++) cin >> h[i];

    Solution solution;
    cout << solution.countVisible(h) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countVisible(h) {
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
  const h = [];
  for (let i = 0; i < n; i++) h.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  console.log(solution.countVisible(h).toString());
});
```
