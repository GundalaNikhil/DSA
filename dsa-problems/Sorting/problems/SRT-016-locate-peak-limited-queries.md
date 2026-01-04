---
problem_id: SRT_LOCATE_PEAK_LIMITED_QUERIES__1358
display_id: SRT-016
slug: locate-peak-limited-queries
title: "Locate Peak with Limited Queries"
difficulty: Medium
difficulty_score: 55
topics:
  - Searching
  - Binary Search
  - Peaks
tags:
  - binary-search
  - peak
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-016: Locate Peak with Limited Queries

## Problem Statement

An array has at least one peak (an index `i` such that `a[i] > a[i-1]` and `a[i] > a[i+1]`, when neighbors exist). You may query array values by index at most `q` times. Devise a strategy that finds any peak index within the query budget.

For this task, the full array is given as input, but your algorithm should still respect the query limit conceptually.

![Problem Illustration](../images/SRT-016/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers

## Output Format

- Single integer: an index of a peak

## Constraints

- `1 <= n <= 100000`
- `1 <= q <= 20`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
5 5
1 3 2 4 1
```

**Output:**

```
1
```

**Explanation:**

Index 1 is a peak since 3 is greater than its neighbors 1 and 2.

![Example Visualization](../images/SRT-016/example-1.png)

## Notes

- A binary-search-like strategy finds a peak in O(log n) queries
- Any valid peak index is acceptable
- Peaks can exist at boundaries if they are greater than their only neighbor
- The query limit is a conceptual constraint

## Related Topics

Binary Search, Peak Finding, Searching

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int findPeak(int n, int q, int[] a) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            Solution sol = new Solution();
            System.out.println(sol.findPeak(n, q, a));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_peak(self, n: int, q: int, a: list) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    a = [int(x) for x in input_data[2:]]

    sol = Solution()
    print(sol.find_peak(n, q, a))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findPeak(int n, int q, const vector<int>& a) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (cin >> n >> q) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution sol;
        cout << sol.findPeak(n, q, a) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findPeak(n, q, a) {
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
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const q = parseInt(input[1]);
  const a = input.slice(2).map(Number);

  const sol = new Solution();
  console.log(sol.findPeak(n, q, a));
});
```
