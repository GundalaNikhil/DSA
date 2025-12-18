---
problem_id: DP_KB_EDIT_SHIFT__3179
display_id: DP-005
slug: keyboard-row-edit-distance-shift
title: "Keyboard Row Edit Distance with Shift Penalty"
difficulty: Medium
difficulty_score: 60
topics:
  - Dynamic Programming
  - String DP
  - Edit Distance
tags:
  - dp
  - strings
  - edit-distance
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-005: Keyboard Row Edit Distance with Shift Penalty

## Problem Statement

You are given two lowercase strings `a` and `b`. You want to convert `a` into `b` using the following operations:

1. **Insert** one character (cost = 1)
2. **Delete** one character (cost = 1)
3. **Replace** one character `x` with another character `y` (cost depends on keyboard position):
   - cost = 1 if `x` and `y` are on the **same keyboard row**
   - cost = 2 if they are on **different rows** but typed with the **same hand**
   - cost = 3 otherwise (different rows and different hands)

Keyboard rows (QWERTY):

- Row 1: `qwertyuiop`
- Row 2: `asdfghjkl`
- Row 3: `zxcvbnm`

Hands (fixed for this problem):

- Left hand: `qwertasdfgzxcvb`
- Right hand: `yuiophjklnm`

Compute the minimum total cost to convert `a` to `b`.

![Problem Illustration](../images/DP-005/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`

## Output Format

Print one integer: the minimum conversion cost.

## Constraints

- `0 <= len(a), len(b) <= 2000`
- `a` and `b` contain only lowercase English letters `a..z`

## Example

**Input:**
```
type
tap
```

**Output:**
```
3
```

**Explanation:**

One optimal sequence:

- Insert `a` after `t` (cost 1): `type -> taype`
- Delete `y` (cost 1): `taype -> tape`
- Delete `e` (cost 1): `tape -> tap`

Total cost = `1 + 1 + 1 = 3`.

![Example Visualization](../images/DP-005/example-1.png)

## Notes

- Replacing a character with itself costs 0 (no operation).
- This is a weighted version of classic edit distance (Levenshtein distance).

## Related Topics

Dynamic Programming, Edit Distance, String DP

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minKeyboardEditCost(String a, String b) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine().trim();
        String b = sc.nextLine().trim();
        System.out.println(new Solution().minKeyboardEditCost(a, b));
        sc.close();
    }
}
```

### Python

```python
def min_keyboard_edit_cost(a: str, b: str) -> int:
    # Your implementation here
    return 0

def main():
    a = input().strip()
    b = input().strip()
    print(min_keyboard_edit_cost(a, b))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int minKeyboardEditCost(const string& a, const string& b) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    getline(cin, a);
    getline(cin, b);
    Solution sol;
    cout << sol.minKeyboardEditCost(a, b) << "\\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minKeyboardEditCost(a, b) {
    // Your implementation here
    return 0;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line));
rl.on("close", () => {
  const a = (lines[0] ?? \"\").trim();
  const b = (lines[1] ?? \"\").trim();
  const sol = new Solution();
  console.log(sol.minKeyboardEditCost(a, b));
});
```
