---
problem_id: REC_TARGET_SUM_LIMITED_NEGATIONS__8206
display_id: REC-014
slug: target-sum-limited-negations
title: "Target Sum With Limited Negations"
difficulty: Medium
difficulty_score: 49
topics:
  - Recursion
  - Backtracking
  - DP
tags:
  - recursion
  - target-sum
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-014: Target Sum With Limited Negations

## Problem Statement

Given an array `nums`, assign each number either `+` or `-` so that the total equals `target`. You may negate at most `K` numbers.

Return the number of valid sign assignments.

![Problem Illustration](../images/REC-014/problem-illustration.png)

## Input Format

- First line: integers `n`, `K`, and `target`
- Second line: `n` space-separated integers `nums[i]`

## Output Format

- Single integer: number of valid assignments

## Constraints

- `1 <= n <= 20`
- `0 <= K <= n`
- `|nums[i]| <= 20`
- `|target| <= 10^9`

## Example

**Input:**

```
3 1 2
1 2 3
```

**Output:**

```
2
```

**Explanation:**

Valid assignments include `+1 +2 -3` and `-1 +2 +3`.

![Example Visualization](../images/REC-014/example-1.png)

## Notes

- Track position, current sum, and negations used
- Use recursion with pruning or memoization
- The search space is size `2^n`
- Count all assignments that meet constraints

## Related Topics

Backtracking, Target Sum, Recursion

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countAssignments(int n, int k, long target, int[] nums) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        long target = sc.nextLong();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countAssignments(n, k, target, nums));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_assignments(self, n, k, target, nums):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    target = int(input_data[2])
    nums = [int(x) for x in input_data[3:3+n]]
    sol = Solution()
    print(sol.count_assignments(n, k, target, nums))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long countAssignments(int n, int k, long long target, const vector<int>& nums) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    long long target;
    if (!(cin >> n >> k >> target)) return 0;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    Solution sol;
    cout << sol.countAssignments(n, k, target, nums) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countAssignments(n, k, target, nums) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  const target = BigInt(input[2]);
  const nums = [];
  for (let i = 0; i < n; i++) nums.push(parseInt(input[3 + i]));
  const sol = new Solution();
  console.log(sol.countAssignments(n, k, target, nums).toString());
}

solve();
```
