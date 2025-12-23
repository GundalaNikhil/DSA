---
problem_id: BIT_SUBSET_AND_EQUALS_X__8410
display_id: BIT-010
slug: subset-and-equals-x
title: "Subset AND Equals X"
difficulty: Medium
difficulty_score: 52
topics:
  - Bitwise Operations
  - AND
  - Subset
  - Dynamic Programming
tags:
  - bitwise
  - and-operation
  - subset
  - dp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-010: Subset AND Equals X

## Problem Statement

Given an array of integers and a target `X`, count the number of non-empty subsets such that the bitwise AND of the subset elements is exactly `X`.

![Problem Illustration](../images/BIT-010/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer X

## Output Format

Print the number of non-empty subsets with AND equal to X.

## Constraints

- `1 <= n <= 20`
- `0 <= a[i], X <= 1000000`

## Example

**Input:**

```
3
6 4 2
2
```

**Output:**

```
2
```

**Explanation:**

The subsets [6, 2] and [2] have AND equal to 2.

![Example Visualization](../images/BIT-010/example-1.png)

## Notes

- The empty subset does not count.
- Use 64-bit integers for the count.

## Related Topics

Bitwise Operations, DP, Subsets

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long subsetAndEqualsX(int[] a, int X) {
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
        int X = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.subsetAndEqualsX(a, X);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def subset_and_equals_x(a: list[int], X: int) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    X = int(input())

    result = subset_and_equals_x(a, X)
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
    long long subsetAndEqualsX(vector<int>& a, int X) {
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
    int X;
    cin >> X;

    Solution solution;
    long long result = solution.subsetAndEqualsX(a, X);
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
  subsetAndEqualsX(a, X) {
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
const X = Number(data[idx++]);

const solution = new Solution();
const result = solution.subsetAndEqualsX(a, X);
console.log(String(result));
```
