---
problem_id: ARR_TEMP_OFFLINE_RANGES__5631
display_id: ARR-004
slug: lab-temperature-offline-ranges
title: "Lab Temperature Offline Ranges"
difficulty: Medium
difficulty_score: 46
topics:
  - Arrays
  - Difference Array
  - Prefix Sum
tags:
  - arrays
  - difference-array
  - prefix-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-004: Lab Temperature Offline Ranges

## Problem Statement

You are given an array of temperatures and a list of queries. Each query is either an add-range operation or a sum-range request.
All add queries appear before sum queries and should be applied cumulatively. 
After applying all adds, answer each sum query in order.

![Problem Illustration](../images/ARR-004/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers temps[i]
- Third line: integer q, the number of queries
- Next q lines: either "add l r x" or "sum l r"

## Output Format

Print the answers to sum queries in order, space-separated.

## Constraints

- `1 <= n, q <= 100000`
- `-1000000000 <= temps[i], x <= 1000000000`
- `0 <= l <= r < n`

## Example

**Input:**
```
3
1 2 3
4
add 0 1 5
add 2 2 -1
sum 0 2
sum 1 2
```

**Output:**
```
15 9
```

**Explanation:**

After both add queries, temps become [6, 7, 2].
Then sum 0..2 is 15 and sum 1..2 is 9.

![Example Visualization](../images/ARR-004/example-1.png)

## Notes

- All add queries appear before sum queries.
- Use 64-bit integers for sums.

## Related Topics

Difference Array, Prefix Sum, Range Queries

---

## Solution Template

### Java

```java
import java.io.InputStream;

class Solution {
    private static class SegmentTree {
        private final int n;
        private final long[] tree;
        private final long[] lazy;

        SegmentTree(int[] arr) {
            this.n = arr.length;
            this.tree = new long[4 * n];
            this.lazy = new long[4 * n];
            build(arr, 0, 0, n - 1);
        }

        private void build(int[] arr, int node, int start, int end) {
            if (start == end) {
                tree[node] = arr[start];
                return;
            }
            int mid = (start + end) >>> 1;
            build(arr, node * 2 + 1, start, mid);
            build(arr, node * 2 + 2, mid + 1, end);
            tree[node] = tree[node * 2 + 1] + tree[node * 2 + 2];
        }

        private void push(int node, int start, int end) {
            if (lazy[node] != 0) {
                tree[node] += lazy[node] * (end - start + 1L);
                if (start != end) {
                    lazy[node * 2 + 1] += lazy[node];
                    lazy[node * 2 + 2] += lazy[node];
                }
                lazy[node] = 0;
            }
        }

        void update(int l, int r, long val) {
            update(0, 0, n - 1, l, r, val);
        }

        private void update(int node, int start, int end, int l, int r, long val) {
            push(node, start, end);
            if (start > r || end < l) {
                return;
            }
            if (start >= l && end <= r) {
                lazy[node] += val;
                push(node, start, end);
                return;
            }
            int mid = (start + end) >>> 1;
            update(node * 2 + 1, start, mid, l, r, val);
            update(node * 2 + 2, mid + 1, end, l, r, val);
            tree[node] = tree[node * 2 + 1] + tree[node * 2 + 2];
        }

        long query(int l, int r) {
            return query(0, 0, n - 1, l, r);
        }

        private long query(int node, int start, int end, int l, int r) {
            push(node, start, end);
            if (start > r || end < l) {
                return 0;
            }
            if (start >= l && end <= r) {
                return tree[node];
            }
            int mid = (start + end) >>> 1;
            return query(node * 2 + 1, start, mid, l, r)
                    + query(node * 2 + 2, mid + 1, end, l, r);
        }
    }

    public long[] processTemperatureQueries(int[] temps, String[] types, int[] l, int[] r, long[] x) {
        return null;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        Integer nObj = fs.nextInt();
        if (nObj == null) return;
        int n = nObj;
        int[] temps = new int[n];
        for (int i = 0; i < n; i++) temps[i] = fs.nextInt();
        int q = fs.nextInt();
        String[] types = new String[q];
        int[] l = new int[q];
        int[] r = new int[q];
        long[] x = new long[q];
        for (int i = 0; i < q; i++) {
            types[i] = fs.next();
            l[i] = fs.nextInt();
            r[i] = fs.nextInt();
            if ("add".equals(types[i])) {
                x[i] = fs.nextLong();
            }
        }

        Solution solution = new Solution();
        long[] result = solution.processTemperatureQueries(temps, types, l, r, x);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]);
            if (i + 1 < result.length) sb.append('\n');
        }
        System.out.print(sb.toString());
    }

    private static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0;
        private int len = 0;

        FastScanner(InputStream in) {
            this.in = in;
        }

        private int read() throws Exception {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        Integer nextInt() throws Exception {
            int c;
            do {
                c = read();
                if (c == -1) return null;
            } while (c <= ' ');
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }

        long nextLong() throws Exception {
            int c;
            do {
                c = read();
            } while (c <= ' ');
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            long val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }

        String next() throws Exception {
            int c;
            do {
                c = read();
            } while (c <= ' ');
            StringBuilder sb = new StringBuilder();
            while (c > ' ') {
                sb.append((char) c);
                c = read();
            }
            return sb.toString();
        }
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep trees if necessary
sys.setrecursionlimit(200000)

class SegmentTree:
    def __init__(self, size, arr):
        return 0
    def _build(self, arr, node, start, end):
        return 0
    def _push(self, node, start, end):
        return 0
    def update(self, l, r, val):
        return 0
    def _update(self, node, start, end, l, r, val):
        return 0
    def query(self, l, r):
        return 0
    def _query(self, node, start, end, l, r):
        return 0
def process_temperature_queries(temps: list[int], queries: list[tuple]) -> list[int]:
    return []
def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        temps = [int(next(iterator)) for _ in range(n)]
        q_count = int(next(iterator))
        
        queries = []
        for _ in range(q_count):
            type = next(iterator)
            l = int(next(iterator))
            r = int(next(iterator))
            if type == "add":
                x = int(next(iterator))
                queries.append((type, l, r, x))
            else:
                queries.append((type, l, r))
                
        result = process_temperature_queries(temps, queries)
        print("\n".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Query {
    string type;
    int l, r;
    long long x;
};

class Solution {
public:
    vector<long long> processTemperatureQueries(vector<int>& temps, vector<Query>& queries) {
        int n = temps.size();
        vector<long long> diff(n + 1, 0);
        vector<long long> results;

        // Process queries in order
        for (auto& q : queries) {
            if (q.type == "add") {
                diff[q.l] += q.x;
                if (q.r + 1 <= n) {
                    diff[q.r + 1] -= q.x;
                }
            } else {
                // Reconstruct & Build Prefix for this query
                vector<long long> P(n + 1, 0);
                long long currentAdd = 0;

                for (int i = 0; i < n; i++) {
                    currentAdd += diff[i];
                    long long finalVal = temps[i] + currentAdd;
                    P[i + 1] = P[i] + finalVal;
                }

                results.push_back(P[q.r + 1] - P[q.l]);
            }
        }

        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> temps(n);
    for (int i = 0; i < n; i++) cin >> temps[i];
    
    int q;
    cin >> q;
    vector<Query> queries;
    queries.reserve(q);
    
    for (int i = 0; i < q; i++) {
        Query query;
        cin >> query.type >> query.l >> query.r;
        if (query.type == "add") cin >> query.x;
        else query.x = 0;
        queries.push_back(query);
    }

    Solution solution;
    vector<long long> result = solution.processTemperatureQueries(temps, queries);

    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processTemperatureQueries(temps, queries) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const temps = [];
    for (let i = 0; i < n; i++) temps.push(Number(tokens[ptr++]));
    
    const q = Number(tokens[ptr++]);
    const queries = [];
    for (let i = 0; i < q; i++) {
      const type = tokens[ptr++];
      const l = Number(tokens[ptr++]);
      const r = Number(tokens[ptr++]);
      let x = 0;
      if (type === "add") {
        x = Number(tokens[ptr++]);
      }
      queries.push({ type, l, r, x });
    }
    
    const solution = new Solution();
    const result = solution.processTemperatureQueries(temps, queries);
    console.log(result.join("\n"));
});
```

