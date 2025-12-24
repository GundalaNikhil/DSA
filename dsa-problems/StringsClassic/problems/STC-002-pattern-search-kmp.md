---
problem_id: STC_PATTERN_SEARCH_KMP__6142
display_id: STC-002
slug: pattern-search-kmp
title: "Pattern Search With KMP"
difficulty: Easy
difficulty_score: 30
topics:
  - Strings
  - KMP
  - Pattern Matching
tags:
  - strings
  - kmp
  - pattern-search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-002: Pattern Search With KMP

## Problem Statement

Given a pattern `p` and text `t`, find all starting indices where `p` occurs in `t` using the KMP algorithm.

Indices are 0-based and should be returned in increasing order.

![Problem Illustration](../images/STC-002/problem-illustration.png)

## Input Format

- First line: pattern string `p`
- Second line: text string `t`

## Output Format

- Single line: space-separated indices of all occurrences
- If there are no occurrences, print an empty line

## Constraints

- `1 <= |p|, |t| <= 200000`
- `p` and `t` contain lowercase English letters

## Example

**Input:**

```
aba
ababa
```

**Output:**

```
0 2
```

**Explanation:**

The pattern "aba" occurs at positions 0 and 2.

![Example Visualization](../images/STC-002/example-1.png)

## Notes

- Use the prefix function for `p`
- KMP runs in O(|p| + |t|)
- Overlapping matches should be included
- Output order must be increasing

## Related Topics

KMP, Pattern Matching, Prefix Function

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] findOccurrences(String p, String t) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String p = sc.next();
        String t = sc.next();

        Solution solution = new Solution();
        int[] result = solution.findOccurrences(p, t);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def find_occurrences(p: str, t: str) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    p = data[0]
    t = data[1]
    result = find_occurrences(p, t)
    print(" ".join(str(x) for x in result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> findOccurrences(const string& p, const string& t) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string p, t;
    if (!(cin >> p >> t)) return 0;
    Solution solution;
    vector<int> result = solution.findOccurrences(p, t);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findOccurrences(p, t) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const p = data[0];
  const t = data[1];
  const solution = new Solution();
  const result = solution.findOccurrences(p, t);
  console.log(result.join(" "));
});
```
