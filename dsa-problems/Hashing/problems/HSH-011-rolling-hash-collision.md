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

class Solution {
    public String[] findCollision(long B, long M, int L) {
        // Your implementation here
        return new String[2];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long B = sc.nextLong();
        long M = sc.nextLong();
        int L = sc.nextInt();

        Solution solution = new Solution();
        String[] result = solution.findCollision(B, M, L);

        System.out.println(result[0]);
        System.out.println(result[1]);
        sc.close();
    }
}
```

### Python

```python
def find_collision(B: int, M: int, L: int) -> tuple:
    # Your implementation here
    return ("", "")

def main():
    B, M, L = map(int, input().split())

    s1, s2 = find_collision(B, M, L)
    print(s1)
    print(s2)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    pair<string, string> findCollision(long long B, long long M, int L) {
        // Your implementation here
        return {"", ""};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long B, M;
    int L;
    cin >> B >> M >> L;

    Solution solution;
    auto [s1, s2] = solution.findCollision(B, M, L);

    cout << s1 << "\n" << s2 << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findCollision(B, M, L) {
    // Your implementation here
    return ["", ""];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const [B, M, L] = data[0].split(" ").map(Number);

  const solution = new Solution();
  const [s1, s2] = solution.findCollision(B, M, L);

  console.log(s1);
  console.log(s2);
});
```
