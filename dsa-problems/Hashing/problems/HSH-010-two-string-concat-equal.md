---
problem_id: HSH_TWO_STRING_CONCAT_EQUAL__4156
display_id: HSH-010
slug: two-string-concat-equal
title: "Two-String Concatenation Equal Check"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - String Algorithms
tags:
  - hashing
  - concatenation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-010: Two-String Concatenation Equal Check

## Problem Statement

Given four strings `a`, `b`, `c`, `d`, determine if `a + b == c + d` (concatenation) without explicitly creating the concatenated strings, using polynomial hashing.

![Problem Illustration](../images/HSH-010/problem-illustration.png)

## Input Format

- Four lines, each containing a string: `a`, `b`, `c`, `d`

## Output Format

- Single word: `true` or `false`

## Constraints

- `1 <= |a|, |b|, |c|, |d| <= 10^5`
- Strings contain only lowercase English letters

## Example

**Input:**

```
ab
cd
a
bcd
```

**Output:**

```
true
```

**Explanation:**

a + b = "ab" + "cd" = "abcd"
c + d = "a" + "bcd" = "abcd"

They are equal, so output is true.

![Example Visualization](../images/HSH-010/example-1.png)

## Notes

- Compute hash(a+b) as hash(a) \* B^|b| + hash(b)
- Compute hash(c+d) as hash(c) \* B^|d| + hash(d)
- Compare the two hashes
- Time complexity: O(|a| + |b| + |c| + |d|)
- Space complexity: O(1)

## Related Topics

Hashing, String Concatenation, Polynomial Hash

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public boolean checkConcatenationEqual(String a, String b, String c, String d) {
        //Implemention here
        return false;
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            lines.add(line);
        }
        if (lines.isEmpty()) return;
        while (lines.size() < 4) {
            lines.add("");
        }
        String a = lines.get(0);
        String b = lines.get(1);
        String c = lines.get(2);
        String d = lines.get(3);

        Solution solution = new Solution();
        boolean result = solution.checkConcatenationEqual(a, b, c, d);
        System.out.print(result ? "true" : "false");
    }
}
```

### Python

```python
import sys

def check_concatenation_equal(a, b, c, d):
    # //Implemention here
    return False

def main():
    lines = sys.stdin.read().split('\n')
    if not lines:
        return
    while len(lines) < 4:
        lines.append('')
    a = lines[0]
    b = lines[1]
    c = lines[2]
    d = lines[3]
    result = check_concatenation_equal(a, b, c, d)
    sys.stdout.write('true' if result else 'false')

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool check_concatenation_equal(const string& a, const string& b, const string& c, const string& d) {
    //Implemention here
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> lines;
    string line;
    while (getline(cin, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        lines.push_back(line);
    }
    if (lines.empty()) return 0;
    while (lines.size() < 4) {
        lines.push_back("");
    }
    string a = lines[0];
    string b = lines[1];
    string c = lines[2];
    string d = lines[3];

    bool result = check_concatenation_equal(a, b, c, d);
    cout << (result ? "true" : "false");
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function checkConcatenationEqual(a, b, c, d) {
  //Implemention here
  return false;
}

const raw = fs.readFileSync(0, "utf8");
if (raw.length === 0) {
  process.exit(0);
}
const lines = raw.replace(/\r/g, "").split(/\n/);
while (lines.length < 4) {
  lines.push("");
}
const a = lines[0];
const b = lines[1];
const c = lines[2];
const d = lines[3];
const result = checkConcatenationEqual(a, b, c, d);
process.stdout.write(result ? "true" : "false");
```

