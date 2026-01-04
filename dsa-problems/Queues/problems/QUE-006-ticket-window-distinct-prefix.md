---
problem_id: QUE_TICKET_WINDOW_DISTINCT_PREFIX__5176
display_id: QUE-006
slug: ticket-window-distinct-prefix
title: "Ticket Window Distinct Prefix"
difficulty: Easy
difficulty_score: 30
topics:
  - Queue
  - Hashing
  - Streaming
tags:
  - queue
  - hashing
  - stream
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-006: Ticket Window Distinct Prefix

## Problem Statement

A ticket window receives a stream of lowercase letters that represent customer IDs. After each new letter arrives, report the first letter in the stream so far that has appeared exactly once. If there is no such letter, output `#`.

This is a classic streaming problem where you must answer after each prefix.

![Problem Illustration](../images/QUE-006/problem-illustration.png)

## Input Format

- First line: string `s` of lowercase English letters

## Output Format

- Single line with `n` space-separated characters, where the `i`-th output is the first non-repeating letter in `s[0..i]`, or `#` if none exists

## Constraints

- `1 <= |s| <= 100000`
- `s` contains only `a` to `z`

## Example

**Input:**

```
abacb
```

**Output:**

```
a a b b c
```

**Explanation:**

Prefixes and answers:

- `a` -> `a`
- `ab` -> `a`
- `aba` -> `b`
- `abac` -> `b`
- `abacb` -> `c`

![Example Visualization](../images/QUE-006/example-1.png)

## Notes

- Use a queue to track candidates that are still unique
- Maintain frequency counts for each letter
- Each character is enqueued and dequeued at most once
- Time complexity: O(n)

## Related Topics

Queue, Hashing, Streaming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void firstNonRepeating(String s) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        Solution sol = new Solution();
        sol.firstNonRepeating(s);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def first_non_repeating(self, s):
        # Implement here
        pass

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    sol = Solution()
    sol.first_non_repeating(s)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    void firstNonRepeating(string s) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    Solution sol;
    sol.firstNonRepeating(s);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  firstNonRepeating(s) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").trim();
  if (!input) return;
  const sol = new Solution();
  sol.firstNonRepeating(input);
}

solve();
```
