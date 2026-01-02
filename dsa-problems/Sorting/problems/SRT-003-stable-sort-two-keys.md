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
2. `key2` ascending

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

Records are ordered by `key1` ascending, and for same `key1` values by `key2` ascending.

![Example Visualization](../images/SRT-003/example-1.png)

## Notes

- Use a stable sorting method
- You can sort by `(key1, key2)` and the sort will maintain stability
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
        // Implementation here
        return new int[0][0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        int[][] records = new int[n][2];
        for (int i = 0; i < n; i++) {
            records[i][0] = sc.nextInt();
            records[i][1] = sc.nextInt();
        }
        Solution solution = new Solution();
        int[][] result = solution.stableSort(records);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append('\n');
            sb.append(result[i][0]).append(' ').append(result[i][1]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

def stable_sort(records: list[list[int]]) -> list[list[int]]:
    # Implementation here
    return []

def main():
    n = int(input())
    records = []
    for _ in range(n):
        k1, k2 = map(int, input().split())
        records.append([k1, k2])

    result = stable_sort(records)
    for k1, k2 in result:
        print(k1, k2)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    public:
    vector<vector<int>> stableSort(vector<vector<int>> records) {
        // Implementation here
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
        if (rec.size() >= 2) {
            cout << rec[0] << " " << rec[1] << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const fs = require("fs");

class Solution {
  stableSort(records) {
    // Implementation here
    return null;
  }
}

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const records = [];
for (let i = 0; i < n; i++) {
  const a = parseInt(data[idx++], 10);
  const b = parseInt(data[idx++], 10);
  records.push([a, b]);
}
const solution = new Solution();
const result = solution.stableSort(records);
const lines = result.map((r) => `${r[0]} ${r[1]}`);
console.log(lines.join("\n"));
```
