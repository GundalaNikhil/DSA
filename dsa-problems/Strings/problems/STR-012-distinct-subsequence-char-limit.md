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

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countDistinctSubsequencesWithLimit(String s, int maxFreq, int MOD) {
        return 0;
    }

    private String encode(int[] freq) {
        return "";
    }

    private int[] decode(String s) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int maxFreq = sc.nextInt();
        int MOD = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countDistinctSubsequencesWithLimit(s, maxFreq, MOD));
        sc.close();
    }
}
```

### Python

```python
def count_distinct_subsequences_with_limit(s: str, max_freq: int, MOD: int) -> int:
    return 0
def main():
    import sys

    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if len(parts) >= 3:
        s = parts[0]
        try:
            max_freq = int(parts[1])
            MOD = int(parts[2])
            print(count_distinct_subsequences_with_limit(s, max_freq, MOD))
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
    int countDistinctSubsequencesWithLimit(string s, int maxFreq, int MOD) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int maxFreq; cin >> maxFreq;
    int MOD; cin >> MOD;
    Solution sol;
    cout << sol.countDistinctSubsequencesWithLimit(s, maxFreq, MOD) << endl;
    return 0;
}
```

### JavaScript

```javascript
function countDistinctSubsequencesWithLimit(s, maxFreq, MOD) {
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
    const maxFreq = parseInt(tokens[ptr++]);
    const MOD = parseInt(tokens[ptr++]);
    console.log(countDistinctSubsequencesWithLimit(s, maxFreq, MOD));
});
```

