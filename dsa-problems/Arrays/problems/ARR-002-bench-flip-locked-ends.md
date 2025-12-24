---
problem_id: ARR_BENCH_FLIP_LOCKED__1397
display_id: ARR-002
slug: bench-flip-locked-ends
title: "Bench Flip With Locked Ends"
difficulty: Easy
difficulty_score: 20
topics:
  - Arrays
  - Two Pointers
  - In-place
tags:
  - arrays
  - two-pointers
  - in-place
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-002: Bench Flip With Locked Ends

## Problem Statement

Reverse the array in place, but keep the first and last elements fixed. Only the middle segment is reversed.

![Problem Illustration](../images/ARR-002/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]

## Output Format

Print the resulting array, space-separated.

## Constraints

- `2 <= n <= 200000`
- `-1000000000 <= arr[i] <= 1000000000`

## Example

**Input:**
```
5
9 3 8 1 5
```

**Output:**
```
9 1 8 3 5
```

**Explanation:**

The first and last elements stay. The middle subarray [3, 8, 1] is reversed to
[1, 8, 3].

![Example Visualization](../images/ARR-002/example-1.png)

## Notes

- If n <= 2, the array is unchanged.
- Use two pointers starting at indices 1 and n-2.

## Related Topics

Arrays, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void benchFlipLockedEnds(int[] arr) {
        // Your implementation here
        
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
        solution.benchFlipLockedEnds(arr);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(arr[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```


### Python

```python
def bench_flip_locked_ends(arr: list[int]) -> None:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    bench_flip_locked_ends(arr)
    print(" ".join(map(str, arr)))

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
    void benchFlipLockedEnds(vector<int>& arr) {
        // Your implementation here
        
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
    solution.benchFlipLockedEnds(arr);
    for (size_t i = 0; i < arr.size(); i++) {
        if (i) cout << " ";
        cout << arr[i];
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
  benchFlipLockedEnds(arr) {
    // Your implementation here
    return;
  }
}

let idx = 0;
const n = Number(data[idx++]);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(Number(data[idx++]));
}

const solution = new Solution();
solution.benchFlipLockedEnds(arr);
console.log(arr.join(" "));
```

