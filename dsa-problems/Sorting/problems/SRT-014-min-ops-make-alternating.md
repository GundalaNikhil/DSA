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
    public int minChanges(int[] arr) {
        return 0;
    }
    
    private int[] getTopTwo(Map<Integer, Integer> counts) {
        return null;
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
        System.out.println(solution.minChanges(arr));
        sc.close();
    }
}
```

### Python

```python
from collections import Counter

def min_changes(arr: list[int]) -> int:
    return 0
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = min_changes(arr)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
    struct Top {
        int val = -1;
        int count = 0;
    };
    
    pair<Top, Top> getTopTwo(const map<int, int>& counts) {
        Top first, second;
        for (auto const& [val, count] : counts) {
            if (count > first.count) {
                second = first;
                first = {val, count};
            } else if (count > second.count) {
                second = {val, count};
            }
        }
        return {first, second};
    }

public:
    int minChanges(const vector<int>& arr) {
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
    cout << solution.minChanges(arr) << "\n";
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  minChanges(arr) {
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
console.log(solution.minChanges(arr).toString());
```

