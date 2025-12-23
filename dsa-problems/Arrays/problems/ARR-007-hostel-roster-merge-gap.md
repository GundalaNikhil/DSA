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
        // Your implementation here
        return new int[0];
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        int[] B = new int[m];
        for (int i = 0; i < m; i++) {
            B[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.mergeWithPriority(A, B);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def merge_with_priority(A: list[int], B: list[int]) -> list[int]:
    # Your implementation here
    return []

def main():
    n = int(input())
    A = list(map(int, input().split())) if n > 0 else []
    m = int(input())
    B = list(map(int, input().split())) if m > 0 else []

    result = merge_with_priority(A, B)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <tuple>
using namespace std;


class Solution {
public:
    vector<int> mergeWithPriority(vector<int>& A, vector<int>& B) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    int m;
    cin >> m;
    vector<int> B(m);
    for (int i = 0; i < m; i++) {
        cin >> B[i];
    }

    Solution solution;
    vector<int> result = solution.mergeWithPriority(A, B);
    for (size_t i = 0; i < result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");
const data = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (data.length === 1 && data[0] === "") {
  process.exit(0);
}

class Solution {
  mergeWithPriority(A, B) {
    // Your implementation here
    return [];
  }
}

let idx = 0;
const n = Number(data[idx++]);
const A = [];
for (let i = 0; i < n; i++) {
  A.push(Number(data[idx++]));
}
const m = Number(data[idx++]);
const B = [];
for (let i = 0; i < m; i++) {
  B.push(Number(data[idx++]));
}

const solution = new Solution();
const result = solution.mergeWithPriority(A, B);
console.log(result.join(" "));
```
