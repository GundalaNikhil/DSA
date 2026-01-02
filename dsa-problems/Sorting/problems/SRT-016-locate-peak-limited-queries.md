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
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.findPeak(arr, n));
        sc.close();
    }
}
```

### Python

```python
def find_peak(arr: list[int], q_limit: int) -> int:
    return 0
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_peak(arr, n)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int findPeak(const vector<int>& arr, int qLimit) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.findPeak(arr, n) << "\n";
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  findPeak(arr, qLimit) {
    return 0;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
console.log(solution.findPeak(arr, n).toString());
```

