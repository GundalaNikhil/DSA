---
problem_id: ARR_ZERO_SUM_EVEN__6774
display_id: ARR-012
slug: longest-zero-sum-even
title: "Longest Zero-Sum Even Length"
difficulty: Medium
difficulty_score: 52
topics:
  - Arrays
  - Prefix Sum
  - Hashing
tags:
  - arrays
  - prefix-sum
  - hashing
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-012: Longest Zero-Sum Even Length

## Problem Statement

Find the maximum even length of a subarray whose sum is zero. If no such subarray exists, return 0.

![Problem Illustration](../images/ARR-012/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]

## Output Format

Print the maximum even length of a zero-sum subarray.

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= arr[i] <= 1000000000`

## Example

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

The subarray from index 0 to 3 has sum 0 and length 4, which is even.

![Example Visualization](../images/ARR-012/example-1.png)

## Notes

- Return 0 if no even-length zero-sum subarray exists.
- Use prefix sums with parity to enforce even length.

## Related Topics

Prefix Sum, Hashing, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int longestZeroSumEvenLength(int[] arr) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.longestZeroSumEvenLength(arr);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
import sys

def longest_zero_sum_even_length(arr: list[int]) -> int:
    return 0
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = longest_zero_sum_even_length(arr)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestZeroSumEvenLength(vector<int>& arr) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    cout << solution.longestZeroSumEvenLength(arr) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestZeroSumEvenLength(arr) {
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
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));

  const solution = new Solution();
  console.log(solution.longestZeroSumEvenLength(arr));
});
```

