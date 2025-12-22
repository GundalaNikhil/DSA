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
import java.util.*;

class Solution {
    public boolean[] checkPalindromes(String s, int[][] queries) {
        // Your implementation here
        return new boolean[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int q = sc.nextInt();

        int[][] queries = new int[q][2];
        for (int i = 0; i < q; i++) {
            queries[i][0] = sc.nextInt();
            queries[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        boolean[] result = solution.checkPalindromes(s, queries);

        for (boolean ans : result) {
            System.out.println(ans);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def check_palindromes(s: str, queries: List[List[int]]) -> List[bool]:
    # Your implementation here
    return []

def main():
    s = input().strip()
    q = int(input())
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append([l, r])

    result = check_palindromes(s, queries)
    for ans in result:
        print("true" if ans else "false")

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
    vector<bool> checkPalindromes(string s, vector<pair<int,int>>& queries) {
        // Your implementation here
        return vector<bool>();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);

    int q;
    cin >> q;

    vector<pair<int,int>> queries(q);
    for (int i = 0; i < q; i++) {
        cin >> queries[i].first >> queries[i].second;
    }

    Solution solution;
    vector<bool> result = solution.checkPalindromes(s, queries);

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
  checkPalindromes(s, queries) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  const s = data[ptr++];
  const q = parseInt(data[ptr++]);

  const queries = [];
  for (let i = 0; i < q; i++) {
    const [l, r] = data[ptr++].split(" ").map(Number);
    queries.push([l, r]);
  }

  const solution = new Solution();
  const result = solution.checkPalindromes(s, queries);

  result.forEach((ans) => console.log(ans ? "true" : "false"));
});
```
