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

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean canBalance(String s, int k) {
        // Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.canBalance(s, k));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    s = input_data[0]
    k = int(input_data[1])
    solution = Solution()
    print(str(solution.can_balance(s, k)).lower())

class Solution:
    def can_balance(self, s: str, k: int) -> bool:
        # Implement here
        return False

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool canBalance(string s, int k) {
        // Implement here
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int k;
    if (cin >> s >> k) {
        Solution sol;
        cout << (sol.canBalance(s, k) ? "true" : "false") << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  canBalance(s, k) {
    // Implement here
    return false;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length >= 2) {
    const s = input[0];
    const k = parseInt(input[1]);
    const sol = new Solution();
    console.log(sol.canBalance(s, k));
  }
});
```
