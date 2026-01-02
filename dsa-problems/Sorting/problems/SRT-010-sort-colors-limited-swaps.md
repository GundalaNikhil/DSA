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
    public boolean sortWithSwaps(int[] arr, long S) {
        return false;
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
        long s = sc.nextLong();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        boolean ok = solution.sortWithSwaps(arr, s);
        System.out.println(ok ? "YES" : "NO");
        sc.close();
    }
}
```

### Python

```python
def sort_with_swaps(arr: list[int], S: int) -> bool:
    return False
def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    result = sort_with_swaps(arr, s)
    print("YES" if result else "NO")

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
    bool sortWithSwaps(const vector<int>& arr, long long S) {
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    bool ok = solution.sortWithSwaps(arr, s);
    cout << (ok ? "YES" : "NO") << "\n";
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  sortWithSwaps(arr, S) {
    return 0;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const s = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
const ok = solution.sortWithSwaps(arr, s);
console.log(ok ? "YES" : "NO");
```

