---
problem_id: HSH_POLYNOMIAL_HASH_PREFIXES__3824
display_id: HSH-001
slug: polynomial-hash-prefixes
title: "Polynomial Hash of Prefixes"
difficulty: Easy
difficulty_score: 25
topics:
  - Hashing
  - Rolling Hash
  - String Algorithms
tags:
  - hashing
  - rolling-hash
  - polynomial-hash
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-001: Polynomial Hash of Prefixes

## Problem Statement

Given a lowercase string `s`, compute the polynomial rolling hash for all prefixes using base `B` and modulus `M`.

The polynomial hash for a string is computed as:
- `hash("") = 0`
- `hash(s[0..i]) = (hash(s[0..i-1]) * B + s[i]) mod M`

where `s[i]` is treated as its ASCII value.

Return an array containing the hash values for all prefixes: `hash(s[0..0]), hash(s[0..1]), ..., hash(s[0..n-1])`.

![Problem Illustration](../images/HSH-001/problem-illustration.png)

## Input Format

- First line: string `s` (lowercase letters only)
- Second line: two integers `B M` (base and modulus)

## Output Format

- Single line with `n` space-separated integers representing hash values of all prefixes

## Constraints

- `1 <= |s| <= 2*10^5`
- `1 <= B <= 10^9 + 6`
- `1 <= M <= 10^9 + 7`
- String contains only lowercase English letters

## Example

**Input:**
```
abc
911382323 1000000007
```

**Output:**
```
97 374134515 549818522
```

**Explanation:**

String: "abc"
- Prefix "a": hash = 97 (ASCII of 'a')
- Prefix "ab": hash = (97 * 911382323 + 98) mod 1000000007 = 374134515
- Prefix "abc": hash = (374134515 * 911382323 + 99) mod 1000000007 = 549818522

![Example Visualization](../images/HSH-001/example-1.png)

## Notes

- Use modular arithmetic to prevent integer overflow
- Hash values depend on both the base and modulus chosen
- This technique is fundamental for string matching and comparison
- Time complexity: O(n)
- Space complexity: O(n) for storing results

## Related Topics

Polynomial Hash, Rolling Hash, String Hashing, Rabin-Karp

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] computePrefixHashes(String s, long B, long M) {
        //Implement here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextLong()) {
                long B = sc.nextLong();
                long M = sc.nextLong();

                Solution solution = new Solution();
                long[] result = solution.computePrefixHashes(s, B, M);

                for (int i = 0; i < result.length; i++) {
                    System.out.print(result[i]);
                    if (i < result.length - 1) System.out.print(" ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case, though not needed for iterative

def compute_prefix_hashes(s: str, B: int, M: int) -> list:
    # //Implement here
    return 0

def main():
    # Read input line by line
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return

    s = lines[0]
    B, M = map(int, lines[1].split())

    result = compute_prefix_hashes(s, B, M)
    print(' '.join(map(str, result)))

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
    vector<long long> computePrefixHashes(string s, long long B, long long M) {
        //Implement here
        return {};
    }
};

int main() {
    // Fast I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    long long B, M;

    if (getline(cin, s)) {
        if (cin >> B >> M) {
            Solution solution;
            vector<long long> result = solution.computePrefixHashes(s, B, M);

            for (int i = 0; i < result.size(); i++) {
                cout << result[i];
                if (i < result.size() - 1) cout << " ";
            }
            cout << "\n";
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  computePrefixHashes(s, B, M) {
    //Implement here
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

  let ptr = 0;
  const s = data[ptr++];
  const [B, M] = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  const result = solution.computePrefixHashes(s, B, M);
  console.log(result.join(" "));
});
```

