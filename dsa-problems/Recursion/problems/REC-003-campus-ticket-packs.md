---
problem_id: REC_CAMPUS_TICKET_PACKS__2187
display_id: REC-003
slug: campus-ticket-packs
title: "Campus Ticket Packs"
difficulty: Medium
difficulty_score: 46
topics:
  - Recursion
  - Backtracking
  - Combinations
tags:
  - recursion
  - combinations
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-003: Campus Ticket Packs

## Problem Statement

A ticket system has `n` values `v[i]`. For each value you may take either `0` tickets or exactly `p[i]` tickets (a fixed pack size). List all unique combinations of ticket values that sum exactly to `target`.

Output each combination as a space-separated list of ticket values in nondecreasing order. If no combination exists, output `NONE`.

![Problem Illustration](../images/REC-003/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `v[i]`
- Third line: `n` space-separated integers `p[i]`
- Fourth line: integer `target`

## Output Format

- Each valid combination on its own line (values space-separated)
- Output `NONE` if no solution exists

## Constraints

- `1 <= n <= 15`
- `1 <= target <= 200`
- `1 <= v[i] <= 50`
- `1 <= p[i] <= 10`

## Example

**Input:**

```
2
2 3
2 1
7
```

**Output:**

```
2 2 3
```

**Explanation:**

Choose two 2s and one 3 to reach 7.

![Example Visualization](../images/REC-003/example-1.png)

## Notes

- Decide for each value whether to take its full pack or not
- Sort values to keep combinations ordered
- Prune when current sum exceeds target
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinations, Pruning

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> packCombinations(int[] values, int[] packs, int target) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] packs = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            packs[i] = sc.nextInt();
        }
        int target = sc.nextInt();

        Solution solution = new Solution();
        List<List<Integer>> result = solution.packCombinations(values, packs, target);
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
def pack_combinations(values: list[int], packs: list[int], target: int) -> list[list[int]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    values = [int(next(it)) for _ in range(n)]
    packs = [int(next(it)) for _ in range(n)]
    target = int(next(it))

    result = pack_combinations(values, packs, target)
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
    vector<vector<int>> packCombinations(const vector<int>& values, const vector<int>& packs, int target) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), packs(n);
    for (int i = 0; i < n; i++) cin >> values[i];
    for (int i = 0; i < n; i++) cin >> packs[i];
    int target;
    cin >> target;

    Solution solution;
    vector<vector<int>> result = solution.packCombinations(values, packs, target);
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
  packCombinations(values, packs, target) {
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
  const values = [];
  const packs = [];
  for (let i = 0; i < n; i++) values.push(parseInt(data[idx++], 10));
  for (let i = 0; i < n; i++) packs.push(parseInt(data[idx++], 10));
  const target = parseInt(data[idx++], 10);

  const solution = new Solution();
  const result = solution.packCombinations(values, packs, target);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.map((combo) => combo.join(" ")).join("\n"));
  }
});
```
