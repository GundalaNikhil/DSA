---
problem_id: HSH_PALINDROME_SUBSTRING_QUERIES__2639
display_id: HSH-004
slug: palindrome-substring-queries
title: "Palindrome Substring Queries"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Palindrome
  - String Algorithms
tags:
  - hashing
  - palindrome
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-004: Palindrome Substring Queries

## Problem Statement

Given a string `s` and `q` queries, answer whether substring `s[l..r]` is a palindrome using hash-based comparisons.

For each query `(l, r)`, determine if the substring from index `l` to `r` (inclusive, 0-indexed) reads the same forwards and backwards.

![Problem Illustration](../images/HSH-004/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of queries)
- Next `q` lines: two integers `l r` for each query

## Output Format

- `q` lines, each containing `true` or `false`

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= q <= 2*10^5`
- `0 <= l <= r < |s|`

## Example

**Input:**

```
abccba
3
0 5
1 4
2 3
```

**Output:**

```
true
false
true
```

**Explanation:**

String: "abccba"

Query 1: s[0..5] = "abccba" → palindrome → true
Query 2: s[1..4] = "bccb" → not a palindrome → false
Query 3: s[2..3] = "cc" → palindrome → true

![Example Visualization](../images/HSH-004/example-1.png)

## Notes

- Precompute forward and reverse polynomial hashes
- Compare hash of s[l..r] with hash of reverse(s[l..r])
- Use double hashing to minimize false positives
- Time complexity: O(n + q) with O(n) preprocessing
- Space complexity: O(n)

## Related Topics

Palindrome Detection, Hashing, Rolling Hash, String Reversal

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public List<Boolean> checkPalindromes(String s, List<int[]> queries) {
        //Implemention here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        String s = data[idx++];
        int q = Integer.parseInt(data[idx++]);
        List<int[]> queries = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            int l = Integer.parseInt(data[idx++]);
            int r = Integer.parseInt(data[idx++]);
            queries.add(new int[]{l, r});
        }

        Solution solution = new Solution();
        List<Boolean> result = solution.checkPalindromes(s, queries);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            out.append(result.get(i) ? "true" : "false");
            if (i + 1 < result.size()) out.append('\n');
        }
        System.out.print(out.toString());
    }
}
```

### Python

```python
import sys

def check_palindromes(s, queries):
    # //Implemention here
    return []

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    s = data[idx]
    idx += 1
    q = int(data[idx])
    idx += 1
    queries = []
    for _ in range(q):
        l = int(data[idx]);
        r = int(data[idx + 1]);
        idx += 2
        queries.append([l, r])
    result = check_palindromes(s, queries)
    out_lines = [('true' if ans else 'false') for ans in result]
    sys.stdout.write('\n'.join(out_lines))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <array>

using namespace std;

vector<bool> check_palindromes(const string& s, const vector<array<int, 2>>& queries) {
    //Implemention here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int q;
    if (!(cin >> q)) return 0;
    vector<array<int, 2>> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        queries.push_back({l, r});
    }

    vector<bool> result = check_palindromes(s, queries);
    for (size_t i = 0; i < result.size(); i++) {
        cout << (result[i] ? "true" : "false");
        if (i + 1 < result.size()) cout << '\n';
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function checkPalindromes(s, queries) {
  //Implemention here
  return [];
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/);
let idx = 0;
const s = data[idx++];
const q = parseInt(data[idx++], 10);
const queries = [];
for (let i = 0; i < q; i++) {
  const l = parseInt(data[idx++], 10);
  const r = parseInt(data[idx++], 10);
  queries.push([l, r]);
}
const result = checkPalindromes(s, queries);
const out = result.map(v => (v ? 'true' : 'false')).join('\n');
process.stdout.write(out);
```

