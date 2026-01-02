---
problem_id: ARR_PREFIX_AVG__4252
display_id: ARR-001
slug: snack-restock-snapshot
title: "Snack Restock Snapshot"
difficulty: Easy
difficulty_score: 18
topics:
  - Arrays
  - Prefix Sum
  - Math
tags:
  - arrays
  - prefix-sum
  - math
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-001: Snack Restock Snapshot

## Problem Statement

You are given an array of daily deliveries. For each day i, compute the average of all deliveries from day 0 to day i (inclusive), rounded down to an integer. 
Return the list of prefix averages in order.

![Problem Illustration](../images/ARR-001/problem-illustration.png)

## Input Format

- First line: integer n, the number of days
- Second line: n space-separated integers arr[i]

## Output Format

Print n integers: the prefix averages, in order, space-separated.

## Constraints

- `1 <= n <= 100000`
- `0 <= arr[i] <= 1000000`

## Example

**Input:**
```
4
4 6 6 0
```

**Output:**
```
4 5 5 4
```

**Explanation:**

Running sums are 4, 10, 16, 16. Dividing by 1, 2, 3, 4 and rounding down gives
4, 5, 5, 4.

![Example Visualization](../images/ARR-001/example-1.png)

## Notes

- Use 64-bit arithmetic for the running sum.
- Output values are integers using floor division.

## Related Topics

Arrays, Prefix Sum, Math

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] prefixAverages(int[] arr) {
        // Implementation here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.prefixAverages(arr);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
```

### Python

```python
import sys

def prefix_averages(arr: list[int]) -> list[int]:
    # Implementation here
    return []

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = prefix_averages(arr)
    print(" ".join(map(str, result)))

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
    vector<int> prefixAverages(vector<int>& arr) {
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
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    vector<int> result = solution.prefixAverages(arr);
    
    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  prefixAverages(arr) {
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
  
  // Flatten data in case multiple lines
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(Number(tokens[ptr++]));
  }

  const solution = new Solution();
  const result = solution.prefixAverages(arr);
  console.log(result.join(" "));
});
```
