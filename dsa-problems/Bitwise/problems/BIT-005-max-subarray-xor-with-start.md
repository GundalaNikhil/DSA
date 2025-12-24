---
problem_id: BIT_MAX_SUBARRAY_XOR_START__8405
display_id: BIT-005
slug: max-subarray-xor-with-start
title: "Max Subarray XOR With Start"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Prefix Sum
tags:
  - bitwise
  - xor
  - trie
  - prefix-xor
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-005: Max Subarray XOR With Start

## Problem Statement

Given an array of integers and a fixed starting index `s`, find the subarray `a[s...k]` (where `k >= s`) that has the maximum XOR sum.

![Problem Illustration](../images/BIT-005/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer s (0-based)

## Output Format

Print the maximum XOR of a subarray starting at s.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
4
3 8 2 6
1
```

**Output:**

```
12
```

**Explanation:**

The subarray [8, 2, 6] has XOR 12, which is the maximum among subarrays starting at 1.

![Example Visualization](../images/BIT-005/example-1.png)

## Notes

- Index s is 0-based.
- The subarray must start at s but can end at any index >= s.

## Related Topics

Bitwise Operations, XOR, Trie

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxSubarrayXorWithStart(int[] a, int s) {
        // Your implementation here
        return 0L;
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
        int s = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.maxSubarrayXorWithStart(a, s);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def max_subarray_xor_with_start(a: list[int], s: int) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = int(input())

    result = max_subarray_xor_with_start(a, s)
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
    long long maxSubarrayXorWithStart(vector<int>& a, int s) {
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
    int s;
    cin >> s;

    Solution solution;
    long long result = solution.maxSubarrayXorWithStart(a, s);
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
  maxSubarrayXorWithStart(a, s) {
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
const s = Number(data[idx++]);

const solution = new Solution();
const result = solution.maxSubarrayXorWithStart(a, s);
console.log(String(result));
```
