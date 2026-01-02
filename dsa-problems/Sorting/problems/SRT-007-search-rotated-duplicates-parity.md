---
problem_id: SRT_SEARCH_ROTATED_DUPLICATES_PARITY__9062
display_id: SRT-007
slug: search-rotated-duplicates-parity
title: "Search Rotated With Duplicates Parity Count"
difficulty: Medium
difficulty_score: 52
topics:
  - Sorting
  - Binary Search
  - Rotated Arrays
tags:
  - binary-search
  - rotated-array
  - duplicates
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-007: Search Rotated With Duplicates Parity Count

## Problem Statement

Given a rotated sorted array that may contain duplicates, count how many occurrences of a value `x` appear at even indices.

Indices are 0-based.

![Problem Illustration](../images/SRT-007/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers
- Third line: integer `x`

## Output Format

- Single integer: count of occurrences of `x` at even indices

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
6
4 5 5 1 2 3
5
```

**Output:**

```
1
```

**Explanation:**

Value 5 appears at indices 1 and 2; only index 2 is even.

![Example Visualization](../images/SRT-007/example-1.png)

## Notes

- Find the rotation pivot to map to a sorted order
- Use binary search to locate the range of `x`
- Count how many indices in the occurrence range are even
- Time complexity: O(log n)

## Related Topics

Binary Search, Rotated Array, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countEvenIndices(int[] arr, int x) {
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
        int x = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.countEvenIndices(arr, x));
        sc.close();
    }
}
```

### Python

```python
def find_first_occurrence(arr: list[int], x: int) -> int:
    return 0
def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    result = find_first_occurrence(arr, x)
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
    int countEvenIndices(const vector<int>& arr, int x) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    if (!(cin >> n >> x)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.countEvenIndices(arr, x) << "\n";
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  countEvenIndices(arr, x) {
    return 0;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const x = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
console.log(solution.countEvenIndices(arr, x).toString());
```

