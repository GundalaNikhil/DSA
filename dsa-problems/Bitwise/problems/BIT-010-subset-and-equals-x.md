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
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int X = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.subsetAndEqualsX(a, X));
        sc.close();
    }
}
```

### Python

```python
import sys

def subset_and_equals_x(a: list[int], X: int) -> int:
    # Implementation here
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

    X = int(data[ptr]); ptr += 1

    result = subset_and_equals_x(a, X)
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
    long subsetAndEqualsX(vector<int>& a, int X) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int X;
    cin >> X;
    
    Solution solution;
    cout << solution.subsetAndEqualsX(a, X) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  subsetAndEqualsX(a, X) {
    // Implementation here
    return null;
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
    
    const X = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(String(solution.subsetAndEqualsX(a, X)));
});
```
