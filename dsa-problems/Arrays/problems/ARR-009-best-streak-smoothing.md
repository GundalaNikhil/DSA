---
problem_id: ARR_KADANE_SMOOTH__4460
display_id: ARR-009
slug: best-streak-smoothing
title: "Best Streak With One Smoothing"
difficulty: Medium
difficulty_score: 60
topics:
  - Array
  - Dynamic Programming
  - Kadane's Algorithm
  - Optimization
tags:
  - arrays
  - dynamic-programming
  - kadane
  - medium
premium: true
subscription_tier: pro
time_limit: 2000
memory_limit: 256
---

# Best Streak With One Smoothing

## Problem Statement

You may choose exactly one index `i` and replace `a[i]` with `floor((a[i-1]+a[i]+a[i+1])/3)` (use existing neighbors; for endpoints, smoothing not allowed). Then compute the maximum subarray sum. Find the maximum achievable sum.

![Problem Illustration](../images/ARR-009/problem-illustration.png)


## Input Format

- First line: Integer `n` (3 ≤ n ≤ 2 × 10^5) - size of array
- Second line: `n` space-separated integers representing the array

## Output Format

Print the maximum achievable subarray sum after one smoothing operation.

## Constraints

- 3 ≤ n ≤ 2 × 10^5
- -10^9 ≤ a[i] ≤ 10^9
- Must smooth exactly one middle element (not first or last)

## Examples

### Example 1

**Input:**

```
4
-2 3 -4 5
```

**Output:**

```
9
```

**Explanation:**

- Original max subarray is 5
- Smooth index 2: floor((3+(-4)+5)/3) = floor(4/3) = 1
- Array becomes [-2, 3, 1, 5]
- Max subarray is 3 + 1 + 5 = 9

![Example 1 Visualization](../images/ARR-009/example-1.png)

### Example 2

**Input:**

```
5
5 -10 3 -2 8
```

**Output:**

```
14
```

**Explanation:**

- Original max subarray is 8
- Smooth index 3: floor((3+(-2)+8)/3) = floor(9/3) = 3
- Array becomes [5, -10, 3, 3, 8]
- Max subarray is 3 + 3 + 8 = 14

## Notes

- Precompute best prefix/suffix Kadane values
- Test smoothing effect by replacing a[i] with new value and combining left/right bests

## Related Topics

Array, Dynamic Programming, Kadane's Algorithm, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxSubarrayWithSmoothing(int[] a) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.maxSubarrayWithSmoothing(a);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def max_subarray_with_smoothing(a: List[int]) -> int:
    # Your implementation here
    pass

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = max_subarray_with_smoothing(a)
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
    int maxSubarrayWithSmoothing(vector<int>& a) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution solution;
    int result = solution.maxSubarrayWithSmoothing(a);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    maxSubarrayWithSmoothing(a) {
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
        const a = lines[1].split(' ').map(Number);

        const solution = new Solution();
        const result = solution.maxSubarrayWithSmoothing(a);

        console.log(result);
        rl.close();
    }
});
```
