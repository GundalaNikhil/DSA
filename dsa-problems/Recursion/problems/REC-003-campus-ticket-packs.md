---
problem_id: REC_CAMPUS_TICKET_PACKS__2187
display_id: REC-003
slug: campus-ticket-packs
title: "Campus Ticket Packs"
difficulty: Medium
difficulty_score: 46
topics:
  - Recursion
  - Backtracking
  - Combinations
tags:
  - recursion
  - combinations
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-003: Campus Ticket Packs

## Problem Statement

A ticket system has `n` values `v[i]`. For each value you may take either `0` tickets or exactly `p[i]` tickets (a fixed pack size). List all unique combinations of ticket values that sum exactly to `target`.

Output each combination as a space-separated list of ticket values in nondecreasing order. If no combination exists, output `NONE`.

![Problem Illustration](../images/REC-003/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `v[i]`
- Third line: `n` space-separated integers `p[i]`
- Fourth line: integer `target`

## Output Format

- Each valid combination on its own line (values space-separated)
- Output `NONE` if no solution exists

## Constraints

- `1 <= n <= 15`
- `1 <= target <= 200`
- `1 <= v[i] <= 50`
- `1 <= p[i] <= 10`

## Example

**Input:**

```
2
2 3
2 1
7
```

**Output:**

```
2 2 3
```

**Explanation:**

Choose two 2s and one 3 to reach 7.

![Example Visualization](../images/REC-003/example-1.png)

## Notes

- Decide for each value whether to take its full pack or not
- Sort values to keep combinations ordered
- Prune when current sum exceeds target
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinations, Pruning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countCombinations(List<Integer> values, int target) {
        return 0;
    }

    private long backtrack(int index, int currentSum, List<Integer> values, int target) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int target = sc.nextInt();
        
        List<Integer> values = new ArrayList<>();
        // Read remaining ints
        while(sc.hasNextInt()) {
            values.add(sc.nextInt());
        }
        
        Solution sol = new Solution();
        System.out.println(sol.countCombinations(values, target));
        sc.close();
    }
}
```

### Python

```python
def count_combinations(values: list[int], target: int) -> int:
    return 0
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    first_line = list(map(int, lines[0].split()))
    n = first_line[0]
    target = first_line[1]
    values = list(map(int, lines[1].split()))

    result = count_combinations(values, target)
    print(result)

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
    long long countCombinations(const vector<int>& values, int target) {
        return 0;
    }

private:
    long long backtrack(int index, int currentSum, const vector<int>& values, int target) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, target;
    if (!(cin >> n >> target)) return 0;
    
    vector<int> values(n);
    for(int i=0; i<n; i++) cin >> values[i];
    
    Solution sol;
    cout << sol.countCombinations(values, target) << endl;
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
    
    if(ptr >= tokens.length) return;
    const n = parseInt(tokens[ptr++]);
    const target = parseInt(tokens[ptr++]);
    
    const values = [];
    for(let i=0; i<n; i++) {
        if(ptr < tokens.length) values.push(parseInt(tokens[ptr++]));
    }
    
    const sol = new Solution();
    console.log(sol.countCombinations(values, target));
});

class Solution {
    countCombinations(values, target) {
    return 0;
  }

    backtrack(index, currentSum, values, target) {
    return 0;
  }
}
```

