---
problem_id: ARR_MERGE_PRIOR__3B97
display_id: ARR-007
slug: hostel-roster-merge
title: "Hostel Roster Merge With Priority"
difficulty: Medium
difficulty_score: 50
topics:
  - Array
  - Merge
  - Sorted Arrays
  - Gap Requirement
tags:
  - arrays
  - merge
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Hostel Roster Merge With Priority

## Problem Statement

Merge two sorted arrays `A` and `B` into sorted order, but if two equal elements come from different arrays, place the one from `A` before the one from `B`. Return the merged array.

![Problem Illustration](../images/ARR-007/problem-illustration.png)

## Input Format

- First line: Integer `n` (0 ≤ n ≤ 10^5) - size of array A
- Second line: `n` space-separated integers representing array A (sorted)
- Third line: Integer `m` (0 ≤ m ≤ 10^5) - size of array B
- Fourth line: `m` space-separated integers representing array B (sorted)

## Output Format

Print `n + m` space-separated integers representing the merged sorted array.

## Constraints

- 0 ≤ n, m ≤ 10^5
- -10^9 ≤ A[i], B[i] ≤ 10^9
- Both arrays are sorted in non-decreasing order

## Examples

### Example 1

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

- When merging, A's elements come first on equality
- Two 3s from A, one 3 from B → A's 3s come first

![Example 1 Visualization](../images/ARR-007/example-1.png)

### Example 2

**Input:**

```
2
2 5
3
1 3 6
```

**Output:**

```
1 2 3 5 6
```

**Explanation:**

- Standard merge as no equal elements between arrays

## Notes

- Standard merge with tie-break on source (A before B)
- Time complexity: O(n + m)

## Related Topics

Array, Merge, Sorted Arrays, Gap Requirement

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> mergeWithPriority(int[] A, int[] B) {
        // Your implementation here
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
        List<Integer> result = solution.mergeWithPriority(A, B);

        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
from typing import List

def merge_with_gap(A: List[int], B: List[int], gap: int) -> List[int]:
    # Your implementation here
    pass

def main():
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    gap = int(input())
    result = merge_with_gap(A, B, gap)
    print(' '.join(map(str, result)))

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
    vector<int> mergeWithGap(vector<int>& A, vector<int>& B, int gap) {
        // Your implementation here
    }
};

int main() {
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
    int gap;
    cin >> gap;

    Solution solution;
    vector<int> result = solution.mergeWithGap(A, B, gap);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mergeWithGap(A, B, gap) {
    // Your implementation here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
  if (lines.length === 5) {
    const n = parseInt(lines[0]);
    const A = lines[1].split(" ").map(Number);
    const m = parseInt(lines[2]);
    const B = lines[3].split(" ").map(Number);
    const gap = parseInt(lines[4]);

    const solution = new Solution();
    const result = solution.mergeWithGap(A, B, gap);

    console.log(result.join(" "));
    rl.close();
  }
});
```
