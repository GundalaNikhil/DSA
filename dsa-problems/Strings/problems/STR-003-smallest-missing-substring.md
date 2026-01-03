---
problem_id: STR_SMALLEST_MISSING_SUBSTRING__1003
display_id: STR-003
slug: smallest-missing-substring
title: "Smallest Missing Substring"
difficulty: Medium
difficulty_score: 40
topics:
  - String Manipulation
  - DFS
  - Hashing
tags:
  - substring-search
  - lexicographic
  - lazy-generation
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-003: Smallest Missing Substring

## Problem Statement

Given a string `s` consisting of lowercase English letters and an integer `k`, find the lexicographically smallest string of length `k` that is NOT a substring of `s`.

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 2 × 10^5)
- Second line: Integer `k` (1 ≤ k ≤ 20)

## Output Format

- A single string of length `k` representing the lexicographically smallest string not present in `s`

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `1 ≤ k ≤ 20`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
ababa
2
```

**Output:**

```
aa
```

**Explanation:**

- Substrings of length 2 in "ababa": "ab", "ba", "ab", "ba"
- Unique: {"ab", "ba"}
- Checking lexicographically: "aa" is not in set → answer

## Example 2

**Input:**

```
abc
3
```

**Output:**

```
aaa
```

**Explanation:**

- "abc" only has one substring of length 3: "abc"
- "aaa" is lexicographically first and not in "abc"

## Notes

- Use DFS with lazy generation to avoid creating all 26^k possibilities
- Build a set of existing k-length substrings for O(1) lookup
- Generate candidates in lexicographic order and stop at first missing

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String smallestMissingSubstring(String s, int k) {
        //Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.smallestMissingSubstring(s, k));
        sc.close();
    }
}
```

### Python

```python
def smallest_missing_substring(s: str, k: int) -> str:
    # //Implement here
    return 0

def main():
    import sys
    # Read all input
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
        
    # Parse input: expect string s and integer k
    # Using split() handles newlines and spaces
    parts = input_data.split()
    if len(parts) >= 2:
        s = parts[0]
        try:
            k = int(parts[1])
            print(smallest_missing_substring(s, k))
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
    string smallestMissingSubstring(string s, int k) {
        //Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int k; cin >> k;
    Solution sol;
    cout << sol.smallestMissingSubstring(s, k) << endl;
    return 0;
}
```

### JavaScript

```javascript
function smallestMissingSubstring(s, k) {
  //Implement here
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
    console.log(smallestMissingSubstring(s, k));
});
```
