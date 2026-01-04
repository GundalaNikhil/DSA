---
problem_id: HEP_MERGE_K_STREAMS_RATE_LIMIT__9034
display_id: HEP-002
slug: merge-k-streams-rate-limit
title: "Merge K Streams with Rate Limit"
difficulty: Medium
difficulty_score: 52
topics:
  - Heaps
  - K-Way Merge
  - Streaming
tags:
  - heaps
  - k-way-merge
  - rate-limit
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-002: Merge K Streams with Rate Limit

## Problem Statement

You are given `k` sorted streams. In each round, every stream can contribute at most `r` elements. After a stream has contributed `r` elements in the current round, it is blocked until the next round. Within a round, always output the smallest available element among the unblocked streams.

Return the merged sequence produced by this round-based rate limit.

![Problem Illustration](../images/HEP-002/problem-illustration.png)

## Input Format

- First line: two integers `k` and `r`
- For each stream `i` from 1 to `k`:
  - Line 1: integer `m_i` (length of stream)
  - Line 2: `m_i` integers in non-decreasing order

## Output Format

- Single line of integers: the merged sequence in order

## Constraints

- `1 <= k <= 100000`
- `0 <= total elements <= 200000`
- `1 <= r <= 100000`
- `-10^9 <= value <= 10^9`

## Example

**Input:**

```
2 1
2
1 4
3
2 3 5
```

**Output:**

```
1 2 3 4 5
```

**Explanation:**

Round 1 (limit 1 per stream): available heads {1, 2} -> output 1, 2

Round 2: available heads {4, 3} -> output 3, 4

Round 3: available heads {5} -> output 5

![Example Visualization](../images/HEP-002/example-1.png)

## Notes

- Use a min-heap of (value, stream index)
- Track how many elements each stream has emitted in the current round
- When the heap is empty but elements remain, reset round counters
- Time complexity: O(N log k)
- Space complexity: O(k)

## Related Topics

Heaps, K-Way Merge, Streaming, Rate Limiting

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> mergeStreams(int k, int r, List<List<Integer>> streams) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int k = Integer.parseInt(parts[0]);
        int r = Integer.parseInt(parts[1]);

        List<List<Integer>> streams = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int m = Integer.parseInt(br.readLine().trim());
            List<Integer> stream = new ArrayList<>();
            String[] vals = br.readLine().trim().split("\\s+");
            for (int j = 0; j < m; j++) {
                stream.add(Integer.parseInt(vals[j]));
            }
            streams.add(stream);
        }

        Solution sol = new Solution();
        List<Integer> result = sol.mergeStreams(k, r, streams);

        PrintWriter out = new PrintWriter(System.out);
        for (int i = 0; i < result.size(); i++) {
            out.print(result.get(i) + (i == result.size() - 1 ? "" : " "));
        }
        out.println();
        out.flush();
    }
}
```

### Python

```python
import sys

class Solution:
    def merge_streams(self, k, r, streams):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    k = int(input_data[idx])
    r = int(input_data[idx + 1])
    idx += 2

    streams = []
    for _ in range(k):
        m = int(input_data[idx])
        idx += 1
        stream = []
        for _ in range(m):
            stream.append(int(input_data[idx]))
            idx += 1
        streams.append(stream)

    sol = Solution()
    result = sol.merge_streams(k, r, streams)
    print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> mergeStreams(int k, int r, vector<vector<int>>& streams) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int k, r;
    if (!(cin >> k >> r)) return 0;

    vector<vector<int>> streams(k);
    for (int i = 0; i < k; i++) {
        int m;
        cin >> m;
        streams[i].resize(m);
        for (int j = 0; j < m; j++) {
            cin >> streams[i][j];
        }
    }

    Solution sol;
    vector<int> result = sol.mergeStreams(k, r, streams);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  mergeStreams(k, r, streams) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const k = parseInt(input[idx++]);
  const r = parseInt(input[idx++]);

  const streams = [];
  for (let i = 0; i < k; i++) {
    const m = parseInt(input[idx++]);
    const stream = [];
    for (let j = 0; j < m; j++) {
      stream.push(parseInt(input[idx++]));
    }
    streams.push(stream);
  }

  const sol = new Solution();
  const result = sol.mergeStreams(k, r, streams);
  console.log(result.join(" "));
}

solve();
```
