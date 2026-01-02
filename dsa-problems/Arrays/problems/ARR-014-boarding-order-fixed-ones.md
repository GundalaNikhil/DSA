---
problem_id: ARR_FIXED_ONES_SORT__5412
display_id: ARR-014
slug: boarding-order-fixed-ones
title: "Boarding Order With Fixed Ones"
difficulty: Medium
difficulty_score: 48
topics:
  - Arrays
  - Sorting
  - Two Pointers
tags:
  - arrays
  - sorting
  - two-pointers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-014: Boarding Order With Fixed Ones

## Problem Statement

The array contains only 0s, 1s, and 2s. All 1s are fixed in their current positions and cannot move. Sort the array so 0s come first, then 1s, then 2s, while keeping every 1 in place.

![Problem Illustration](../images/ARR-014/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i] (each 0, 1, or 2)

## Output Format

Print the resulting array, space-separated.

## Constraints

- `1 <= n <= 200000`
- `arr[i] in {0, 1, 2}`

## Example

**Input:**
```
6
2 1 0 2 0 1
```

**Output:**
```
0 1 0 1 2 2
```

**Explanation:**

The 1s remain at indices 1 and 5. The remaining positions are filled with 0s
from left to right and 2s from right to left.

![Example Visualization](../images/ARR-014/example-1.png)

## Notes

- Do not move any index containing 1.
- The array should be sorted around the fixed 1s.

## Related Topics

Arrays, Sorting, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void sortWithFixedOnes(int[] arr) {
        // Implementation here
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        solution.sortWithFixedOnes(arr);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]).append(i == arr.length - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
```

### Python

```python
import sys

def sort_with_fixed_ones(arr: list[int]) -> None:
    # Implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sort_with_fixed_ones(arr)
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void sortWithFixedOnes(vector<int>& arr) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    solution.sortWithFixedOnes(arr);

    for (size_t i = 0; i < arr.size(); i++) {
        cout << arr[i] << (i == arr.size() - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  sortWithFixedOnes(arr) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));

  const solution = new Solution();
  solution.sortWithFixedOnes(arr);
  console.log(arr.join(" "));
});
```
