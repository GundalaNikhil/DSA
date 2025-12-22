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
    public int findPeak(int[] arr, int qLimit) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int qLimit = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.findPeak(arr, qLimit));
        sc.close();
    }
}
```

### Python

```python
def find_peak(arr: list[int], q_limit: int) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q_limit = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    print(find_peak(arr, q_limit))

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
    int findPeak(const vector<int>& arr, int qLimit) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, qLimit;
    if (!(cin >> n >> qLimit)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    cout << solution.findPeak(arr, qLimit) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findPeak(arr, qLimit) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const qLimit = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  console.log(solution.findPeak(arr, qLimit).toString());
});
```
