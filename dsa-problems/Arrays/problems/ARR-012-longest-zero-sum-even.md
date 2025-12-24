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
        // Your implementation here
        return 0;
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
        int result = solution.longestZeroSumEvenLength(arr);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def longest_zero_sum_even_length(arr: list[int]) -> int:
    # Your implementation here
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
#include <unordered_set>
#include <tuple>
using namespace std;


class Solution {
public:
    int longestZeroSumEvenLength(vector<int>& arr) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    int result = solution.longestZeroSumEvenLength(arr);
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
  longestZeroSumEvenLength(arr) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const n = Number(data[idx++]);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(Number(data[idx++]));
}

const solution = new Solution();
const result = solution.longestZeroSumEvenLength(arr);
console.log(String(result));
```
