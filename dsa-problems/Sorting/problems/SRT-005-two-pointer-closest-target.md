---
problem_id: SRT_TWO_POINTER_CLOSEST_TARGET__2651
display_id: SRT-005
slug: two-pointer-closest-target
title: "Two-Pointer Sum Closest to Target"
difficulty: Easy
difficulty_score: 28
topics:
  - Sorting
  - Two Pointers
  - Searching
tags:
  - two-pointers
  - sorted-array
  - search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-005: Two-Pointer Sum Closest to Target

## Problem Statement

You are given a sorted array and a target value. Find the pair of values whose sum is closest to the target.

If there are multiple valid pairs with the same distance to the target, return the pair with the smaller first value.

![Problem Illustration](../images/SRT-005/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (sorted ascending)
- Third line: integer `target`

## Output Format

- Two integers: the pair values in increasing order

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= a[i], target <= 10^9`

## Example

**Input:**

```
4
1 4 6 8
10
```

**Output:**

```
4 6
```

**Explanation:**

The sum 4 + 6 = 10 exactly matches the target.

![Example Visualization](../images/SRT-005/example-1.png)

## Notes

- Use a two-pointer scan from both ends
- Track the closest difference seen so far
- If equal differences occur, pick the smaller first value
- Time complexity: O(n)

## Related Topics

Two Pointers, Sorted Array, Searching

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] findClosestPair(int n, int[] a, int target) {
        // Implement here
        return new int[]{0, 0};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            int target = sc.nextInt();

            Solution sol = new Solution();
            int[] result = sol.findClosestPair(n, a, target);
            System.out.println(result[0] + " " + result[1]);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_closest_pair(self, n: int, a: list, target: int) -> list:
        # Implement here
        return [0, 0]

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:1+n]]
    target = int(input_data[1+n])

    sol = Solution()
    result = sol.find_closest_pair(n, a, target)
    print(f"{result[0]} {result[1]}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    pair<int, int> findClosestPair(int n, vector<int>& a, int target) {
        // Implement here
        return {0, 0};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        int target;
        cin >> target;

        Solution sol;
        pair<int, int> result = sol.findClosestPair(n, a, target);
        cout << result.first << " " << result.second << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findClosestPair(n, a, target) {
    // Implement here
    return [0, 0];
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
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const a = input.slice(1, 1 + n).map(Number);
  const target = parseInt(input[1 + n]);

  const sol = new Solution();
  const result = sol.findClosestPair(n, a, target);
  console.log(`${result[0]} ${result[1]}`);
});
```
