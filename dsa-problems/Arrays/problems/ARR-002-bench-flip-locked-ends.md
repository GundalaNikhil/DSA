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
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        solution.benchFlipLockedEnds(arr);
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(arr[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
```

### Python

```python
import sys

def bench_flip_locked_ends(arr: list[int]) -> None:
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
#include <algorithm>
using namespace std;

class Solution {
public:
    void benchFlipLockedEnds(vector<int>& arr) {
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
    solution.benchFlipLockedEnds(arr);
    
    for (int i = 0; i < n; i++) {
        cout << arr[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  benchFlipLockedEnds(arr) {
    return 0;
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
    for (let i = 0; i < n; i++) {
        arr.push(Number(tokens[ptr++]));
    }
    
    const solution = new Solution();
    solution.benchFlipLockedEnds(arr);
    console.log(arr.join(" "));
});
```

