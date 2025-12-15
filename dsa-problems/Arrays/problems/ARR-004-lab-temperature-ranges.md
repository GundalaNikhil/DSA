---
problem_id: ARR_DIFF_ARRAY__53AA
display_id: ARR-004
slug: lab-temperature-ranges
title: "Lab Temperature Offline Ranges"
difficulty: Medium
difficulty_score: 50
topics:
  - Array
  - Difference Array
  - Range Queries
tags:
  - arrays
  - difference-array
  - range-queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Lab Temperature Offline Ranges

## Problem Statement

Given a temperature array and queries, some queries are type "add x to range [l,r]" (offline, applied cumulatively), others ask for range sum after all adds. Return answers to sum queries.

![Problem Illustration](../images/ARR-004/problem-illustration.png)


## Input Format

- First line: Integer `n` (1 ≤ n ≤ 10^5) - size of array
- Second line: `n` space-separated integers representing temperatures
- Third line: Integer `q` (1 ≤ q ≤ 10^5) - number of queries
- Next `q` lines: Either "add l r x" or "sum l r"

## Output Format

Print the answers to sum queries, one per line.

## Constraints

- 1 ≤ n, q ≤ 10^5
- -10^9 ≤ temp[i], x ≤ 10^9
- 0 ≤ l ≤ r < n
- All add queries are processed before sum queries

## Examples

### Example 1

**Input:**

```
3
1 2 3
4
add 0 1 5
sum 0 2
add 2 2 -1
sum 1 2
```

**Output:**

```
16
9
```

**Explanation:**

- Initial temps: [1, 2, 3]
- After "add 0 1 5": [6, 7, 3]
- "sum 0 2": 6 + 7 + 3 = 16
- After "add 2 2 -1": [6, 7, 2]
- "sum 1 2": 7 + 2 = 9

![Example 1 Visualization](../images/ARR-004/example-1.png)

### Example 2

**Input:**

```
3
5 5 5
2
add 0 2 3
sum 0 2
```

**Output:**

```
24
```

**Explanation:**

- Initial temps: [5, 5, 5]
- After "add 0 2 3": [8, 8, 8]
- "sum 0 2": 8 + 8 + 8 = 24

## Notes

- Use difference array to accumulate adds, then prefix for final temps before answering sums with prefix sums
- All add queries are processed before sum queries are answered

## Related Topics

Array, Difference Array, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] processQueries(int[] temps, String[][] queries) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] temps = new int[n];
        for (int i = 0; i < n; i++) {
            temps[i] = sc.nextInt();
        }
        int q = sc.nextInt();
        String[][] queries = new String[q][];
        for (int i = 0; i < q; i++) {
            String type = sc.next();
            if (type.equals("add")) {
                queries[i] = new String[]{type, sc.next(), sc.next(), sc.next()};
            } else {
                queries[i] = new String[]{type, sc.next(), sc.next()};
            }
        }

        Solution solution = new Solution();
        long[] result = solution.processQueries(temps, queries);

        for (long val : result) {
            System.out.println(val);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List, Tuple

def process_queries(temps: List[int], queries: List[Tuple]) -> List[int]:
    # Your implementation here
    pass

def main():
    n = int(input())
    temps = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        parts = input().split()
        queries.append(tuple(parts))
    result = process_queries(temps, queries)
    for val in result:
        print(val)

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
    vector<long long> processQueries(vector<int>& temps, vector<vector<string>>& queries) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> temps(n);
    for (int i = 0; i < n; i++) {
        cin >> temps[i];
    }
    int q;
    cin >> q;
    vector<vector<string>> queries(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "add") {
            string l, r, val;
            cin >> l >> r >> val;
            queries[i] = {type, l, r, val};
        } else {
            string l, r;
            cin >> l >> r;
            queries[i] = {type, l, r};
        }
    }

    Solution solution;
    vector<long long> result = solution.processQueries(temps, queries);

    for (long long val : result) {
        cout << val << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    processQueries(temps, queries) {
        // Your implementation here
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];
let lineIndex = 0;

rl.on('line', (line) => {
    lines.push(line);
});

rl.on('close', () => {
    const n = parseInt(lines[lineIndex++]);
    const temps = lines[lineIndex++].split(' ').map(Number);
    const q = parseInt(lines[lineIndex++]);
    const queries = [];
    for (let i = 0; i < q; i++) {
        queries.push(lines[lineIndex++].split(' '));
    }

    const solution = new Solution();
    const result = solution.processQueries(temps, queries);

    result.forEach(val => console.log(val));
});
```
