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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513327/dsa/dp/pfaduug7ecmdedrdshaj.jpg)

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
import java.io.*;

class Solution {
    public boolean canFormSubset(int n, int target, int k, int[] arr) {
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int target = Integer.parseInt(parts[1]);
        int k = Integer.parseInt(parts[2]);

        int[] arr = new int[n];
        String aLine = br.readLine();
        if (aLine != null) {
            String[] aParts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(aParts[i]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.canFormSubset(n, target, k, arr));
    }
}
```

### Python

```python
import sys

class Solution:
    def can_form_subset(self, n, target, k, arr):
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n, target, k = map(int, input_data[:3])
    arr = list(map(int, input_data[3:3+n]))

    sol = Solution()
    print(str(sol.can_form_subset(n, target, k, arr)).lower())

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool canFormSubset(int n, int target, int k, const vector<int>& arr) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, target, k;
    if (!(cin >> n >> target >> k)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution sol;
    cout << (sol.canFormSubset(n, target, k, arr) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  canFormSubset(n, target, k, arr) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const target = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.canFormSubset(n, target, k, arr));
}

solve();
```
