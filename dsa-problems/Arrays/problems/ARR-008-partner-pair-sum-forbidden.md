---
problem_id: ARR_PAIR_FORBID__25BE
display_id: ARR-008
slug: partner-pair-sum-forbidden
title: "Partner Pair Sum With Forbidden"
difficulty: Medium
difficulty_score: 55
topics:
  - Array
  - Two Pointers
  - Hash Set
  - Pair Finding
tags:
  - arrays
  - two-pointers
  - hashset
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Partner Pair Sum With Forbidden

## Problem Statement

Given a sorted array and target, find if a pair sums to target such that neither element index is in the `forbidden` set.

![Problem Illustration](../images/ARR-008/problem-illustration.png)


## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5) - size of array
- Second line: `n` space-separated integers representing the sorted array
- Third line: Integer `target` - the target sum
- Fourth line: Integer `f` (0 ≤ f ≤ n) - number of forbidden indices
- Fifth line: `f` space-separated integers representing forbidden indices

## Output Format

Print "true" if such a pair exists, "false" otherwise.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- |forbidden| ≤ n
- -10^9 ≤ arr[i], target ≤ 10^9
- Array is sorted in non-decreasing order

## Examples

### Example 1

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

- Index 0 is forbidden
- 4 + 7 = 11 (indices 1 and 3, both valid)

![Example 1 Visualization](../images/ARR-008/example-1.png)

### Example 2

**Input:**

```
4
2 3 5 8
10
2
1 3
```

**Output:**

```
false
```

**Explanation:**

- Forbidden indices: 1, 3 (elements 3 and 8)
- 2 + 8 = 10, but index 3 is forbidden
- 5 + 5 not available
- No valid pair exists

## Notes

- Two-pointer skipping forbidden indices
- Skip to next valid index when pointer lands on forbidden

## Related Topics

Array, Two Pointers, Hash Set, Pair Finding

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean pairSumWithForbidden(int[] arr, int target, Set<Integer> forbidden) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int target = sc.nextInt();
        int f = sc.nextInt();
        Set<Integer> forbidden = new HashSet<>();
        for (int i = 0; i < f; i++) {
            forbidden.add(sc.nextInt());
        }

        Solution solution = new Solution();
        boolean result = solution.pairSumWithForbidden(arr, target, forbidden);

        System.out.println(result ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
from typing import List, Set

def pair_sum_with_forbidden(arr: List[int], target: int, forbidden: Set[int]) -> bool:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    f = int(input())
    forbidden = set(map(int, input().split())) if f > 0 else set()
    result = pair_sum_with_forbidden(arr, target, forbidden)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    bool pairSumWithForbidden(vector<int>& arr, int target, set<int>& forbidden) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int target, f;
    cin >> target >> f;
    set<int> forbidden;
    for (int i = 0; i < f; i++) {
        int x;
        cin >> x;
        forbidden.insert(x);
    }

    Solution solution;
    bool result = solution.pairSumWithForbidden(arr, target, forbidden);

    cout << (result ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    pairSumWithForbidden(arr, target, forbidden) {
        // Your implementation here
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];
rl.on('line', (line) => {
    lines.push(line);
    if (lines.length === 5) {
        const n = parseInt(lines[0]);
        const arr = lines[1].split(' ').map(Number);
        const target = parseInt(lines[2]);
        const f = parseInt(lines[3]);
        const forbidden = f > 0 ? new Set(lines[4].split(' ').map(Number)) : new Set();

        const solution = new Solution();
        const result = solution.pairSumWithForbidden(arr, target, forbidden);

        console.log(result ? "true" : "false");
        rl.close();
    }
});
```
