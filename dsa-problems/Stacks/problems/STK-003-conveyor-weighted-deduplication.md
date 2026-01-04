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
    public static class Result {
        public String reducedString;
        public long totalWeight;
        public Result(String s, long w) {
            this.reducedString = s;
            this.totalWeight = w;
        }
    }

    public Result deduplicate(String s, int[] weights) {
        // Implement here
        return new Result("", 0);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            int n = s.length();
            int[] weights = new int[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) weights[i] = sc.nextInt();
            }
            Solution sol = new Solution();
            Solution.Result res = sol.deduplicate(s, weights);
            System.out.println(res.reducedString);
            System.out.println(res.totalWeight);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def deduplicate(self, s: str, weights: list) -> tuple:
        # Implement here
        return ("", 0)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    weights = [int(x) for x in input_data[1:]]
    sol = Solution()
    res_s, res_w = sol.deduplicate(s, weights)
    print(res_s)
    print(res_w)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    pair<string, long long> deduplicate(string s, const vector<int>& weights) {
        // Implement here
        return {"", 0};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        int n = s.length();
        vector<int> weights(n);
        for (int i = 0; i < n; i++) {
            cin >> weights[i];
        }
        Solution sol;
        auto res = sol.deduplicate(s, weights);
        cout << res.first << "\n";
        cout << res.second << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  deduplicate(s, weights) {
    // Implement here
    return { reducedString: "", totalWeight: 0 };
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(line.trim());
}).on("close", () => {
  if (input.length < 2) return;
  const s = input[0];
  const weights = input[1].split(/\s+/).map(Number);
  const sol = new Solution();
  const res = sol.deduplicate(s, weights);
  console.log(res.reducedString);
  console.log(res.totalWeight);
});
```
