---
problem_id: TRI_SHORTEST_ABSENT_BINARY__7241
display_id: TRI-013
slug: shortest-absent-binary-length-l
title: "Shortest Absent Binary String of Length L"
difficulty: Medium
difficulty_score: 52
topics:
  - Trie
  - Binary String
  - Backtracking
tags:
  - trie
  - binary
  - lexicographic
  - missing-element
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-013: Shortest Absent Binary String of Length L

## Problem Statement

Given a set of binary strings all of length exactly `L`, find the lexicographically smallest binary string of length `L` that is NOT present in the set. If all possible strings of length `L` are present, return an empty string.

![Problem Illustration](../images/TRI-013/problem-illustration.png)

## Input Format

- First line: two integers `L` (length) and `n` (number of binary strings)
- Next `n` lines: each contains a binary string of length exactly `L`

## Output Format

Return the lexicographically smallest missing binary string of length `L`, or an empty string if all are present.

## Constraints

- `1 <= L <= 20`
- `0 <= n <= 2^L` (set size cannot exceed total possibilities)
- All input strings have length exactly `L`
- Input strings consist only of '0' and '1'
- No duplicate strings in input

## Example

**Input:**

```
2 2
00
01
```

**Output:**

```
10
```

**Explanation:**

All possible binary strings of length 2: `["00", "01", "10", "11"]`

Given set: `{"00", "01"}`

Missing strings: `{"10", "11"}`

Lexicographically smallest missing: `"10"` (comes before "11")

![Example Visualization](../images/TRI-013/example-1.png)

## Notes

- Lexicographic order for binary strings: "00" < "01" < "10" < "11"
- If `n = 2^L`, all possible strings are present, return empty string
- Use a binary trie for efficient missing string detection
- DFS traversal in lexicographic order (explore '0' child before '1' child)

## Related Topics

Trie, Binary String, Lexicographic Order, DFS, Coding Theory

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String findShortestAbsent(String[] binaryStrings, int L) {
        // Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int L = sc.nextInt();
        int n = sc.nextInt();

        String[] binaryStrings = new String[n];
        for (int i = 0; i < n; i++) {
            binaryStrings[i] = sc.next();
        }

        Solution solution = new Solution();
        String result = solution.findShortestAbsent(binaryStrings, L);
        System.out.println(result);
    }
}
```

### Python

```python
from typing import List

class Solution:
    def find_shortest_absent(self, binary_strings: List[str], L: int) -> str:
        # Implement here
        return ""

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    L = int(input_data[0])
    n = int(input_data[1])
    binary_strings = input_data[2:n+2]

    solution = Solution()
    result = solution.find_shortest_absent(binary_strings, L)
    print(result)

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
    string findShortestAbsent(const vector<string>& binaryStrings, int L) {
        // Implement here
        return "";
    }
};

int main() {
    int L, n;
    if (!(cin >> L >> n)) return 0;

    vector<string> binaryStrings(n);
    for (int i = 0; i < n; i++) {
        cin >> binaryStrings[i];
    }

    Solution solution;
    string result = solution.findShortestAbsent(binaryStrings, L);
    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findShortestAbsent(binaryStrings, L) {
    // Implement here
    return "";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  const L = parseInt(tokens[0]);
  const n = parseInt(tokens[1]);
  const binaryStrings = tokens.slice(2, n + 2);

  const solution = new Solution();
  const result = solution.findShortestAbsent(binaryStrings, L);
  process.stdout.write(result + "\n");
});
```
