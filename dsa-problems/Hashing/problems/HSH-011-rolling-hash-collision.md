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
    private long B, M;
    private int L;
    private Map<Long, String> seen;
    
    public String[] findCollision(long B, long M, int L) {
        return null;
    }
    
    private String[] dfs(StringBuilder sb) {
        return null;
    }
    
    private long computeHash(String s) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long B = sc.nextLong();
            long M = sc.nextLong();
            int L = sc.nextInt();
            
            Solution solution = new Solution();
            String[] result = solution.findCollision(B, M, L);
            
            if (result != null) {
                System.out.println(result[0]);
                System.out.println(result[1]);
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(20000)

class Solution:
    def find_collision(self, B: int, M: int, L: int) -> tuple:
        return 0
def find_collision(B: int, M: int, L: int) -> tuple:
    return 0
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    B = int(input_data[0])
    M = int(input_data[1])
    L = int(input_data[2])
    
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
#include <vector>

using namespace std;

class Solution {
    long long B, M;
    int L;
    unordered_map<long long, string> seen;

public:
    pair<string, string> findCollision(long long B, long long M, int L) {
        this->B = B;
        this->M = M;
        this->L = L;
        seen.clear();
        
        string current = "";
        return dfs(current);
    }
    
    pair<string, string> dfs(string& current) {
        if (current.length() == L) {
            long long h = computeHash(current);
            if (seen.count(h)) {
                return {seen[h], current};
            }
            seen[h] = current;
            return {"", ""};
        }
        
        for (char c = 'a'; c <= 'z'; c++) {
            current.push_back(c);
            pair<string, string> res = dfs(current);
            if (res.first != "") return res;
            current.pop_back();
        }
        return {"", ""};
    }
    
    long long computeHash(const string& s) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long B, M;
    int L;
    if (cin >> B >> M >> L) {
        Solution solution;
        auto result = solution.findCollision(B, M, L);
        cout << result.first << "\n" << result.second << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findCollision(B, M, L) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const [B, M, L] = data[0].split(" ").map(Number);

  const solution = new Solution();
  const [s1, s2] = solution.findCollision(B, M, L);

  console.log(s1);
  console.log(s2);
});
```

