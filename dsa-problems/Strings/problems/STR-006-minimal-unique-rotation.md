---
problem_id: STR_MINIMAL_UNIQUE_ROTATION__1006
display_id: STR-006
slug: minimal-unique-rotation
title: "Minimal Unique Rotation"
difficulty: Medium
difficulty_score: 42
topics:
  - String Manipulation
  - Booth Algorithm
  - Rotation
tags:
  - circular-string
  - lexicographic
  - minimal-rotation
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-006: Minimal Unique Rotation

## Problem Statement

Given a string `s`, find its lexicographically smallest rotation that is NOT equal to the original string. If all rotations are equal (all characters identical), return the original string.

A rotation is obtained by moving characters from the beginning to the end.

## Input Format

- A single string `s` (1 ≤ |s| ≤ 10^5)

## Output Format

- A single string representing the smallest unique rotation

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
bba
```

**Output:**

```
abb
```

**Explanation:**

- Rotations: "bba" (original), "bab", "abb"
- Excluding original: "bab", "abb"
- Lexicographically smallest: "abb"

## Example 2

**Input:**

```
aaa
```

**Output:**

```
aaa
```

**Explanation:**

- All rotations are "aaa" (all equal)
- Return original

## Notes

- Use Booth's algorithm to find minimal rotation in O(n)
- Check if minimal equals original
- Booth's algorithm uses doubled string trick

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String minimalUniqueRotation(String s) {
        // Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution sol = new Solution();
            System.out.println(sol.minimalUniqueRotation(s));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    solution = Solution()
    print(solution.minimal_unique_rotation(s))

class Solution:
    def minimal_unique_rotation(self, s: str) -> str:
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
    string minimalUniqueRotation(string s) {
        // Implement here
        return "";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        Solution sol;
        cout << sol.minimalUniqueRotation(s) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimalUniqueRotation(s) {
    // Implement here
    return "";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const s = line.trim();
  if (s) {
    const sol = new Solution();
    console.log(sol.minimalUniqueRotation(s));
  }
});
```
