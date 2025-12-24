---
problem_id: REC_CAMPUS_LIGHTS_PLACEMENT__4928
display_id: REC-007
slug: campus-lights-placement
title: "Campus Lights Placement"
difficulty: Medium
difficulty_score: 47
topics:
  - Recursion
  - Backtracking
  - Combinations
tags:
  - recursion
  - backtracking
  - combinations
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-007: Campus Lights Placement

## Problem Statement

A campus walkway has `n` positions labeled `0` to `n-1`. Place exactly `k` lights so that any two lights are at least `d` positions apart (absolute difference >= `d`).

Generate all valid sets of positions in increasing order.

![Problem Illustration](../images/REC-007/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `d`

## Output Format

- Each valid placement on its own line as space-separated positions
- Output `NONE` if no valid placement exists

## Constraints

- `1 <= n <= 12`
- `0 <= k <= n`
- `0 <= d <= n`

## Example

**Input:**

```
5 2 2
```

**Output:**

```
0 2
0 3
1 3
1 4
2 4
```

**Explanation:**

Each listed pair has distance at least 2.

![Example Visualization](../images/REC-007/example-1.png)

## Notes

- Build positions in increasing order to avoid duplicates
- Prune when remaining positions are insufficient
- Track the last chosen position to enforce distance
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinatorics, Recursion

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> placeLights(int n, int k, int d) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int d = sc.nextInt();

        Solution solution = new Solution();
        List<List<Integer>> result = solution.placeLights(n, k, d);
        if (result.isEmpty()) {
            System.out.println("NONE");
        } else {
            for (List<Integer> combo : result) {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < combo.size(); i++) {
                    if (i > 0) sb.append(' ');
                    sb.append(combo.get(i));
                }
                System.out.println(sb.toString());
            }
        }
        sc.close();
    }
}
```

### Python

```python
def place_lights(n: int, k: int, d: int) -> list[list[int]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, k, d = map(int, data[:3])
    result = place_lights(n, k, d)
    if not result:
        print("NONE")
    else:
        for combo in result:
            print(" ".join(str(x) for x in combo))

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
    vector<vector<int>> placeLights(int n, int k, int d) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, d;
    if (!(cin >> n >> k >> d)) return 0;
    Solution solution;
    vector<vector<int>> result = solution.placeLights(n, k, d);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (const auto& combo : result) {
            for (int i = 0; i < (int)combo.size(); i++) {
                if (i) cout << ' ';
                cout << combo[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  placeLights(n, k, d) {
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
  const n = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  const d = parseInt(data[2], 10);

  const solution = new Solution();
  const result = solution.placeLights(n, k, d);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.map((combo) => combo.join(" ")).join("\n"));
  }
});
```
