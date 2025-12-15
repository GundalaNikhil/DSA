---
problem_id: ARR_ZERO_SLIDE__7E16
display_id: ARR-006
slug: zero-slide-limit
title: "Zero Slide With Limit"
difficulty: Easy
difficulty_score: 35
topics:
  - Array
  - Two Pointers
  - In-Place
  - Conditional Movement
tags:
  - arrays
  - two-pointers
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Zero Slide With Limit

## Problem Statement

Move all zeros to the end but allow at most `m` swaps total; stop once swaps exceed `m`. Return the resulting array.

![Problem Illustration](../images/ARR-006/problem-illustration.png)

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5) - size of array
- Second line: `n` space-separated integers representing the array
- Third line: Integer `m` (0 ≤ m ≤ 10^9) - maximum number of swaps allowed

## Output Format

Print `n` space-separated integers representing the array after moving zeros with the swap limit.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- 0 ≤ m ≤ 10^9
- Array contains integers

## Examples

### Example 1

**Input:**

```
5
0 4 0 5 7
1
```

**Output:**

```
4 0 0 5 7
```

**Explanation:**

- One swap moves 4 to position 0, then stop (swap limit reached)

![Example 1 Visualization](../images/ARR-006/example-1.png)

### Example 2

**Input:**

```
5
0 0 3 0 5
3
```

**Output:**

```
3 5 0 0 0
```

**Explanation:**

- Move 3 (1 swap), then 5 (2 swaps), total 2 swaps used
- All zeros moved to the end within the limit

## Notes

- Use write pointer; count swaps when writing non-zero over zero
- If m is larger than needed, complete the full zero-slide operation

## Related Topics

Array, Two Pointers, In-Place, Conditional Movement

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void zeroSlideWithLimit(int[] arr, int m) {
        // Your implementation here (modifies arr in-place)
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
        int m = sc.nextInt();

        Solution solution = new Solution();
        solution.zeroSlideWithLimit(arr, m);

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
from typing import List

def zero_slide_with_limit(arr: List[int], m: int) -> None:
    # Your implementation here (modifies arr in-place)
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    zero_slide_with_limit(arr, k)
    print(' '.join(map(str, arr)))

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
    void zeroSlideWithLimit(vector<int>& arr, int m) {
        // Your implementation here (modifies arr in-place)
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int m;
    cin >> m;

    Solution solution;
    solution.zeroSlideWithLimit(arr, k);

    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i < arr.size() - 1) cout << " ";
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  zeroSlideWithLimit(arr, m) {
    // Your implementation here (modifies arr in-place)
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
  if (lines.length === 3) {
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);
    const m = parseInt(lines[2]);

    const solution = new Solution();
    solution.zeroSlideWithLimit(arr, m);

    console.log(arr.join(" "));
    rl.close();
  }
});
```
