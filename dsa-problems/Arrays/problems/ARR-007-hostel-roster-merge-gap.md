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

class Solution {
    public int[] mergeWithPriority(int[] A, int[] B) {
        // Implementation here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextInt();

        int m = sc.nextInt();
        int[] B = new int[m];
        for (int i = 0; i < m; i++) B[i] = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.mergeWithPriority(A, B);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]).append(i == result.length - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
```

### Python

```python
import sys

def merge_with_priority(A: list[int], B: list[int]) -> list[int]:
    # Implementation here
    return []

def main():

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
    vector<int> mergeWithPriority(vector<int>& A, vector<int>& B) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    int m;
    cin >> m;
    vector<int> B(m);
    for (int i = 0; i < m; i++) cin >> B[i];

    Solution solution;
    vector<int> result = solution.mergeWithPriority(A, B);

    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mergeWithPriority(A, B) {
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
  const A = [];
  for (let i = 0; i < n; i++) A.push(Number(tokens[ptr++]));

  const m = Number(tokens[ptr++]);
  const B = [];
  for (let i = 0; i < m; i++) B.push(Number(tokens[ptr++]));

  const solution = new Solution();
  const result = solution.mergeWithPriority(A, B);
  console.log(result.join(" "));
});
```
