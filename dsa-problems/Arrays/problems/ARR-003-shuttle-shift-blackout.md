---
problem_id: ARR_SHUTTLE_SHIFT_BLACKOUT__2845
display_id: ARR-003
slug: shuttle-shift-blackout
title: "Shuttle Shift With Blackout"
difficulty: Medium
difficulty_score: 32
topics:
  - Arrays
  - Rotation
  - Simulation
tags:
  - arrays
  - rotation
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-003: Shuttle Shift With Blackout

## Problem Statement

Rotate the array to the left by k positions, but indices listed in the blackout
set must stay fixed. Only the elements at non-blackout indices rotate among
themselves in order.

![Problem Illustration](../images/ARR-003/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer k
- Fourth line: integer b, the number of blackout indices
- Fifth line: b space-separated indices (0-based); if b = 0, this line is omitted

## Output Format

Print the resulting array, space-separated.

## Constraints

- `1 <= n <= 200000`
- `0 <= k <= 1000000000`
- `0 <= b <= n`
- `Blackout indices are in range 0..n-1`

## Example

**Input:**

```
5
1 2 3 4 5
2
2
1 3
```

**Output:**

```
3 2 5 4 1
```

**Explanation:**

Indices 1 and 3 stay fixed (values 2 and 4). The remaining elements [1, 3, 5]
rotate left by 2 to [5, 1, 3], yielding [3, 2, 5, 4, 1].

![Example Visualization](../images/ARR-003/example-1.png)

## Notes

- If there are no movable indices, the array is unchanged.
- Use k % movable_count to avoid full rotations.

## Related Topics

Arrays, Rotation, Simulation

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] shiftWithBlackout(int n, int[] arr, int k, int b, HashSet<Integer> blackout) {
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

        int[] arr = new int[n];
        String arrLine = br.readLine();
        if (arrLine != null) {
            String[] parts = arrLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(parts[i]);
            }
        }

        String kLine = br.readLine();
        if (kLine == null) return;
        int k = Integer.parseInt(kLine.trim());

        String bLine = br.readLine();
        if (bLine == null) return;
        int b = Integer.parseInt(bLine.trim());

        HashSet<Integer> blackout = new HashSet<>();
        if (b > 0) {
            String blackoutLine = br.readLine();
            if (blackoutLine != null) {
                String[] parts = blackoutLine.trim().split("\\s+");
                for (String p : parts) {
                    blackout.add(Integer.parseInt(p));
                }
            }
        }

        Solution sol = new Solution();
        int[] result = sol.shiftWithBlackout(n, arr, k, b, blackout);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
    }
}
```

### Python

```python
import sys

class Solution:
    def shift_with_blackout(self, n, arr, k, b, blackout):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        arr = [int(next(iterator)) for _ in range(n)]
        k = int(next(iterator))
        b = int(next(iterator))
        blackout = set()
        for _ in range(b):
            blackout.add(int(next(iterator)))
    except StopIteration:
        return

    sol = Solution()
    result = sol.shift_with_blackout(n, arr, k, b, blackout)

    print(*(result))

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
    vector<int> shiftWithBlackout(int n, vector<int>& arr, int k, int b, unordered_set<int>& blackout) {
        // Implement here
        return {};
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

    int k, b;
    cin >> k >> b;

    unordered_set<int> blackout;
    for (int i = 0; i < b; i++) {
        int idx;
        cin >> idx;
        blackout.insert(idx);
    }

    Solution sol;
    vector<int> result = sol.shiftWithBlackout(n, arr, k, b, blackout);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
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
  shiftWithBlackout(n, arr, k, b, blackout) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(input[idx++]));
  }
  const k = parseInt(input[idx++]);
  const b = parseInt(input[idx++]);
  const blackout = new Set();
  for (let i = 0; i < b; i++) {
    blackout.add(parseInt(input[idx++]));
  }

  const sol = new Solution();
  const result = sol.shiftWithBlackout(n, arr, k, b, blackout);

  console.log(result.join(" "));
}

solve();
```
