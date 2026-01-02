---
problem_id: GRD_LIBRARY_POWER_BACKUP__4928
display_id: GRD-004
slug: library-power-backup
title: "Library Power Backup"
difficulty: Medium
difficulty_score: 40
topics:
  - Greedy Algorithms
  - Sorting
  - Optimization
tags:
  - greedy
  - sorting
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-004: Library Power Backup

## Problem Statement

A library server needs continuous power for `T` hours. You have `n` backup batteries, where battery `i` has a capacity of `c[i]` hours.

Each hour, you must draw power from exactly one battery until it is depleted. When a battery runs out, you switch to another battery (if available).

Your goal is to minimize the number of battery swaps (the number of times you change from one battery to another) while ensuring the server runs for the full `T` hours.

Return the minimum number of swaps, or `-1` if it's impossible to power the server for `T` hours.

![Problem Illustration](../images/GRD-004/problem-illustration.png)

## Input Format

- First line: two integers `n T` (number of batteries and required hours)
- Second line: `n` space-separated integers representing battery capacities `c[0], c[1], ..., c[n-1]`

## Output Format

- Single integer: minimum number of battery swaps, or `-1` if impossible

## Constraints

- `1 <= n <= 10^5`
- `1 <= c[i] <= 10^9`
- `1 <= T <= 10^9`

## Example

**Input:**

```
3 7
3 5 2
```

**Output:**

```
1
```

**Explanation:**

Batteries: [3, 5, 2] hours each
Required time: 7 hours
Total capacity: 3 + 5 + 2 = 10 hours (sufficient)

Greedy strategy (use largest capacities first):

1. Sort batteries by capacity: [5, 3, 2]
2. Use battery with 5 hours → powers for hours 0-4
3. Switch to battery with 3 hours → powers for hours 5-7 (only need 2 hours)

Total swaps: 1 (from first battery to second battery)

![Example Visualization](../images/GRD-004/example-1.png)

## Notes

- First check if total capacity >= T; if not, return -1
- Sort batteries in descending order by capacity
- Greedily use largest batteries first to minimize switches
- Number of swaps = (number of batteries used) - 1
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Sorting, Resource Allocation, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minBatterySwaps(int n, long T, long[] capacities) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long T = sc.nextLong();

        long[] capacities = new long[n];
        for (int i = 0; i < n; i++) {
            capacities[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        System.out.println(solution.minBatterySwaps(n, T, capacities));
        sc.close();
    }
}
```

### Python

```python
import sys

def min_battery_swaps(n: int, T: int, capacities: list) -> int:
    # Implementation here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    T = int(next(iterator))
    
    capacities = []
    for _ in range(n):
        capacities.append(int(next(iterator)))

    result = min_battery_swaps(n, T, capacities)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int minBatterySwaps(int n, long long T, vector<long long>& capacities) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long T;
    if (!(cin >> n >> T)) return 0;

    vector<long long> capacities(n);
    for (int i = 0; i < n; i++) {
        cin >> capacities[i];
    }

    Solution solution;
    cout << solution.minBatterySwaps(n, T, capacities) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minBatterySwaps(n, T, capacities) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const [n, T] = data[ptr++].split(" ").map(Number);
  const capacities = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.minBatterySwaps(n, T, capacities));
});
```
