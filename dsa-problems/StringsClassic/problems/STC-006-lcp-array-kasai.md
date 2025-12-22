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
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
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
        sc.close();
    }
}
```

### Python

```python
def lcp_array(s: str, sa: list[int]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    s = next(it)
    n = int(next(it))
    sa = [int(next(it)) for _ in range(n)]

    lcp = lcp_array(s, sa)
    print(" ".join(str(x) for x in lcp))

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
    vector<int> lcpArray(const string& s, const vector<int>& sa) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int n;
    cin >> n;
    vector<int> sa(n);
    for (int i = 0; i < n; i++) cin >> sa[i];

    Solution solution;
    vector<int> lcp = solution.lcpArray(s, sa);
    for (int i = 0; i < (int)lcp.size(); i++) {
        if (i) cout << ' ';
        cout << lcp[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  lcpArray(s, sa) {
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
  let idx = 0;
  const s = data[idx++];
  const n = parseInt(data[idx++], 10);
  const sa = [];
  for (let i = 0; i < n; i++) sa.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const lcp = solution.lcpArray(s, sa);
  console.log(lcp.join(" "));
});
```
