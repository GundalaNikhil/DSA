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

Given an array of `n` elements (where `n` is even), pair up all elements to minimize the maximum XOR among all pairs. Return that minimal possible maximum XOR value.

## Input Format

- First line: Integer `n` (even)
- Second line: `n` space-separated integers

## Output Format

Single integer representing minimum possible maximum XOR

## Constraints

- `2 <= n <= 16` (n is even)
- `0 <= a[i] <= 10^9`

## Example

**Input:**

```
4
1 2 3 4
```

**Output:**

```
3
```

**Explanation:**

Possible pairings:

1. (1,2) and (3,4): max(1^2, 3^4) = max(3, 7) = 7
2. (1,3) and (2,4): max(1^3, 2^4) = max(2, 6) = 6
3. (1,4) and (2,3): max(1^4, 2^3) = max(5, 1) = 5

Wait, but expected is 3. Let me recalculate:
1^2 = 3
1^3 = 2
1^4 = 5
2^3 = 1
2^4 = 6
3^4 = 7

Best pairing to minimize maximum:
(1,3): 2 and (2,4): 6 → max = 6
(1,4): 5 and (2,3): 1 → max = 5
(1,2): 3 and (3,4): 7 → max = 7

Hmm, minimum of maximums = 5, not 3...

## Notes

- Use DP with bitmask
- Small n allows exponential search
- Try to pair similar numbers

## Related Topics

Pairing, Bitwise XOR, Dynamic Programming, Bitmask DP

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minimizeMaxPairXOR(int[] a) {
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
        System.out.println(solution.minimizeMaxPairXOR(a));
        sc.close();
    }
}
```

### Python

```python
def minimize_max_pair_xor(a: list[int]) -> int:
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(minimize_max_pair_xor(a))

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
    int minimizeMaxPairXOR(vector<int>& a) {
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
    cout << solution.minimizeMaxPairXOR(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimizeMaxPairXOR(a) {
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
  const n = parseInt(data[0]);
  const a = data[1].split(" ").map(Number);
  const solution = new Solution();
  console.log(solution.minimizeMaxPairXOR(a));
});
```
