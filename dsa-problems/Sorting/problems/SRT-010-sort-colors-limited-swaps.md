---
problem_id: SRT_SORT_COLORS_LIMITED_SWAPS__4762
display_id: SRT-010
slug: sort-colors-limited-swaps
title: "Sort Colors With Limited Swaps"
difficulty: Medium
difficulty_score: 57
topics:
  - Sorting
  - Greedy
  - Adjacent Swaps
tags:
  - greedy
  - adjacent-swaps
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-010: Sort Colors With Limited Swaps

## Problem Statement

You are given an array of 0s, 1s, and 2s. You may swap only adjacent elements and perform at most `S` swaps. Determine whether the array can be fully sorted with at most `S` adjacent swaps.

![Problem Illustration](../images/SRT-010/problem-illustration.png)

## Input Format

- First line: integers `n` and `S`
- Second line: `n` space-separated integers (each is 0, 1, or 2)

## Output Format

- Single line: YES if the array can be fully sorted with at most `S` adjacent swaps, NO otherwise

## Constraints

- `1 <= n <= 200000`
- `0 <= S <= 10^9`
- Values are only 0, 1, or 2

## Example

**Input:**

```
8 2
2 1 0 0 0 2 0 2
```

**Output:**

```
YES
```

**Explanation:**

The array `[2,1,0,0,0,2,0,2]` can be fully sorted with at most 2 adjacent swaps.

![Example Visualization](../images/SRT-010/example-1.png)

## Notes

- Greedily move smaller values left while swaps remain
- Adjacent swaps act like limited bubble steps
- Track remaining swaps to avoid exceeding `S`
- Time complexity should be near O(n)

## Related Topics

Greedy, Adjacent Swaps, Sorting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String canSort(int n, long s, int[] a) {
        // Implement here
        return "NO";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            long s = sc.nextLong();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            Solution sol = new Solution();
            System.out.println(sol.canSort(n, s, a));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def can_sort(self, n: int, s: int, a: list) -> str:
        # Implement here
        return "NO"

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    s = int(input_data[1])
    a = [int(x) for x in input_data[2:]]

    sol = Solution()
    print(sol.can_sort(n, s, a))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string canSort(int n, long long s, vector<int>& a) {
        // Implement here
        return "NO";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long s;
    if (cin >> n >> s) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution sol;
        cout << sol.canSort(n, s, a) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  canSort(n, s, a) {
    // Implement here
    return "NO";
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
  const s = BigInt(input[1]);
  const a = input.slice(2).map(Number);

  const sol = new Solution();
  console.log(sol.canSort(n, s, a));
});
```
