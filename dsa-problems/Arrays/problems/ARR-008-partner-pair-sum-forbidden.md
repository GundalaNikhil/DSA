---
problem_id: ARR_PAIR_SUM_FORBIDDEN__8320
display_id: ARR-008
slug: partner-pair-sum-forbidden
title: "Partner Pair Sum With Forbidden"
difficulty: Medium
difficulty_score: 36
topics:
  - Arrays
  - Two Pointers
  - Hashing
tags:
  - arrays
  - two-pointers
  - hashing
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-008: Partner Pair Sum With Forbidden

## Problem Statement

Given a sorted array and a target sum, determine if there exists a pair of elements that sums to the target such that neither index is in the forbidden set.

![Problem Illustration](../images/ARR-008/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i] (sorted)
- Third line: integer target
- Fourth line: integer f, the number of forbidden indices
- Fifth line: f space-separated indices (0-based); if f = 0, this line is omitted

## Output Format

Print "true" if a valid pair exists, otherwise "false".

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= arr[i], target <= 1000000000`
- `0 <= f <= n`

## Example

**Input:**

```
4
1 4 6 7
11
1
0
```

**Output:**

```
true
```

**Explanation:**

Indices 1 and 3 are not forbidden, and 4 + 7 = 11.

![Example Visualization](../images/ARR-008/example-1.png)

## Notes

- Forbidden indices are 0-based.
- Two-pointer scans should skip forbidden indices.

## Related Topics

Arrays, Two Pointers, Hashing

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean hasForbiddenPair(int n, int[] arr, int target, int f, HashSet<Integer> forbidden) {
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] arr = new int[n];
        String arrLine = br.readLine();
        if (arrLine != null) {
            String[] parts = arrLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(parts[i]);
            }
        }

        String tLine = br.readLine();
        if (tLine == null) return;
        int target = Integer.parseInt(tLine.trim());

        String fLine = br.readLine();
        if (fLine == null) return;
        int f = Integer.parseInt(fLine.trim());

        HashSet<Integer> forbidden = new HashSet<>();
        if (f > 0) {
            String forbiddenLine = br.readLine();
            if (forbiddenLine != null) {
                String[] parts = forbiddenLine.trim().split("\\s+");
                for (String p : parts) {
                    forbidden.add(Integer.parseInt(p));
                }
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.hasForbiddenPair(n, arr, target, f, forbidden));
    }
}
```

### Python

```python
import sys

class Solution:
    def has_forbidden_pair(self, n, arr, target, f, forbidden):
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        arr = [int(next(iterator)) for _ in range(n)]
        target = int(next(iterator))
        f = int(next(iterator))
        forbidden = set()
        for _ in range(f):
            forbidden.add(int(next(iterator)))
    except StopIteration:
        pass

    sol = Solution()
    print("true" if sol.has_forbidden_pair(n, arr, target, f, forbidden) else "false")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool hasForbiddenPair(int n, vector<int>& arr, int target, int f, unordered_set<int>& forbidden) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int target, f;
    cin >> target >> f;

    unordered_set<int> forbidden;
    for (int i = 0; i < f; i++) {
        int idx;
        cin >> idx;
        forbidden.insert(idx);
    }

    Solution sol;
    cout << (sol.hasForbiddenPair(n, arr, target, f, forbidden) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  hasForbiddenPair(n, arr, target, f, forbidden) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(readInt());
  const target = readInt();
  const f = readInt();
  const forbidden = new Set();
  for (let i = 0; i < f; i++) forbidden.add(readInt());

  const sol = new Solution();
  console.log(sol.hasForbiddenPair(n, arr, target, f, forbidden));
}

solve();
```
