---
problem_id: ARR_SHUTTLE_SHIFT_BLACKOUT__2845
display_id: ARR-003
slug: shuttle-shift-blackout
title: "Shuttle Shift With Blackout"
difficulty: Easy-Medium
difficulty_score: 32
topics:
  - Arrays
  - Rotation
  - Simulation
tags:
  - arrays
  - rotation
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-003: Shuttle Shift With Blackout

## Problem Statement

Rotate the array to the left by k positions, but indices listed in the blackout
set must stay fixed. Only the elements at non-blackout indices rotate among
themselves in order.

![Problem Illustration](../images/ARR-003/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer k
- Fourth line: integer b, the number of blackout indices
- Fifth line: b space-separated indices (0-based); if b = 0, this line is omitted

## Output Format

Print the resulting array, space-separated.

## Constraints

- `1 <= n <= 200000`
- `0 <= k <= 1000000000`
- `0 <= b <= n`
- `Blackout indices are in range 0..n-1`

## Example

**Input:**
```
5
1 2 3 4 5
2
2
1 3
```

**Output:**
```
3 2 5 4 1
```

**Explanation:**

Indices 1 and 3 stay fixed (values 2 and 4). The remaining elements [1, 3, 5]
rotate left by 2 to [5, 1, 3], yielding [3, 2, 5, 4, 1].

![Example Visualization](../images/ARR-003/example-1.png)

## Notes

- If there are no movable indices, the array is unchanged.
- Use k % movable_count to avoid full rotations.

## Related Topics

Arrays, Rotation, Simulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] shuttleShiftBlackout(int[] arr, int k, Set<Integer> blackout) {
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
        int k = sc.nextInt();
        int b = sc.nextInt();
        Set<Integer> blackout = new HashSet<>();
        for (int i = 0; i < b; i++) {
            blackout.add(sc.nextInt());
        }

        Solution solution = new Solution();
        int[] result = solution.shuttleShiftBlackout(arr, k, blackout);
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
def shuttle_shift_blackout(arr: list[int], k: int, blackout: set[int]) -> list[int]:
    # Your implementation here
    return []

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    b = int(input())
    blackout = set(map(int, input().split())) if b > 0 else set()

    result = shuttle_shift_blackout(arr, k, blackout)
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
    vector<int> shuttleShiftBlackout(vector<int>& arr, int k, unordered_set<int>& blackout) {
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
    int k, b;
    cin >> k;
    cin >> b;
    unordered_set<int> blackout;
    for (int i = 0; i < b; i++) {
        int idx;
        cin >> idx;
        blackout.insert(idx);
    }

    Solution solution;
    vector<int> result = solution.shuttleShiftBlackout(arr, k, blackout);
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
  shuttleShiftBlackout(arr, k, blackout) {
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
const k = Number(data[idx++]);
const b = Number(data[idx++]);
const blackout = new Set();
for (let i = 0; i < b; i++) {
  blackout.add(Number(data[idx++]));
}

const solution = new Solution();
const result = solution.shuttleShiftBlackout(arr, k, blackout);
console.log(result.join(" "));
```

