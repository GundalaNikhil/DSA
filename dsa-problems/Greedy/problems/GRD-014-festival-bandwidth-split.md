---
problem_id: GRD_FESTIVAL_BANDWIDTH_SPLIT__9163
display_id: GRD-014
slug: festival-bandwidth-split
title: "Festival Bandwidth Split"
difficulty: Medium
difficulty_score: 45
topics:
  - Greedy Algorithms
  - Knapsack
  - Optimization
tags:
  - greedy
  - knapsack
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-014: Festival Bandwidth Split

## Problem Statement

You're managing `n` performance stages at a festival, all sharing a total bandwidth of `B` units. Each stage `i` requires a minimum bandwidth of `b[i]` units to operate. If a stage doesn't get its minimum bandwidth, it cannot run at all.

Unused bandwidth is wasted (you can't save it or redistribute it).

Your goal is to:

1. **Primary**: Maximize the number of stages that can run
2. **Secondary**: Among solutions with maximum stages, minimize wasted bandwidth

Return the maximum number of stages you can run.

![Problem Illustration](../images/GRD-014/problem-illustration.png)

## Input Format

- First line: two integers `n B` (number of stages and total bandwidth)
- Second line: `n` space-separated integers representing minimum bandwidth `b[i]` for each stage

## Output Format

- Single integer: maximum number of stages that can run

## Constraints

- `1 <= n <= 10^5`
- `1 <= B <= 10^12`
- `1 <= b[i] <= 10^9`

## Example

**Input:**

```
3 7
5 2 4
```

**Output:**

```
2
```

**Explanation:**

Stages with bandwidth requirements: [5, 2, 4]
Total available: B = 7

Possible allocations:

1. Stage 0 only: uses 5, waste 2 → 1 stage
2. Stage 1 only: uses 2, waste 5 → 1 stage
3. Stage 2 only: uses 4, waste 3 → 1 stage
4. Stages 0 + 1: uses 7, waste 0 → 2 stages ✓
5. Stages 0 + 2: uses 9 > 7 → impossible
6. Stages 1 + 2: uses 6, waste 1 → 2 stages ✓
7. All three: uses 11 > 7 → impossible

Maximum stages: 2

Among 2-stage solutions:

- Stages 0 + 1: waste = 0
- Stages 1 + 2: waste = 1

Best choice: Stages 0 + 1 (waste = 0)

Output: 2 stages

![Example Visualization](../images/GRD-014/example-1.png)

## Notes

- Sort bandwidth requirements in ascending order
- Greedily select stages with smallest requirements first
- Keep adding stages until total exceeds B
- This maximizes the number of stages
- To minimize waste among solutions with same stage count, this greedy approach already achieves it
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Knapsack Problem, Resource Allocation, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxStages(int n, long B, long[] bandwidths) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long B = sc.nextLong();

        long[] bandwidths = new long[n];
        for (int i = 0; i < n; i++) {
            bandwidths[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxStages(n, B, bandwidths));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def max_stages(n: int, B: int, bandwidths: List[int]) -> int:
    # Your implementation here
    return 0

def main():
    n, B = map(int, input().split())
    bandwidths = list(map(int, input().split()))

    result = max_stages(n, B, bandwidths)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxStages(int n, long long B, vector<long long>& bandwidths) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long B;
    cin >> n >> B;

    vector<long long> bandwidths(n);
    for (int i = 0; i < n; i++) {
        cin >> bandwidths[i];
    }

    Solution solution;
    cout << solution.maxStages(n, B, bandwidths) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxStages(n, B, bandwidths) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  const [n, B] = data[ptr++].split(" ").map(Number);
  const bandwidths = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.maxStages(n, B, bandwidths));
});
```
