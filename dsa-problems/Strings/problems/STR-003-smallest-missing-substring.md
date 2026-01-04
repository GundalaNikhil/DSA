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

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String smallestMissing(String s, int k) {
        // Implement here
        return "";
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
                System.out.println(sol.smallestMissing(s, k));
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
    print(solution.smallest_missing(s, k))

class Solution:
    def smallest_missing(self, s: str, k: int) -> str:
        # Implement here
        return ""

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
    string smallestMissing(string s, int k) {
        // Implement here
        return "";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int k;
    if (cin >> s >> k) {
        Solution sol;
        cout << sol.smallestMissing(s, k) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  smallestMissing(s, k) {
    // Implement here
    return "";
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
    console.log(sol.smallestMissing(s, k));
  }
});
```
