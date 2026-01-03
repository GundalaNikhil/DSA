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
    public boolean countAssignments(List<Integer> nums, int k, int target) {
        //Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int target = sc.nextInt();
        
        List<Integer> nums = new ArrayList<>();
        for(int i=0; i<n; i++) nums.add(sc.nextInt());
        
        Solution sol = new Solution();
        if(sol.countAssignments(nums, k, target)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}
```

### Python

```python
def can_achieve_target(nums: list[int], K: int, target: int) -> bool:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return
    first_line = lines[0].split()
    n = int(first_line[0])
    K = int(first_line[1])
    target = int(first_line[2])
    nums = list(map(int, lines[1].split()))
    result = can_achieve_target(nums, K, target)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <map>

using namespace std;

class Solution {
public:
    bool countAssignments(const vector<int>& nums, int k, int target) {
        //Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; 
    if (!(cin >> n)) return 0;
    
    int k, target; 
    cin >> k >> target;
    
    vector<int> nums(n);
    for(int i=0; i<n; i++) cin >> nums[i];

    Solution sol;
    if (sol.countAssignments(nums, k, target)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const k = parseInt(tokens[ptr++]);
    const target = parseInt(tokens[ptr++]);
    
    const nums = [];
    for(let i=0; i<n; i++) nums.push(parseInt(tokens[ptr++]));
    
    const sol = new Solution();
    if(sol.countAssignments(nums, k, target)) {
        console.log("YES");
    } else {
        console.log("NO");
    }
});

class Solution {
  countAssignments(nums, k, target) {
    //Implement here
    return 0;
  }
}
```

