---
problem_id: REC_SUBSET_SUM_EXACT_COUNT__1854
display_id: REC-006
slug: subset-sum-exact-count
title: "Subset Sum Exact Count"
difficulty: Medium
difficulty_score: 43
topics:
  - Recursion
  - Backtracking
  - Subset Sum
tags:
  - recursion
  - subset-sum
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-006: Subset Sum Exact Count

## Problem Statement

Given an array `arr`, determine whether there exists a subset of exactly `k` elements that sums to `target`. Return one such subset if it exists, otherwise output `NONE`.

![Problem Illustration](../images/REC-006/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `target`
- Second line: `n` space-separated integers `arr[i]`

## Output Format

- One line with a valid subset (space-separated), or `NONE` if no solution exists

## Constraints

- `1 <= n <= 20`
- `0 <= k <= n`
- `|arr[i]| <= 10000`
- `|target| <= 10^9`

## Example

**Input:**

```
4 2 7
4 1 6 2
```

**Output:**

```
1 6
```

**Explanation:**

The subset `{1, 6}` uses exactly two elements and sums to 7.

![Example Visualization](../images/REC-006/example-1.png)

## Notes

- Use recursion to choose or skip each element
- Track how many elements have been chosen
- Prune when remaining elements are insufficient to reach `k`
- Any valid subset is acceptable

## Related Topics

Backtracking, Subset Sum, Pruning

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<Integer> findSubset(int[] arr, int k, int target) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int target = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<Integer> result = solution.findSubset(arr, k, target);
        if (result.isEmpty()) {
            System.out.println("NONE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(result.get(i));
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
def find_subset(arr: list[int], k: int, target: int) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    target = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    result = find_subset(arr, k, target)
    if not result:
        print("NONE")
    else:
        print(" ".join(str(x) for x in result))

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
    vector<int> findSubset(const vector<int>& arr, int k, int target) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, target;
    if (!(cin >> n >> k >> target)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    vector<int> result = solution.findSubset(arr, k, target);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findSubset(arr, k, target) {
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
  const k = parseInt(data[idx++], 10);
  const target = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.findSubset(arr, k, target);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.join(" "));
  }
});
```
