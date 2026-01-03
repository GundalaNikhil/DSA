---
problem_id: HSH_SUBSTRING_EQUALITY_QUERIES__5917
display_id: HSH-002
slug: substring-equality-queries
title: "Substring Equality Queries"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - Rolling Hash
  - String Matching
tags:
  - hashing
  - rolling-hash
  - substring
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-002: Substring Equality Queries

## Problem Statement

Given a string `s` and `q` queries, each query asks whether two substrings of `s` are equal.

Each query is specified as `(l1, r1, l2, r2)` where:

- First substring: `s[l1..r1]` (inclusive, 0-indexed)
- Second substring: `s[l2..r2]` (inclusive, 0-indexed)

For each query, output `true` if the two substrings are equal, `false` otherwise.

Use polynomial hashing with double hashing (two different moduli) to minimize collision probability.

![Problem Illustration](../images/HSH-002/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of queries)
- Next `q` lines: four integers `l1 r1 l2 r2` for each query

## Output Format

- `q` lines, each containing `true` or `false`

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= q <= 2*10^5`
- `0 <= l1 <= r1 < |s|`
- `0 <= l2 <= r2 < |s|`
- `r1 - l1 == r2 - l2` (substring lengths must match)

## Example

**Input:**

```
ababa
3
0 1 2 3
0 2 2 4
1 1 3 3
```

**Output:**

```
true
true
true
```

**Explanation:**

String: "ababa"

Query 1: s[0..1] = "ab", s[2..3] = "ab" → true
Query 2: s[0..2] = "aba", s[2..4] = "aba" → true
Query 3: s[1..1] = "b", s[3..3] = "b" → true

![Example Visualization](../images/HSH-002/example-1.png)

## Notes

- Precompute prefix hashes during initialization
- Use two different moduli for double hashing to reduce collision probability
- Hash comparison: O(1) per query after O(n) preprocessing
- Time complexity: O(n + q)
- Space complexity: O(n)

## Related Topics

Rolling Hash, String Matching, Substring Comparison, Double Hashing

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public List<Boolean> checkSubstringEquality(String s, List<int[]> queries) {
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
            int l1 = Integer.parseInt(data[idx++]);
            int r1 = Integer.parseInt(data[idx++]);
            int l2 = Integer.parseInt(data[idx++]);
            int r2 = Integer.parseInt(data[idx++]);
            queries.add(new int[]{l1, r1, l2, r2});
        }

        Solution solution = new Solution();
        List<Boolean> result = solution.checkSubstringEquality(s, queries);
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

def check_substring_equality(s, queries):
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
        l1 = int(data[idx]);
        r1 = int(data[idx + 1]);
        l2 = int(data[idx + 2]);
        r2 = int(data[idx + 3]);
        idx += 4
        queries.append([l1, r1, l2, r2])
    result = check_substring_equality(s, queries)
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

vector<bool> check_substring_equality(const string& s, const vector<array<int, 4>>& queries) {
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
    vector<array<int, 4>> queries;
    queries.reserve(q);
    for (int i = 0; i < q; i++) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        queries.push_back({l1, r1, l2, r2});
    }

    vector<bool> result = check_substring_equality(s, queries);
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

function checkSubstringEquality(s, queries) {
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
  const l1 = parseInt(data[idx++], 10);
  const r1 = parseInt(data[idx++], 10);
  const l2 = parseInt(data[idx++], 10);
  const r2 = parseInt(data[idx++], 10);
  queries.push([l1, r1, l2, r2]);
}
const result = checkSubstringEquality(s, queries);
const out = result.map(v => (v ? 'true' : 'false')).join('\n');
process.stdout.write(out);
```

