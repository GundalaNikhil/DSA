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
import java.io.*;
import java.util.*;

class Solution {
    public String[] findCollision(long B, long M, int L) {
        //Implemention here
        return new String[]{"", ""};
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
        long B = Long.parseLong(data[idx++]);
        long M = Long.parseLong(data[idx++]);
        int L = Integer.parseInt(data[idx++]);
        Solution solution = new Solution();
        String[] result = solution.findCollision(B, M, L);
        if (result.length >= 2) {
            System.out.println(result[0]);
            System.out.print(result[1]);
        }
    }
}
```

### Python

```python
import sys

def find_collision(B, M, L):
    # //Implemention here
    return ("", "")

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    B = int(data[idx]);
    M = int(data[idx + 1]);
    L = int(data[idx + 2]);
    result = find_collision(B, M, L)
    if result:
        sys.stdout.write(str(result[0]) + '\n' + str(result[1]))

if __name__ == '__main__':
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <utility>

using namespace std;

pair<string, string> find_collision(long long B, long long M, int L) {
    //Implemention here
    return {"", ""};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long B, M;
    int L;
    if (!(cin >> B >> M >> L)) return 0;
    auto result = find_collision(B, M, L);
    cout << result.first << "\n" << result.second;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function findCollision(B, M, L) {
  //Implemention here
  return ["", ""];
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/);
let idx = 0;
const B = parseInt(data[idx++], 10);
const M = parseInt(data[idx++], 10);
const L = parseInt(data[idx++], 10);
const result = findCollision(B, M, L);
if (result && result.length >= 2) {
  process.stdout.write(String(result[0]) + '\n' + String(result[1]));
}
```

