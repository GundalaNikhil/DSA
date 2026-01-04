---
problem_id: ARR_MERGE_PRIORITY_TIE__6153
display_id: ARR-007
slug: hostel-roster-merge-gap
title: "Hostel Roster Merge With Gap"
difficulty: Medium
difficulty_score: 42
topics:
  - Arrays
  - Two Pointers
  - Merge
tags:
  - arrays
  - two-pointers
  - merge
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-007: Hostel Roster Merge With Gap

## Problem Statement

Merge two sorted arrays A and B into a single sorted array. If two equal elements appear from different arrays, place the element from A before the one from B.

![Problem Illustration](../images/ARR-007/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers A[i]
- Third line: integer m
- Fourth line: m space-separated integers B[i]

## Output Format

Print the merged array, space-separated.

## Constraints

- `0 <= n, m <= 100000`
- `-1000000000 <= A[i], B[i] <= 1000000000`

## Example

**Input:**

```
3
1 3 3
2
3 4
```

**Output:**

```
1 3 3 3 4
```

**Explanation:**

On ties, elements from A are placed before elements from B.

![Example Visualization](../images/ARR-007/example-1.png)

## Notes

- This is a stable merge with a tie-breaker for A.
- If one array is empty, return the other.

## Related Topics

Arrays, Two Pointers, Merge

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] mergeRosters(int n, int[] a, int m, int[] b) {
        // Implement here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] a = new int[n];
        String aLine = br.readLine();
        if (aLine != null && n > 0) {
            String[] parts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(parts[i]);
            }
        }

        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        int[] b = new int[m];
        String bLine = br.readLine();
        if (bLine != null && m > 0) {
            String[] parts = bLine.trim().split("\\s+");
            for (int i = 0; i < m; i++) {
                b[i] = Integer.parseInt(parts[i]);
            }
        }

        Solution sol = new Solution();
        int[] result = sol.mergeRosters(n, a, m, b);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]).append(i == result.length - 1 ? "" : " ");
        }
        System.out.println(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def merge_rosters(self, n, a, m, b):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n_str = next(iterator)
        n = int(n_str)
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))

        m_str = next(iterator)
        m = int(m_str)
        b = []
        for _ in range(m):
            b.append(int(next(iterator)))
    except StopIteration:
        pass

    sol = Solution()
    result = sol.merge_rosters(n, a, m, b)

    print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> mergeRosters(int n, vector<int>& a, int m, vector<int>& b) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int m;
    cin >> m;

    vector<int> b(m);
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    Solution sol;
    vector<int> result = sol.mergeRosters(n, a, m, b);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
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
  mergeRosters(n, a, m, b) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;

  let n = 0;
  if (idx < input.length && input[idx] !== "") n = parseInt(input[idx++]);
  else if (idx < input.length) {
    idx++;
    n = 0;
  } // consume empty string if any?
  // Logic: readInt

  // Re-reading logic to be robust against empty arrays
  // Restarting parsing with cleaner logic for possible empties
  // Actually, standard split by whitespace handles newlines.
  // If n=0, next token is m.
}

// Redefining solve for robust parsing
function solveRobust() {
  const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);
  if (input.length < 1) return;
  let idx = 0;

  function readInt() {
    if (idx >= input.length) return 0;
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const a = [];
  for (let i = 0; i < n; i++) a.push(readInt());

  const m = readInt();
  const b = [];
  for (let i = 0; i < m; i++) b.push(readInt());

  const sol = new Solution();
  const result = sol.mergeRosters(n, a, m, b);
  console.log(result.join(" "));
}

solveRobust();
```
