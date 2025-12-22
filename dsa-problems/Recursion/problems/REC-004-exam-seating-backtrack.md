---
problem_id: REC_EXAM_SEATING_BACKTRACK__6392
display_id: REC-004
slug: exam-seating-backtrack
title: "Exam Seating Backtrack"
difficulty: Medium
difficulty_score: 44
topics:
  - Recursion
  - Backtracking
  - Combinatorics
tags:
  - recursion
  - backtracking
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-004: Exam Seating Backtrack

## Problem Statement

An exam hall has `n` seats in a single row, indexed `0` to `n-1`. You must place exactly `k` students so that any two students have at least `d` empty seats between them.

Count how many valid arrangements are possible.

![Problem Illustration](../images/REC-004/problem-illustration.png)

## Input Format

- First line: three integers `n`, `k`, and `d`

## Output Format

- Single integer: number of valid arrangements

## Constraints

- `1 <= n <= 15`
- `0 <= k <= n`
- `0 <= d <= n`

## Example

**Input:**

```
5 2 2
```

**Output:**

```
3
```

**Explanation:**

With at least 2 empty seats between students, valid pairs are (0,3), (0,4), (1,4).

![Example Visualization](../images/REC-004/example-1.png)

## Notes

- If positions are `i < j`, then `j - i - 1 >= d`
- Use recursion to choose the next valid seat index
- Prune when remaining seats are insufficient
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinatorics, Recursion

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public long countArrangements(int n, int k, int d) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int d = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countArrangements(n, k, d));
        sc.close();
    }
}
```

### Python

```python
def count_arrangements(n: int, k: int, d: int) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, k, d = map(int, data[:3])
    print(count_arrangements(n, k, d))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    long long countArrangements(int n, int k, int d) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, d;
    if (!(cin >> n >> k >> d)) return 0;
    Solution solution;
    cout << solution.countArrangements(n, k, d) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countArrangements(n, k, d) {
    // Your implementation here
    return 0;
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
  const k = parseInt(data[1], 10);
  const d = parseInt(data[2], 10);
  const solution = new Solution();
  console.log(solution.countArrangements(n, k, d).toString());
});
```
