---
problem_id: REC_EXPRESSION_TARGET_ONE_FLIP__9316
display_id: REC-009
slug: expression-target-one-flip
title: "Expression Target With One Negation Flip"
difficulty: Medium
difficulty_score: 57
topics:
  - Recursion
  - Backtracking
  - Expressions
tags:
  - recursion
  - backtracking
  - expressions
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-009: Expression Target With One Negation Flip

## Problem Statement

Given a digit string `s`, insert `+` or `-` operators between digits or concatenate digits to form an expression that evaluates to `T`.

You may also apply a unary negation to at most one operand chunk (write it with a leading `-` without adding an operator). Use at most `c` binary operators in total.

Return all valid expressions in lexicographic order. If none exist, output `NONE`.

![Problem Illustration](../images/REC-009/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `T`
- Third line: integer `c`

## Output Format

- Each valid expression on its own line, in lexicographic order
- Output `NONE` if no expression matches

## Constraints

- `1 <= |s| <= 10`
- `0 <= c <= 9`
- `-10^9 <= T <= 10^9`
- No chunk may have leading zeros unless the chunk is exactly `"0"`

## Example

**Input:**

```
1203
-202
2
```

**Output:**

```
1+-203
```

**Explanation:**

Split into `1` and `203`, insert `+`, and apply the unary flip to `203`: `1 + (-203) = -202`.

![Example Visualization](../images/REC-009/example-1.png)

## Notes

- Track current value, previous operator count, and whether a flip has been used
- Avoid leading-zero chunks
- The unary flip applies to a chosen chunk only once
- Backtracking is required to explore all splits

## Related Topics

Backtracking, Expression Evaluation, Recursion

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int findFlipIndex(List<Integer> nums, String ops, int target) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        List<Integer> nums = new ArrayList<>();
        for(int i=0; i<n; i++) nums.add(sc.nextInt());
        
        String ops = sc.next();
        int target = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.findFlipIndex(nums, ops, target));
        sc.close();
    }
}
```

### Python

```python
import sys

def find_flip_index(nums: list[int], ops: str, target: int) -> int:
    # Implementation here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 4:
        return
    n = int(lines[0].strip())
    nums = list(map(int, lines[1].split()))
    ops = lines[2].strip()
    target = int(lines[3].strip())
    result = find_flip_index(nums, ops, target)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int findFlipIndex(const vector<int>& nums, string ops, int target) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> nums(n);
    for(int i=0; i<n; i++) cin >> nums[i];
    
    string ops; cin >> ops;
    int target; cin >> target;
    
    Solution sol;
    cout << sol.findFlipIndex(nums, ops, target) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findFlipIndex(nums, ops, target) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const nums = [];
    for(let i=0; i<n; i++) nums.push(parseInt(tokens[ptr++]));
    
    const ops = tokens[ptr++];
    const target = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.findFlipIndex(nums, ops, target));
});
```
