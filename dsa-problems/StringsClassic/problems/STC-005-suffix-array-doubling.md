---
problem_id: STC_SUFFIX_ARRAY_DOUBLING__3726
display_id: STC-005
slug: suffix-array-doubling
title: "Suffix Array (Doubling) Construction"
difficulty: Medium
difficulty_score: 48
topics:
  - Strings
  - Suffix Array
  - Sorting
tags:
  - strings
  - suffix-array
  - doubling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-005: Suffix Array (Doubling) Construction

## Problem Statement

Given a string `s`, build its suffix array using the O(n log n) doubling algorithm. Output the starting indices of suffixes in lexicographic order.

![Problem Illustration](../images/STC-005/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: `n` integers, the suffix array indices

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
cababa
```

**Output:**

```
5 3 1 4 2 0
```

**Explanation:**

The suffixes in order are: a, aba, ababa, ba, baba, cababa.

![Example Visualization](../images/STC-005/example-1.png)

## Notes

- Doubling sorts by pairs of ranks (2^k length)
- Use counting sort or std::sort on tuples
- Output indices are 0-based
- Time complexity: O(n log n)

## Related Topics

Suffix Array, Sorting, String Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] suffixArray(String s) {
        // Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            int[] sa = solution.suffixArray(s);

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < sa.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(sa[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from typing import List

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return

    solution = Solution()
    sa = solution.suffix_array(s)
    print(*(sa))

class Solution:
    def suffix_array(self, s: str) -> List[int]:
        # Implement here
        return []

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> suffixArray(string s) {
        // Implement here
        return {};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        Solution sol;
        vector<int> sa = sol.suffixArray(s);
        for (int i = 0; i < sa.size(); i++) {
            cout << sa[i] << (i == sa.size() - 1 ? "" : " ");
        }
        cout << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  suffixArray(s) {
    // Implement here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const s = line.trim();
  if (!s) return;

  const sol = new Solution();
  console.log(sol.suffixArray(s).join(" "));
});
```
