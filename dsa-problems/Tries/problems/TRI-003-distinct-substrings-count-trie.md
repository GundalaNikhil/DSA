---
problem_id: TRI_DISTINCT_SUBS__4254
display_id: TRI-003
slug: distinct-substrings-count-trie
title: "Distinct Substrings Count via Trie"
difficulty: Medium
difficulty_score: 45
topics:
  - Trie
  - String
  - Suffix Trie
  - Substring
tags:
  - trie
  - string
  - suffix-trie
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Distinct Substrings Count via Trie

## Problem Statement

Given a string `s`, count the number of distinct non-empty substrings using a suffix trie data structure.

![Problem Illustration](../images/TRI-003/problem-illustration.png)

## Input Format

- Single line: String `s` consisting of lowercase English letters

## Output Format

Print a single integer representing the count of distinct non-empty substrings.

## Constraints

- 1 ≤ |s| ≤ 10^5

## Examples

### Example 1

**Input:**

```
aaa
```

**Output:**

```
3
```

**Explanation:**

The distinct substrings are:

- "a"
- "aa"
- "aaa"

Total count: 3

![Example 1 Visualization](../images/TRI-003/example-1.png)

### Example 2

**Input:**

```
abc
```

**Output:**

```
6
```

**Explanation:**

The distinct substrings are:

- "a", "ab", "abc"
- "b", "bc"
- "c"

Total count: 6

## Notes

- Use a suffix trie where each node represents a unique substring
- Count all nodes in the trie (excluding the root)
- Empty string is not counted as a substring

## Related Topics

Trie, String, Suffix Trie, Substring Analysis

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countDistinctSubstrings(String s) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        
        Solution sol = new Solution();
        System.out.println(sol.countDistinctSubstrings(s));
        sc.close();
    }
}
```

### Python

```python
import sys

def count_distinct_naive(s):
    # Implementation here
    return None

def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    s = input_data
    result = count_distinct_naive(s)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    int countDistinctSubstrings(const string& s) {
        // Implementation here
        return {};
    }
};

int main() {
    string s;
    getline(cin, s);

    Solution solution;
    int result = solution.countDistinctSubstrings(s);

    cout << result << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  constructor() {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

rl.on('line', (line) => {
    const s = line.trim();
    const sol = new Solution();
    console.log(sol.countDistinctSubstrings(s));
    rl.close();
});
```
