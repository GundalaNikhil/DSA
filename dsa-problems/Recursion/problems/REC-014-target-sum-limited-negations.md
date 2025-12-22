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
    public long countAssignments(int[] nums, int K, int target) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int K = sc.nextInt();
        int target = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countAssignments(nums, K, target));
        sc.close();
    }
}
```

### Python

```python
def count_assignments(nums: list[int], K: int, target: int) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    K = int(next(it))
    target = int(next(it))
    nums = [int(next(it)) for _ in range(n)]

    print(count_assignments(nums, K, target))

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
    long long countAssignments(const vector<int>& nums, int K, int target) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, K, target;
    if (!(cin >> n >> K >> target)) return 0;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];

    Solution solution;
    cout << solution.countAssignments(nums, K, target) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countAssignments(nums, K, target) {
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
  const K = parseInt(data[idx++], 10);
  const target = parseInt(data[idx++], 10);
  const nums = [];
  for (let i = 0; i < n; i++) nums.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  console.log(solution.countAssignments(nums, K, target).toString());
});
```
