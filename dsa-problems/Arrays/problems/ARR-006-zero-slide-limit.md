---
problem_id: ARR_ZERO_SLIDE_LIMIT__4908
display_id: ARR-006
slug: zero-slide-limit
title: "Zero Slide With Limit"
difficulty: Easy-Medium
difficulty_score: 34
topics:
  - Arrays
  - Two Pointers
  - Simulation
tags:
  - arrays
  - two-pointers
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-006: Zero Slide With Limit

## Problem Statement

Move all zeros to the end of the array, but you may perform at most m swaps in total. Once the swap budget is exhausted, stop and return the current array.

![Problem Illustration](../images/ARR-006/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer m, the maximum number of swaps

## Output Format

Print the resulting array, space-separated.

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 1000000000`

## Example

**Input:**
```
5
0 4 0 5 7
1
```

**Output:**
```
4 0 0 5 7
```

**Explanation:**

One swap moves 4 left of a zero, and the swap budget is exhausted.

![Example Visualization](../images/ARR-006/example-1.png)

## Notes

- A swap is counted when a non-zero moves left across a zero.
- Stop immediately when the swap count reaches m.

## Related Topics

Arrays, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] zeroSlideWithLimit(int[] arr, int m) {
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
        int m = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.zeroSlideWithLimit(arr, m);
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
def zero_slide_with_limit(arr: list[int], m: int) -> list[int]:
    # Your implementation here
    return []

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    result = zero_slide_with_limit(arr, m)
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
    vector<int> zeroSlideWithLimit(vector<int>& arr, int m) {
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
    int m;
    cin >> m;

    Solution solution;
    vector<int> result = solution.zeroSlideWithLimit(arr, m);
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
  zeroSlideWithLimit(arr, m) {
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
const m = Number(data[idx++]);

const solution = new Solution();
const result = solution.zeroSlideWithLimit(arr, m);
console.log(result.join(" "));
```

