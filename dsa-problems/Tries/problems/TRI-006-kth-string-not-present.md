---
problem_id: TRI_KTH_MISSING__4257
display_id: TRI-006
slug: kth-string-not-present
title: "Lexicographic k-th String Not Present"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Combinatorics
  - DFS
tags:
  - trie
  - string
  - combinatorics
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Lexicographic k-th String Not Present

## Problem Statement

Given a trie of inserted lowercase strings, find the k-th lexicographically smallest string of length up to `L` that is NOT present in the trie.

![Problem Illustration](../images/TRI-006/problem-illustration.png)

## Input Format

- First line: Three integers `n`, `L`, `k` (number of strings, max length, kth position)
- Next `n` lines: Each contains a lowercase string already inserted in the trie

## Output Format

Print the k-th missing string of length ≤ L in lexicographic order, or an empty string if k exceeds the total missing count.

## Constraints

- 0 ≤ n ≤ 10^5
- 1 ≤ L ≤ 6
- 1 ≤ k ≤ 10^9
- All strings consist of lowercase English letters (a-z)

## Examples

### Example 1

**Input:**

```
2 2 1
a
b
```

**Output:**

```
aa
```

**Explanation:**

Inserted: "a", "b"
Missing strings of length ≤ 2 in order:

1. "aa" ← answer
2. "ab"
3. "ac"
   ...

![Example 1 Visualization](../images/TRI-006/example-1.png)

## Notes

- Strings can end at any depth from 1 to L
- Empty string not counted
- Lexicographic order: a < aa < ab < ... < z < za < ...
- Use DFS to count missing strings efficiently

## Related Topics

Trie, String, Combinatorics, DFS, Missing Elements

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void main(String[] args) {
        // Implementation here
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read all tokens
        int n = sc.nextInt();
        int L = sc.nextInt();
        int k = sc.nextInt();

        Set<String> inserted = new HashSet<>();
        for (int i = 0; i < n; i++) {
            if (sc.hasNext()) {
                inserted.add(sc.next());
            }
        }

        List<String> allStrings = new ArrayList<>();

        // Order: a, aa, ab, ..., az, b, ba, bb, ..., bz, c, ...
        for (char c = 'a'; c <= 'z'; c++) {
            // Add single character if not inserted and L >= 1
            if (L >= 1 && !inserted.contains(String.valueOf(c))) {
                allStrings.add(String.valueOf(c));
            }

            // Add all multi-char strings starting with this char
            for (int length = 2; length <= L; length++) {
                generateCombinations(String.valueOf(c), length - 1, inserted, allStrings);
            }
        }

        System.out.println(k <= allStrings.size() ? allStrings.get(k - 1) : "");
        sc.close();
    }

    static void generateCombinations(String prefix, int remaining, Set<String> inserted, List<String> result) {
        if (remaining == 0) {
            if (!inserted.contains(prefix)) {
                result.add(prefix);
            }
            return;
        }

        for (char c = 'a'; c <= 'z'; c++) {
            generateCombinations(prefix + c, remaining - 1, inserted, result);
        }
    }
}
```

### Python

```python
from itertools import product

def all_combinations_of_length(length):
    # Implementation here
    return None

def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')

    n, L, k = map(int, input_data[0].split())
    inserted = set()
    for i in range(1, n + 1):
        inserted.add(input_data[i])

    result = naive(inserted, L, k)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string kthMissingString(const vector<string>& insertedList, int L, int k) {
        // Implementation here
        return {};
    }
};

int main() {
    int n, L, k;
    if (!(cin >> n >> L >> k)) {
        return 0;
    }

    vector<string> inserted(n);
    for (int i = 0; i < n; i++) {
        cin >> inserted[i];
    }

    Solution solution;
    string result = solution.kthMissingString(inserted, L, k);

    cout << result << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  kthMissingString(n, maxLen, k, inserted) {
    // Implementation here
    return "";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  if (lines.length === 0) return;
  const [n, maxLen, k] = lines[0].split(" ").map(Number);
  const inserted = new Set();
  for (let i = 1; i <= n; i++) inserted.add(lines[i]);

  const solution = new Solution();
  console.log(solution.kthMissingString(n, maxLen, k, inserted));
});
```
