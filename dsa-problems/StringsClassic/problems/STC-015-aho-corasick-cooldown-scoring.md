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
    public long maxCooldownScore(String text, String[] patterns, long[] weights, int g) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int k = sc.nextInt();
        String[] patterns = new String[k];
        long[] weights = new long[k];
        for (int i = 0; i < k; i++) {
            patterns[i] = sc.next();
            weights[i] = sc.nextLong();
        }
        int g = sc.nextInt();
        String text = sc.next();

        Solution solution = new Solution();
        System.out.println(solution.maxCooldownScore(text, patterns, weights, g));
        sc.close();
    }
}
```

### Python

```python
def max_cooldown_score(text: str, patterns: list[str], weights: list[int], g: int) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    k = int(data[idx]); idx += 1
    patterns = []
    weights = []
    for _ in range(k):
        patterns.append(data[idx]); idx += 1
        weights.append(int(data[idx])); idx += 1
    g = int(data[idx]); idx += 1
    text = data[idx] if idx < len(data) else ""
    print(max_cooldown_score(text, patterns, weights, g))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    long long maxCooldownScore(const string& text, const vector<string>& patterns,
                               const vector<long long>& weights, int g) {
        // Your implementation here
        return 0LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    vector<string> patterns(k);
    vector<long long> weights(k);
    for (int i = 0; i < k; i++) {
        cin >> patterns[i] >> weights[i];
    }
    int g;
    cin >> g;
    string text;
    cin >> text;

    Solution solution;
    cout << solution.maxCooldownScore(text, patterns, weights, g) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxCooldownScore(text, patterns, weights, g) {
    // Your implementation here
    return 0;
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
  const k = parseInt(data[idx++], 10);
  const patterns = [];
  const weights = [];
  for (let i = 0; i < k; i++) {
    patterns.push(data[idx++]);
    weights.push(parseInt(data[idx++], 10));
  }
  const g = parseInt(data[idx++], 10);
  const text = data[idx] || "";

  const solution = new Solution();
  console.log(solution.maxCooldownScore(text, patterns, weights, g).toString());
});
```
