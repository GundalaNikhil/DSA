---
problem_id: SRT_LONGEST_CONSECUTIVE_ONE_CHANGE__6194
display_id: SRT-011
slug: longest-consecutive-one-change
title: "Longest Consecutive After At Most One Change"
difficulty: Medium
difficulty_score: 53
topics:
  - Sorting
  - Prefix Suffix
  - Arrays
tags:
  - arrays
  - prefix-suffix
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-011: Longest Consecutive After At Most One Change

## Problem Statement

Given an array, you may change at most one element to any value. Find the maximum length of a strictly increasing contiguous subarray you can obtain.

![Problem Illustration](../images/SRT-011/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single integer: maximum possible length

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
6
1 2 3 7 5 6
```

**Output:**

```
6
```

**Explanation:**

Change `7` to `4` to get `[1,2,3,4,5,6]`.

![Example Visualization](../images/SRT-011/example-1.png)

## Notes

- Precompute longest increasing prefix and suffix lengths
- Try bridging around each index with one change
- The answer is at least the original longest run
- Time complexity: O(n)

## Related Topics

Arrays, Prefix/Suffix, Optimization

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int longestAfterChange(int[] arr) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.longestAfterChange(arr));
        sc.close();
    }
}
```

### Python

```python
def longest_after_change(arr: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]

    print(longest_after_change(arr))

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
    int longestAfterChange(const vector<int>& arr) {
        // Your implementation here
        return 0;
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
    cout << solution.longestAfterChange(arr) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestAfterChange(arr) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  console.log(solution.longestAfterChange(arr).toString());
});
```
