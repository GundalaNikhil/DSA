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
    public long countPairs(String s, int L) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int L = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countPairs(s, L));
        sc.close();
    }
}
```

### Python

```python
def count_pairs(s: str, L: int) -> int:
    # Your implementation here
    return 0

def main():
    s = input().strip()
    L = int(input())

    result = count_pairs(s, L)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <map>
using namespace std;

class Solution {
public:
    long long countPairs(string s, int L) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int L;
    getline(cin, s);
    cin >> L;

    Solution solution;
    cout << solution.countPairs(s, L) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countPairs(s, L) {
    // Your implementation here
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
  const s = data[0];
  const L = parseInt(data[1]);

  const solution = new Solution();
  console.log(solution.countPairs(s, L));
});
```
