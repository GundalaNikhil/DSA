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
    public String compress(String s, int w) {
        // Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (sc.hasNextInt()) {
                int w = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.compress(s, w));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    s = input_data[0]
    w = int(input_data[1])
    solution = Solution()
    print(solution.compress(s, w))

class Solution:
    def compress(self, s: str, w: int) -> str:
        # Implement here
        return ""

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string compress(string s, int w) {
        // Implement here
        return "";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int w;
    if (cin >> s >> w) {
        Solution sol;
        cout << sol.compress(s, w) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  compress(s, w) {
    // Implement here
    return "";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length >= 2) {
    const s = input[0];
    const w = parseInt(input[1]);
    const sol = new Solution();
    console.log(sol.compress(s, w));
  }
});
```
