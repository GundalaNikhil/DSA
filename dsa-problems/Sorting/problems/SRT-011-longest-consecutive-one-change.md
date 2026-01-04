---
problem_id: SRT_LONGEST_CONSECUTIVE_ONE_CHANGE__6194
display_id: SRT-011
slug: longest-consecutive-one-change
title: "Longest Consecutive After At Most One Change"
difficulty: Medium
difficulty_score: 53
topics:
  - Sorting
  - Prefix Suffix
  - Arrays
tags:
  - arrays
  - prefix-suffix
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-011: Longest Consecutive After At Most One Change

## Problem Statement

Given an array, you may change at most one element to any value. Find the maximum length of a strictly increasing contiguous subarray you can obtain.

![Problem Illustration](../images/SRT-011/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single integer: maximum possible length

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
6
1 2 3 7 5 6
```

**Output:**

```
6
```

**Explanation:**

Change `7` to `4` to get `[1,2,3,4,5,6]`.

![Example Visualization](../images/SRT-011/example-1.png)

## Notes

- Precompute longest increasing prefix and suffix lengths
- Try bridging around each index with one change
- The answer is at least the original longest run
- Time complexity: O(n)

## Related Topics

Arrays, Prefix/Suffix, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxLengthAfterOneChange(int n, int[] a) {
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
            System.out.println(sol.maxLengthAfterOneChange(n, a));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def max_length_after_one_change(self, n: int, a: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:]]

    sol = Solution()
    print(sol.max_length_after_one_change(n, a))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxLengthAfterOneChange(int n, vector<int>& a) {
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
        cout << sol.maxLengthAfterOneChange(n, a) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxLengthAfterOneChange(n, a) {
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
  console.log(sol.maxLengthAfterOneChange(n, a));
});
```
