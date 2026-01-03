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
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Solution sol = new Solution();
        List<String> res = sol.grayCode(n);
        for(String out_s : res) System.out.println(out_s);
        if(res.isEmpty()) System.out.println("NONE");
        sc.close();
    }
}
```

### Python

```python
def gray_code(n: int) -> list[str]:
    # //Implement here
    return 0

def main():
    import sys
    n = int(sys.stdin.read().strip())

    codes = gray_code(n)
    for code in codes:
        print(code)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> grayCode(int n) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    Solution sol;
    vector<string> res = sol.grayCode(n); for(const string& s : res) cout << s << endl; if(res.empty()) cout << "NONE" << endl;
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  grayCode(n) {
    //Implement here
    return 0;
  }
}

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const sol = new Solution();
    const res = sol.grayCode(n);
    if(res.length===0) console.log('NONE'); else res.forEach(s => console.log(s));
});
```

