---
problem_id: SRT_CLOSEST_PAIR_SORTED_CIRCULAR__3817
display_id: SRT-013
slug: closest-pair-sorted-circular
title: "Closest Pair in Sorted Circular Array"
difficulty: Medium
difficulty_score: 49
topics:
  - Sorting
  - Two Pointers
  - Circular Arrays
tags:
  - two-pointers
  - circular
  - search
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-013: Closest Pair in Sorted Circular Array

## Problem Statement

You are given a sorted circular array (a sorted array rotated at an unknown pivot) and a target. Find a pair of values whose sum is closest to the target.

If multiple pairs tie, return any one. Output the pair values.

![Problem Illustration](../images/SRT-013/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (rotated sorted array)
- Third line: integer `target`

## Output Format

- Two integers: the chosen pair values

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= a[i], target <= 10^9`

## Example

**Input:**

```
5
4 5 1 2 3
7
```

**Output:**

```
4 3
```

**Explanation:**

The pair (4,3) sums to 7 exactly.

![Example Visualization](../images/SRT-013/example-1.png)

## Notes

- Find the pivot (smallest element) to set two pointers
- Use a circular two-pointer technique
- Stop after one full cycle
- Time complexity: O(n)

## Related Topics

Two Pointers, Circular Arrays, Searching

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] findClosestPairCircular(int n, int[] a, int target) {
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
            int[] result = sol.findClosestPairCircular(n, a, target);
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
    def find_closest_pair_circular(self, n: int, a: list, target: int) -> list:
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
    result = sol.find_closest_pair_circular(n, a, target)
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
    pair<int, int> findClosestPairCircular(int n, vector<int>& a, int target) {
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
        pair<int, int> result = sol.findClosestPairCircular(n, a, target);
        cout << result.first << " " << result.second << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findClosestPairCircular(n, a, target) {
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
  const result = sol.findClosestPairCircular(n, a, target);
  console.log(`${result[0]} ${result[1]}`);
});
```
