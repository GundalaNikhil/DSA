---
problem_id: HSH_COUNT_DISTINCT_SUBSTRINGS__8741
display_id: HSH-005
slug: count-distinct-substrings-hash
title: "Count Distinct Substrings"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Set Operations
tags:
  - hashing
  - substring
  - distinct
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-005: Count Distinct Substrings

## Problem Statement

Given a string `s`, count the number of distinct substrings (including the empty string) using polynomial hashing.

A substring is a contiguous sequence of characters within the string. Two substrings are considered the same if they have identical characters in the same order.

![Problem Illustration](../images/HSH-005/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single integer: number of distinct substrings

## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
aaa
```

**Output:**

```
4
```

**Explanation:**

String: "aaa"

All substrings:

- "" (empty) - 1 distinct
- "a" (positions 0, 1, 2) - 1 distinct
- "aa" (positions 0-1, 1-2) - 1 distinct
- "aaa" (position 0-2) - 1 distinct

Total distinct: 4

![Example Visualization](../images/HSH-005/example-1.png)

## Notes

- Generate all O(n²) substrings
- Compute hash for each substring
- Use a set to store unique hashes
- Use double hashing to minimize collisions
- Time complexity: O(n²)
- Space complexity: O(n²)

## Related Topics

Hashing, Substring Generation, Set Operations, Suffix Array

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public long countDistinctSubstrings(String s) {
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
        Solution solution = new Solution();
        long result = solution.countDistinctSubstrings(s);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def count_distinct_substrings(s):
    # //Implemention here
    return 0

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    s = data[idx]
    result = count_distinct_substrings(s)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

long long count_distinct_substrings(const string& s) {
    //Implemention here
    return 0LL;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    long long result = count_distinct_substrings(s);
    cout << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function countDistinctSubstrings(s) {
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
const result = countDistinctSubstrings(s);
process.stdout.write(String(result));
```

