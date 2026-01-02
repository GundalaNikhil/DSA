---
problem_id: STC_MINIMAL_ROTATION_SA__6042
display_id: STC-009
slug: minimal-rotation-sa
title: "Lexicographically Minimal Rotation (SA)"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
  - Suffix Array
  - Rotation
tags:
  - strings
  - suffix-array
  - rotation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-009: Lexicographically Minimal Rotation (SA)

## Problem Statement

Given a string `s`, consider all its cyclic rotations. Return the starting index (0-based) of the lexicographically smallest rotation. If multiple rotations are identical, return the smallest index.

![Problem Illustration](../images/STC-009/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single integer: index of the minimal rotation

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
bba
```

**Output:**

```
2
```

**Explanation:**

Rotations: index 0 -> "bba", index 1 -> "bab", index 2 -> "abb". The smallest is "abb" at index 2.

![Example Visualization](../images/STC-009/example-1.png)

## Notes

- Build suffix array for `s + s`
- The first suffix with start < n gives the answer
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Suffix Array, Rotations, String Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minimalRotationIndex(String s) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.minimalRotationIndex(s));
        }
        sc.close();
    }
}
```

### Python

```python
def minimal_rotation_index(s: str) -> int:
    return 0
def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(minimal_rotation_index(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimalRotationIndex(const string& s) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.minimalRotationIndex(s) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimalRotationIndex(s) {
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
  console.log(solution.minimalRotationIndex(s).toString());
});
```

