---
problem_id: QUE_EVENT_REGISTRATION_MERGE__6205
display_id: QUE-011
slug: event-registration-merge
title: "Event Registration Merge"
difficulty: Easy
difficulty_score: 22
topics:
  - Queue
  - Merge
  - Two Pointers
tags:
  - queue
  - merge
  - two-pointers
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-011: Event Registration Merge

## Problem Statement

Two event registration lines are already sorted by registration ID. Merge the two queues into one sorted queue while preserving the order of equal IDs.

![Problem Illustration](../images/QUE-011/problem-illustration.png)

## Input Format

- First line: integer `n` (length of first queue)
- Second line: `n` space-separated integers (first queue)
- Third line: integer `m` (length of second queue)
- Fourth line: `m` space-separated integers (second queue)

## Output Format

- Single line: merged queue values in nondecreasing order
- If both queues are empty, print an empty line

## Constraints

- `0 <= n, m <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
3
3 5 9
3
1 4 10
```

**Output:**

```
1 3 4 5 9 10
```

**Explanation:**

Merge by repeatedly taking the smaller front value:

- 1 (from second)
- 3 (from first)
- 4 (from second)
- 5 (from first)
- 9 (from first)
- 10 (from second)

![Example Visualization](../images/QUE-011/example-1.png)

## Notes

- This is the queue version of merge in merge sort
- Always compare fronts of both queues
- Time complexity: O(n + m)
- Space complexity: O(1) beyond the output

## Related Topics

Queue, Merge, Two Pointers

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] mergeQueues(int[] a, int[] b) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.mergeQueues(a, b);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
from typing import List

def merge_queues(a: List[int], b: List[int]) -> List[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    b = [int(next(it)) for _ in range(m)]

    result = merge_queues(a, b)
    sys.stdout.write(" ".join(str(x) for x in result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> mergeQueues(const vector<int>& a, const vector<int>& b) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int m;
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    Solution solution;
    vector<int> result = solution.mergeQueues(a, b);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mergeQueues(a, b) {
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
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(data[idx++], 10));
  }
  const m = parseInt(data[idx++], 10);
  const b = [];
  for (let i = 0; i < m; i++) {
    b.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.mergeQueues(a, b);
  console.log(result.join(" "));
});
```
