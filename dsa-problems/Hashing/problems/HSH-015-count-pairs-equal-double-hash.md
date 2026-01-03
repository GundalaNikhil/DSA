---
problem_id: HSH_COUNT_PAIRS_EQUAL_DOUBLE_HASH__9418
display_id: HSH-015
slug: count-pairs-equal-double-hash
title: "Count Pairs with Equal Hash Mod Two Mods"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Combinatorics
  - String Algorithms
tags:
  - hashing
  - double-hash
  - pairs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-015: Count Pairs with Equal Hash Mod Two Mods

## Problem Statement

Given a string `s` and length `L`, count the number of pairs of substrings of length `L` that have equal hash values under two different moduli (assume collisions are negligible with double hashing).

Return the count of such pairs.

![Problem Illustration](../images/HSH-015/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `L`

## Output Format

- Single integer: number of pairs with equal double hash

## Constraints

- `1 <= |s| <= 10^5`
- `1 <= L <= |s|`
- String contains only lowercase English letters

## Example

**Input:**

```
aaaa
2
```

**Output:**

```
3
```

**Explanation:**

String: "aaaa"
Length L: 2

All substrings of length 2:

- s[0..1] = "aa"
- s[1..2] = "aa"
- s[2..3] = "aa"

All three substrings are identical, so pairs with equal hash:

- (0,1), (0,2), (1,2)

Total: 3 pairs

![Example Visualization](../images/HSH-015/example-1.png)

## Notes

- Compute double hash (using two different moduli) for all substrings of length L
- Group substrings by their hash pair (hash1, hash2)
- For each group of size n, count C(n, 2) = n\*(n-1)/2 pairs
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Hashing, Double Hashing, Combinatorics, Substring Matching

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public long countPairs(String s, int L) {
        //Implemention here
        return 0L;
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
        int L = Integer.parseInt(data[idx++]);
        Solution solution = new Solution();
        long result = solution.countPairs(s, L);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def count_pairs(s, L):
    # //Implemention here
    return 0

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    s = data[idx]
    idx += 1
    L = int(data[idx])
    result = count_pairs(s, L)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

long long count_pairs(const string& s, int L) {
    //Implemention here
    return 0LL;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int L;
    if (!(cin >> L)) return 0;
    long long result = count_pairs(s, L);
    cout << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function countPairs(s, L) {
  //Implemention here
  return 0;
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/);
let idx = 0;
const s = data[idx++];
const L = parseInt(data[idx++], 10);
const result = countPairs(s, L);
process.stdout.write(String(result));
```

