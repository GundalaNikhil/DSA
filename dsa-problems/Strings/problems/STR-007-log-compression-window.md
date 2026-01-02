---
problem_id: STR_LOG_COMPRESSION_WINDOW__1007
display_id: STR-007
slug: log-compression-window
title: "Log Compression With Window"
difficulty: Medium
difficulty_score: 35
topics:
  - String Manipulation
  - Run-Length Encoding
tags:
  - compression
  - threshold-based
  - encoding
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-007: Log Compression With Window

## Problem Statement

Given a string `s` and an integer `w` (window threshold), compress the string by replacing runs of consecutive identical characters of length ≥ `w` with the character followed by its count. Runs shorter than `w` remain unchanged.

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 2 × 10^5)
- Second line: Integer `w` (1 ≤ w ≤ 10^5)

## Output Format

- A single string representing the compressed version

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `1 ≤ w ≤ 10^5`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
aaabbbbcc
3
```

**Output:**

```
a3b4cc
```

**Explanation:**

- "aaa" (length 3 ≥ 3) → "a3"
- "bbbb" (length 4 ≥ 3) → "b4"
- "cc" (length 2 < 3) → "cc" (unchanged)

## Example 2

**Input:**

```
abc
2
```

**Output:**

```
abc
```

**Explanation:**

- All runs have length 1 < 2
- No compression applied

## Notes

- Single-pass algorithm with O(n) time
- Track consecutive character counts
- StringBuilder for efficient string building

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String compressWithWindow(String s, int w) {
        // Implementation here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int w = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.compressWithWindow(s, w));
        sc.close();
    }
}
```

### Python

```python
import sys

def compress_with_window(s: str, w: int) -> str:
    # Implementation here
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
            w = int(parts[1])
            print(compress_with_window(s, w))
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
#include <algorithm>

using namespace std;

class Solution {
public:
    string compressWithWindow(string s, int w) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int w; cin >> w;
    Solution sol;
    cout << sol.compressWithWindow(s, w) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  compressWithWindow(s, w) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const w = parseInt(tokens[ptr++]);
    console.log(new Solution().compressWithWindow(s, w));
});
```
