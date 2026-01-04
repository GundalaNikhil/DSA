---
problem_id: HEP_K_CLOSEST_STREAM_WEIGHT__4950
display_id: HEP-011
slug: k-closest-stream-weight
title: "K Closest Points to Origin (Stream) with Weight"
difficulty: Medium
difficulty_score: 53
topics:
  - Heaps
  - Streaming
  - Geometry
tags:
  - heaps
  - streaming
  - geometry
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-011: K Closest Points to Origin (Stream) with Weight

## Problem Statement

You receive a stream of points. Each point `(x, y)` has a positive weight `w`. The weighted distance is:

```
(x^2 + y^2) / w
```

Maintain the `k` points with the smallest weighted distance. Each `ADD` assigns an increasing id starting from 1. For each `QUERY`, output the ids of the current `k` closest points in ascending order of weighted distance (break ties by smaller id). If fewer than `k` points exist, output all. If no points exist, output `EMPTY`.

![Problem Illustration](../images/HEP-011/problem-illustration.png)

## Input Format

- First line: integers `q` and `k`
- Next `q` lines:
  - `ADD x y w`
  - `QUERY`

## Output Format

- For each `QUERY`, output one line with ids separated by spaces, or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= k <= 100000`
- `-10^6 <= x, y <= 10^6`
- `1 <= w <= 10^6`

## Example

**Input:**

```
3 1
ADD 1 1 1
ADD 2 2 1
QUERY
```

**Output:**

```
1
```

**Explanation:**

Distances:

- id 1: (1^2 + 1^2) / 1 = 2
- id 2: (2^2 + 2^2) / 1 = 8

The closest point is id 1.

![Example Visualization](../images/HEP-011/example-1.png)

## Notes

- Use a max-heap of size k to keep the closest points
- Compare distances by cross-multiplying to avoid floating errors
- Time complexity: O(q log k)
- Space complexity: O(k)

## Related Topics

Heaps, Streaming, Geometry, Top K

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public void processPoints(int q, int k, List<String> commands) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int q = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);

        List<String> commands = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            commands.add(br.readLine());
        }

        Solution sol = new Solution();
        sol.processPoints(q, k, commands);
    }
}
```

### Python

```python
import sys

class Solution:
    def process_points(self, q, k, commands):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    first_line = input_data[0].split()
    q = int(first_line[0])
    k = int(first_line[1])

    commands = input_data[1:q+1]

    sol = Solution()
    sol.process_points(q, k, commands)

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
    void processPoints(int q, int k, const vector<string>& commands) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int q, k;
    if (!(cin >> q >> k)) return 0;
    cin.ignore();

    vector<string> commands(q);
    for (int i = 0; i < q; i++) {
        getline(cin, commands[i]);
    }

    Solution sol;
    sol.processPoints(q, k, commands);

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  processPoints(q, k, commands) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const firstLine = input[0].trim().split(/\s+/);
  const q = parseInt(firstLine[0]);
  const k = parseInt(firstLine[1]);

  const commands = input.slice(1, q + 1);

  const sol = new Solution();
  sol.processPoints(q, k, commands);
}

solve();
```
