---
problem_id: NUM_WAYS_CLIMB_JUMP_SET__7681
display_id: NUM-011
slug: ways-climb-jump-set
title: "Ways to Climb With Jumps Set"
difficulty: Medium
difficulty_score: 48
topics:
  - Number Theory
  - Dynamic Programming
  - Combinatorics
tags:
  - number-theory
  - dp
  - combinatorics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-011: Ways to Climb With Jumps Set

## Problem Statement

You are climbing `n` stairs. You may take jumps only from a given set `J`. Count the number of distinct ways to reach exactly stair `n`, modulo `1000000007`.

![Problem Illustration](../images/NUM-011/problem-illustration.png)

## Input Format

- First line: integers `n` and `m` (size of set J)
- Second line: `m` integers (the jump sizes)

## Output Format

- Single integer: number of ways modulo `1000000007`

## Constraints

- `1 <= n <= 100000`
- `1 <= m <= 20`
- `1 <= J[i] <= 100000`

## Example

**Input:**

```
4 2
1 3
```

**Output:**

```
3
```

**Explanation:**

Ways: 1+1+1+1, 1+3, 3+1.

![Example Visualization](../images/NUM-011/example-1.png)

## Notes

- DP: dp[i] = sum(dp[i-j]) for j in J and i >= j
- Base: dp[0] = 1
- Time complexity: O(n * m)
- Space complexity: O(n)

## Related Topics

Dynamic Programming, Modular Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countWays(int n, int[] jumps) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] jumps = new int[m];
        for (int i = 0; i < m; i++) jumps[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countWays(n, jumps));
        sc.close();
    }
}
```

### Python

```python
def count_ways(n: int, jumps):
    # Your implementation here
    return 0

def main():
    n, m = map(int, input().split())
    jumps = list(map(int, input().split()))
    print(count_ways(n, jumps))

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
    int countWays(int n, const vector<int>& jumps) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> jumps(m);
    for (int i = 0; i < m; i++) cin >> jumps[i];

    Solution solution;
    cout << solution.countWays(n, jumps) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function countWays(n, jumps) {
  // Your implementation here
  return 0;
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
  const m = parseInt(data[idx++], 10);
  const jumps = [];
  for (let i = 0; i < m; i++) jumps.push(parseInt(data[idx++], 10));
  console.log(countWays(n, jumps));
});
```
