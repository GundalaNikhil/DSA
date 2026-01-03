---
problem_id: DP_CONSTRAINED_DECODE__3012
display_id: DP-014
slug: constrained-decode-ways
title: "Constrained Decode Ways"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
  - Strings
  - Combinatorics
tags:
  - dp
  - decoding
  - strings
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-014: Constrained Decode Ways

## Problem Statement

A digit string encodes letters `1 -> A`, `2 -> B`, ..., `26 -> Z`. You must count how many distinct decodings exist under an extra rule:

- Any digit `0` is valid **only** when immediately preceded by `2`, forming the two-digit code `20`. No other placement of `0` is allowed.

Return the number of valid decodings modulo `1_000_000_007`.

![Problem Illustration](../images/DP-014/problem-illustration.png)

## Input Format

- Single line: a digit string `s` (no spaces).

## Output Format

- Single integer: number of valid decodings modulo `1_000_000_007`.

## Constraints

- `1 <= |s| <= 100000`
- `s` consists of digits `0-9`
- Leading zeros invalidate the string

## Example

**Input:**
```
2012
```

**Output:**
```
2
```

**Explanation:**

Two decodings satisfy the rule:

- `20 1 2`
- `20 12`

![Example Visualization](../images/DP-014/example-1.png)

## Notes

- The pair `10` is **invalid** because `0` must follow an even digit forming `20` only.
- Standalone `0` makes the entire string invalid.
- Use modulo arithmetic throughout to avoid overflow.

## Related Topics

Dynamic Programming, Strings, Combinatorics

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long decodeWays(String s) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        Solution sol = new Solution();
        System.out.println(sol.decodeWays(s));
        sc.close();
    }
}
```

### Python

```python
def decode_ways(s: str) -> int:
    # //Implement here
    return 0

def main():
    s = input().strip()
    print(decode_ways(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <cmath>
#include <cstring>
#include <utility>

using namespace std;

long long decodeWays(const string& s) {
    //Implement here
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    cout << decodeWays(s) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function decodeWays(s) {
  //Implement here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  const s = data[0];
  console.log(decodeWays(s));
});
```

