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
import java.util.*;

class Solution {
    private static final long MOD1 = 1000000007L;
    private static final long BASE1 = 313L;
    private static final long MOD2 = 1000000009L;
    private static final long BASE2 = 317L;

    public boolean[] checkSubstringEquality(String s, int[][] queries) {
        return false;
    }
    
    private long getHash(long[] h, long[] p, int l, int r, long mod) {
        // h is 1-based prefix hash array
        // substring s[l..r] corresponds to h[r+1] and h[l]
        // Formula: (h[r+1] - h[l] * p[len]) % mod
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % mod + mod) % mod;
        return val;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int q = sc.nextInt();
                int[][] queries = new int[q][4];
                for (int i = 0; i < q; i++) {
                    queries[i][0] = sc.nextInt();
                    queries[i][1] = sc.nextInt();
                    queries[i][2] = sc.nextInt();
                    queries[i][3] = sc.nextInt();
                }
                
                Solution solution = new Solution();
                boolean[] result = solution.checkSubstringEquality(s, queries);
                
                for (boolean ans : result) {
                    System.out.println(ans);
                }
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

class Solution:
    def check_substring_equality(self, s: str, queries: list) -> list:
        return []
def check_substring_equality(s: str, queries: list) -> list:
    return []
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        s = next(iterator)
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            l1 = int(next(iterator))
            r1 = int(next(iterator))
            l2 = int(next(iterator))
            r2 = int(next(iterator))
            queries.append([l1, r1, l2, r2])
            
        result = check_substring_equality(s, queries)
        for ans in result:
            print("true" if ans else "false")
    except StopIteration:
        pass

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
    const long long MOD1 = 1e9 + 7;
    const long long BASE1 = 313;
    const long long MOD2 = 1e9 + 9;
    const long long BASE2 = 317;

public:
    vector<bool> checkSubstringEquality(string s, vector<vector<int>>& queries) {
        return false;
    }
    
    long long getHash(const vector<long long>& h, const vector<long long>& p, int l, int r, long long mod) {
        int len = r - l + 1;
        long long val = (h[r + 1] - (h[l] * p[len]) % mod + mod) % mod;
        return val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (!(cin >> s)) return 0;
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++) {
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2] >> queries[i][3];
    }
    
    Solution solution;
    vector<bool> result = solution.checkSubstringEquality(s, queries);
    
    for (bool ans : result) {
        cout << (ans ? "true" : "false") << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  checkSubstringEquality(s, queries) {
    return 0;
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
  
  let ptr = 0;
  const s = data[ptr++];
  const q = parseInt(data[ptr++]);
  
  const queries = [];
  for (let i = 0; i < q; i++) {
    const parts = data[ptr++].split(" ").map(Number);
    queries.push(parts);
  }
  
  const solution = new Solution();
  const result = solution.checkSubstringEquality(s, queries);
  
  result.forEach((ans) => console.log(ans ? "true" : "false"));
});
```

