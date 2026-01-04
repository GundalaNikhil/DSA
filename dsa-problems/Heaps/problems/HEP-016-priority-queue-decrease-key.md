---
problem_id: HEP_PRIORITY_QUEUE_DECREASE_KEY__8091
display_id: HEP-016
slug: priority-queue-decrease-key
title: "Priority Queue with Decrease-Key"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Priority Queue
  - Data Structures
tags:
  - heaps
  - priority-queue
  - decrease-key
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-016: Priority Queue with Decrease-Key

## Problem Statement

Implement a priority queue that supports:

- `INSERT id value`
- `DECREASE id delta` (decrease the key of `id` by `delta`)
- `EXTRACT` (remove and output the minimum key)

If `EXTRACT` is called on an empty queue, output `EMPTY`. If multiple ids have the same key, return the lexicographically smallest id.

![Problem Illustration](../images/HEP-016/problem-illustration.png)

## Input Format

- First line: integer `q`
- Next `q` lines: one of the operations above

## Output Format

- For each `EXTRACT`, output `value id` or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= value, delta <= 10^9`
- `1 <= |id| <= 20` (alphanumeric)

## Example

**Input:**

```
5
INSERT id1 5
INSERT id2 3
DECREASE id1 4
EXTRACT
EXTRACT
```

**Output:**

```
1 id1
3 id2
```

**Explanation:**

- id1 decreases from 5 to 1
- Extracts return id1 (1) then id2 (3)

![Example Visualization](../images/HEP-016/example-1.png)

## Notes

- Use a binary heap with a position map
- Decrease-key can be O(log n) with index tracking
- Time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Heaps, Priority Queue, Decrease-Key, Data Structures

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public void processPriorityQueue(int q, List<String> ops) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        int q = Integer.parseInt(firstLine.trim());

        List<String> ops = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            ops.add(br.readLine());
        }

        Solution sol = new Solution();
        sol.processPriorityQueue(q, ops);
    }
}
```

### Python

```python
import sys

class Solution:
    def process_priority_queue(self, q, ops):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    q = int(input_data[0].strip())
    ops = input_data[1:q+1]

    sol = Solution()
    sol.process_priority_queue(q, ops)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void processPriorityQueue(int q, const vector<string>& ops) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int q;
    if (!(cin >> q)) return 0;
    cin.ignore();

    vector<string> ops(q);
    for (int i = 0; i < q; i++) {
        getline(cin, ops[i]);
    }

    Solution sol;
    sol.processPriorityQueue(q, ops);

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  processPriorityQueue(q, ops) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const q = parseInt(input[0].trim());
  const ops = input.slice(1, q + 1);

  const sol = new Solution();
  sol.processPriorityQueue(q, ops);
}

solve();
```
