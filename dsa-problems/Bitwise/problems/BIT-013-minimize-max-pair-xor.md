---
problem_id: BIT_MINIMIZE_MAX_PAIR_XOR__8413
display_id: BIT-013
slug: minimize-max-pair-xor
title: "Minimize Max Pair XOR"
difficulty: Medium
difficulty_score: 58
topics:
  - Bitwise Operations
  - XOR
  - Dynamic Programming
  - Pairing
tags:
  - bitwise
  - xor
  - dp
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-013: Minimize Max Pair XOR

## Problem Statement

Pair up all elements (n is even) to minimize the maximum XOR among all pairs.
Return the minimal possible maximum XOR.

![Problem Illustration](../images/BIT-013/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the minimal possible maximum XOR.

## Constraints

- `2 <= n <= 16`
- `n is even`

## Example

**Input:**
```
4
1 2 3 4
```

**Output:**
```
5
```

**Explanation:**

Pairing (1,4) and (2,3) gives XORs 5 and 1, so the maximum is 5, which is minimal.

![Example Visualization](../images/BIT-013/example-1.png)

## Notes

- n is small; exponential DP over subsets is feasible.
- All elements must be paired exactly once.

## Related Topics

Bitwise Operations, DP

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minimizeMaxPairXor(int[] a) {
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

        Solution solution = new Solution();
        int result = solution.minimizeMaxPairXor(a);
        System.out.println(result);
        sc.close();
    }
}
```


### Python

```python
def minimize_max_pair_xor(a: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = minimize_max_pair_xor(a)
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
    int minimizeMaxPairXor(vector<int>& a) {
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
    int result = solution.minimizeMaxPairXor(a);
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
  minimizeMaxPairXor(a) {
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
const result = solution.minimizeMaxPairXor(a);
console.log(String(result));
```

