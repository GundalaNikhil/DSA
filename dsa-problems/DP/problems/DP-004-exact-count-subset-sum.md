---
problem_id: DP_SUBSET_EXACT_K__9053
display_id: DP-004
slug: exact-count-subset-sum
title: "Exact Count Subset Sum"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
  - Subset Sum
  - Bitset
tags:
  - dp
  - subset-sum
  - bitset
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-004: Exact Count Subset Sum

## Problem Statement

Given an integer array `arr` of length `n`, determine whether there exists a subset of **exactly `k` elements** whose sum is exactly `target`.

Print `true` if such a subset exists, otherwise print `false`.

![Problem Illustration](../images/DP-004/problem-illustration.png)

## Input Format

- First line: three integers `n`, `target`, `k`
- Second line: `n` space-separated integers `arr[i]`

## Output Format

Print one word:

- `true` if there exists a subset of exactly `k` elements summing to `target`
- `false` otherwise

## Constraints

- `1 <= n <= 200`
- `0 <= target <= 5000`
- `0 <= k <= n`
- `0 <= arr[i] <= 5000`

## Example

**Input:**
```
4 10 2
3 1 9 7
```

**Output:**
```
true
```

**Explanation:**

Choose exactly 2 elements:

- `3 + 7 = 10` ✅

So the answer is `true`.

![Example Visualization](../images/DP-004/example-1.png)

## Notes

- This is not the classic subset-sum: you must use **exactly `k`** elements.
- If `k = 0`, only the empty subset is allowed, so the answer is `true` iff `target = 0`.
- Time constraints require avoiding `O(n * k * target)` if implemented naively in slow languages.

## Related Topics

Dynamic Programming, Subset Sum, Bitset Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean exactCountSubsetSum(int[] arr, int target, int k) {
        // Implementation here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int target = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.println(new Solution().exactCountSubsetSum(arr, target, k) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys

def exact_count_subset_sum(arr: list[int], target: int, k: int) -> bool:
    # Implementation here
    return False

def main():
    n, target, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print("true" if exact_count_subset_sum(arr, target, k) else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>

using namespace std;

class Solution {
public:
    bool exactCountSubsetSum(const vector<int>& arr, int target, int k) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, target, k;
    cin >> n >> target >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution sol;
    cout << (sol.exactCountSubsetSum(arr, target, k) ? "true" : "false") << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  exactCountSubsetSum(arr, target, k) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  const [n, target, k] = lines[0].split(" ").map(Number);
  const arr = lines[1].split(" ").map(Number);
  const sol = new Solution();
  console.log(sol.exactCountSubsetSum(arr, target, k) ? "true" : "false");
});
```
