---
problem_id: STR_BALANCED_BRACKETS_LIMITED_SKIPS__1010
display_id: STR-010
slug: balanced-brackets-limited-skips
title: "Balanced Brackets With Limited Skips"
difficulty: Medium
difficulty_score: 37
topics:
  - String Manipulation
  - Stack
  - Greedy
tags:
  - parentheses
  - balance-checking
  - skip-tokens
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-010: Balanced Brackets With Limited Skips

## Problem Statement

Given a string `s` consisting of '(' and ')' characters, and an integer `k` representing the number of skip tokens available, determine if the string can be balanced using at most `k` skips.

A skip token allows you to remove one parenthesis from consideration.

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 2 × 10^5)
- Second line: Integer `k` (0 ≤ k ≤ |s|)

## Output Format

- `true` if string can be balanced, `false` otherwise

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `0 ≤ k ≤ |s|`
- `s` contains only '(' and ')'

## Example 1

**Input:**

```
())(
2
```

**Output:**

```
true
```

**Explanation:**

- Skip ')' at index 2
- Skip '(' at index 3
- Remaining: "()" → balanced

## Example 2

**Input:**

```
(((
1
```

**Output:**

```
false
```

**Explanation:**

- Need to skip all 3 '(' but only have 1 skip token

## Notes

- Greedy balance tracking with O(n) time
- Skip ')' immediately when balance goes negative
- Final balance indicates unmatched '(' needing skips

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean canBalanceWithSkips(String s, int k) {
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.canBalanceWithSkips(s, k));
        sc.close();
    }
}
```

### Python

```python
def can_balance_with_skips(s: str, k: int) -> bool:
    return False
def main():
    import sys

    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print("false")
        return
        
    parts = input_data.split()
    if len(parts) >= 2:
        s = parts[0]
        try:
            k = int(parts[1])
            result = can_balance_with_skips(s, k)
            print("true" if result else "false")
        except ValueError:
            pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
class Solution {
public:
    bool canBalanceWithSkips(string s, int k) {
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int k; cin >> k;
    Solution sol;
    cout << (sol.canBalanceWithSkips(s, k) ? "true" : "false") << endl;
    return 0;
}
```

### JavaScript

```javascript
function canBalanceWithSkips(s, k) {
    return 0;
  }

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const k = parseInt(tokens[ptr++]);
    console.log(canBalanceWithSkips(s, k));
});
```

