---
problem_id: STC_KMP_PREFIX_FUNCTION__5824
display_id: STC-001
slug: kmp-prefix-function
title: "Prefix Function (KMP) Construction"
difficulty: Easy
difficulty_score: 22
topics:
  - Strings
  - KMP
  - Prefix Function
tags:
  - strings
  - kmp
  - prefix-function
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-001: Prefix Function (KMP) Construction

## Problem Statement

Given a string `s`, compute its prefix function array `pi`, where `pi[i]` is the length of the longest proper prefix of `s[0..i]` that is also a suffix of `s[0..i]`.

![Problem Illustration](../images/STC-001/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: `n` integers `pi[0..n-1]`, space-separated

## Constraints

- `1 <= |s| <= 200000`
- `s` contains lowercase English letters

## Example

**Input:**

```
ababa
```

**Output:**

```
0 0 1 2 3
```

**Explanation:**

The prefix function grows because the string repeats the pattern "ab".

![Example Visualization](../images/STC-001/example-1.png)

## Notes

- `pi[0] = 0`
- Use the standard linear KMP prefix computation
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

KMP, Prefix Function, String Matching

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] prefixFunction(String s) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            int[] pi = solution.prefixFunction(s);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < pi.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(pi[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
def prefix_function(s: str) -> list[int]:
    return []
def main():
    import sys
    sys.setrecursionlimit(200000)
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    s = input_data[0]
    pi = prefix_function(s)
    print(*(pi))

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
    vector<int> prefixFunction(const string& s) {
        return {};
    }
};

int main() {
    // Fast I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        vector<int> pi = solution.prefixFunction(s);
        
        for (int i = 0; i < (int)pi.size(); i++) {
            if (i > 0) cout << " ";
            cout << pi[i];
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
  prefixFunction(s) {
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
  const pi = solution.prefixFunction(s);
  console.log(pi.join(" "));
});
```

