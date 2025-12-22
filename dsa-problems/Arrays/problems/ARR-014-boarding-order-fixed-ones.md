---
problem_id: ARR_PARTITION_3WAY__308B
display_id: ARR-014
slug: boarding-order-fixed-ones
title: "Boarding Order With Fixed Ones"
difficulty: Medium
difficulty_score: 55
topics:
  - Array
  - Sorting
  - Two Pointers
  - Partitioning
tags:
  - arrays
  - sorting
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Boarding Order With Fixed Ones

## Problem Statement

You are given an array containing only 0s, 1s, and 2s. **All 1s are at their final positions and CANNOT be moved.** Rearrange the array so that:
1. All 0s come before all 2s
2. Every 1 remains at its original index
3. All 0s go in the leftmost available positions
4. All 2s go in the rightmost available positions

![Problem Illustration](../images/ARR-014/problem-illustration.png)


## Input Format

- First line: Integer `n` — size of the array (1 ≤ n ≤ 2 × 10^5)
- Second line: `n` space-separated integers, each 0, 1, or 2

## Output Format

Print the sorted array as `n` space-separated integers with 1s staying in their original positions.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- Array contains only values 0, 1, or 2
- Positions of 1s must not change

## Examples

### Example 1

**Input:**

```
6
2 1 0 2 0 1
```

**Output:**

```
0 1 0 1 2 2
```

**Explanation:**

Indices of 1s (1 and 5) are fixed. Place all 0s in the remaining left-most free spots and 2s in the remaining right-most spots, producing `[0,1,0,1,2,2]`.

![Example 1 Visualization](../images/ARR-014/example-1.png)

### Example 2

**Input:**

```
5
0 1 2 1 0
```

**Output:**

```
0 1 0 1 2
```

**Explanation:**

The 1s at indices 1 and 3 stay fixed. The remaining positions are filled with 0,0 on the left and 2 on the right, giving `[0,1,0,1,2]`.

## Notes

- A two-pass approach works: first fill available positions from the left with 0s (skipping fixed 1s), then fill available positions from the right with 2s; remaining unfixed cells will already contain 1s.

## Related Topics

Array, Sorting, Two Pointers, Partitioning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] sortWithAnchors(int[] arr) {
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

        Solution solution = new Solution();
        int[] result = solution.sortWithAnchors(arr);

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
from typing import List

def sort_with_anchors(arr: List[int]) -> List[int]:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = sort_with_anchors(arr)
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
    vector<int> sortWithAnchors(vector<int>& arr) {
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

    Solution solution;
    vector<int> result = solution.sortWithAnchors(arr);

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
const readline = require('readline');

class Solution {
    sortWithAnchors(arr) {
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
    if (lines.length === 2) {
        const n = parseInt(lines[0]);
        const arr = lines[1].split(' ').map(Number);

        const solution = new Solution();
        const result = solution.sortWithAnchors(arr);

        console.log(result.join(' '));
        rl.close();
    }
});
```
