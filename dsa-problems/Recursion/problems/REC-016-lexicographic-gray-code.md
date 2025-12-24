---
problem_id: REC_LEXICOGRAPHIC_GRAY_CODE__6685
display_id: REC-016
slug: lexicographic-gray-code
title: "Lexicographic Gray Code"
difficulty: Medium
difficulty_score: 45
topics:
  - Recursion
  - Bit Manipulation
  - Gray Code
tags:
  - recursion
  - gray-code
  - bitwise
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-016: Lexicographic Gray Code

## Problem Statement

Generate an `n`-bit Gray code sequence using the standard recursive construction: prefix `0` to the previous sequence and prefix `1` to the reverse of the previous sequence.

Output the resulting sequence in order, one code per line.

![Problem Illustration](../images/REC-016/problem-illustration.png)

## Input Format

- First line: integer `n`

## Output Format

- `2^n` lines, each an `n`-bit string

## Constraints

- `1 <= n <= 12`

## Example

**Input:**

```
2
```

**Output:**

```
00
01
11
10
```

**Explanation:**

The recursive Gray code for `n=2` is `00, 01, 11, 10`.

![Example Visualization](../images/REC-016/example-1.png)

## Notes

- Base case: `n=1` yields `0, 1`
- Each consecutive pair differs by exactly one bit
- The sequence size is `2^n`
- Recursion makes the construction straightforward

## Related Topics

Gray Code, Recursion, Bit Manipulation

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<String> grayCode(int n) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Solution solution = new Solution();
        List<String> result = solution.grayCode(n);
        for (String line : result) {
            System.out.println(line);
        }
        sc.close();
    }
}
```

### Python

```python
def gray_code(n: int) -> list[str]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])

    result = gray_code(n)
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
    vector<string> grayCode(int n) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    Solution solution;
    vector<string> result = solution.grayCode(n);
    for (const string& line : result) {
        cout << line << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  grayCode(n) {
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
  const n = parseInt(data[0], 10);

  const solution = new Solution();
  const result = solution.grayCode(n);
  console.log(result.join("\n"));
});
```
