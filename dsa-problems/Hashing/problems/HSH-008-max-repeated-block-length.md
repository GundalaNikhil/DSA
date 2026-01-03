---
problem_id: HSH_MAX_REPEATED_BLOCK_LENGTH__5827
display_id: HSH-008
slug: max-repeated-block-length
title: "Maximum Repeated Block Length"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - Binary Search
  - String Algorithms
tags:
  - hashing
  - binary-search
  - substring
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-008: Maximum Repeated Block Length

## Problem Statement

Find the longest length `L` such that there exist two non-overlapping substrings of length `L` that are equal.

Given a string `s`, determine the maximum length of a substring that appears at least twice without overlapping.

![Problem Illustration](../images/HSH-008/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single integer: maximum length of repeated non-overlapping substring

## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
abcabc
```

**Output:**

```
3
```

**Explanation:**

String: "abcabc"

The substring "abc" appears at positions 0-2 and 3-5 (non-overlapping).
Length: 3

![Example Visualization](../images/HSH-008/example-1.png)

## Notes

- Use binary search on the answer (length L)
- For each candidate length, check if any substring of that length appears twice non-overlapping
- Use hashing to compare substrings efficiently
- Track positions to ensure non-overlapping constraint
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Binary Search, Hashing, Rolling Hash, Longest Repeated Substring

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public int maxRepeatedBlockLength(String s) {
        //Implemention here
        return 0;
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
        int result = solution.maxRepeatedBlockLength(s);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def max_repeated_block_length(s):
    # //Implemention here
    return 0

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    s = data[idx]
    result = max_repeated_block_length(s)
    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

int max_repeated_block_length(const string& s) {
    //Implemention here
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int result = max_repeated_block_length(s);
    cout << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function maxRepeatedBlockLength(s) {
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
const result = maxRepeatedBlockLength(s);
process.stdout.write(String(result));
```

