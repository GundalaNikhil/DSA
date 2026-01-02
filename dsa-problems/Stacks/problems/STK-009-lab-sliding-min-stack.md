---
problem_id: STK_LAB_SLIDING_MIN_STACK__5027
display_id: STK-009
slug: lab-sliding-min-stack
title: "Lab Sliding-Min Stack"
difficulty: Medium
difficulty_score: 52
topics:
  - Stack
  - Range Minimum
  - Data Structures
tags:
  - stack
  - min-stack
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-009: Lab Sliding-Min Stack

## Problem Statement

Maintain a stack with operations:

- `PUSH x`
- `POP`: remove and output top value
- `MIN k`: output the minimum among the top `k` elements (top counts as 1)

If `POP` is called on an empty stack, output `EMPTY`. If `MIN k` is requested with fewer than `k` elements, output `NA`.

![Problem Illustration](../images/STK-009/problem-illustration.png)

## Input Format

- First line: integer `m`
- Next `m` lines: commands as above

## Output Format

- For each `POP` and `MIN`, output one line with the result

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`
- `1 <= k <= 100000`

## Example

**Input:**

```
6
PUSH 5
PUSH 1
PUSH 3
MIN 2
POP
MIN 2
```

**Output:**

```
1
3
1
```

**Explanation:**

Top 2 elements are [1,3], min is 1. POP removes 3. Top 2 are [5,1], min is 1.

![Example Visualization](../images/STK-009/example-1.png)

## Notes

- Store prefix mins to answer `MIN` quickly
- Use an auxiliary stack of minimums with counts
- Keep size to validate `MIN k`
- Time complexity per operation: O(1) amortized

## Related Topics

Stack, Min Stack, Range Queries

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    int[] tree;
    int n = 100005;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return Integer.MAX_VALUE;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        return Math.min(query(2 * node, start, mid, l, r),
                        query(2 * node + 1, mid + 1, end, l, r));
    }

    public List<String> process(List<String[]> ops) {
        return null;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line == null) return;
        int m = Integer.parseInt(line.trim());
        
        List<String[]> ops = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String l = br.readLine();
            if (l != null) {
                ops.add(l.trim().split("\\s+"));
            }
        }
        
        Solution sol = new Solution();
        List<String> res = sol.process(ops);
        for (String s : res) {
            System.out.println(s);
        }
    }
}
```

### Python

```python
def process(ops: list[list[str]]) -> list[str]:
    return []
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    m = int(lines[0])
    ops = []
    for i in range(1, m + 1):
        parts = lines[i].split()
        ops.append(parts)

    result = process(ops)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    vector<int> tree;
    int n = 100005;

    void update(int node, int start, int end, int idx, int val) {
    }

    int query(int node, int start, int end, int l, int r) {
        return 0;
    }

public:
    vector<string> process(const vector<vector<string>>& ops) {
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int m;
    if (!(cin >> m)) return 0;
    
    vector<vector<string>> ops;
    string method;
    
    for (int i = 0; i < m; i++) {
        cin >> method;
        if (method == "PUSH" || method == "MIN") {
            string val;
            cin >> val;
            ops.push_back({method, val});
        } else {
            ops.push_back({method});
        }
    }
    
    Solution sol;
    vector<string> res = sol.process(ops);
    
    for (const string& s : res) {
        cout << s << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  update(node, start, end, idx, val) {
    return 0;
  }

  query(node, start, end, l, r) {
    return 0;
  }

  process(ops) {
    return 0;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length === 0) return;
  
  const m = parseInt(lines[0].trim(), 10);
  const ops = [];
  
  for (let i = 1; i <= m; i++) {
    if (i < lines.length) {
      ops.push(lines[i].trim().split(/\s+/));
    }
  }
  
  const solution = new Solution();
  const res = solution.process(ops);
  console.log(res.join("\n"));
});
```

