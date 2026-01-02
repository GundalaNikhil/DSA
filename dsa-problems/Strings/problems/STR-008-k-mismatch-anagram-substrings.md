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

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countKMismatchAnagrams(String s, String p, int k) {
        return 0;
    }

    private int mismatchCost(int[] freqW, int[] freqP) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String p = sc.next();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.countKMismatchAnagrams(s, p, k));
        sc.close();
    }
}
```

### Python

```python
def count_k_mismatch_anagrams(s: str, p: str, k: int) -> int:
    return 0
def main():
    import sys

    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
        
    parts = input_data.split()
    if len(parts) >= 3:
        s = parts[0]
        p = parts[1]
        try:
            k = int(parts[2])
            print(count_k_mismatch_anagrams(s, p, k))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
class Solution {
public:
    int countKMismatchAnagrams(string s, string p, int k) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    string p; cin >> p;
    int k; cin >> k;
    Solution sol;
    cout << sol.countKMismatchAnagrams(s, p, k) << endl;
    return 0;
}
```

### JavaScript

```javascript
function countKMismatchAnagrams(s, p, k) {
    return 0;
  }
  function mismatchCost(fw, fp) {
    return 0;
  }

  let count = 0;

  // Check first window
  if (mismatchCost(freqWindow, freqP) <= k) {
    count++;
  }

  // Slide window
  for (let i = 1; i <= n - m; i++) {
    // Remove leftmost
    freqWindow[s.charCodeAt(i - 1) - 97]--;
    // Add rightmost
    freqWindow[s.charCodeAt(i + m - 1) - 97]++;

    if (mismatchCost(freqWindow, freqP) <= k) {
      count++;
    }
  }

  return count;
}

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const p = tokens[ptr++];
    const k = parseInt(tokens[ptr++]);
    console.log(countKMismatchAnagrams(s, p, k));
});
```

