---
problem_id: STR_CYCLIC_SHIFT_EQUALITY_CLASSES__1015
display_id: STR-015
slug: cyclic-shift-equality-classes
title: "Cyclic Shift Equality Classes"
difficulty: Medium
difficulty_score: 40
topics:
  - String Manipulation
  - Hashing
  - Equivalence Relations
tags:
  - rotation-equivalence
  - canonical-form
  - booth-algorithm
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-015: Cyclic Shift Equality Classes

## Problem Statement

Given `n` strings, group them into equivalence classes where two strings are equivalent if one is a cyclic shift (rotation) of the other. Return the number of equivalence classes.

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5)
- Next n lines: One string per line (each length ≤ 20)

## Output Format

- A single integer representing the number of equivalence classes

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- Each string length ≤ 20

## Example 1

**Input:**

```
5
ab
ba
abc
bca
cab
```

**Output:**

```
2
```

**Explanation:**

- Class 1: {"ab", "ba"} (rotations of each other)
- Class 2: {"abc", "bca", "cab"} (rotations of each other)

## Example 2

**Input:**

```
3
aaa
aaa
bbb
```

**Output:**

```
2
```

**Explanation:**

- Class 1: {"aaa", "aaa"}
- Class 2: {"bbb"}

## Notes

- Use minimal rotation (Booth's algorithm) as canonical form
- Hash canonical forms to count unique classes
- O(n × m) time where m is max string length

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countEqualityClasses(int n, String[] strings) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            String[] strings = new String[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNext()) strings[i] = sc.next();
            }
            Solution sol = new Solution();
            System.out.println(sol.countEqualityClasses(n, strings));
        }
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
    n = int(input_data[0])
    strings = input_data[1:1+n]
    solution = Solution()
    print(solution.count_equality_classes(n, strings))

class Solution:
    def count_equality_classes(self, n: int, strings: list) -> int:
        # Implement here
        return 0

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int countEqualityClasses(int n, const vector<string>& strings) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<string> strings(n);
        for (int i = 0; i < n; i++) cin >> strings[i];
        Solution sol;
        cout << sol.countEqualityClasses(n, strings) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countEqualityClasses(n, strings) {
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
  input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length > 0) {
    const n = parseInt(input[0]);
    const strings = input.slice(1, 1 + n);
    const sol = new Solution();
    console.log(sol.countEqualityClasses(n, strings));
  }
});
```
