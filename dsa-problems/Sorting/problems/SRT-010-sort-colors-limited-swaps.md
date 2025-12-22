---
problem_id: SRT_SORT_COLORS_LIMITED_SWAPS__4762
display_id: SRT-010
slug: sort-colors-limited-swaps
title: "Sort Colors With Limited Swaps"
difficulty: Medium
difficulty_score: 57
topics:
  - Sorting
  - Greedy
  - Adjacent Swaps
tags:
  - greedy
  - adjacent-swaps
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-010: Sort Colors With Limited Swaps

## Problem Statement

You are given an array of 0s, 1s, and 2s. You may swap only adjacent elements and perform at most `S` swaps. Produce the lexicographically smallest array reachable within `S` swaps.

![Problem Illustration](../images/SRT-010/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (each is 0, 1, or 2)
- Third line: integer `S`

## Output Format

- Single line: lexicographically smallest array reachable within `S` swaps

## Constraints

- `1 <= n <= 200000`
- `0 <= S <= 10^9`
- Values are only 0, 1, or 2

## Example

**Input:**

```
3
2 1 0
1
```

**Output:**

```
1 2 0
```

**Explanation:**

With one adjacent swap, the smallest reachable array is `[1,2,0]`.

![Example Visualization](../images/SRT-010/example-1.png)

## Notes

- Greedily move smaller values left while swaps remain
- Adjacent swaps act like limited bubble steps
- Track remaining swaps to avoid exceeding `S`
- Time complexity should be near O(n)

## Related Topics

Greedy, Adjacent Swaps, Sorting

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] sortWithSwaps(int[] arr, long S) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        long S = sc.nextLong();

        Solution solution = new Solution();
        int[] result = solution.sortWithSwaps(arr, S);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def sort_with_swaps(arr: list[int], S: int) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    S = int(next(it))

    result = sort_with_swaps(arr, S)
    sys.stdout.write(" ".join(str(x) for x in result))

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
    vector<int> sortWithSwaps(const vector<int>& arr, long long S) {
        // Your implementation here
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
    long long S;
    cin >> S;

    Solution solution;
    vector<int> result = solution.sortWithSwaps(arr, S);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  sortWithSwaps(arr, S) {
    // Your implementation here
    return [];
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
  const S = parseInt(data[idx++], 10);

  const solution = new Solution();
  const result = solution.sortWithSwaps(arr, S);
  console.log(result.join(" "));
});
```
