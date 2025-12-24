---
problem_id: STK_CONVEYOR_WEIGHTED_DEDUPLICATION__5318
display_id: STK-003
slug: conveyor-weighted-deduplication
title: "Conveyor Weighted Deduplication"
difficulty: Easy
difficulty_score: 36
topics:
  - Stack
  - Simulation
  - Strings
tags:
  - stack
  - simulation
  - strings
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-003: Conveyor Weighted Deduplication

## Problem Statement

You are given a string `s` and an array of weights `w` of the same length. Process characters from left to right. When the current character matches the top of the stack, you may remove the pair only if the sum of their weights is even. The removed sum is added to a running total. The remaining characters form the reduced string.

Output the reduced string and the total removed weight.

![Problem Illustration](../images/STK-003/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: `n` space-separated integers `w[i]` (where `n = |s|`)

## Output Format

- First line: reduced string
- Second line: total removed weight

## Constraints

- `1 <= |s| <= 200000`
- `1 <= w[i] <= 1000`

## Example

**Input:**

```
xxyyz
1 3 2 2 5
```

**Output:**

```
xyz
4
```

**Explanation:**

The pair `y` with weights 2 and 2 is removed, contributing 4 to the total.

![Example Visualization](../images/STK-003/example-1.png)

## Notes

- Use a stack of (char, weight)
- Only adjacent equal characters can be removed
- Each character is pushed and popped at most once
- Time complexity: O(n)

## Related Topics

Stack, Simulation, String Processing

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public String[] reduce(String s, int[] w) {
        // Your implementation here
        return new String[]{"", "0"};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int n = s.length();
        int[] w = new int[n];
        for (int i = 0; i < n; i++) w[i] = sc.nextInt();

        Solution solution = new Solution();
        String[] result = solution.reduce(s, w);
        System.out.println(result[0]);
        System.out.println(result[1]);
        sc.close();
    }
}
```

### Python

```python
def reduce_stack(s: str, w: list[int]) -> tuple[str, int]:
    # Your implementation here
    return "", 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    w = [int(x) for x in data[1:1+len(s)]]

    reduced, total = reduce_stack(s, w)
    print(reduced)
    print(total)

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
    pair<string,long long> reduce(const string& s, const vector<int>& w) {
        // Your implementation here
        return {"", 0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int n = s.size();
    vector<int> w(n);
    for (int i = 0; i < n; i++) cin >> w[i];

    Solution solution;
    auto result = solution.reduce(s, w);
    cout << result.first << "\n" << result.second << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  reduce(s, w) {
    // Your implementation here
    return ["", "0"];
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
  const w = [];
  for (let i = 0; i < s.length; i++) w.push(parseInt(data[1 + i], 10));

  const solution = new Solution();
  const result = solution.reduce(s, w);
  console.log(result[0]);
  console.log(result[1]);
});
```
