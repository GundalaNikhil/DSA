---
problem_id: STR_EQUAL_DISTINCT_SPLIT__1005
display_id: STR-005
slug: equal-distinct-split
title: "Equal Distinct Split"
difficulty: Medium
difficulty_score: 38
topics:
  - String Manipulation
  - Prefix-Suffix
  - Hashing
tags:
  - distinct-characters
  - split-point
  - frequency-analysis
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-005: Equal Distinct Split

## Problem Statement

Given a string `s` of lowercase English letters, count the number of split points where the left substring and right substring have the same number of distinct characters.

A split point after index `i` creates:

- Left: s[0..i]
- Right: s[i+1..n-1]

## Input Format

- A single string `s` (1 ≤ |s| ≤ 2 × 10^5)

## Output Format

- A single integer representing the count of valid split points

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
ababa
```

**Output:**

```
2
```

**Explanation:**

- Split after index 1: left="ab" (2 distinct), right="aba" (2 distinct) ✓
- Split after index 2: left="aba" (2 distinct), right="ba" (2 distinct) ✓
- Total: 2 valid splits

## Example 2

**Input:**

```
abc
```

**Output:**

```
0
```

**Explanation:**

- Split after index 0: left="a" (1), right="bc" (2) ✗
- Split after index 1: left="ab" (2), right="c" (1) ✗
- No valid splits

## Notes

- Precompute suffix distinct counts in O(n)
- Scan left-to-right maintaining prefix distinct count
- O(n) time and O(n) space solution

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countEqualDistinctSplits(String s) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution sol = new Solution();
            System.out.println(sol.countEqualDistinctSplits(s));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    solution = Solution()
    print(solution.count_equal_distinct_splits(s))

class Solution:
    def count_equal_distinct_splits(self, s: str) -> int:
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
    int countEqualDistinctSplits(string s) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        Solution sol;
        cout << sol.countEqualDistinctSplits(s) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countEqualDistinctSplits(s) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const s = line.trim();
  if (s) {
    const sol = new Solution();
    console.log(sol.countEqualDistinctSplits(s));
  }
});
```
