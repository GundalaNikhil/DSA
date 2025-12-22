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
    public List<List<String>> ladders(String start, String end, List<String> dict) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String start = sc.next();
        String end = sc.next();
        int m = sc.nextInt();
        List<String> dict = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            dict.add(sc.next());
        }

        Solution solution = new Solution();
        List<List<String>> result = solution.ladders(start, end, dict);
        if (result.isEmpty()) {
            System.out.println("NONE");
        } else {
            for (List<String> path : result) {
                System.out.println(String.join(" ", path));
            }
        }
        sc.close();
    }
}
```

### Python

```python
def ladders(start: str, end: str, dict_words: list[str]) -> list[list[str]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    start = next(it)
    end = next(it)
    m = int(next(it))
    dict_words = [next(it) for _ in range(m)]

    result = ladders(start, end, dict_words)
    if not result:
        print("NONE")
    else:
        for path in result:
            print(" ".join(path))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<string>> ladders(const string& start, const string& end, const vector<string>& dict) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string start, end;
    if (!(cin >> start >> end)) return 0;
    int m;
    cin >> m;
    vector<string> dict(m);
    for (int i = 0; i < m; i++) cin >> dict[i];

    Solution solution;
    vector<vector<string>> result = solution.ladders(start, end, dict);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (const auto& path : result) {
            for (int i = 0; i < (int)path.size(); i++) {
                if (i) cout << ' ';
                cout << path[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  ladders(start, end, dict) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const start = data[idx++];
  const end = data[idx++];
  const m = parseInt(data[idx++], 10);
  const dict = [];
  for (let i = 0; i < m; i++) dict.push(data[idx++]);

  const solution = new Solution();
  const result = solution.ladders(start, end, dict);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.map((path) => path.join(" ")).join("\n"));
  }
});
```
