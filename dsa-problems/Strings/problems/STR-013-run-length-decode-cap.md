---
problem_id: STR_RUN_LENGTH_DECODE_CAP__1013
display_id: STR-013
slug: run-length-decode-cap
title: "Run-Length Decode with Cap"
difficulty: Easy-Medium
difficulty_score: 30
topics:
  - String Manipulation
  - Encoding
  - Parsing
tags:
  - run-length-decoding
  - capping
  - string-parsing
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-013: Run-Length Decode with Cap

## Problem Statement

Given a run-length encoded string (format: "char+count") and an integer `cap`, decode the string but limit any run exceeding `cap` to exactly `cap` occurrences.

## Input Format

- First line: Encoded string `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `cap` (1 ≤ cap ≤ 10^4)

## Output Format

- A single string representing the decoded result

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ cap ≤ 10^4`
- Encoded format: character followed by count (digits)

## Example 1

**Input:**

```
a10b2
3
```

**Output:**

```
aaabb
```

**Explanation:**

- "a10" → "aaa" (capped from 10 to 3)
- "b2" → "bb" (no cap needed)

## Example 2

**Input:**

```
x100y50
5
```

**Output:**

```
xxxxxyyyyy
```

**Explanation:**

- Both runs capped to 5

## Notes

- Parse character and following digits
- Apply min(count, cap) for each run
- O(n + output_size) time complexity

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String decodeWithCap(String s, int cap) {
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int cap = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.decodeWithCap(s, cap));
        sc.close();
    }
}
```

### Python

```python
def decode_with_cap(s: str, cap: int) -> str:
    return ""
def main():
    import sys

    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
        
    parts = input_data.split()
    if len(parts) >= 2:
        s = parts[0]
        try:
            cap = int(parts[1])
            print(decode_with_cap(s, cap))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
class Solution {
public:
    string decodeWithCap(string s, int cap) {
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int cap; cin >> cap;
    Solution sol;
    cout << sol.decodeWithCap(s, cap) << endl;
    return 0;
}
```

### JavaScript

```javascript
function decodeWithCap(s, cap) {
    return 0;
  }

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const cap = parseInt(tokens[ptr++]);
    console.log(decodeWithCap(s, cap));
});
```

