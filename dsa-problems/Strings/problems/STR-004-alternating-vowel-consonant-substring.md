---
problem_id: STR_ALTERNATING_VOWEL_CONSONANT_SUBSTRING__1004
display_id: STR-004
slug: alternating-vowel-consonant-substring
title: "Alternating Vowel-Consonant Substring"
difficulty: Easy-Medium
difficulty_score: 32
topics:
  - String Manipulation
  - Sliding Window
tags:
  - pattern-matching
  - vowel-consonant
  - substring
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-004: Alternating Vowel-Consonant Substring

## Problem Statement

Given a string `s` of lowercase English letters, find the longest substring where vowels and consonants strictly alternate. Treat 'y' as a consonant.

Return both the length and one such longest substring.

## Input Format

- A single string `s` (1 ≤ |s| ≤ 2 × 10^5)

## Output Format

- First line: Integer representing the length
- Second line: One longest alternating substring

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `s` contains only lowercase English letters
- Vowels: a, e, i, o, u (y is consonant)

## Example 1

**Input:**

```
abracadabra
```

**Output:**

```
3
ada
```

**Explanation:**

- "ada" has alternating pattern: a(vowel), d(consonant), a(vowel)
- Length 3 is the maximum alternating substring

## Example 2

**Input:**

```
aaa
```

**Output:**

```
1
a
```

**Explanation:**

- No alternating pattern possible with all vowels
- Single character has length 1

## Notes

- Use sliding window with reset on pattern break
- O(n) time complexity with single pass
- Track current alternation status with boolean flag

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private boolean isVowel(char c) {
        return false;
    }

    public Object[] longestAlternatingVC(String s) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.useDelimiter("\\A").hasNext() ? sc.next() : "";
        s = s.trim();
        Solution sol = new Solution();
        Object[] res = sol.longestAlternatingVC(s);
        System.out.println(res[0]);
        System.out.println(res[1]);
        sc.close();
    }
}
```

### Python

```python
def longest_alternating_vc(s: str) -> tuple:
    return 0
def main():
    import sys
    # Read input string
    input_data = sys.stdin.read().strip()
    if not input_data:
        # Handle empty input if necessary
        print("0")
        print("")
        return
        
    # Call solution
    length, substring = longest_alternating_vc(input_data)
    
    # Print result
    print(length)
    print(substring)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

class Solution {
    bool isVowel(char c) {
        return false;
    }
public:
    pair<int, string> longestAlternatingVC(string s) {
        if (s.empty()) return {0, ""};

        int maxLen = 1;
        int bestStart = 0;
        int currentLen = 1;
        int start = 0;
        bool prevIsVowel = isVowel(s[0]);

        for (int i = 1; i < s.length(); i++) {
            bool currIsVowel = isVowel(s[i]);
            if (currIsVowel != prevIsVowel) {
                currentLen++;
                if (currentLen > maxLen) {
                    maxLen = currentLen;
                    bestStart = start;
                }
            } else {
                start = i;
                currentLen = 1;
            }
            prevIsVowel = currIsVowel;
        }

        return {maxLen, s.substr(bestStart, maxLen)};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    while(!s.empty() && isspace(s.back())) s.pop_back();
    while(!s.empty() && isspace(s.front())) s.erase(0, 1);
    Solution sol;
    pair<int, string> res = sol.longestAlternatingVC(s); cout << res.first << endl; cout << res.second << endl;
    return 0;
}
```

### JavaScript

```javascript
function longestAlternatingVC(s) {
    return 0;
  }

const fs = require('fs');
const s = fs.readFileSync(0, 'utf-8').trim();
const res = longestAlternatingVC(s);
console.log(res[0]);
console.log(res[1]);
```

