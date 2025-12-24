---
problem_id: STC_LONGEST_PAL_ONE_WILDCARD__7405
display_id: STC-014
slug: longest-palindrome-one-wildcard
title: "Longest Palindromic Substring With One Wildcard"
difficulty: Medium
difficulty_score: 55
topics:
  - Strings
  - Palindromes
  - Two Pointers
tags:
  - strings
  - palindromes
  - wildcard
  - medium
premium: true
subscription_tier: basic
---

# STC-014: Longest Palindromic Substring With One Wildcard

## 📋 Problem Summary

Given a string `s` containing lowercase letters and at most one wildcard character `?`, find the longest substring that can become a palindrome by replacing the `?` with some character.

## 🌍 Real-World Scenario

**Scenario Title:** DNA Sequencing with Errors

In DNA sequencing, read errors are common. Sometimes a base cannot be determined with certainty and is marked as 'N' (unknown). When searching for palindromic sequences (which are biologically significant, e.g., restriction sites), we want to be tolerant of these unknown bases. Finding the longest palindrome allowing for one "wildcard" helps identify these structures even in imperfect data.

**Why This Problem Matters:**

- **Fuzzy Search:** Allowing mismatches or wildcards in pattern matching.
- **Data Recovery:** Reconstructing corrupted text where symmetry is expected.

![Real-World Application](../images/STC-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "ab?ba"`.
Possible centers:
- Center at `?` (index 2):
  - `?` matches itself.
  - `s[1]` ('b') vs `s[3]` ('b') -> Match.
  - `s[0]` ('a') vs `s[4]` ('a') -> Match.
  - Radius expands to cover "ab?ba". Length 5.

Let `s = "ax?yb"`.
- Center at `?`: `x` vs `y` -> Mismatch.
- Center at `x`: `a` vs `?` -> Match (replace `?` with `a`). "ax?" becomes "axa". Length 3.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **One Wildcard:** There is at most one `?`.
- **Replacement:** The `?` can be any character. This means `?` matches any character `c`.
- **Output:** Return the substring from the original string (keeping `?`).

## Naive Approach

### Intuition

For every possible center (2N-1 centers), expand outwards. Treat `?` as a match for any character.

### Algorithm

1. Iterate center `c` from `0` to `2*N`.
2. Expand `L, R` outwards.
3. Check `s[L] == s[R]`.
   - If `s[L] == '?'` or `s[R] == '?'`, it's a match.
   - Else if `s[L] == s[R]`, match.
   - Else, break.
4. Track max length.

### Time Complexity

- **O(N^2)**: Expansion takes O(N), done 2N times.
- Acceptable for N=2000? No, N=200,000. We need O(N).

## Optimal Approach (Manacher's Algorithm)

### Key Insight

Standard Manacher's algorithm works by using previously computed palindrome lengths to initialize the length for the current center: `P[i] = min(P[mirror], R - i)`.
This optimization relies on the symmetry of palindromes.
Does the wildcard break this?
- If the main palindrome at `center` covers the wildcard, the characters around `center` are symmetric *assuming* `?` matches its reflection.
- When we process a new center `i` inside this main palindrome, we initialize `P[i]` using `P[mirror]`.
- `P[mirror]` was computed using characters that are reflections of characters around `i`.
- Since `?` matches *anything*, it effectively satisfies any equality constraint it is involved in.
- Therefore, the palindrome at `i` is guaranteed to be *at least* as long as the palindrome at `mirror` (clipped by the boundary of the main palindrome), because any match that happened at `mirror` (e.g., `x == x`) will also happen at `i` (e.g., `x == ?` or `? == x` or `x == x`).
- Thus, Manacher's logic holds perfectly if we simply define equality as `a == b || a == '?' || b == '?'`.

### Algorithm

1. Transform `s` into `T` with separators `#`. Example: `aba` -> `^#a#b#a#$`.
   - Note: `?` becomes a character in `T`. `#` remains `#`.
   - `?` never matches `#`. `?` only matches letters.
2. Run Manacher's:
   - Initialize `P` array. `C = 0`, `R = 0`.
   - Loop `i` from 1 to `len(T)-2`.
   - `P[i] = (R > i) ? min(R - i, P[2*C - i]) : 0`.
   - Attempt to expand: `while T[i + 1 + P[i]] matches T[i - 1 - P[i]]`: `P[i]++`.
     - Match condition: `c1 == c2` OR (`c1` is `?` and `c2` != `#`) OR (`c2` is `?` and `c1` != `#`).
     - Note: `#` must match `#`. `?` is a "letter" placeholder, so it behaves like a letter. It cannot match a separator.
   - Update `C`, `R` if `i + P[i] > R`.
3. Find max `P[i]`. Extract substring.

### Time Complexity

- **O(N)**: Manacher's is linear.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/STC-014/algorithm-visualization.png)
![Algorithm Steps](../images/STC-014/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public String longestWildcardPalindrome(String s) {
        if (s == null || s.length() == 0) return "";
        
        StringBuilder sb = new StringBuilder();
        sb.append('^');
        for (char c : s.toCharArray()) {
            sb.append('#').append(c);
        }
        sb.append("#$");
        String T = sb.toString();
        
        int n = T.length();
        int[] P = new int[n];
        int C = 0, R = 0;
        
        for (int i = 1; i < n - 1; i++) {
            P[i] = (R > i) ? Math.min(R - i, P[2 * C - i]) : 0;
            
            while (match(T.charAt(i + 1 + P[i]), T.charAt(i - 1 - P[i]))) {
                P[i]++;
            }
            
            if (i + P[i] > R) {
                C = i;
                R = i + P[i];
            }
        }
        
        int maxLen = 0;
        int centerIndex = 0;
        for (int i = 1; i < n - 1; i++) {
            if (P[i] > maxLen) {
                maxLen = P[i];
                centerIndex = i;
            }
        }
        
        int start = (centerIndex - maxLen) / 2;
        return s.substring(start, start + maxLen);
    }
    
    private boolean match(char c1, char c2) {
        if (c1 == '#' || c2 == '#') return c1 == c2;
        if (c1 == '^' || c2 == '^' || c1 == '`' || c2 == '`') return c1 == c2;
        // Both are letters or ?
        return c1 == c2 || c1 == '?' || c2 == '?';
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.longestWildcardPalindrome(s));
        }
        sc.close();
    }
}
```

### Python

```python
def longest_wildcard_palindrome(s: str) -> str:
    if not s:
        return ""
        
    T = ['^']
    for c in s:
        T.append('#')
        T.append(c)
    T.append('#')
    T.append('$')
    
    n = len(T)
    P = [0] * n
    C = 0
    R = 0
    
    for i in range(1, n - 1):
        P[i] = min(R - i, P[2 * C - i]) if R > i else 0
        
        # Expand
        while True:
            c1 = T[i + 1 + P[i]]
            c2 = T[i - 1 - P[i]]
            
            is_match = False
            if c1 == '#' or c2 == '#':
                is_match = (c1 == c2)
            elif c1 == '^' or c2 == '^' or c1 == '`' or c2 == '`':
                is_match = (c1 == c2)
            else:
                # Letters or ?
                is_match = (c1 == c2 or c1 == '?' or c2 == '?')
                
            if is_match:
                P[i] += 1
            else:
                break
                
        if i + P[i] > R:
            C = i
            R = i + P[i]
            
    max_len = 0
    center_idx = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_idx = i
            
    start = (center_idx - max_len) // 2
    return s[start : start + max_len]

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(longest_wildcard_palindrome(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestWildcardPalindrome(const string& s) {
        if (s.empty()) return "";
        
        string T = "^";
        for (char c : s) {
            T += "#";
            T += c;
        }
        T += "#$";
        
        int n = T.length();
        vector<int> P(n, 0);
        int C = 0, R = 0;
        
        for (int i = 1; i < n - 1; i++) {
            P[i] = (R > i) ? min(R - i, P[2 * C - i]) : 0;
            
            while (true) {
                char c1 = T[i + 1 + P[i]];
                char c2 = T[i - 1 - P[i]];
                
                bool match = false;
                if (c1 == '#' || c2 == '#') match = (c1 == c2);
                else if (c1 == '^' || c2 == '^' || c1 == '`' || c2 == '`') match = (c1 == c2);
                else match = (c1 == c2 || c1 == '?' || c2 == '?');
                
                if (match) P[i]++;
                else break;
            }
            
            if (i + P[i] > R) {
                C = i;
                R = i + P[i];
            }
        }
        
        int maxLen = 0;
        int centerIndex = 0;
        for (int i = 1; i < n - 1; i++) {
            if (P[i] > maxLen) {
                maxLen = P[i];
                centerIndex = i;
            }
        }
        
        int start = (centerIndex - maxLen) / 2;
        return s.substr(start, maxLen);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.longestWildcardPalindrome(s) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestWildcardPalindrome(s) {
    if (!s) return "";
    
    let T = "^";
    for (const c of s) {
      T += "#" + c;
    }
    T += "#$";
    
    const n = T.length;
    const P = new Array(n).fill(0);
    let C = 0, R = 0;
    
    for (let i = 1; i < n - 1; i++) {
      P[i] = (R > i) ? Math.min(R - i, P[2 * C - i]) : 0;
      
      while (true) {
        const c1 = T[i + 1 + P[i]];
        const c2 = T[i - 1 - P[i]];
        
        let match = false;
        if (c1 === '#' || c2 === '#') match = (c1 === c2);
        else if (c1 === '^' || c2 === '^' || c1 === '`' || c2 === '`') match = (c1 === c2);
        else match = (c1 === c2 || c1 === '?' || c2 === '?');
        
        if (match) P[i]++;
        else break;
      }
      
      if (i + P[i] > R) {
        C = i;
        R = i + P[i];
      }
    }
    
    let maxLen = 0;
    let centerIndex = 0;
    for (let i = 1; i < n - 1; i++) {
      if (P[i] > maxLen) {
        maxLen = P[i];
        centerIndex = i;
      }
    }
    
    const start = Math.floor((centerIndex - maxLen) / 2);
    return s.substring(start, start + maxLen);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.longestWildcardPalindrome(s));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`s = "ab?ba"`
`T = ^#a#b#?#b#a#$`
Indices:
0: ^
1: #
2: a
3: #
4: b
5: #
6: ?
7: #
8: b
9: #
10: a
11: #
12: $

Run Manacher:
- `i=6` (center `?`):
  - `match(#, #)` -> P=1
  - `match(b, b)` -> P=2
  - `match(#, #)` -> P=3
  - `match(a, a)` -> P=4
  - `match(#, #)` -> P=5
  - `match(^, $)` -> False.
  - `P[6] = 5`.
  - `maxLen = 5`. `centerIndex = 6`.
  - `start = (6 - 5) / 2 = 0`.
  - Substring `s[0...5]` = "ab?ba".

Result: "ab?ba". Correct.

## ✅ Proof of Correctness

### Invariant

Manacher's algorithm correctly computes the longest palindrome radius at each center `i` provided the comparison function satisfies reflexivity and symmetry relative to the center.
Since `?` matches any character, the condition `s[i] == s[j]` is relaxed to `s[i] == s[j] || s[i] == '?' || s[j] == '?'`.
This relaxation preserves the property that if `P` is a palindrome, any sub-segment centered at `C` is also a palindrome (potentially using the wildcard).
The initialization `P[i] = min(P[mirror], R-i)` provides a valid lower bound because any match established for `mirror` (which might involve `?` or not) is guaranteed to hold for `i` due to the universal matching property of `?`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: K Wildcards**
  - If K is large, Manacher's doesn't work directly because `?` matching `x` on one side implies `?` matching `x` on the other side? No, `?` is just one char.
  - If we have multiple `?`, say `?` at `i` and `?` at `j`.
  - `match(?, ?)` is true.
  - `match(?, x)` is true.
  - So Manacher's STILL works for ANY number of wildcards!
  - The problem "at most one" is a simplification, but the O(N) solution works for any number of wildcards.

### Common Mistakes to Avoid

1. **Matching Separators**
   - ❌ `match(?, #)` returning true.
   - ✅ `?` is a character position, `#` is a boundary. They never match.

2. **Index Mapping**
   - ❌ Incorrectly converting `T` indices back to `s` indices.
   - ✅ `start = (center - maxLen) / 2`.

## Related Concepts

- **Manacher's Algorithm**: The core logic.
- **KMP**: For pattern matching.
