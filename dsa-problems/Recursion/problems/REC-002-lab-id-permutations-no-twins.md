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
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        Solution solution = new Solution();
        List<String> result = solution.generatePermutations(s);
        if (result.isEmpty()) {
            System.out.println("NONE");
        } else {
            for (String line : result) {
                System.out.println(line);
            }
        }
        sc.close();
    }
}
```

### Python

```python
def generate_permutations(s: str) -> list[str]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    result = generate_permutations(s)
    if not result:
        print("NONE")
    else:
        print("\n".join(result))

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
    vector<string> generatePermutations(const string& s) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    Solution solution;
    vector<string> result = solution.generatePermutations(s);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        for (const string& line : result) {
            cout << line << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  generatePermutations(s) {
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
  const solution = new Solution();
  const result = solution.generatePermutations(s);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result.join("\n"));
  }
});
```
