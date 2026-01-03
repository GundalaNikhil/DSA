---
problem_id: REC_PALINDROME_PARTITION_MIN_COUNT__3491
display_id: REC-013
slug: palindrome-partition-min-count
title: "Palindrome Partition with Minimum Count"
difficulty: Medium
difficulty_score: 53
topics:
  - Recursion
  - Backtracking
  - Strings
tags:
  - recursion
  - palindrome
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-013: Palindrome Partition with Minimum Count

## Problem Statement

Given a string `s` and a maximum substring length `L`, partition `s` into palindromic substrings of length at most `L` using the minimum possible number of substrings.

Return the lexicographically smallest partition that achieves this minimum (when comparing palindromes at each step from shortest to longest). If no partition is possible, output `NONE`.

![Problem Illustration](../images/REC-013/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `L`

## Output Format

- One line with the lexicographically smallest minimum partition, substrings space-separated
- Output `NONE` if no partition is possible

## Constraints

- `1 <= |s| <= 12`
- `1 <= L <= |s|`
- `s` contains lowercase English letters

## Example

**Input:**

```
aab
2
```

**Output:**

```
aa b
```

**Explanation:**

The minimum number of palindromic substrings is 2: "aa" and "b".

![Example Visualization](../images/REC-013/example-1.png)

## Notes

- Precompute palindrome checks for fast pruning
- Use recursion to explore partitions with length <= L
- Keep track of the current minimum size
- When exploring at each step, try shorter palindromes first to get lexicographically smallest partition
- Among all partitions with minimum count, return the first one found (which will be lexicographically smallest)

## Related Topics

Backtracking, Palindromes, Recursion

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public String minPalindromePartitions(String s, int l) {
        //Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNext()) return;
        String s = sc.next();
        if(!sc.hasNextInt()) return;
        int L = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.minPalindromePartitions(s, L));
        sc.close();
    }
}
```

### Python

```python
def min_palindrome_partitions(s: str, L: int) -> list[str]:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return
    s = lines[0].strip()
    L = int(lines[1].strip())
    result = min_palindrome_partitions(s, L)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string minPalindromePartitions(string s, int l) {
        //Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    int L; cin >> L;
    
    Solution sol;
    cout << sol.minPalindromePartitions(s, L) << endl;
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
    const s = tokens[ptr++];
    const L = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.minPalindromePartitions(s, L));
});

class Solution {
  minPalindromePartitions(s, L) {
    //Implement here
    return 0;
  }
}
```

