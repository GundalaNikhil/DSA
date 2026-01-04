---
problem_id: STC_LCP_ARRAY_KASAI__6109
display_id: STC-006
slug: lcp-array-kasai
title: "LCP Array (Kasai)"
difficulty: Medium
difficulty_score: 46
topics:
  - Strings
  - Suffix Array
  - LCP
tags:
  - strings
  - lcp
  - kasai
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-006: LCP Array (Kasai)

## Problem Statement

Given a string `s` and its suffix array, compute the LCP array where `lcp[i]` is the longest common prefix length of the suffixes at `sa[i]` and `sa[i+1]`.

![Problem Illustration](../images/STC-006/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `n` (length of `s`)
- Third line: `n` space-separated integers (suffix array)

## Output Format

- Single line: `n-1` integers (LCP array)

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
cababa
6
5 3 1 4 2 0
```

**Output:**

```
1 3 0 2 0
```

**Explanation:**

Adjacent suffix pairs share prefixes of lengths 1, 3, 0, 2, 0.

![Example Visualization](../images/STC-006/example-1.png)

## Notes

- Use Kasai's algorithm for O(n)
- Build inverse rank array from suffix array
- LCP array length is `n-1`
- Output values are 0-based lengths

## Related Topics

Kasai Algorithm, Suffix Array, LCP

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] lcpArray(String s, int[] sa) {
        // Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (sc.hasNextInt()) {
                int n = sc.nextInt();
                int[] sa = new int[n];
                for (int i = 0; i < n; i++) sa[i] = sc.nextInt();

                Solution solution = new Solution();
                int[] lcp = solution.lcpArray(s, sa);

                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < lcp.length; i++) {
                    if (i > 0) sb.append(' ');
                    sb.append(lcp[i]);
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
from typing import List

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]
    n = int(input_data[1])
    sa = [int(input_data[i]) for i in range(2, 2 + n)]

    solution = Solution()
    lcp = solution.lcp_array(s, sa)
    print(*(lcp))

class Solution:
    def lcp_array(self, s: str, sa: List[int]) -> List[int]:
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
    vector<int> lcpArray(string s, const vector<int>& sa) {
        // Implement here
        return {};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int n;
    if (cin >> s >> n) {
        vector<int> sa(n);
        for (int i = 0; i < n; i++) cin >> sa[i];

        Solution sol;
        vector<int> lcp = sol.lcpArray(s, sa);
        for (int i = 0; i < lcp.size(); i++) {
            cout << lcp[i] << (i == lcp.size() - 1 ? "" : " ");
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
  lcpArray(s, sa) {
    // Implement here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 2) return;
  const s = input[0];
  const n = parseInt(input[1]);
  const sa = input.slice(2, 2 + n).map((x) => parseInt(x));

  const sol = new Solution();
  console.log(sol.lcpArray(s, sa).join(" "));
});
```
