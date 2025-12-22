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
---

# HSH-009: Substring Hash Under Edits

## 📋 Problem Summary

You are given a string `s`. You need to support two operations:
1. **Update:** Change the character at index `i` to `c`.
2. **Query:** Return the polynomial rolling hash of the substring `s[l..r]`.

## 🌍 Real-World Scenario

**Scenario Title:** Collaborative Document Editing

Imagine a collaborative text editor like Google Docs.
- Users are constantly typing (updating characters).
- The system needs to quickly verify if two sections of the document are identical (e.g., to merge changes or detect duplicates).
- Recomputing the hash of the entire document after every keystroke is too slow.
- We need a way to update the hash locally and query any part instantly.

![Real-World Application](../images/HSH-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Segment Tree for Hashing

String: "abc" (Indices 0, 1, 2)
Base: 10 (for simplicity)

Tree Structure:
```text
        [0-2]
       /     \
    [0-1]    [2-2] ('c')
    /   \
 [0-0] [1-1]
 ('a') ('b')
```

**Leaf Nodes:**
- Node `[0-0]`: Hash("a") = 97
- Node `[1-1]`: Hash("b") = 98
- Node `[2-2]`: Hash("c") = 99

**Merging Nodes:**
- To merge left child (hash $H_L$, length $Len_L$) and right child (hash $H_R$, length $Len_R$):
- Combined Hash = $H_L \times B^{Len_R} + H_R$.
- Node `[0-1]`: Hash("ab") = $97 \times 10^1 + 98 = 1068$.
- Node `[0-2]`: Hash("abc") = $1068 \times 10^1 + 99 = 10779$.

**Update:**
- Change 'b' to 'x'.
- Update leaf `[1-1]`.
- Recompute parent `[0-1]`.
- Recompute root `[0-2]`.
- Complexity: $O(\log N)$.

### Key Concept: Associativity of Hashing

Polynomial hashing is associative if we track lengths.
$Hash(A + B) = Hash(A) \times Base^{Length(B)} + Hash(B)$.
This property allows us to use a **Segment Tree**. Each node stores the hash of the substring it covers.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, list of operations.
- **Output:** Hashes for query operations.
- **Constraints:** $N, Q \le 2 \cdot 10^5$.
- **Indexing:** 0-based.

## Naive Approach

### Intuition

- **Update:** Modify string array ($O(1)$).
- **Query:** Compute hash by iterating from `l` to `r` ($O(N)$).

### Time Complexity

- **O(Q * N)**: Too slow for $2 \cdot 10^5$ operations.

## Optimal Approach

### Key Insight

Use a **Segment Tree**.
- Each node stores the hash of its range.
- **Build:** $O(N)$.
- **Update:** $O(\log N)$. Traverse path to root, applying the merge formula.
- **Query:** $O(\log N)$. Combine hashes of relevant nodes.

### Algorithm

1. Precompute powers of Base: $B^0, B^1, \dots, B^N$.
2. Build Segment Tree.
   - Leaf: $H = s[i]$.
   - Internal: $H = (H_{left} \times B^{len_{right}} + H_{right}) \pmod M$.
3. **Update(i, c):**
   - Go to leaf `i`. Update value.
   - Recalculate ancestors.
4. **Query(l, r):**
   - Standard range query.
   - Be careful when combining partial results: ensure correct powers are multiplied.
   - So, query should return `{hash, length}`.

### Time Complexity

- **O(Q log N)**.

### Space Complexity

- **O(N)**: Segment Tree size ($4N$).

![Algorithm Visualization](../images/HSH-009/algorithm-visualization.png)

## Implementations

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
        n = s.length();
        chars = s.toCharArray();
        tree = new long[4 * n];
        power = new long[n + 1];
        
        power[0] = 1;
        for (int i = 1; i <= n; i++) {
            power[i] = (power[i - 1] * BASE) % MOD;
        }
        
        build(1, 0, n - 1);
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("U")) {
                int idx = Integer.parseInt(op[1]);
                char c = op[2].charAt(0);
                update(1, 0, n - 1, idx, c);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                // Query returns {hash, length}
                // But since we query range [l, r], length is always r-l+1.
                // Standard query logic:
                results.add(query(1, 0, n - 1, l, r));
            }
        }
        
        return results;
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

public class Main {
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
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        chars = list(s)
        tree = [0] * (4 * n)
        power = [1] * (n + 1)
        
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * BASE) % MOD
            
        def build(node, start, end):
            if start == end:
                tree[node] = ord(chars[start])
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            
            right_len = end - mid
            tree[node] = (tree[2 * node] * power[right_len] + tree[2 * node + 1]) % MOD
            
        def update(node, start, end, idx, val):
            if start == end:
                chars[idx] = val
                tree[node] = ord(val)
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
                
            right_len = end - mid
            tree[node] = (tree[2 * node] * power[right_len] + tree[2 * node + 1]) % MOD
            
        def query(node, start, end, l, r):
            if r < start or end < l:
                return -1
            if l <= start and end <= r:
                return tree[node]
            
            mid = (start + end) // 2
            p1 = query(2 * node, start, mid, l, r)
            p2 = query(2 * node + 1, mid + 1, end, l, r)
            
            if p1 == -1: return p2
            if p2 == -1: return p1
            
            right_start = max(mid + 1, l)
            right_end = min(end, r)
            right_len = right_end - right_start + 1
            
            return (p1 * power[right_len] + p2) % MOD
            
        build(1, 0, n - 1)
        results = []
        
        for op in operations:
            if op[0] == 'U':
                idx = int(op[1])
                c = op[2]
                update(1, 0, n - 1, idx, c)
            else:
                l = int(op[1])
                r = int(op[2])
                results.append(query(1, 0, n - 1, l, r))
                
        return results

def process_operations(s: str, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(s, operations)

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
    
    void update(int node, int start, int end, int idx, char val) {
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
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const chars = s.split('').map(c => BigInt(c.charCodeAt(0)));
    const tree = new BigInt64Array(4 * n);
    const power = new BigInt64Array(n + 1);
    
    power[0] = 1n;
    for (let i = 1; i <= n; i++) {
      power[i] = (power[i - 1] * BASE) % MOD;
    }
    
    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = chars[start];
        return;
      }
      const mid = Math.floor((start + end) / 2);
      build(2 * node, start, mid);
      build(2 * node + 1, mid + 1, end);
      
      const rightLen = end - mid;
      tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    };
    
    const update = (node, start, end, idx, val) => {
      if (start === end) {
        chars[idx] = val;
        tree[node] = val;
        return;
      }
      const mid = Math.floor((start + end) / 2);
      if (idx <= mid) update(2 * node, start, mid, idx, val);
      else update(2 * node + 1, mid + 1, end, idx, val);
      
      const rightLen = end - mid;
      tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    };
    
    const query = (node, start, end, l, r) => {
      if (r < start || end < l) return -1n;
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const p1 = query(2 * node, start, mid, l, r);
      const p2 = query(2 * node + 1, mid + 1, end, l, r);
      
      if (p1 === -1n) return p2;
      if (p2 === -1n) return p1;
      
      const rightStart = Math.max(mid + 1, l);
      const rightEnd = Math.min(end, r);
      const rightLen = rightEnd - rightStart + 1;
      
      return (p1 * power[rightLen] + p2) % MOD;
    };
    
    build(1, 0, n - 1);
    
    const results = [];
    for (const op of operations) {
      if (op[0] === 'U') {
        const idx = parseInt(op[1]);
        const c = BigInt(op[2].charCodeAt(0));
        update(1, 0, n - 1, idx, c);
      } else {
        const l = parseInt(op[1]);
        const r = parseInt(op[2]);
        results.push(query(1, 0, n - 1, l, r));
      }
    }
    
    return results;
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

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
abc
Q 0 2
U 1 x
Q 0 2
```

**Build:**
- Leaf `[0]`: 'a'(97).
- Leaf `[1]`: 'b'(98).
- Leaf `[2]`: 'c'(99).
- Root `[0-2]`: Hash("abc") = $97 \cdot 100 + 98 \cdot 10 + 99 = 10779$. (Using base 10 for simplicity).

**Op 1 (Q 0 2):**
- Returns root hash: 10779.

**Op 2 (U 1 x):**
- Update index 1 to 'x'(120).
- Leaf `[1]` becomes 120.
- Parent `[0-1]` recomputed: $97 \cdot 10 + 120 = 1090$.
- Root `[0-2]` recomputed: $1090 \cdot 10 + 99 = 11009$.

**Op 3 (Q 0 2):**
- Returns new root hash: 11009.

## ✅ Proof of Correctness

### Invariant
Each node in the segment tree correctly stores the polynomial hash of the substring it covers.
The merge operation $H = H_L \times B^{Len_R} + H_R$ correctly combines two adjacent substrings.
Updates propagate correctly up the tree.

## 💡 Interview Extensions

- **Extension 1:** Range Updates?
  - *Answer:* Lazy propagation. Need to maintain sum of powers to update a range to a specific character.
- **Extension 2:** Find first index where two strings differ (with updates).
  - *Answer:* Binary search on Segment Tree ($O(\log N)$).

### C++ommon Mistakes to Avoid

1. **Incorrect Merge Logic**
   - ❌ Wrong: $H_L + H_R$.
   - ✅ Correct: Shift $H_L$ by length of $R$.
2. **Query Overlap Calculation**
   - ❌ Wrong: Using full length of right child.
   - ✅ Correct: Use length of the *intersection* of query range and right child range.

## Related Concepts

- **Fenwick Tree:** Can also be used (Hash = $\sum s[i] \cdot B^i$). Update is adding $(c_{new} - c_{old}) \cdot B^i$. Query is range sum.
- **Treap:** For splitting/merging strings.
