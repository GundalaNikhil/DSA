---
problem_id: REC_PALINDROME_PARTITION_MIN_COUNT__3491
display_id: REC-013
slug: palindrome-partition-min-count
title: "Palindrome Partition with Minimum Count"
difficulty: Medium
difficulty_score: 53
topics:
  - Recursion
  - Backtracking
  - Strings
tags:
  - recursion
  - palindrome
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-013: Palindrome Partition with Minimum Count

## Problem Statement

Given a string `s` and a maximum substring length `L`, partition `s` into palindromic substrings of length at most `L` using the minimum possible number of substrings.

Return the lexicographically smallest partition that achieves this minimum (when comparing palindromes at each step from shortest to longest). If no partition is possible, output `NONE`.

![Problem Illustration](../images/REC-013/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `L`

## Output Format

- One line with the lexicographically smallest minimum partition, substrings space-separated
- Output `NONE` if no partition is possible

## Constraints

- `1 <= |s| <= 12`
- `1 <= L <= |s|`
- `s` contains lowercase English letters

## Example

**Input:**

```
aab
2
```

**Output:**

```
aa b
```

**Explanation:**

The minimum number of palindromic substrings is 2: "aa" and "b".

![Example Visualization](../images/REC-013/example-1.png)

## Notes

- Precompute palindrome checks for fast pruning
- Use recursion to explore partitions with length <= L
- Keep track of the current minimum size
- When exploring at each step, try shorter palindromes first to get lexicographically smallest partition
- Among all partitions with minimum count, return the first one found (which will be lexicographically smallest)

## Related Topics

Backtracking, Palindromes, Recursion

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<List<String>> minPalindromePartitions(String s, int L) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int L = sc.nextInt();

        Solution solution = new Solution();
        List<List<String>> result = solution.minPalindromePartitions(s, L);
        if (result.isEmpty()) {
            System.out.println("NONE");
        } else {
            for (List<String> part : result) {
                System.out.println(String.join(" ", part));
            }
        }
        sc.close();
    }
}
```

### Python

```python
def min_palindrome_partitions(s: str, L: int) -> list[list[str]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    L = int(data[1])

    result = min_palindrome_partitions(s, L)
    if not result:
        print("NONE")
    else:
        for part in result:
            print(" ".join(part))

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
    vector<vector<string>> minPalindromePartitions(const string& s, int L) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int L;
    if (!(cin >> s >> L)) return 0;

    Solution solution;
    vector<vector<string>> result = solution.minPalindromePartitions(s, L);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (const auto& part : result) {
            for (int i = 0; i < (int)part.size(); i++) {
                if (i) cout << ' ';
                cout << part[i];
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
  minPalindromePartitions(s, L) {
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
  const s = data[0];
  const L = parseInt(data[1], 10);

  const solution = new Solution();
  const result = solution.minPalindromePartitions(s, L);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.map((part) => part.join(" ")).join("\n"));
  }
});
```
