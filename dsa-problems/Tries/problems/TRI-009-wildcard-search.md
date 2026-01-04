---
problem_id: TRI_WILDCARD_SEARCH__5672
display_id: TRI-009
slug: wildcard-search
title: "Wildcard Search"
difficulty: Medium
difficulty_score: 52
topics:
  - Trie
  - String
  - Recursion
  - Backtracking
tags:
  - trie
  - pattern-matching
  - wildcards
  - dfs
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-009: Wildcard Search

## Problem Statement

Implement search on a trie with wildcard pattern matching. The pattern may contain:

- `?` matches any single character
- `*` matches any sequence of characters (including empty)

Return `true` if any word in the trie matches the pattern.

![Problem Illustration](../images/TRI-009/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: lowercase words to insert into trie
- Last line: pattern string (may contain lowercase letters, `?`, and `*`)

## Output Format

Return `true` if any word matches the pattern, `false` otherwise.

## Constraints

- `1 <= n <= 10^5` (total words)
- `1 <= |word| <= 30` (word length)
- `1 <= |pattern| <= 30` (pattern length)
- Words contain only lowercase English letters
- Pattern contains lowercase letters, `?`, and `*`

## Example 1

**Input:**

```
3
code
coder
codec
co*e
```

**Output:**

```
true
```

**Explanation:**

Pattern `co*e`:

- `*` can match "d" → `code` matches ✓
- `*` can match "dec" → `codec` matches ✓

![Example Visualization](../images/TRI-009/example-1.png)

## Example 2

**Input:**

```
4
hello
help
helper
helpful
hel?
```

**Output:**

```
true
```

**Explanation:**

Pattern `hel?`:

- `?` matches 'l' → `hell` (not in trie) ✗
- `?` matches 'p' → `help` matches ✓

## Notes

- `?` matches exactly one character
- `*` matches zero or more characters
- Use DFS/backtracking to explore all possibilities
- Early termination when match is found

## Related Topics

Trie, String, Recursion, Backtracking, Pattern Matching

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void insertWord(String word) {
        // Implement here
    }

    public boolean search(String pattern) {
        // Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        sc.nextLine(); // consume newline

        Solution solution = new Solution();
        for (int i = 0; i < n; i++) {
            if (sc.hasNextLine()) {
                solution.insertWord(sc.nextLine().trim());
            }
        }

        if (sc.hasNextLine()) {
            String pattern = sc.nextLine().trim();
            boolean result = solution.search(pattern);
            System.out.println(result);
        }
    }
}
```

### Python

```python
class Solution:
    def insert_word(self, word: str):
        # Implement here
        pass

    def search(self, pattern: str) -> bool:
        # Implement here
        return False

def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])
    solution = Solution()
    for i in range(1, n + 1):
        solution.insert_word(input_data[i].strip())

    pattern = input_data[n + 1].strip() if len(input_data) > n + 1 else ""
    result = solution.search(pattern)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void insertWord(const string& word) {
        // Implement here
    }

    bool search(const string& pattern) {
        // Implement here
        return false;
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    cin.ignore();

    Solution solution;
    for (int i = 0; i < n; i++) {
        string word;
        getline(cin, word);
        solution.insertWord(word);
    }

    string pattern;
    getline(cin, pattern);

    bool result = solution.search(pattern);
    cout << (result ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  insertWord(word) {
    // Implement here
  }

  search(pattern) {
    // Implement here
    return false;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  if (lines.length === 0) return;
  const n = parseInt(lines[0]);

  const solution = new Solution();
  for (let i = 1; i <= n; i++) {
    solution.insertWord(lines[i].trim());
  }

  const pattern = lines[n + 1] ? lines[n + 1].trim() : "";
  const result = solution.search(pattern);

  console.log(result ? "true" : "false");
});
```
