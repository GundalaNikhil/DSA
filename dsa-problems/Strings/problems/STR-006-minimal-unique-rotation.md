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
        // Implementation here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.useDelimiter("\\A").hasNext() ? sc.next() : "";
        s = s.trim();
        Solution sol = new Solution();
        System.out.println(sol.minimalUniqueRotation(s));
        sc.close();
    }
}
```

### Python

```python
import sys

def minimal_unique_rotation(s: str) -> str:
    # Implementation here
    return ""

def main():
    import sys


    # Read input string
    input_data = sys.stdin.read().strip()
    if not input_data:
        print("")
        return
        
    # Call solution
    result = minimal_unique_rotation(input_data)
    print(result)

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
    string minimalUniqueRotation(string s) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    while(!s.empty() && isspace(s.back())) s.pop_back();
    while(!s.empty() && isspace(s.front())) s.erase(0, 1);
    Solution sol;
    cout << sol.minimalUniqueRotation(s) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minimalUniqueRotation(s) {
    // Implementation here
    return null;
  }
}

// I/O handling
```
