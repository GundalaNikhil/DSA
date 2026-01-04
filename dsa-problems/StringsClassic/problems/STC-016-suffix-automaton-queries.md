---
problem_id: STC_SUFFIX_AUTOMATON_QUERIES__9036
display_id: STC-016
slug: suffix-automaton-queries
title: "Suffix Automaton Substring Queries"
difficulty: Medium
difficulty_score: 62
topics:
  - Strings
  - Suffix Automaton
  - Counting
tags:
  - strings
  - suffix-automaton
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-016: Suffix Automaton Substring Queries

## Problem Statement

Build a suffix automaton for a string `s`. For each query string `p`, output how many times `p` occurs as a substring of `s`.

If `p` is not a substring, output 0.

![Problem Illustration](../images/STC-016/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q`, number of queries
- Next `q` lines: a query string `p`

## Output Format

- Print `q` lines, each the occurrence count for the query

## Constraints

- `1 <= |s| <= 100000`
- `1 <= q <= 100000`
- Sum of query lengths `<= 200000`
- Strings contain lowercase English letters

## Example

**Input:**

```
ababa
2
aba
baa
```

**Output:**

```
2
0
```

**Explanation:**

"aba" occurs twice in "ababa" (positions 0 and 2). "baa" does not occur.

![Example Visualization](../images/STC-016/example-1.png)

## Notes

- After building the automaton, propagate end counts in order of state length.
- Each query is answered by walking transitions; the terminal state's count is the answer.
- Time complexity: O(|s| + total query length) after preprocessing.
- Use 64-bit integers for counts if needed.

## Related Topics

Suffix Automaton, Substring Queries, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] countOccurrences(String s, String[] queries) {
        // Implement here
        return new int[queries.length];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        if (!sc.hasNextInt()) return;
        int q = sc.nextInt();
        String[] queries = new String[q];
        for (int i = 0; i < q; i++) queries[i] = sc.next();

        Solution solution = new Solution();
        int[] ans = solution.countOccurrences(s, queries);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.length; i++) {
            sb.append(ans[i]);
            if (i + 1 < ans.length) sb.append('\n');
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]
    q = int(input_data[1])
    queries = input_data[2:2+q]

    solution = Solution()
    ans = solution.count_occurrences(s, queries)
    for a in ans:
        print(a)

class Solution:
    def count_occurrences(self, s: str, queries: list) -> list:
        # Implement here
        return [0] * len(queries)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> countOccurrences(string s, const vector<string>& queries) {
        // Implement here
        return vector<int>(queries.size(), 0);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int q;
    if (cin >> s >> q) {
        vector<string> queries(q);
        for (int i = 0; i < q; i++) cin >> queries[i];

        Solution sol;
        vector<int> ans = sol.countOccurrences(s, queries);
        for (int a : ans) {
            cout << a << "\n";
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countOccurrences(s, queries) {
    // Implement here
    return new Array(queries.length).fill(0);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 2) return;
  const s = input[0];
  const q = parseInt(input[1]);
  const queries = input.slice(2, 2 + q);

  const sol = new Solution();
  console.log(sol.countOccurrences(s, queries).join("\n"));
});
```
