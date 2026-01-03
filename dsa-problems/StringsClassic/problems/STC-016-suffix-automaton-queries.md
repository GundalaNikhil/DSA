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
    public long[] countOccurrences(String s, String[] queries) {
        //Implement here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        int q = sc.nextInt();
        String[] queries = new String[q];
        for (int i = 0; i < q; i++) {
            queries[i] = sc.next();
        }

        Solution solution = new Solution();
        long[] ans = solution.countOccurrences(s, queries);
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
sys.setrecursionlimit(200000)

class State:
    def __init__(self, length=0, link=-1):
        self.len = length
        self.link = link
        self.next = {}
        self.cnt = 0

def count_occurrences(s: str, queries: list[str]) -> list[int]:
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    q = int(input_data[1])
    queries = input_data[2:2 + q]
    
    ans = count_occurrences(s, queries)
    sys.stdout.write("\n".join(str(x) for x in ans) + "\n")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct State {
    int len, link;
    map<char, int> next;
    long long cnt = 0;
};

class Solution {
public:
    vector<long long> countOccurrences(const string& s, const vector<string>& queries) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        int q;
        cin >> q;
        vector<string> queries(q);
        for (int i = 0; i < q; i++) {
            cin >> queries[i];
        }
        
        Solution solution;
        vector<long long> ans = solution.countOccurrences(s, queries);
        for (long long x : ans) cout << x << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class State {
  constructor(len = 0, link = -1) {
    this.len = len;
    this.link = link;
    this.next = new Map();
    this.cnt = 0n;
  }
}

class Solution {
  countOccurrences(s, queries) {
    //Implement here
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
  const q = parseInt(data[1], 10);
  const queries = data.slice(2, 2 + q);
  const solution = new Solution();
  const ans = solution.countOccurrences(s, queries);
  console.log(ans.join("\n"));
});
```

