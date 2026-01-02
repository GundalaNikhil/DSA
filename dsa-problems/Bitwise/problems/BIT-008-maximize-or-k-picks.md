---
problem_id: BIT_MAXIMIZE_OR_K_PICKS__8408
display_id: BIT-008
slug: maximize-or-k-picks
title: "Maximize OR With K Picks"
difficulty: Medium
difficulty_score: 48
topics:
  - Bitwise Operations
  - OR
  - Greedy
  - Array
tags:
  - bitwise
  - or-operation
  - greedy
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-008: Maximize OR With K Picks

## Problem Statement

Choose exactly k elements from the array to maximize the bitwise OR of the chosen set. Return the maximum OR value.

![Problem Illustration](../images/BIT-008/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer k

## Output Format

Print the maximum possible OR value.

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`

## Example

**Input:**
```
3
1 2 4
2
```

**Output:**
```
6
```

**Explanation:**

Choosing 2 and 4 gives OR = 6, which is the maximum.

![Example Visualization](../images/BIT-008/example-1.png)

## Notes

- You must choose exactly k elements.
- The order of chosen elements does not matter.

## Related Topics

Bitwise Operations, Greedy

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maximizeOrWithKPicks(int[] a, int k) {
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
        int k = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maximizeOrWithKPicks(a, k));
        sc.close();
    }
}
```

### Python

```python
import sys

def maximize_or_with_k_picks(a: list[int], k: int) -> int:
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
    
    k = int(data[ptr]); ptr += 1
    
    result = maximize_or_with_k_picks(a, k)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maximizeOrWithKPicks(vector<int>& a, int k) {
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
    int k;
    cin >> k;

    Solution solution;
    cout << solution.maximizeOrWithKPicks(a, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maximizeOrWithKPicks(a, k) {
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
    const k = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maximizeOrWithKPicks(a, k));
});
```

