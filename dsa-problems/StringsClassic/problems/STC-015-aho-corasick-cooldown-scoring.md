---
problem_id: STC_AHO_CORASICK_COOLDOWN__1658
display_id: STC-015
slug: aho-corasick-cooldown-scoring
title: "Aho-Corasick With Cooldown Scoring"
difficulty: Medium
difficulty_score: 60
topics:
  - Strings
  - Aho-Corasick
  - Dynamic Programming
tags:
  - strings
  - aho-corasick
  - dp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STC-015: Aho-Corasick With Cooldown Scoring

## Problem Statement

You are given `k` patterns, each with an integer score, and a text `t`. While scanning `t`, you may choose a subset of pattern occurrences to collect their scores.

If you choose an occurrence that ends at position `r`, then the next chosen occurrence must start at position `>= r + G + 1` (a cooldown of `G` characters after the end).

Return the maximum total score you can collect.

![Problem Illustration](../images/STC-015/problem-illustration.png)

## Input Format

- First line: integer `k`
- Next `k` lines: a pattern string `p_i` and an integer score `w_i`
- Next line: integer `G`
- Last line: text string `t`

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= k <= 100000`
- `1 <= |t| <= 200000`
- Sum of pattern lengths `<= 200000`
- `0 <= w_i <= 1000000`
- `0 <= G <= 1000`
- All strings contain lowercase English letters

## Example

**Input:**

```
2
ab 5
b 2
1
abb
```

**Output:**

```
5
```

**Explanation:**

Matches are "ab" at [1,2] with score 5 and "b" at [2,2] and [3,3] with score 2. Taking "ab" ends at 2, and cooldown `G=1` blocks any chosen match starting at 3, so the best total is 5.

![Example Visualization](../images/STC-015/example-1.png)

## Notes

- Use Aho-Corasick to list all occurrences (end index, start index, score).
- Sort or bucket occurrences by end index for DP transitions.
- This is weighted interval scheduling with a cooldown gap.
- Use 64-bit integers for the DP values.

## Related Topics

Aho-Corasick, Pattern Matching, Dynamic Programming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxScore(int k, String[] patterns, int[] scores, int g, String t) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        String[] patterns = new String[k];
        int[] scores = new int[k];
        for (int i = 0; i < k; i++) {
            patterns[i] = sc.next();
            scores[i] = sc.nextInt();
        }
        if (!sc.hasNextInt()) return;
        int g = sc.nextInt();
        if (!sc.hasNext()) return;
        String t = sc.next();

        Solution solution = new Solution();
        System.out.println(solution.maxScore(k, patterns, scores, g, t));
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    patterns = []
    scores = []
    idx = 1
    for _ in range(k):
        patterns.append(input_data[idx])
        scores.append(int(input_data[idx+1]))
        idx += 2

    g = int(input_data[idx])
    t = input_data[idx+1]

    solution = Solution()
    print(solution.max_score(k, patterns, scores, g, t))

class Solution:
    def max_score(self, k: int, patterns: list, scores: list, g: int, t: str) -> int:
        # Implement here
        return 0

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
    long long maxScore(int k, const vector<string>& patterns, const vector<int>& scores, int g, string t) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int k;
    if (cin >> k) {
        vector<string> patterns(k);
        vector<int> scores(k);
        for (int i = 0; i < k; i++) {
            cin >> patterns[i] >> scores[i];
        }
        int g;
        string t;
        if (cin >> g >> t) {
            Solution sol;
            cout << sol.maxScore(k, patterns, scores, g, t) << endl;
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxScore(k, patterns, scores, g, t) {
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
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 4) return;
  const k = parseInt(input[0]);
  const patterns = [];
  const scores = [];
  let idx = 1;
  for (let i = 0; i < k; i++) {
    patterns.push(input[idx]);
    scores.push(parseInt(input[idx + 1]));
    idx += 2;
  }
  const g = parseInt(input[idx]);
  const t = input[idx + 1];

  const sol = new Solution();
  console.log(sol.maxScore(k, patterns, scores, g, t));
});
```
