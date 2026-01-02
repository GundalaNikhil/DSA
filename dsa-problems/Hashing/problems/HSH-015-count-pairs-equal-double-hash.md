---
problem_id: HSH_COUNT_PAIRS_EQUAL_DOUBLE_HASH__9418
display_id: HSH-015
slug: count-pairs-equal-double-hash
title: "Count Pairs with Equal Hash Mod Two Mods"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Combinatorics
  - String Algorithms
tags:
  - hashing
  - double-hash
  - pairs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-015: Count Pairs with Equal Hash Mod Two Mods

## Problem Statement

Given a string `s` and length `L`, count the number of pairs of substrings of length `L` that have equal hash values under two different moduli (assume collisions are negligible with double hashing).

Return the count of such pairs.

![Problem Illustration](../images/HSH-015/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `L`

## Output Format

- Single integer: number of pairs with equal double hash

## Constraints

- `1 <= |s| <= 10^5`
- `1 <= L <= |s|`
- String contains only lowercase English letters

## Example

**Input:**

```
aaaa
2
```

**Output:**

```
3
```

**Explanation:**

String: "aaaa"
Length L: 2

All substrings of length 2:

- s[0..1] = "aa"
- s[1..2] = "aa"
- s[2..3] = "aa"

All three substrings are identical, so pairs with equal hash:

- (0,1), (0,2), (1,2)

Total: 3 pairs

![Example Visualization](../images/HSH-015/example-1.png)

## Notes

- Compute double hash (using two different moduli) for all substrings of length L
- Group substrings by their hash pair (hash1, hash2)
- For each group of size n, count C(n, 2) = n\*(n-1)/2 pairs
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Hashing, Double Hashing, Combinatorics, Substring Matching

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD1 = 1_000_000_007L;
    private static final long BASE1 = 313L;
    private static final long MOD2 = 1_000_000_009L;
    private static final long BASE2 = 317L;
    
    public long countPairs(String s, int L) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int L = sc.nextInt();
                Solution solution = new Solution();
                System.out.println(solution.countPairs(s, L));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_pairs(self, s: str, L: int) -> int:
        return 0
def count_pairs(s: str, L: int) -> int:
    return 0
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    s = input_data[0]
    if len(input_data) > 1:
        L = int(input_data[1])
        print(count_pairs(s, L))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

class Solution {
    const long long MOD1 = 1e9 + 7;
    const long long BASE1 = 313;
    const long long MOD2 = 1e9 + 9;
    const long long BASE2 = 317;

public:
    long long countPairs(string s, int L) {
        int n = s.length();
        if (L > n) return 0;
        
        map<pair<long long, long long>, int> counts;
        
        long long h1 = 0, h2 = 0;
        long long p1 = 1, p2 = 1;
        
        for (int i = 0; i < L - 1; i++) {
            p1 = (p1 * BASE1) % MOD1;
            p2 = (p2 * BASE2) % MOD2;
        }
        
        for (int i = 0; i < L; i++) {
            h1 = (h1 * BASE1 + s[i]) % MOD1;
            h2 = (h2 * BASE2 + s[i]) % MOD2;
        }
        
        counts[{h1, h2}]++;
        
        for (int i = 1; i <= n - L; i++) {
            long long remove1 = (s[i - 1] * p1) % MOD1;
            h1 = (h1 - remove1 + MOD1) % MOD1;
            h1 = (h1 * BASE1 + s[i + L - 1]) % MOD1;
            
            long long remove2 = (s[i - 1] * p2) % MOD2;
            h2 = (h2 - remove2 + MOD2) % MOD2;
            h2 = (h2 * BASE2 + s[i + L - 1]) % MOD2;
            
            counts[{h1, h2}]++;
        }
        
        long long ans = 0;
        for (auto const& [key, count] : counts) {
            ans += (long long)count * (count - 1) / 2;
        }
        
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    int L;
    if (getline(cin, s) && cin >> L) {
        Solution solution;
        cout << solution.countPairs(s, L) << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countPairs(s, L) {
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
  if (data.length < 2) return;
  const s = data[0];
  const L = parseInt(data[1]);

  const solution = new Solution();
  console.log(solution.countPairs(s, L));
});
```

