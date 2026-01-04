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

class Record {
    long key1, key2;
    int originalIndex;
    Record(long key1, long key2, int originalIndex) {
        this.key1 = key1;
        this.key2 = key2;
        this.originalIndex = originalIndex;
    }
}

class Solution {
    public void stableSort(int n, Record[] records) {
        // Implement here
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Record[] records = new Record[n];
            for (int i = 0; i < n; i++) {
                records[i] = new Record(sc.nextLong(), sc.nextLong(), i);
            }

            Solution sol = new Solution();
            sol.stableSort(n, records);

            for (int i = 0; i < n; i++) {
                System.out.println(records[i].key1 + " " + records[i].key2);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Record:
    def __init__(self, key1, key2, original_index):
        self.key1 = key1
        self.key2 = key2
        self.original_index = original_index

class Solution:
    def stable_sort(self, n: int, records: list):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    records = []
    for i in range(n):
        key1 = int(input_data[1 + 2*i])
        key2 = int(input_data[2 + 2*i])
        records.append(Record(key1, key2, i))

    sol = Solution()
    sol.stable_sort(n, records)

    for r in records:
        print(f"{r.key1} {r.key2}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Record {
    long long key1, key2;
    int originalIndex;
};

class Solution {
public:
    void stableSort(int n, vector<Record>& records) {
        // Implement here
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<Record> records(n);
        for (int i = 0; i < n; i++) {
            cin >> records[i].key1 >> records[i].key2;
            records[i].originalIndex = i;
        }

        Solution sol;
        sol.stableSort(n, records);

        for (int i = 0; i < n; i++) {
            cout << records[i].key1 << " " << records[i].key2 << "\n";
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Record {
  constructor(key1, key2, originalIndex) {
    this.key1 = key1;
    this.key2 = key2;
    this.originalIndex = originalIndex;
  }
}

class Solution {
  stableSort(n, records) {
    // Implement here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const records = [];
  for (let i = 0; i < n; i++) {
    const key1 = BigInt(input[1 + 2 * i]);
    const key2 = BigInt(input[2 + 2 * i]);
    records.push(new Record(key1, key2, i));
  }

  const sol = new Solution();
  sol.stableSort(n, records);

  for (let i = 0; i < n; i++) {
    console.log(`${records[i].key1.toString()} ${records[i].key2.toString()}`);
  }
});
```
