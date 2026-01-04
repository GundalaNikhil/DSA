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
    public void findLadders(String startWord, String endWord, List<String> dictionary) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String startWord = sc.next();
        String endWord = sc.next();
        int m = sc.nextInt();
        List<String> dictionary = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            dictionary.add(sc.next());
        }
        Solution sol = new Solution();
        sol.findLadders(startWord, endWord, dictionary);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_ladders(self, start_word, end_word, dictionary):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    start_word = input_data[0]
    end_word = input_data[1]
    m = int(input_data[2])
    dictionary = input_data[3:3+m]
    sol = Solution()
    sol.find_ladders(start_word, end_word, dictionary)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void findLadders(string startWord, string endWord, const vector<string>& dictionary) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string startWord, endWord;
    if (!(cin >> startWord >> endWord)) return 0;
    int m;
    cin >> m;
    vector<string> dictionary(m);
    for (int i = 0; i < m; i++) cin >> dictionary[i];
    Solution sol;
    sol.findLadders(startWord, endWord, dictionary);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findLadders(startWord, endWord, dictionary) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  const startWord = input[0];
  const endWord = input[1];
  const m = parseInt(input[2]);
  const dictionary = input.slice(3, 3 + m);
  const sol = new Solution();
  sol.findLadders(startWord, endWord, dictionary);
}

solve();
```
