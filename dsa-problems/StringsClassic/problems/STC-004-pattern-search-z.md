---
problem_id: STC_PATTERN_SEARCH_Z__4681
display_id: STC-004
slug: pattern-search-z
title: "Pattern Search With Z-Function"
difficulty: Easy
difficulty_score: 32
topics:
  - Strings
  - Z-Algorithm
  - Pattern Matching
tags:
  - strings
  - z-function
  - pattern-search
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-004: Pattern Search With Z-Function

## Problem Statement

Given a pattern `p` and text `t`, find all starting indices where `p` occurs in `t` using the Z-function on `p + '#' + t`.

Indices are 0-based and should be output in increasing order.

![Problem Illustration](../images/STC-004/problem-illustration.png)

## Input Format

- First line: pattern string `p`
- Second line: text string `t`

## Output Format

- Single line: space-separated indices of all occurrences
- If there are no occurrences, print an empty line

## Constraints

- `1 <= |p|, |t| <= 200000`
- Strings contain lowercase English letters

## Example

**Input:**

```
aa
aaa
```

**Output:**

```
0 1
```

**Explanation:**

The pattern "aa" occurs at indices 0 and 1.

![Example Visualization](../images/STC-004/example-1.png)

## Notes

- Use a delimiter `#` not appearing in the strings
- Compute Z on the concatenated string
- Match positions where `Z[i] == |p|`
- Time complexity: O(|p| + |t|)

## Related Topics

Z-Algorithm, Pattern Matching, String Search

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] findOccurrences(String p, String t) {
        // Implementation here
        return new int[0];
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
import sys

def find_occurrences(p: str, t: str) -> list[int]:
    # Implementation here
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
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findOccurrences(const string& p, const string& t) {
        // Implementation here
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
    // Implementation here
    return null;
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
