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

Find the length of the longest subarray `nums[i..j]` such that `nums[i] | nums[i+1] | ... | nums[j] <= K`.

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
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int K = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maxOrSubarrayLeqK(a, K));
        sc.close();
    }
}
```

### Python

```python
import sys

def max_or_subarray_leq_k(a: list[int], K: int) -> int:
    return 0
def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    if not data: return

    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1

    K = int(data[ptr]); ptr += 1

    result = max_or_subarray_leq_k(a, K)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxOrSubarrayLeqK(vector<int>& a, int K) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int K;
    cin >> K;
    
    Solution solution;
    cout << solution.maxOrSubarrayLeqK(a, K) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxOrSubarrayLeqK(a, K) {
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
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    
    const K = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maxOrSubarrayLeqK(a, K));
});
```

