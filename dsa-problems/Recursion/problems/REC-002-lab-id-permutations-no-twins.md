---
problem_id: REC_LAB_ID_PERMUTATIONS_NO_TWINS__9064
display_id: REC-002
slug: lab-id-permutations-no-twins
title: "Lab ID Permutations With No Adjacent Twins"
difficulty: Easy
difficulty_score: 30
topics:
  - Recursion
  - Backtracking
  - Strings
tags:
  - recursion
  - backtracking
  - permutations
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-002: Lab ID Permutations With No Adjacent Twins

## Problem Statement

Given a string `s` (may contain duplicate characters), generate all unique permutations such that no two identical characters are adjacent. Output permutations in lexicographic order.

![Problem Illustration](../images/REC-002/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Each valid permutation on its own line, in lexicographic order
- If no permutation exists, output `NONE`

## Constraints

- `1 <= |s| <= 8`
- `s` contains lowercase English letters

## Example

**Input:**

```
aab
```

**Output:**

```
aba
```

**Explanation:**

The permutations are `aab`, `aba`, `baa`. Only `aba` avoids adjacent identical letters.

![Example Visualization](../images/REC-002/example-1.png)

## Notes

- Sort the characters and use a visited array for lexicographic order
- Skip duplicates by checking previous identical characters
- Track the last placed character to avoid twins
- Time complexity is bounded by O(n! ) for `n <= 8`

## Related Topics

Backtracking, Permutations, Pruning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<String> generatePermutations(String s) {
        return null;
    }

    private void backtrack(char[] chars, boolean[] used, StringBuilder current, List<String> result) {
        if (current.length() == chars.length) {
            result.add(current.toString());
            return;
        }

        for (int i = 0; i < chars.length; i++) {
            // Skip used characters
            if (used[i]) continue;

            // Skip duplicates: if current is same as previous and previous was not used,
            // it means we are in a new branch for the same character value, which leads to duplicates.
            if (i > 0 && chars[i] == chars[i - 1] && !used[i - 1]) continue;

            // Constraint: No adjacent twins
            if (current.length() > 0 && current.charAt(current.length() - 1) == chars[i]) continue;

            used[i] = true;
            current.append(chars[i]);
            backtrack(chars, used, current, result);
            current.deleteCharAt(current.length() - 1);
            used[i] = false;
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        Solution sol = new Solution();
        List<String> res = sol.generatePermutations(s);
        for(String out_s : res) System.out.println(out_s);
        if(res.isEmpty()) System.out.println("NONE");
        sc.close();
    }
}
```

### Python

```python
def generate_permutations(s: str) -> list[str]:
    return []
def main():
    import sys
    s = sys.stdin.read().strip()
    if not s:
        return

    perms = generate_permutations(s)
    if perms:
        for perm in perms:
            print(perm)
    else:
        print("NONE")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> generatePermutations(string s) {
        return "";
    }

private:
    void backtrack(const string& s, vector<bool>& used, string& current, vector<string>& result) {
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    Solution sol;
    vector<string> res = sol.generatePermutations(s); for(const string& s : res) cout << s << endl; if(res.empty()) cout << "NONE" << endl;
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  generatePermutations(s) {
    return 0;
  }
}

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const sol = new Solution();
    const res = sol.generatePermutations(s);
    if(res.length===0) console.log('NONE'); else res.forEach(s => console.log(s));
});
```

