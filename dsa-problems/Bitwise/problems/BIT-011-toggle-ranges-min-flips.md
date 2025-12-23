---
problem_id: BIT_TOGGLE_RANGES_MIN_FLIPS__8411
display_id: BIT-011
slug: toggle-ranges-min-flips
title: "Toggle Ranges Minimum Flips"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - Array
  - Greedy
  - Flipping
tags:
  - bitwise
  - array-transformation
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-011: Toggle Ranges Minimum Flips

## Problem Statement

You may flip all bits in any chosen subarray (0 -> 1, 1 -> 0). Find the minimum number of flips required to convert binary array A into binary array B.

![Problem Illustration](../images/BIT-011/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated bits of A
- Third line: n space-separated bits of B

## Output Format

Print the minimum number of flips.

## Constraints

- `1 <= n <= 200000`

## Example

**Input:**
```
4
0 1 1 0
1 0 1 1
```

**Output:**
```
2
```

**Explanation:**

Mismatch segments are indices 0..1 and 3, so two flips are sufficient.

![Example Visualization](../images/BIT-011/example-1.png)

## Notes

- A flip inverts every bit in the chosen subarray.
- Count contiguous mismatch runs to minimize flips.

## Related Topics

Bitwise Operations, Greedy

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int toggleRangesMinFlips(int[] A, int[] B) {
        // Your implementation here
        return 0;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        int[] B = new int[n];
        for (int i = 0; i < n; i++) {
            B[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.toggleRangesMinFlips(A, B);
        System.out.println(result);
        sc.close();
    }
}
```


### Python

```python
def toggle_ranges_min_flips(A: list[int], B: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = toggle_ranges_min_flips(A, B)
    print(result)

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
    int toggleRangesMinFlips(vector<int>& A, vector<int>& B) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    vector<int> B(n);
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }

    Solution solution;
    int result = solution.toggleRangesMinFlips(A, B);
    cout << result << "\n";
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
  toggleRangesMinFlips(A, B) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const n = Number(data[idx++]);
const A = [];
for (let i = 0; i < n; i++) {
  A.push(Number(data[idx++]));
}
const B = [];
for (let i = 0; i < n; i++) {
  B.push(Number(data[idx++]));
}

const solution = new Solution();
const result = solution.toggleRangesMinFlips(A, B);
console.log(String(result));
```

