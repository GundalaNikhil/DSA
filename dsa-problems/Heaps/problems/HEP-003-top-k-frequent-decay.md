---
problem_id: HEP_TOP_K_FREQUENT_DECAY__5829
display_id: HEP-003
slug: top-k-frequent-decay
title: "Top K Frequent with Decay"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Lazy Updates
  - Time Decay
tags:
  - heaps
  - decay
  - frequency
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-003: Top K Frequent with Decay

## Problem Statement

You receive events with timestamps. Each event adds 1 to the count of a key. Every `d` seconds, counts decay by half. At query time `t`, the effective count for a key is:

```
count * 0.5^(floor((t - last_update) / d))
```

Return the top `k` keys by effective count at each query. Break ties by lexicographic order. If fewer than `k` keys exist, return all. If no keys exist, output `EMPTY`.

![Problem Illustration](../images/HEP-003/problem-illustration.png)

## Input Format

- First line: three integers `q`, `d`, and `k`
- Next `q` lines:
  - `ADD key t`
  - `QUERY t`

## Output Format

- For each `QUERY`, output one line with up to `k` keys separated by spaces, or `EMPTY`

## Constraints

- `1 <= q <= 100000`
- `1 <= d <= 10^9`
- `1 <= k <= 100000`
- `0 <= t <= 10^9`
- `1 <= |key| <= 20` (lowercase letters)

## Example

**Input:**

```
4 5 1
ADD a 0
ADD a 5
ADD b 5
QUERY 10
```

**Output:**

```
a
```

**Explanation:**

At t=10:

- a was updated at t=5 with count 1.5, then decays once -> 0.75
- b was updated at t=5 with count 1, then decays once -> 0.5

Top 1 key is a.

![Example Visualization](../images/HEP-003/example-1.png)

## Notes

- Store last update time and current count per key
- Apply decay lazily when a key is accessed
- Use a max-heap for retrieving top k keys per query
- Time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Heaps, Time Decay, Lazy Updates, Streaming

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public void processEvents(int q, int d, int k, List<String> events) {
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
        int d = Integer.parseInt(parts[1]);
        int k = Integer.parseInt(parts[2]);

        List<String> events = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            events.add(br.readLine());
        }

        Solution sol = new Solution();
        sol.processEvents(q, d, k, events);
    }
}
```

### Python

```python
import sys

class Solution:
    def process_events(self, q, d, k, events):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    first_line = input_data[0].split()
    q = int(first_line[0])
    d = int(first_line[1])
    k = int(first_line[2])

    events = input_data[1:q+1]

    sol = Solution()
    sol.process_events(q, d, k, events)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    void processEvents(int q, int d, int k, const vector<string>& events) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int q, d, k;
    if (!(cin >> q >> d >> k)) return 0;
    cin.ignore();

    vector<string> events(q);
    for (int i = 0; i < q; i++) {
        getline(cin, events[i]);
    }

    Solution sol;
    sol.processEvents(q, d, k, events);

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  processEvents(q, d, k, events) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 1) return;

  const firstLine = input[0].trim().split(/\s+/);
  const q = parseInt(firstLine[0]);
  const d = parseInt(firstLine[1]);
  const k = parseInt(firstLine[2]);

  const events = input.slice(1, q + 1);

  const sol = new Solution();
  sol.processEvents(q, d, k, events);
}

solve();
```
