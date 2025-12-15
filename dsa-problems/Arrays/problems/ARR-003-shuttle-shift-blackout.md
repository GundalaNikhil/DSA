---
problem_id: ARR_ROTATE_LOCK__7DB3
display_id: ARR-003
slug: shuttle-shift-blackout
title: "Shuttle Shift With Blackout"
difficulty: Medium
difficulty_score: 45
topics:
  - Array
  - Rotation
  - Conditional Operations
  - Hash Set
tags:
  - arrays
  - rotation
  - hashset
  - medium
  - conditional-logic
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Shuttle Shift With Blackout

## Problem Statement

You are given an array `arr` of integers, an integer `k` representing the number of positions to rotate left, and an array `blackout` containing indices that must remain fixed in place.

Rotate the array elements left by `k` positions, but keep all elements at blackout indices unchanged.

![Problem Illustration](../images/ARR-003/problem-illustration.png)


## Input Format

- First line: Integer `n` (1 ≤ n ≤ 10^5) - size of array
- Second line: `n` space-separated integers representing `arr[i]` (-10^9 ≤ arr[i] ≤ 10^9)
- Third line: Integer `k` (0 ≤ k ≤ 10^9) - number of left rotations
- Fourth line: Integer `b` (0 ≤ b ≤ n) - number of blackout indices
- Fifth line: `b` space-separated integers representing blackout indices (0 ≤ index < n)

## Output Format

Print `n` space-separated integers representing the array after rotation with blackout constraints.

## Constraints

- 1 ≤ n ≤ 10^5
- -10^9 ≤ arr[i] ≤ 10^9
- 0 ≤ k ≤ 10^9
- 0 ≤ b ≤ n
- All blackout indices are valid and unique

## Examples

### Example 1

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
5 2 1 4 3
```

**Explanation:**

- Blackout indices: 1, 3 (elements 2 and 4 stay fixed)
- Movable elements: [1, 3, 5] at positions [0, 2, 4]
- After rotating movable by 2: [5, 1, 3]
- Result: [5, 2, 1, 4, 3]

![Example 1 Visualization](../images/ARR-003/example-1.png)

### Example 2

**Input:**

```
5
10 20 30 40 50
1
2
1 3
```

**Output:**

```
30 20 50 40 10
```

**Explanation:**

- Blackout indices: 1, 3 (elements 20 and 40 stay fixed)
- Movable elements: [10, 30, 50] at positions [0, 2, 4]
- After rotating movable by 1: [30, 50, 10]
- Result: [30, 20, 50, 40, 10]

### Example 3

**Input:**

```
3
1 2 3
0
1
1
```

**Output:**

```
1 2 3
```

**Explanation:**

- k = 0, so no rotation occurs
- Result remains unchanged

## Notes

- When k is greater than the number of movable elements, use k % movableCount
- If all indices are blackout, return the original array
- If no indices are blackout, perform a normal left rotation

## Related Topics

Array, Rotation, Conditional Operations, Hash Set

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] rotateWithBlackout(int[] arr, int k, int[] blackout) {
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
        int k = sc.nextInt();
        int b = sc.nextInt();
        int[] blackout = new int[b];
        for (int i = 0; i < b; i++) {
            blackout[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.rotateWithBlackout(arr, k, blackout);

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

def rotate_with_blackout(arr: List[int], k: int, blackout: List[int]) -> List[int]:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    b = int(input())
    blackout = list(map(int, input().split())) if b > 0 else []
    result = rotate_with_blackout(arr, k, blackout)
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
    vector<int> rotateWithBlackout(vector<int>& arr, int k, vector<int>& blackout) {
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
    int k, b;
    cin >> k >> b;
    vector<int> blackout(b);
    for (int i = 0; i < b; i++) {
        cin >> blackout[i];
    }

    Solution solution;
    vector<int> result = solution.rotateWithBlackout(arr, k, blackout);

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
    rotateWithBlackout(arr, k, blackout) {
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
        const k = parseInt(lines[2]);
        const b = parseInt(lines[3]);
        const blackout = b > 0 ? lines[4].split(' ').map(Number) : [];

        const solution = new Solution();
        const result = solution.rotateWithBlackout(arr, k, blackout);

        console.log(result.join(' '));
        rl.close();
    }
});
```
