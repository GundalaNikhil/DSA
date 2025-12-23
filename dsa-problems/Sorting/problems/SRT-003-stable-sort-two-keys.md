---
problem_id: SRT_STABLE_SORT_TWO_KEYS__5920
display_id: SRT-003
slug: stable-sort-two-keys
title: "Stable Sort By Two Keys"
difficulty: Easy
difficulty_score: 30
topics:
  - Sorting
  - Stability
  - Records
tags:
  - sorting
  - stable-sort
  - records
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-003: Stable Sort By Two Keys

## Problem Statement

You are given `n` records, each with keys `(key1, key2)`. Sort the records by:

1. `key1` ascending
2. `key2` descending

If two records have identical `(key1, key2)` values, their original order must be preserved.

![Problem Illustration](../images/SRT-003/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `key1` and `key2`

## Output Format

- `n` lines of sorted `(key1, key2)` pairs

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= key1, key2 <= 10^9`

## Example

**Input:**

```
3
1 2
1 1
0 9
```

**Output:**

```
0 9
1 2
1 1
```

**Explanation:**

Records are ordered by `key1` ascending, and for `key1=1` by `key2` descending.

![Example Visualization](../images/SRT-003/example-1.png)

## Notes

- Use a stable sorting method
- You can sort by `(key1, -key2)` and keep stability for equal pairs
- Time complexity: O(n log n)
- Space complexity depends on sorting method

## Related Topics

Stable Sort, Sorting Keys, Records

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[][] stableSort(int[][] records) {
        // Your implementation here
        return new int[0][0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] records = new int[n][2];
        for (int i = 0; i < n; i++) {
            records[i][0] = sc.nextInt();
            records[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[][] result = solution.stableSort(records);
        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i][0] + " " + result[i][1]);
        }
        sc.close();
    }
}
```

### Python

```python
def stable_sort(records: list[list[int]]) -> list[list[int]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    records = [[int(next(it)), int(next(it))] for _ in range(n)]

    result = stable_sort(records)
    for a, b in result:
        print(a, b)

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
    vector<vector<int>> stableSort(const vector<vector<int>>& records) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> records(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> records[i][0] >> records[i][1];
    }

    Solution solution;
    vector<vector<int>> result = solution.stableSort(records);
    for (const auto& rec : result) {
        cout << rec[0] << " " << rec[1] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  stableSort(records) {
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
  const records = [];
  for (let i = 0; i < n; i++) {
    records.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }

  const solution = new Solution();
  const result = solution.stableSort(records);
  console.log(result.map((r) => ``r[0]`{r[1]}`).join("\n"));
});
```
