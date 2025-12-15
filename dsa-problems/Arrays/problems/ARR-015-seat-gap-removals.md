---
problem_id: ARR_MIN_REMOVE__1DC9
display_id: ARR-015
slug: seat-gap-removals
title: "Seat Gap After Removals"
difficulty: Hard
difficulty_score: 70
topics:
  - Array
  - Hash Set
  - Filtering
  - Maximum Gap
tags:
  - arrays
  - hashset
  - hard
premium: true
subscription_tier: pro
time_limit: 2000
memory_limit: 256
---

# Seat Gap After Removals

## Problem Statement

You are given a sorted array `seats` of seat positions. You must remove the seats whose indices (0-based positions in the array, not seat numbers) are listed in `remove_indices`. After all removals, find the maximum gap between any two consecutive remaining seats. It is guaranteed that at least two seats remain.

![Problem Illustration](../images/ARR-015/problem-illustration.png)


## Input Format

- First line: Integer `n` — number of seats (2 ≤ n ≤ 2 × 10^5)
- Second line: `n` space-separated integers `seats[i]` in non-decreasing order
- Third line: Integer `r` — number of indices to remove
- Fourth line: `r` space-separated integers denoting indices to remove (0-based)

## Output Format

Print a single integer — the maximum gap between consecutive remaining seats.

## Constraints

- 2 ≤ n ≤ 2 × 10^5
- 0 ≤ seats[i] ≤ 10^9
- `seats` is sorted in non-decreasing order
- 1 ≤ r ≤ n − 2 (at least two seats remain)
- Removal indices are valid (0 ≤ idx < n)

## Examples

### Example 1

**Input:**

```
4
2 5 9 10
1
1
```

**Output:**

```
7
```

**Explanation:**

Remove seat at index 1 (value 5). Remaining seats are [2, 9, 10]; gaps are 7 and 1, so the maximum gap is 7.

![Example 1 Visualization](../images/ARR-015/example-1.png)

### Example 2

**Input:**

```
5
1 3 7 12 20
2
0 2
```

**Output:**

```
9
```

**Explanation:**

Remove indices 0 and 2 (values 1 and 7). Remaining seats are [3, 12, 20]; gaps are 9 and 8, so the maximum is 9.

## Notes

- Converting removal indices to a hash set allows `O(1)` checks while scanning the seats to compute gaps.

## Related Topics

Array, Hash Set, Filtering, Maximum Gap

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxGapAfterRemovals(int[] seats, int[] remove_indices) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] seats = new int[n];
        for (int i = 0; i < n; i++) {
            seats[i] = sc.nextInt();
        }
        int r = sc.nextInt();
        int[] remove_indices = new int[r];
        for (int i = 0; i < r; i++) {
            remove_indices[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.maxGapAfterRemovals(seats, remove_indices);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def max_gap_after_removals(seats: List[int], remove_indices: List[int]) -> int:
    # Your implementation here
    pass

def main():
    n = int(input())
    seats = list(map(int, input().split()))
    r = int(input())
    remove_indices = list(map(int, input().split())) if r > 0 else []
    result = max_gap_after_removals(seats, remove_indices)
    print(result)

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
    int maxGapAfterRemovals(vector<int>& seats, vector<int>& remove_indices) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> seats(n);
    for (int i = 0; i < n; i++) {
        cin >> seats[i];
    }
    int r;
    cin >> r;
    vector<int> remove_indices(r);
    for (int i = 0; i < r; i++) {
        cin >> remove_indices[i];
    }

    Solution solution;
    int result = solution.maxGapAfterRemovals(seats, remove_indices);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    maxGapAfterRemovals(seats, remove_indices) {
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
    if (lines.length === 4) {
        const n = parseInt(lines[0]);
        const seats = lines[1].split(' ').map(Number);
        const r = parseInt(lines[2]);
        const remove_indices = r > 0 ? lines[3].split(' ').map(Number) : [];

        const solution = new Solution();
        const result = solution.maxGapAfterRemovals(seats, remove_indices);

        console.log(result);
        rl.close();
    }
});
```
