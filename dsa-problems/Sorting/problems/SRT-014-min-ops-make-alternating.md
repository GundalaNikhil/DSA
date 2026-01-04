---
problem_id: SRT_MIN_OPS_MAKE_ALTERNATING__4621
display_id: SRT-014
slug: min-ops-make-alternating
title: "Minimum Operations to Make Array Alternating"
difficulty: Medium
difficulty_score: 51
topics:
  - Sorting
  - Counting
  - Greedy
tags:
  - counting
  - greedy
  - arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-014: Minimum Operations to Make Array Alternating

## Problem Statement

You want the array to alternate between two distinct values `x` and `y`, i.e., `x, y, x, y, ...` or `y, x, y, x, ...`. You may change any element to any value.

Compute the minimum number of changes required.

![Problem Illustration](../images/SRT-014/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single integer: minimum changes to make the array alternating

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
4
1 1 1 2
```

**Output:**

```
1
```

**Explanation:**

Change the second element to 2 to get `[1,2,1,2]`.

![Example Visualization](../images/SRT-014/example-1.png)

## Notes

- Count frequencies separately on even and odd indices
- Choose the best pair of values to maximize already-correct positions
- `x` and `y` must be different
- Time complexity: O(n)

## Related Topics

Greedy, Frequency Counting, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minOperationsToAlternate(int n, int[] a) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            Solution sol = new Solution();
            System.out.println(sol.minOperationsToAlternate(n, a));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def min_operations_to_alternate(self, n: int, a: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:]]

    sol = Solution()
    print(sol.min_operations_to_alternate(n, a))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minOperationsToAlternate(int n, vector<int>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution sol;
        cout << sol.minOperationsToAlternate(n, a) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minOperationsToAlternate(n, a) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 1) return;
  const n = parseInt(input[0]);
  const a = input.slice(1).map(Number);

  const sol = new Solution();
  console.log(sol.minOperationsToAlternate(n, a));
});
```
