---
problem_id: STR_K_MISMATCH_ANAGRAM_SUBSTRINGS__1008
display_id: STR-008
slug: k-mismatch-anagram-substrings
title: "K-Mismatch Anagram Substrings"
difficulty: Medium
difficulty_score: 43
topics:
  - String Manipulation
  - Sliding Window
  - Frequency Analysis
tags:
  - anagram
  - fuzzy-matching
  - window-algorithm
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-008: K-Mismatch Anagram Substrings

## Problem Statement

Given a string `s`, a pattern `p`, and integers `m` (substring length) and `k` (allowed mismatches), count how many substrings of length `m` in `s` become anagrams of `p` after at most `k` character substitutions.

Note: `m = |p|`

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: String `p` (1 ≤ |p| ≤ 10^5)
- Third line: Integer `k` (0 ≤ k ≤ m)

## Output Format

- A single integer representing the count of valid substrings

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ m ≤ |s|`
- `m = |p|`
- `0 ≤ k ≤ m`

## Example 1

**Input:**

```
abxcab
aabc
1
```

**Output:**

```
3
```

**Explanation:**

- Substring "abxc": need 1 substitution (x→a) → valid
- Substring "bxca": need 1 substitution (x→a) → valid
- Substring "xcab": need 1 substitution (x→a) → valid

## Notes

- Use sliding window with incremental frequency updates
- Mismatch cost = Σ max(0, freq_p[c] - freq_window[c])
- O(n) time with O(1) space (fixed 26 chars)

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countAnagramSubstrings(String s, String p, int k) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (sc.hasNext()) {
                String p = sc.next();
                if (sc.hasNextInt()) {
                    int k = sc.nextInt();
                    Solution sol = new Solution();
                    System.out.println(sol.countAnagramSubstrings(s, p, k));
                }
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
    if len(input_data) < 3:
        return
    s = input_data[0]
    p = input_data[1]
    k = int(input_data[2])
    solution = Solution()
    print(solution.count_anagram_substrings(s, p, k))

class Solution:
    def count_anagram_substrings(self, s: str, p: str, k: int) -> int:
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
    int countAnagramSubstrings(string s, string p, int k) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s, p;
    int k;
    if (cin >> s >> p >> k) {
        Solution sol;
        cout << sol.countAnagramSubstrings(s, p, k) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countAnagramSubstrings(s, p, k) {
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
  if (input.length >= 3) {
    const s = input[0];
    const p = input[1];
    const k = parseInt(input[2]);
    const sol = new Solution();
    console.log(sol.countAnagramSubstrings(s, p, k));
  }
});
```
