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
        // Your implementation here
        return new int[0];
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.prefixAverages(arr);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```


### Python

```python
def prefix_averages(arr: list[int]) -> list[int]:
    # Your implementation here
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
#include <unordered_set>
#include <tuple>
using namespace std;


class Solution {
public:
    vector<int> prefixAverages(vector<int>& arr) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    vector<int> result = solution.prefixAverages(arr);
    for (size_t i = 0; i < result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```


### JavaScript

```javascript
const fs = require("fs");
const data = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (data.length === 1 && data[0] === "") {
  process.exit(0);
}

class Solution {
  prefixAverages(arr) {
    // Your implementation here
    return [];
  }
}

let idx = 0;
const n = Number(data[idx++]);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(Number(data[idx++]));
}

const solution = new Solution();
const result = solution.prefixAverages(arr);
console.log(result.join(" "));
```

