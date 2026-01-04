---
problem_id: ARR_TEMP_OFFLINE_RANGES__5631
display_id: ARR-004
slug: lab-temperature-offline-ranges
title: "Lab Temperature Offline Ranges"
difficulty: Medium
difficulty_score: 46
topics:
  - Arrays
  - Difference Array
  - Prefix Sum
tags:
  - arrays
  - difference-array
  - prefix-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-004: Lab Temperature Offline Ranges

## Problem Statement

You are given an array of temperatures and a list of queries. Each query is either an add-range operation or a sum-range request.
All add queries appear before sum queries and should be applied cumulatively.
After applying all adds, answer each sum query in order.

![Problem Illustration](../images/ARR-004/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers temps[i]
- Third line: integer q, the number of queries
- Next q lines: either "add l r x" or "sum l r"

## Output Format

Print the answers to sum queries in order, space-separated.

## Constraints

- `1 <= n, q <= 100000`
- `-1000000000 <= temps[i], x <= 1000000000`
- `0 <= l <= r < n`

## Example

**Input:**

```
3
1 2 3
4
add 0 1 5
add 2 2 -1
sum 0 2
sum 1 2
```

**Output:**

```
15 9
```

**Explanation:**

After both add queries, temps become [6, 7, 2].
Then sum 0..2 is 15 and sum 1..2 is 9.

![Example Visualization](../images/ARR-004/example-1.png)

## Notes

- All add queries appear before sum queries.
- Use 64-bit integers for sums.

## Related Topics

Difference Array, Prefix Sum, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long[] solveOfflineRanges(int n, int[] temps, List<String> queries) {
        // Implement here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] temps = new int[n];
        String tempLine = br.readLine();
        if (tempLine != null) {
            String[] parts = tempLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                temps[i] = Integer.parseInt(parts[i]);
            }
        }

        String qLine = br.readLine();
        if (qLine == null) return;
        int q = Integer.parseInt(qLine.trim());

        List<String> queries = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            queries.add(br.readLine().trim());
        }

        Solution sol = new Solution();
        long[] results = sol.solveOfflineRanges(n, temps, queries);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < results.length; i++) {
            sb.append(results[i]).append(i == results.length - 1 ? "" : " ");
        }
        System.out.println(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def solve_offline_ranges(self, n, temps, queries):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        temps = list(map(int, next(iterator).split()))
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            queries.append(next(iterator))
    except StopIteration:
        return

    sol = Solution()
    results = sol.solve_offline_ranges(n, temps, queries)

    print(*(results))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    vector<long long> solveOfflineRanges(int n, vector<int>& temps, const vector<string>& queries) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> temps(n);
    for (int i = 0; i < n; i++) {
        cin >> temps[i];
    }

    int q;
    cin >> q;
    string dummy;
    getline(cin, dummy); // consume newline

    vector<string> queries(q);
    for (int i = 0; i < q; i++) {
        getline(cin, queries[i]);
    }

    Solution sol;
    vector<long long> results = sol.solveOfflineRanges(n, temps, queries);

    for (int i = 0; i < results.size(); i++) {
        cout << results[i] << (i == results.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveOfflineRanges(n, temps, queries) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim().split("\n");
  if (input.length < 3) return;

  let lineIdx = 0;
  const n = parseInt(input[lineIdx++].trim());
  const temps = input[lineIdx++].trim().split(/\s+/).map(Number);
  const q = parseInt(input[lineIdx++].trim());

  const queries = [];
  for (let i = 0; i < q; i++) {
    queries.push(input[lineIdx++].trim());
  }

  const sol = new Solution();
  const results = sol.solveOfflineRanges(n, temps, queries);

  console.log(results.join(" "));
}

solve();
```
