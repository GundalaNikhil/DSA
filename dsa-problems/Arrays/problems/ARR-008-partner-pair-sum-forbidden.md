---
problem_id: ARR_PAIR_SUM_FORBIDDEN__8320
display_id: ARR-008
slug: partner-pair-sum-forbidden
title: "Partner Pair Sum With Forbidden"
difficulty: Easy-Medium
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

class Solution {
    public boolean hasPairWithForbidden(int[] arr, int target, Set<Integer> forbidden) {
        // Implementation here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        int target = sc.nextInt();
        int f = sc.nextInt();
        Set<Integer> forbidden = new HashSet<>();
        for (int i = 0; i < f; i++) forbidden.add(sc.nextInt());

        Solution solution = new Solution();
        boolean result = solution.hasPairWithForbidden(arr, target, forbidden);
        System.out.println(result ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys

def has_pair_with_forbidden(arr: list[int], target: int, forbidden: set[int]) -> bool:
    # Implementation here
    return False

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    f = int(input())
    forbidden = set(map(int, input().split())) if f > 0 else set()

    result = has_pair_with_forbidden(arr, target, forbidden)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool hasPairWithForbidden(vector<int>& arr, int target, unordered_set<int>& forbidden) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    int target, f;
    cin >> target >> f;

    unordered_set<int> forbidden;
    for (int i = 0; i < f; i++) {
        int idx;
        cin >> idx;
        forbidden.insert(idx);
    }

    Solution solution;
    cout << (solution.hasPairWithForbidden(arr, target, forbidden) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasPairWithForbidden(arr, target, forbidden) {
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
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));

  const target = Number(tokens[ptr++]);
  const f = Number(tokens[ptr++]);
  const forbidden = new Set();
  for (let i = 0; i < f; i++) forbidden.add(Number(tokens[ptr++]));

  const solution = new Solution();
  console.log(
    solution.hasPairWithForbidden(arr, target, forbidden) ? "true" : "false"
  );
});
```
