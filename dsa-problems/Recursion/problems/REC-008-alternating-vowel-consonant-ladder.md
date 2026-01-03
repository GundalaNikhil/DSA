---
problem_id: REC_ALTERNATING_VOWEL_CONSONANT_LADDER__6073
display_id: REC-008
slug: alternating-vowel-consonant-ladder
title: "Alternating Vowel-Consonant Ladder"
difficulty: Medium
difficulty_score: 54
topics:
  - Recursion
  - Backtracking
  - Graphs
tags:
  - recursion
  - word-ladder
  - bfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-008: Alternating Vowel-Consonant Ladder

## Problem Statement

Given a start word, an end word, and a dictionary, find all shortest transformation sequences where each step changes exactly one letter and remains in the dictionary.

Additionally, the first letter of successive words must alternate between vowel-start and consonant-start. Return all shortest valid ladders.

![Problem Illustration](../images/REC-008/problem-illustration.png)

## Input Format

- First line: start word
- Second line: end word
- Third line: integer `m` (dictionary size)
- Next `m` lines: dictionary words

## Output Format

- Each shortest ladder on its own line (words space-separated)
- Output `NONE` if no ladder exists

## Constraints

- `1 <= |word| <= 6`
- `1 <= m <= 3000`
- All words are lowercase and of equal length

## Example

**Input:**

```
eat
cot
4
eat
cat
cot
eot
```

**Output:**

```
eat cat cot
eat eot cot
```

**Explanation:**

Both sequences have length 3 and alternate vowel-start/consonant-start at each step.

![Example Visualization](../images/REC-008/example-1.png)

## Notes

- Use BFS to find the shortest distance levels
- Use backtracking to enumerate all shortest paths
- The start and end words may appear in the dictionary
- Treat vowels as `a, e, i, o, u`

## Related Topics

BFS, Backtracking, Word Ladder

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<String> getAlternatingPermutations(String s) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNext()) return;
        String s = sc.next();
        
        Solution sol = new Solution();
        List<String> res = sol.getAlternatingPermutations(s);
        if(res.isEmpty()) {
            System.out.println("NONE");
        } else {
            for(String p : res) System.out.println(p);
        }
        sc.close();
    }
}
```

### Python

```python
def get_alternating_permutations(s: str) -> list[str]:
    # //Implement here
    return 0

def main():
    import sys
    s = sys.stdin.read().strip()
    results = get_alternating_permutations(s)
    if results:
        for perm in results:
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
#include <set>

using namespace std;

class Solution {
public:
    vector<string> getAlternatingPermutations(string s) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    
    Solution sol;
    vector<string> res = sol.getAlternatingPermutations(s);
    if(res.empty()) {
        cout << "NONE" << endl;
    } else {
        for(const string& p : res) cout << p << endl;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    
    const sol = new Solution();
    const res = sol.getAlternatingPermutations(s);
    
    if(res.length === 0) {
        console.log("NONE");
    } else {
        res.forEach(p => console.log(p));
    }
});

class Solution {
  getAlternatingPermutations(s) {
    //Implement here
    return 0;
  }
}
```

