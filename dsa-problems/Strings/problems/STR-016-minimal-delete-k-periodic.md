---
problem_id: STR_MINIMAL_DELETE_K_PERIODIC__1016
display_id: STR-016
slug: minimal-delete-k-periodic
title: "Minimal Delete to Make K-Periodic"
difficulty: Medium
difficulty_score: 39
topics:
  - String Manipulation
  - Greedy
  - Frequency Analysis
tags:
  - periodicity
  - deletion
  - position-class
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-016: Minimal Delete to Make K-Periodic

## Problem Statement

Given a string `s` and an integer `k`, delete the minimum number of characters so that the resulting string is periodic with period exactly `k` (can be written as repetitions of a k-length block).

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `k` (1 ≤ k ≤ |s|)

## Output Format

- A single integer representing minimum deletions

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ k ≤ |s|`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
abac
2
```

**Output:**

```
1
```

**Explanation:**

- Position 0 (mod 2): 'a','a' → keep 'a'
- Position 1 (mod 2): 'b','c' → keep 'b' (or 'c')
- Delete 'c' → 1 deletion
- Pattern: "ab" repeated

## Example 2

**Input:**

```
aabbcc
3
```

**Output:**

```
3
```

**Explanation:**

- For each position mod 3, keep most frequent character
- Total deletions needed: 3

## Notes

- Group positions by i mod k
- Keep most frequent char at each position class
- O(n) greedy algorithm

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minDeletions(String s, int k) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.minDeletions(s, k));
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    s = input_data[0]
    k = int(input_data[1])
    solution = Solution()
    print(solution.min_deletions(s, k))

class Solution:
    def min_deletions(self, s: str, k: int) -> int:
        # Implement here
        return 0

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int minDeletions(string s, int k) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int k;
    if (cin >> s >> k) {
        Solution sol;
        cout << sol.minDeletions(s, k) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minDeletions(s, k) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length >= 2) {
    const s = input[0];
    const k = parseInt(input[1]);
    const sol = new Solution();
    console.log(sol.minDeletions(s, k));
  }
});
```
