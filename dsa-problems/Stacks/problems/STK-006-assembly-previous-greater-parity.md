---
problem_id: STK_ASSEMBLY_PREVIOUS_GREATER_PARITY__6802
display_id: STK-006
slug: assembly-previous-greater-parity
title: "Assembly Previous Greater with Parity"
difficulty: Medium
difficulty_score: 46
topics:
  - Stack
  - Monotonic Stack
  - Parity
tags:
  - stack
  - monotonic
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-006: Assembly Previous Greater with Parity

## Problem Statement

For each element `a[i]`, find the nearest element to its left that is strictly greater and has opposite parity (one even, one odd). If no such element exists, output `-1` for that position.

![Problem Illustration](../images/STK-006/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers, the previous greater with opposite parity or `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
5
2 9 5 7 3
```

**Output:**

```
-1 2 9 9 9
```

**Explanation:**

For 9 (odd), previous greater with opposite parity is 2. For 5 (odd), previous greater even is 9.

![Example Visualization](../images/STK-006/example-1.png)

## Notes

- Maintain separate monotonic stacks for even and odd values
- Pop smaller values while searching for a greater element
- Each element is pushed and popped at most once
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Parity, Previous Greater Element

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] previousGreaterOppositeParity(int n, long[] a) {
        // Implement here
        return new long[n];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextLong()) a[i] = sc.nextLong();
            }
            Solution sol = new Solution();
            long[] res = sol.previousGreaterOppositeParity(n, a);
            for (int i = 0; i < n; i++) {
                System.out.print(res[i] + (i == n - 1 ? "" : " "));
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def previous_greater_opposite_parity(self, n: int, a: list) -> list:
        # Implement here
        return [-1] * n

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:]]
    sol = Solution()
    res = sol.previous_greater_opposite_parity(n, a)
    print(*(res))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<long long> previousGreaterOppositeParity(int n, const vector<long long>& a) {
        // Implement here
        return vector<long long>(n, -1);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<long long> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution sol;
        vector<long long> res = sol.previousGreaterOppositeParity(n, a);
        for (int i = 0; i < n; i++) {
            cout << res[i] << (i == n - 1 ? "" : " ");
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  previousGreaterOppositeParity(n, a) {
    // Implement here
    return new Array(n).fill(-1n);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(line.trim());
}).on("close", () => {
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const a = input[1].split(/\s+/).map(BigInt);
  const sol = new Solution();
  const res = sol.previousGreaterOppositeParity(n, a);
  console.log(res.join(" "));
});
```
