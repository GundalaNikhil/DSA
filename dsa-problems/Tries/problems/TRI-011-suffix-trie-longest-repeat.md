---
problem_id: TRI_SUFFIX_LONGEST_REPEAT__3945
display_id: TRI-011
slug: suffix-trie-longest-repeat
title: "Suffix Trie Longest Repeat"
difficulty: Medium
difficulty_score: 58
topics:
  - Trie
  - String
  - Suffix Structures
tags:
  - trie
  - suffix-trie
  - longest-repeat
  - string-algorithms
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-011: Suffix Trie Longest Repeat

## Problem Statement

Build a suffix trie (or use suffix array alternative) to find the length of the longest repeated substring in string `s`.

![Problem Illustration](../images/TRI-011/problem-illustration.png)

## Input Format

- Single line: string `s` (lowercase letters)

## Output Format

Return an integer representing the length of the longest repeated substring.

## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
banana
```

**Output:**

```
3
```

**Explanation:**

"ana" appears twice (at positions 1-3 and 3-5), length = 3.

![Example Visualization](../images/TRI-011/example-1.png)

## Notes

- A repeated substring must appear at least twice
- Return 0 if no substring repeats
- Overlapping occurrences count (e.g., "ana" in "banana")

## Related Topics

Trie, Suffix Structures, String Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int longestRepeatedSubstring(String s) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        String s = sc.nextLine().trim();

        Solution solution = new Solution();
        int result = solution.longestRepeatedSubstring(s);
        System.out.println(result);
    }
}
```

### Python

```python
class Solution:
    def longest_repeated_substring(self, s: str) -> int:
        # Implement here
        return 0

def main():
    import sys
    s = sys.stdin.read().strip()
    if not s:
        return

    solution = Solution()
    result = solution.longest_repeated_substring(s)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int longestRepeatedSubstring(const string& s) {
        // Implement here
        return 0;
    }
};

int main() {
    string s;
    if (!getline(cin, s)) return 0;

    Solution solution;
    int result = solution.longestRepeatedSubstring(s);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestRepeatedSubstring(s) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const solution = new Solution();
  const result = solution.longestRepeatedSubstring(line.trim());
  console.log(result);
});
```
