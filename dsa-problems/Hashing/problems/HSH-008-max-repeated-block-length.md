---
problem_id: HSH_MAX_REPEATED_BLOCK_LENGTH__5827
display_id: HSH-008
slug: max-repeated-block-length
title: "Maximum Repeated Block Length"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - Binary Search
  - String Algorithms
tags:
  - hashing
  - binary-search
  - substring
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-008: Maximum Repeated Block Length

## Problem Statement

Find the longest length `L` such that there exist two non-overlapping substrings of length `L` that are equal.

Given a string `s`, determine the maximum length of a substring that appears at least twice without overlapping.

![Problem Illustration](../images/HSH-008/problem-illustration.png)

## Input Format

- Single line: string `s`

## Output Format

- Single integer: maximum length of repeated non-overlapping substring

## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
abcabc
```

**Output:**

```
3
```

**Explanation:**

String: "abcabc"

The substring "abc" appears at positions 0-2 and 3-5 (non-overlapping).
Length: 3

![Example Visualization](../images/HSH-008/example-1.png)

## Notes

- Use binary search on the answer (length L)
- For each candidate length, check if any substring of that length appears twice non-overlapping
- Use hashing to compare substrings efficiently
- Track positions to ensure non-overlapping constraint
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Binary Search, Hashing, Rolling Hash, Longest Repeated Substring

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxRepeatedBlockLength(String s) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        Solution solution = new Solution();
        System.out.println(solution.maxRepeatedBlockLength(s));
        sc.close();
    }
}
```

### Python

```python
def max_repeated_block_length(s: str) -> int:
    # Your implementation here
    return 0

def main():
    s = input().strip()
    result = max_repeated_block_length(s)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int maxRepeatedBlockLength(string s) {
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
    cout << solution.maxRepeatedBlockLength(s) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxRepeatedBlockLength(s) {
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
  console.log(solution.maxRepeatedBlockLength(s));
});
```
