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

Count the number of non-empty subsets whose bitwise AND equals exactly `X`.

## Input Format

- First line: Two integers `n` and `X`
- Second line: `n` space-separated integers

## Output Format

Single integer representing count of valid subsets

## Constraints

- `1 <= n <= 20`
- `0 <= a[i], X <= 10^6`

## Example

**Input:**

```
3 2
6 3 2
```

**Output:**

```
2
```

**Explanation:**

Subsets with AND = 2:

1. {6, 2}: 6 AND 2 = 2
2. {2}: 2 AND = 2

## Notes

- Use bitmask DP or backtracking
- Small n allows exponential solutions

## Related Topics

Subset Generation, Bitwise AND, Dynamic Programming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countSubsetsWithAND(int[] a, int X) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int X = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.countSubsetsWithAND(a, X));
        sc.close();
    }
}
```

### Python

```python
def count_subsets_with_and(a: list[int], X: int) -> int:
    return 0

def main():
    n, X = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_subsets_with_and(a, X))

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
    int countSubsetsWithAND(vector<int>& a, int X) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, X;
    cin >> n >> X;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    Solution solution;
    cout << solution.countSubsetsWithAND(a, X) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countSubsetsWithAND(a, X) {
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
  const [n, X] = data[0].split(" ").map(Number);
  const a = data[1].split(" ").map(Number);
  const solution = new Solution();
  console.log(solution.countSubsetsWithAND(a, X));
});
```
