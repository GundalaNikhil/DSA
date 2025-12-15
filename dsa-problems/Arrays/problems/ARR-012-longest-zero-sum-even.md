---
problem_id: ARR_ZERO_SUM_EVEN__3900
display_id: ARR-012
slug: longest-zero-sum-even
title: "Longest Zero-Sum Even Length"
difficulty: Hard
difficulty_score: 75
topics:
  - Array
  - Prefix Sum
  - Hash Map
  - Subarray
  - Parity
tags:
  - arrays
  - prefix-sum
  - hashmap
  - hard
premium: true
subscription_tier: pro
time_limit: 2000
memory_limit: 256
---

# Longest Zero-Sum Even Length

## Problem Statement

Find the maximum even length of a subarray with sum equal to zero.

![Problem Illustration](../images/ARR-012/problem-illustration.png)


## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5) - size of array
- Second line: `n` space-separated integers

## Output Format

Print the maximum even length of a zero-sum subarray, or 0 if none exists.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- -10^9 ≤ arr[i] ≤ 10^9
- Return 0 if no such subarray exists

## Examples

### Example 1

**Input:**

```
5
1 -1 3 -3 2
```

**Output:**

```
4
```

**Explanation:**

- Subarray [1, -1, 3, -3] from indices 0 to 3
- Sum = 1 + (-1) + 3 + (-3) = 0
- Length = 4 (even)

![Example 1 Visualization](../images/ARR-012/example-1.png)

### Example 2

**Input:**

```
6
2 -2 5 -5 1 -1
```

**Output:**

```
6
```

**Explanation:**

- Entire array sums to 0: 2 + (-2) + 5 + (-5) + 1 + (-1) = 0
- Length = 6 (even)

## Notes

- Prefix sums with hashmap of first index for each parity bucket
- Zero-sum subarray exists when same prefix sum appears at two indices with same parity

## Related Topics

Array, Prefix Sum, Hash Map, Subarray, Parity

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int longestZeroSumEvenLength(int[] a) {
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
        int result = solution.longestZeroSumEvenLength(a);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def longest_zero_sum_even_length(a: List[int]) -> int:
    # Your implementation here
    pass

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = longest_zero_sum_even_length(a)
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
    int longestZeroSumEvenLength(vector<int>& a) {
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
    int result = solution.longestZeroSumEvenLength(a);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    longestZeroSumEvenLength(a) {
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
        const result = solution.longestZeroSumEvenLength(a);

        console.log(result);
        rl.close();
    }
});
```
