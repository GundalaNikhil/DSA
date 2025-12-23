---
problem_id: BIT_DISTINCT_SUBARRAY_XORS__8412
display_id: BIT-012
slug: distinct-subarray-xors
title: "Distinct Subarray XORs"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Subarray
  - Trie
tags:
  - bitwise
  - xor
  - subarray
  - trie
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-012: Distinct Subarray XORs

## Problem Statement

Compute how many distinct XOR results appear among all subarrays of the array.

![Problem Illustration](../images/BIT-012/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the number of distinct subarray XOR values.

## Constraints

- `1 <= n <= 10000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
3
1 2 3
```

**Output:**

```
4
```

**Explanation:**

The distinct XORs across all subarrays are {0, 1, 2, 3}.

![Example Visualization](../images/BIT-012/example-1.png)

## Notes

- The total number of subarrays is n \* (n + 1) / 2.
- Use a set to track distinct XOR results.

## Related Topics

Bitwise Operations, Prefix XOR

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long distinctSubarrayXors(int[] a) {
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

        Solution solution = new Solution();
        long result = solution.distinctSubarrayXors(a);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def distinct_subarray_xors(a: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = distinct_subarray_xors(a)
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
    long long distinctSubarrayXors(vector<int>& a) {
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

    Solution solution;
    long long result = solution.distinctSubarrayXors(a);
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
  distinctSubarrayXors(a) {
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

const solution = new Solution();
const result = solution.distinctSubarrayXors(a);
console.log(String(result));
```
