---
problem_id: STR_DISTINCT_SUBSEQUENCE_CHAR_LIMIT__1012
display_id: STR-012
slug: distinct-subsequence-char-limit
title: "Distinct Subsequence Count with Character Limit"
difficulty: Medium
difficulty_score: 48
topics:
  - String Manipulation
  - Dynamic Programming
  - Subsequence
tags:
  - frequency-constraint
  - dp-optimization
  - modular-arithmetic
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-012: Distinct Subsequence Count with Character Limit

## Problem Statement

Given a string `s`, an integer `maxFreq`, and a modulus `MOD`, count the number of distinct subsequences where each character appears at most `maxFreq` times. Return the count modulo `MOD`.

The empty subsequence counts.

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `maxFreq` (1 ≤ maxFreq ≤ 10)
- Third line: Integer `MOD` (prime, ≤ 10^9+7)

## Output Format

- A single integer representing the count modulo MOD

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ maxFreq ≤ 10`
- Prime `MOD ≤ 10^9+7`

## Example 1

**Input:**

```
aaa
2
1000000007
```

**Output:**

```
7
```

**Explanation:**

- Valid subsequences by position:
  - Empty: 1
  - Single 'a': positions {0}, {1}, {2} → 3
  - Double 'aa': positions {0,1}, {0,2}, {1,2} → 3
  - Triple 'aaa' excluded (freq=3 > maxFreq=2)
- Total: 7

## Notes

- DP with frequency state tracking
- Use map for sparse state representation
- Apply modulo at every step

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countDistinctSubsequences(String s, int maxFreq, int MOD) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (sc.hasNextInt()) {
                int maxFreq = sc.nextInt();
                if (sc.hasNextInt()) {
                    int MOD = sc.nextInt();
                    Solution sol = new Solution();
                    System.out.println(sol.countDistinctSubsequences(s, maxFreq, MOD));
                }
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
    if len(input_data) < 3:
        return
    s = input_data[0]
    max_freq = int(input_data[1])
    MOD = int(input_data[2])
    solution = Solution()
    print(solution.count_distinct_subsequences(s, max_freq, MOD))

class Solution:
    def count_distinct_subsequences(self, s: str, max_freq: int, MOD: int) -> int:
        # Implement here
        return 0

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
    int countDistinctSubsequences(string s, int maxFreq, int MOD) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int maxFreq, MOD;
    if (cin >> s >> maxFreq >> MOD) {
        Solution sol;
        cout << sol.countDistinctSubsequences(s, maxFreq, MOD) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countDistinctSubsequences(s, maxFreq, MOD) {
    // Implement here
    return 0;
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
  if (input.length >= 3) {
    const s = input[0];
    const maxFreq = parseInt(input[1]);
    const MOD = parseInt(input[2]);
    const sol = new Solution();
    console.log(sol.countDistinctSubsequences(s, maxFreq, MOD));
  }
});
```
