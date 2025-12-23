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

Find the maximum length of a subarray whose bitwise OR is less than or equal to K.

![Problem Illustration](../images/BIT-016/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer K

## Output Format

Print the maximum length of a subarray with OR <= K.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i], K <= 1000000000`

## Example

**Input:**

```
4
1 2 4 1
7
```

**Output:**

```
4
```

**Explanation:**

The OR of the entire array is 7, so the maximum length is 4.

![Example Visualization](../images/BIT-016/example-1.png)

## Notes

- Use a sliding window with bit counts.
- All elements and K are non-negative.

## Related Topics

Bitwise Operations, Sliding Window

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxOrSubarrayLeqK(int[] a, int K) {
        // Your implementation here
        return 0;
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
        int K = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.maxOrSubarrayLeqK(a, K);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def max_or_subarray_leq_k(a: list[int], K: int) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    K = int(input())

    result = max_or_subarray_leq_k(a, K)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <tuple>
using namespace std;


class Solution {
public:
    int maxOrSubarrayLeqK(vector<int>& a, int K) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int K;
    cin >> K;

    Solution solution;
    int result = solution.maxOrSubarrayLeqK(a, K);
    cout << result << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");
const data = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (data.length === 1 && data[0] === "") {
  process.exit(0);
}

class Solution {
  maxOrSubarrayLeqK(a, K) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const n = Number(data[idx++]);
const a = [];
for (let i = 0; i < n; i++) {
  a.push(Number(data[idx++]));
}
const K = Number(data[idx++]);

const solution = new Solution();
const result = solution.maxOrSubarrayLeqK(a, K);
console.log(String(result));
```
