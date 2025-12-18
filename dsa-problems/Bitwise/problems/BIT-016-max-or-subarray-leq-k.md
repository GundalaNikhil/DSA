---
problem_id: BIT_MAX_OR_SUBARRAY_LEQ_K__8416
display_id: BIT-016
slug: max-or-subarray-leq-k
title: "Max Bitwise OR Subarray <= K"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - OR
  - Sliding Window
  - Array
tags:
  - bitwise
  - or-operation
  - sliding-window
  - subarray
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-016: Max Bitwise OR Subarray <= K

## Problem Statement

Find the maximum length of a contiguous subarray whose bitwise OR value is less than or equal to `K`.

```
ASCII Diagram: OR Subarray Concept
===================================
Array: [1, 2, 4, 1], K = 7

Checking subarrays:
[1]: OR = 1 ≤ 7 ✓ length 1
[1,2]: OR = 1|2 = 3 ≤ 7 ✓ length 2
[1,2,4]: OR = 1|2|4 = 7 ≤ 7 ✓ length 3
[1,2,4,1]: OR = 1|2|4|1 = 7 ≤ 7 ✓ length 4 ← Maximum!

Result: 4
```

## Input Format

- First line: Two integers `n` and `K`
- Second line: `n` space-separated integers

## Output Format

Single integer representing maximum subarray length

## Constraints

- `1 <= n <= 2 * 10^5`
- `0 <= a[i], K <= 10^9`

## Example

**Input:**

```
4 7
1 2 4 1
```

**Output:**

```
4
```

**Explanation:**

```
Check all subarrays:
====================
Starting at index 0:
[1]: 1 ≤ 7 ✓
[1,2]: 1|2 = 3 ≤ 7 ✓
[1,2,4]: 1|2|4 = 7 ≤ 7 ✓
[1,2,4,1]: 1|2|4|1 = 7 ≤ 7 ✓ length 4!

Starting at index 1:
[2]: 2 ≤ 7 ✓
[2,4]: 2|4 = 6 ≤ 7 ✓
[2,4,1]: 2|4|1 = 7 ≤ 7 ✓ length 3

Starting at index 2:
[4]: 4 ≤ 7 ✓
[4,1]: 4|1 = 5 ≤ 7 ✓ length 2

Starting at index 3:
[1]: 1 ≤ 7 ✓ length 1

Maximum length: 4
```

```
Binary Visualization:
=====================
Array values in binary:
1 = 001
2 = 010
4 = 100
1 = 001

OR accumulation:
001
001 | 010 = 011 (3)
011 | 100 = 111 (7)
111 | 001 = 111 (7) ← Still ≤ 7

All 4 elements can be included!
```

## Notes

- Use sliding window technique
- Maintain bit counts in current window
- Shrink window when OR exceeds K
- OR operation is monotonic: adding elements never decreases OR

## Related Topics

Sliding Window, Bitwise OR, Subarray, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxORSubarray(int[] a, int K) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int K = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.maxORSubarray(a, K);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def max_or_subarray(a: list[int], K: int) -> int:
    # Your implementation here
    return 0

def main():
    n, K = map(int, input().split())
    a = list(map(int, input().split()))

    result = max_or_subarray(a, K)
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
    int maxORSubarray(vector<int>& a, int K) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, K;
    cin >> n >> K;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution solution;
    cout << solution.maxORSubarray(a, K) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxORSubarray(a, K) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  const [n, K] = data[ptr++].split(" ").map(Number);
  const a = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.maxORSubarray(a, K));
});
```
