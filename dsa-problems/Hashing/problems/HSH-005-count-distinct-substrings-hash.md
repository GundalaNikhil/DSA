---
problem_id: HSH_COUNT_DISTINCT_SUBSTRINGS__8741
display_id: HSH-005
slug: count-distinct-substrings-hash
title: "Count Distinct Substrings"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - String Algorithms
  - Set Operations
tags:
  - hashing
  - substring
  - distinct
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-005: Count Distinct Substrings

## Problem Statement

Given a string `s`, count the number of distinct substrings (including the empty string) using polynomial hashing.

A substring is a contiguous sequence of characters within the string. Two substrings are considered the same if they have identical characters in the same order.

![Problem Illustration](../images/HSH-005/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single integer: number of distinct substrings

## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
aaa
```

**Output:**

```
4
```

**Explanation:**

String: "aaa"

All substrings:

- "" (empty) - 1 distinct
- "a" (positions 0, 1, 2) - 1 distinct
- "aa" (positions 0-1, 1-2) - 1 distinct
- "aaa" (position 0-2) - 1 distinct

Total distinct: 4

![Example Visualization](../images/HSH-005/example-1.png)

## Notes

- Generate all O(n²) substrings
- Compute hash for each substring
- Use a set to store unique hashes
- Use double hashing to minimize collisions
- Time complexity: O(n²)
- Space complexity: O(n²)

## Related Topics

Hashing, Substring Generation, Set Operations, Suffix Array

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countDistinctSubstrings(String s) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        Solution solution = new Solution();
        System.out.println(solution.countDistinctSubstrings(s));
        sc.close();
    }
}
```

### Python

```python
def count_distinct_substrings(s: str) -> int:
    # Your implementation here
    return 0

def main():
    s = input().strip()
    result = count_distinct_substrings(s)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int countDistinctSubstrings(string s) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);

    Solution solution;
    cout << solution.countDistinctSubstrings(s) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countDistinctSubstrings(s) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const s = data[0];

  const solution = new Solution();
  console.log(solution.countDistinctSubstrings(s));
});
```
