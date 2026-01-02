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
    private int[] memo;
    private int n;
    private int[] a;

    private int solve(int mask) {
        return 0;
    }

    public int minimizeMaxPairXor(int[] a) {
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

        Solution solution = new Solution();
        System.out.println(solution.minimizeMaxPairXor(a));
        sc.close();
    }
}
```

### Python

```python
import sys

def minimize_max_pair_xor(a: list[int]) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
        
    result = minimize_max_pair_xor(a)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

class Solution {
    int memo[1 << 16];
    int n;
    vector<int> a;

    int solve(int mask) {
        return 0;
    }

public:
    int minimizeMaxPairXor(vector<int>& a) {
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

    Solution solution;
    cout << solution.minimizeMaxPairXor(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimizeMaxPairXor(a) {
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
    
    const solution = new Solution();
    console.log(solution.minimizeMaxPairXor(a));
});
```

