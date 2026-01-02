---
problem_id: HSH_SUBSTRING_HASH_UNDER_EDITS__7394
display_id: HSH-009
slug: substring-hash-under-edits
title: "Substring Hash Under Edits"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - Data Structures
  - Segment Tree
tags:
  - hashing
  - segment-tree
  - updates
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HSH-009: Substring Hash Under Edits

## Problem Statement

Support two types of operations on a string `s`:

1. **Update**: Change character at position `i` to character `c`
2. **Query**: Return the polynomial hash of substring `s[l..r]`

Use a data structure (Segment Tree or Fenwick Tree) to handle updates and queries efficiently.

![Problem Illustration](../images/HSH-009/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q` (number of operations)
- Next `q` lines: either
  - `U i c` (update position i to character c)
  - `Q l r` (query hash of substring [l, r])

## Output Format

- For each query operation, output the hash value on a new line

## Constraints

- `1 <= |s|, q <= 2*10^5`
- `0 <= i, l, r < |s|`
- Character `c` is a lowercase English letter

## Example

**Input:**

```
abc
3
Q 0 2
U 1 x
Q 0 2
```

**Output:**

```
549818522
650293847
```

**Explanation:**

Initial string: "abc"

Operation 1: Query hash of "abc" (positions 0-2)
Operation 2: Update position 1 to 'x' → string becomes "axc"
Operation 3: Query hash of "axc" (positions 0-2)

![Example Visualization](../images/HSH-009/example-1.png)

## Notes

- Use Segment Tree with each node storing hash value
- Precompute powers of base for combination
- Update: O(log n), Query: O(log n)
- Total time complexity: O(q log n)
- Space complexity: O(n)

## Related Topics

Segment Tree, Fenwick Tree, Hashing, Dynamic Updates

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    private long[] tree;
    private long[] power;
    private int n;
    private char[] chars;
    
    public List<Long> processOperations(String s, List<String[]> operations) {
        return null;
    }
    
    private void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = chars[start];
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
        
        int rightLen = end - mid;
        tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    }
    
    private void update(int node, int start, int end, int idx, char val) {
        if (start == end) {
            chars[idx] = val;
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        
        int rightLen = end - mid;
        tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    }
    
    private long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return -1; // Null
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        long p1 = query(2 * node, start, mid, l, r);
        long p2 = query(2 * node + 1, mid + 1, end, l, r);
        
        if (p1 == -1) return p2;
        if (p2 == -1) return p1;
        
        // We need length of the right part that was actually included in the query
        // Intersection of [mid+1, end] and [l, r]
        int rightStart = Math.max(mid + 1, l);
        int rightEnd = Math.min(end, r);
        int rightLen = rightEnd - rightStart + 1;
        
        return (p1 * power[rightLen] + p2) % MOD;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int q = sc.nextInt();
                sc.nextLine();
                List<String[]> operations = new ArrayList<>();
                for (int i = 0; i < q; i++) {
                    operations.add(sc.nextLine().split(" "));
                }
                Solution solution = new Solution();
                List<Long> result = solution.processOperations(s, operations);
                for (long hash : result) {
                    System.out.println(hash);
                }
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

class Solution:
    def process_operations(self, s: str, operations: list) -> list:
        return []
def process_operations(s: str, operations: list) -> list:
    return []
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        s = next(iterator)
        q = int(next(iterator))
        operations = []
        for _ in range(q):
            type_op = next(iterator)
            if type_op == 'U':
                idx = next(iterator)
                c = next(iterator)
                operations.append(['U', idx, c])
            else:
                l = next(iterator)
                r = next(iterator)
                operations.append(['Q', l, r])
                
        result = process_operations(s, operations)
        for val in result:
            print(val)
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
#include <sstream>
#include <algorithm>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;
    
    vector<long long> tree;
    vector<long long> power;
    string chars;
    int n;

public:
    vector<long long> processOperations(string s, vector<vector<string>>& operations) {
        n = s.length();
        chars = s;
        tree.resize(4 * n);
        power.resize(n + 1);
        
        power[0] = 1;
        for (int i = 1; i <= n; i++) {
            power[i] = (power[i - 1] * BASE) % MOD;
        }
        
        build(1, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : operations) {
            if (op[0] == "U") {
                int idx = stoi(op[1]);
                char c = op[2][0];
                update(1, 0, n - 1, idx, c);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                results.push_back(query(1, 0, n - 1, l, r));
            }
        }
        return results;
    }
    
    void build(int node, int start, int end) {
    }
    
    void update(int node, int start, int end, int idx, char val) {
    }
    
    long long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return -1;
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        long long p1 = query(2 * node, start, mid, l, r);
        long long p2 = query(2 * node + 1, mid + 1, end, l, r);
        
        if (p1 == -1) return p2;
        if (p2 == -1) return p1;
        
        int rightStart = max(mid + 1, l);
        int rightEnd = min(end, r);
        int rightLen = rightEnd - rightStart + 1;
        
        return (p1 * power[rightLen] + p2) % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (!(cin >> s)) return 0;
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<vector<string>> operations(q);
    for (int i = 0; i < q; i++) {
        char type;
        cin >> type;
        if (type == 'U') {
            int idx;
            char c;
            cin >> idx >> c;
            operations[i] = {"U", to_string(idx), string(1, c)};
        } else {
            int l, r;
            cin >> l >> r;
            operations[i] = {"Q", to_string(l), to_string(r)};
        }
    }
    
    Solution solution;
    vector<long long> result = solution.processOperations(s, operations);
    
    for (long long hash : result) {
        cout << hash << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  processOperations(s, operations) {
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
  let ptr = 0;
  const s = data[ptr++];
  const q = parseInt(data[ptr++]);
  
  const operations = [];
  for (let i = 0; i < q; i++) {
    operations.push(data[ptr++].split(" "));
  }
  
  const solution = new Solution();
  const result = solution.processOperations(s, operations);
  
  result.forEach((hash) => console.log(hash.toString()));
});
```

