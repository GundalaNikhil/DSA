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
    public List<Integer> mergeStreams(List<List<Integer>> streams, int r) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] firstLine = br.readLine().split(" ");
        int k = Integer.parseInt(firstLine[0]);
        int r = Integer.parseInt(firstLine[1]);

        List<List<Integer>> streams = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int m = Integer.parseInt(br.readLine());
            String[] streamElements = br.readLine().split(" ");
            List<Integer> stream = new ArrayList<>();
            for (String s : streamElements) {
                stream.add(Integer.parseInt(s));
            }
            streams.add(stream);
        }

        Solution solution = new Solution();
        List<Integer> result = solution.mergeStreams(streams, r);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i));
            if (i < result.size() - 1) sb.append(" ");
        }
        System.out.println(sb.toString());
    }
}
```

### Python

```python
import sys

def merge_streams(streams: list, r: int) -> list:
    # //Implement here
    return []

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        k = int(next(it))
        r = int(next(it))
        streams = []
        for _ in range(k):
            m = int(next(it))
            stream = []
            for _ in range(m):
                stream.append(int(next(it)))
            streams.append(stream)

        result = merge_streams(streams, r)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> mergeStreams(const vector<vector<int>>& streams, int r) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, r;
    if (cin >> k >> r) {
        vector<vector<int>> streams(k);
        for (int i = 0; i < k; i++) {
            int m;
            cin >> m;
            streams[i].resize(m);
            for (int j = 0; j < m; j++) {
                cin >> streams[i][j];
            }
        }

        Solution solution;
        vector<int> result = solution.mergeStreams(streams, r);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mergeStreams(streams, r) {
    //Implement here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const k = parseInt(data[idx++]);
  const r = parseInt(data[idx++]);
  const streams = [];
  for (let i = 0; i < k; i++) {
    const m = parseInt(data[idx++]);
    const stream = [];
    for (let j = 0; j < m; j++) {
      stream.push(BigInt(data[idx++]));
    }
    streams.push(stream);
  }

  const solution = new Solution();
  const result = solution.mergeStreams(streams, r);
  console.log(result.join(" "));
});
```
