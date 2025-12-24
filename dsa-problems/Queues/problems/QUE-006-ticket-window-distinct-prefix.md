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
    public List<String> firstNonRepeating(String s) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        Solution solution = new Solution();
        List<String> result = solution.firstNonRepeating(s);
        System.out.println(String.join(" ", result));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def first_non_repeating(s: str) -> List[str]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    result = first_non_repeating(s)
    sys.stdout.write(" ".join(result))

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
    vector<string> firstNonRepeating(const string& s) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    Solution solution;
    vector<string> result = solution.firstNonRepeating(s);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  firstNonRepeating(s) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  const result = solution.firstNonRepeating(s);
  console.log(result.join(" "));
});
```
