---
problem_id: HSH_MINIMAL_ROTATION_HASH__4729
display_id: HSH-006
slug: minimal-rotation-hash
title: "Minimal Rotation via Hash Compare"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Rotation
tags:
  - hashing
  - rotation
  - lexicographic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-006: Minimal Rotation via Hash Compare

## Problem Statement

Given a string `s`, find its lexicographically smallest rotation using hashing and binary search for comparison.

A rotation of a string is obtained by moving some prefix to the end. For example, rotations of "abc" are: "abc", "bca", "cab".

![Problem Illustration](../images/HSH-006/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single line: lexicographically smallest rotation of `s`

## Constraints

- `1 <= |s| <= 2*10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
bba
```

**Output:**

```
abb
```

**Explanation:**

String: "bba"

All rotations:

- "bba" (start at index 0)
- "bab" (start at index 1)
- "abb" (start at index 2) ← lexicographically smallest

Output: "abb"

![Example Visualization](../images/HSH-006/example-1.png)

## Notes

- Concatenate s with itself to simulate all rotations
- Use hashing with binary search to compare rotations efficiently
- For each starting position, determine lexicographic order using hash comparison
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

String Rotation, Hashing, Binary Search, Lexicographic Order

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String minimalRotation(String s) {
        // Implementation here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.minimalRotation(s));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def minimal_rotation(self, s: str) -> str:
        # Implementation here
        return ""

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(minimal_rotation(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string minimalRotation(string s) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.minimalRotation(s) << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimalRotation(s) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];

  const solution = new Solution();
  console.log(solution.minimalRotation(s));
});
```
