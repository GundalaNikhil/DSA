---
problem_id: HSH_ROLLING_HASH_COLLISION__8932
display_id: HSH-011
slug: rolling-hash-collision
title: "Rolling Hash Collision Finder"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - Collision
  - Brute Force
tags:
  - hashing
  - collision
  - cryptography
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-011: Rolling Hash Collision Finder

## Problem Statement

Given a base `B`, modulus `M`, and length `L`, find two different strings of length `L` that produce the same polynomial hash value (a hash collision).

Return any pair of distinct strings that collide under the given hash parameters.

![Problem Illustration](../images/HSH-011/problem-illustration.png)

## Input Format

- Single line: three integers `B M L`

## Output Format

- Two lines, each containing a string of length `L` that produces the same hash

## Constraints

- `1 <= L <= 8`
- `1 <= B <= 10^9`
- `1 <= M <= 10^9 + 7`
- Strings contain only lowercase English letters

## Example

**Input:**

```
3 7 3
```

**Output:**

```
aaa
dac
```

**Explanation:**

Base B=3, Modulus M=7, Length L=3

hash("aaa") = (0*3^2 + 0*3 + 0) mod 7 = 0
hash("dac") = (3*9 + 0*3 + 2) mod 7 = 29 mod 7 = 1

(Note: Example may vary, any valid collision pair is acceptable)

![Example Visualization](../images/HSH-011/example-1.png)

## Notes

- Use birthday paradox approach or brute force search
- Generate random strings and store their hashes
- When a collision is found, return the pair
- Small L makes brute force feasible
- Time complexity: O(26^L) worst case
- Space complexity: O(26^L)

## Related Topics

Hash Collision, Birthday Paradox, Brute Force Search, Cryptography

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String[] findCollision(long b, long m, int l) {
        // Implement here
        return new String[0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        long b = Long.parseLong(parts[0]);
        long m = Long.parseLong(parts[1]);
        int l = Integer.parseInt(parts[2]);

        Solution sol = new Solution();
        String[] result = sol.findCollision(b, m, l);

        if (result.length >= 2) {
            System.out.println(result[0]);
            System.out.println(result[1]);
        }
    }
}
```

### Python

```python
import sys

class Solution:
    def find_collision(self, b, m, l):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return

    b = int(input_data[0])
    m = int(input_data[1])
    l = int(input_data[2])

    sol = Solution()
    result = sol.find_collision(b, m, l)
    for res in result:
        print(res)

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
    vector<string> findCollision(long long b, long long m, int l) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long b, m;
    int l;
    if (!(cin >> b >> m >> l)) return 0;

    Solution sol;
    vector<string> result = sol.findCollision(b, m, l);

    for (const string& res : result) {
        cout << res << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findCollision(b, m, l) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  const b = BigInt(input[0]);
  const m = BigInt(input[1]);
  const l = parseInt(input[2]);

  const sol = new Solution();
  const result = sol.findCollision(b, m, l);
  result.forEach((res) => console.log(res));
}

solve();
```
