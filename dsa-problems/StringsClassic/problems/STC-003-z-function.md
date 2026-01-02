---
problem_id: STC_Z_FUNCTION__9307
display_id: STC-003
slug: z-function
title: "Z-Function Construction"
difficulty: Easy
difficulty_score: 24
topics:
  - Strings
  - Z-Algorithm
  - Prefix Matching
tags:
  - strings
  - z-function
  - prefix
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-003: Z-Function Construction

## Problem Statement

Given a string `s`, compute its Z-array. `Z[i]` is the length of the longest substring starting at `i` that matches the prefix of `s`. By convention, `Z[0] = |s|`.

![Problem Illustration](../images/STC-003/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: `n` integers `Z[0..n-1]`, space-separated

## Constraints

- `1 <= |s| <= 200000`
- `s` contains lowercase English letters

## Example

**Input:**

```
aabxaabx
```

**Output:**

```
8 1 0 0 4 1 0 0
```

**Explanation:**

The prefix matches at positions 1 and 4 with lengths 1 and 4.

![Example Visualization](../images/STC-003/example-1.png)

## Notes

- Use the linear Z-algorithm
- Maintain a window [l, r] of the current Z-box
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Z-Algorithm, String Matching, Prefixes

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] zFunction(String s) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            int[] z = solution.zFunction(s);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < z.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(z[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
def z_function(s: str) -> list[int]:
    return []
def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    z = z_function(s)
    print(*(z))

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
    vector<int> zFunction(const string& s) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        vector<int> z = solution.zFunction(s);
        for (int i = 0; i < (int)z.size(); i++) {
            if (i > 0) cout << " ";
            cout << z[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  zFunction(s) {
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
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  const z = solution.zFunction(s);
  console.log(z.join(" "));
});
```

