---
problem_id: STR_RUN_LENGTH_DECODE_CAP__1013
display_id: STR-013
slug: run-length-decode-cap
title: "Run-Length Decode with Cap"
difficulty: Medium
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

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String decodeWithCap(String s, int cap) {
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
                int cap = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.decodeWithCap(s, cap));
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
    cap = int(input_data[1])
    solution = Solution()
    print(solution.decode_with_cap(s, cap))

class Solution:
    def decode_with_cap(self, s: str, cap: int) -> str:
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
    string decodeWithCap(string s, int cap) {
        // Implement here
        return "";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int cap;
    if (cin >> s >> cap) {
        Solution sol;
        cout << sol.decodeWithCap(s, cap) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  decodeWithCap(s, cap) {
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
    const cap = parseInt(input[1]);
    const sol = new Solution();
    console.log(sol.decodeWithCap(s, cap));
  }
});
```
