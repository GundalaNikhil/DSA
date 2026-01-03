---
problem_id: STC_DIFF_SUBSTRINGS_TWO_STRINGS__6174
display_id: STC-012
slug: diff-substrings-two-strings
title: "Number of Different Substrings of Two Strings"
difficulty: Medium
difficulty_score: 58
topics:
  - Strings
  - Suffix Array
  - Counting
tags:
  - strings
  - suffix-array
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-012: Number of Different Substrings of Two Strings

## Problem Statement

You are given two strings `a` and `b`. Count how many substrings of `a` do not appear anywhere in `b`.

Return the total number of distinct substrings of `a` that are absent from `b`.

![Problem Illustration](../images/STC-012/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`

## Output Format

- Single integer: number of distinct substrings of `a` not present in `b`

## Constraints

- `1 <= |a|, |b| <= 100000`
- `|a| + |b| <= 200000`
- Strings contain lowercase English letters

## Example

**Input:**

```
ab
b
```

**Output:**

```
2
```

**Explanation:**

Substrings of `a` are "a", "b", and "ab". Only "b" appears in `b`, so the answer is 2.

![Example Visualization](../images/STC-012/example-1.png)

## Notes

- The answer can be large; use 64-bit integers.
- With suffix array and LCP, subtract the longest overlap with `b` for each suffix of `a`.
- A suffix automaton of `b` can also provide longest matches in O(n).
- Time complexity: O(n log n) or O(n) depending on approach.

## Related Topics

Suffix Array, Suffix Automaton, Distinct Substrings

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countExclusiveSubstrings(String a, String b) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String a = sc.next();
            if (sc.hasNext()) {
                String b = sc.next();
                Solution solution = new Solution();
                System.out.println(solution.countExclusiveSubstrings(a, b));
            }
        }
        sc.close();
    }
}
```

### Python

```python
def count_exclusive_substrings(a: str, b: str) -> int:
    # //Implement here
    return 0

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    a, b = input_data[0], input_data[1]
    print(count_exclusive_substrings(a, b))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long countExclusiveSubstrings(const string& a, const string& b) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (cin >> a >> b) {
        Solution solution;
        cout << solution.countExclusiveSubstrings(a, b) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countExclusiveSubstrings(a, b) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length < 2) return;
  const a = data[0];
  const b = data[1];
  const solution = new Solution();
  console.log(solution.countExclusiveSubstrings(a, b).toString());
});
```

