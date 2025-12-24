---
problem_id: ARR_SEAT_GAP_REMOVALS__6037
display_id: ARR-015
slug: seat-gap-after-removals
title: "Seat Gap After Removals"
difficulty: Easy-Medium
difficulty_score: 33
topics:
  - Arrays
  - Simulation
  - Greedy
tags:
  - arrays
  - simulation
  - greedy
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-015: Seat Gap After Removals

## Problem Statement

You are given sorted seat positions and a list of indices to remove (indices refer to the original array). After removals, compute the maximum gap between remaining consecutive seats.

![Problem Illustration](../images/ARR-015/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers seats[i] (sorted)
- Third line: integer r, the number of removals
- Fourth line: r space-separated indices to remove

## Output Format

Print the maximum gap between remaining consecutive seats.

## Constraints

- `2 <= n <= 200000`
- `0 <= seats[i] <= 1000000000`
- `1 <= r <= n - 2`

## Example

**Input:**
```
4
2 5 9 10
1
1
```

**Output:**
```
7
```

**Explanation:**

Seat at index 1 (value 5) is removed. Remaining seats are [2, 9, 10], so the
maximum gap is 7.

![Example Visualization](../images/ARR-015/example-1.png)

## Notes

- Removal indices refer to the original array positions.
- At least two seats remain after removals.

## Related Topics

Simulation, Greedy, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxGapAfterRemovals(int[] seats, int[] removeIndices) {
        // Your implementation here
        return 0;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] seats = new int[n];
        for (int i = 0; i < n; i++) {
            seats[i] = sc.nextInt();
        }
        int r = sc.nextInt();
        int[] removeIndices = new int[r];
        for (int i = 0; i < r; i++) {
            removeIndices[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.maxGapAfterRemovals(seats, removeIndices);
        System.out.println(result);
        sc.close();
    }
}
```


### Python

```python
def max_gap_after_removals(seats: list[int], remove_indices: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    seats = list(map(int, input().split()))
    r = int(input())
    remove_indices = list(map(int, input().split()))

    result = max_gap_after_removals(seats, remove_indices)
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
    int maxGapAfterRemovals(vector<int>& seats, vector<int>& removeIndices) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> seats(n);
    for (int i = 0; i < n; i++) {
        cin >> seats[i];
    }
    int r;
    cin >> r;
    vector<int> removeIndices(r);
    for (int i = 0; i < r; i++) {
        cin >> removeIndices[i];
    }

    Solution solution;
    int result = solution.maxGapAfterRemovals(seats, removeIndices);
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
  maxGapAfterRemovals(seats, removeIndices) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const n = Number(data[idx++]);
const seats = [];
for (let i = 0; i < n; i++) {
  seats.push(Number(data[idx++]));
}
const r = Number(data[idx++]);
const removeIndices = [];
for (let i = 0; i < r; i++) {
  removeIndices.push(Number(data[idx++]));
}

const solution = new Solution();
const result = solution.maxGapAfterRemovals(seats, removeIndices);
console.log(String(result));
```

