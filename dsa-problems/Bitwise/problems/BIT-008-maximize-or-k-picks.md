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

Given an array of `n` non-negative integers, choose exactly `k` elements to maximize the bitwise OR of the chosen set.

```
ASCII Diagram: OR Maximization
===============================
Array: [1, 2, 4], k = 2

Possible selections:
1. {1, 2}: 001 OR 010 = 011 = 3
2. {1, 4}: 001 OR 100 = 101 = 5
3. {2, 4}: 010 OR 100 = 110 = 6 ← Maximum!

Result: 6
```

## Input Format

- First line: Two integers `n` and `k`
- Second line: `n` space-separated integers

## Output Format

Single integer representing maximum bitwise OR

## Constraints

- `1 <= k <= n <= 2 * 10^5`
- `0 <= a[i] <= 10^9`

## Example

**Input:**

```
3 2
1 2 4
```

**Output:**

```
6
```

**Explanation:**

Choose elements 2 and 4: `2 OR 4 = 6`

## Notes

- Greedy approach: prioritize higher-order bits
- OR operation can only add bits, never remove them

## Related Topics

Bitwise OR, Greedy Algorithms, Bit Manipulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maximizeOR(int[] a, int k) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.maximizeOR(a, k));
        sc.close();
    }
}
```

### Python

```python
def maximize_or(a: list[int], k: int) -> int:
    return 0

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(maximize_or(a, k))

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
    int maximizeOR(vector<int>& a, int k) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    Solution solution;
    cout << solution.maximizeOR(a, k) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maximizeOR(a, k) {
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
  const [n, k] = data[0].split(" ").map(Number);
  const a = data[1].split(" ").map(Number);
  const solution = new Solution();
  console.log(solution.maximizeOR(a, k));
});
```
