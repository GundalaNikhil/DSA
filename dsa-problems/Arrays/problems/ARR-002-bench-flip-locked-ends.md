---
problem_id: ARR_REVERSE_MID__66B6
display_id: ARR-002
slug: bench-flip-locked-ends
title: "Bench Flip With Locked Ends"
difficulty: Easy
difficulty_score: 30
topics:
  - Array
  - Two Pointers
  - In-Place Algorithm
  - Reversal
tags:
  - arrays
  - two-pointers
  - reversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Bench Flip With Locked Ends

## Problem Statement

Reverse the array in place but keep the first and last elements fixed; only the middle segment reverses.

![Problem Illustration](../images/ARR-002/problem-illustration.png)

## Input Format

- First line: Integer `n` (3 ≤ n ≤ 10^5) - size of array
- Second line: `n` space-separated integers representing `arr[i]` (-10^9 ≤ arr[i] ≤ 10^9)

## Output Format

Print `n` space-separated integers representing the array after reversing the middle portion.

## Constraints

- 3 ≤ n ≤ 10^5 (minimum 3 elements required)
- -10^9 ≤ arr[i] ≤ 10^9

## Examples

### Example 1

**Input:**

```
5
9 3 8 1 5
```

**Output:**

```
9 1 8 3 5
```

**Explanation:**

- First element (9) stays at position 0
- Last element (5) stays at position 4
- Middle elements [3, 8, 1] are reversed to [1, 8, 3]
- Result: [9, 1, 8, 3, 5]

![Example 1 Visualization](../images/ARR-002/example-1.png)

### Example 2

**Input:**

```
4
1 2 3 4
```

**Output:**

```
1 3 2 4
```

**Explanation:**

- First (1) and last (4) stay fixed
- Middle elements [2, 3] are reversed to [3, 2]
- Result: [1, 3, 2, 4]

## Notes

- Array must have at least 3 elements
- Only elements between first and last are reversed
- Use two-pointer technique for O(1) space complexity

## Related Topics

Array, Two Pointers, In-Place Algorithm, Reversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] reverseMiddle(int[] arr) {
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
        int[] result = solution.reverseMiddle(arr);

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

def reverse_middle(arr: List[int]) -> List[int]:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = reverse_middle(arr)
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
    vector<int> reverseMiddle(vector<int>& arr) {
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
    vector<int> result = solution.reverseMiddle(arr);

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
  reverseMiddle(arr) {
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
  if (lines.length === 2) {
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);

    const solution = new Solution();
    const result = solution.reverseMiddle(arr);

    console.log(result.join(" "));
    rl.close();
  }
});
```
