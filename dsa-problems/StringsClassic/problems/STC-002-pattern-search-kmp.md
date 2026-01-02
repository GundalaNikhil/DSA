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
        return null;
    }
    
    private int[] computePrefixFunction(String p) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String t = sc.next();
            String p = sc.next();

            Solution solution = new Solution();
            int[] result = solution.findOccurrences(p, t);

            if (result.length == 0) {
                System.out.println("-1");
            } else {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < result.length; i++) {
                    if (i > 0) sb.append(' ');
                    sb.append(result[i]);
                }
                System.out.println(sb.toString());
            }
        }
        sc.close();
    }
}
```

### Python

```python
def compute_prefix_function(p: str) -> list[int]:
    return []
def find_occurrences(p: str, t: str) -> list[int]:
    return []
def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    t = input_data[0]
    p = input_data[1]
    result = find_occurrences(p, t)
    if not result:
        print("-1")
    else:
        print(*(result))

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
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, p;
    if (cin >> t >> p) {
        Solution solution;
        vector<int> result = solution.findOccurrences(p, t);
        if (result.empty()) {
            cout << "-1\n";
        } else {
            for (int i = 0; i < (int)result.size(); i++) {
                if (i > 0) cout << " ";
                cout << result[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findOccurrences(p, t) {
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
  const t = data[0];
  const p = data[1];
  const solution = new Solution();
  const result = solution.findOccurrences(p, t);
  if (result.length === 0) {
    console.log("-1");
  } else {
    console.log(result.join(" "));
  }
});
```

