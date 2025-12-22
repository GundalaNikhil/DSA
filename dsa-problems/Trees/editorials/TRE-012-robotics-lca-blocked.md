---
problem_id: TRE_ROBOTICS_LCA_BLOCKED__7104
display_id: TRE-012
slug: robotics-lca-blocked
title: "Robotics LCA with Blocked Nodes"
difficulty: Medium
difficulty_score: 54
topics:
  - Trees
  - LCA
  - DFS
tags:
  - trees
  - lca
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-012: Robotics LCA with Blocked Nodes

## 📋 Problem Summary

Find the **Lowest Common Ancestor (LCA)** of two target nodes `u` and `v` in a binary tree. However, some nodes are marked as **blocked**.
-   The LCA must be an **unblocked** node.
-   If the standard LCA is blocked, you must traverse up the tree (towards the root) to find the nearest ancestor that is unblocked.
-   If no unblocked common ancestor exists, return `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** Emergency Meeting Point

Imagine a corporate hierarchy where two employees (nodes `u` and `v`) need to meet with their lowest common manager to resolve a conflict.
-   **Standard LCA:** Their direct supervisor.
-   **Blocked:** The supervisor is out of office, on vacation, or compromised.
-   **Resolution:** They must go up the chain of command to the next available (unblocked) manager.

![Real-World Application](../images/TRE-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      1 (Unblocked)
     / \
    2   3 (Blocked)
       / \
      4   5
```
**Targets:** 4 and 5.
-   **Standard LCA:** Node 3.
-   **Status:** Node 3 is **Blocked**.
-   **Action:** Move up to parent of 3 -> Node 1.
-   **Status:** Node 1 is **Unblocked**.
-   **Result:** Node 1.

### Algorithm Steps

1.  **Find Standard LCA:** Use the classic recursive approach to find the LCA of `u` and `v`. Let's call this `lcaNode`.
2.  **Check Blocked Status:**
    -   If `lcaNode` is unblocked, return its value.
    -   If `lcaNode` is blocked, we need to find its nearest unblocked ancestor.
3.  **Find Parent Pointers:** To move up from `lcaNode`, we need parent pointers. We can populate a `parent` map during the initial traversal or run a second DFS/BFS to find the path from Root to `lcaNode`.
4.  **Traverse Up:** From `lcaNode`, move to `parent` repeatedly until an unblocked node is found or we run out of ancestors.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Targets:** `u` and `v` are guaranteed to be unblocked.
-   **Result:** Return the **value** of the node, not the index.
-   **-1:** Return if even the root is blocked (and all intermediate ancestors).

## Naive Approach

### Intuition

Find the path from Root to `u` and Root to `v`. The last common node in these paths is the standard LCA. Iterate backwards from this node in the path until an unblocked node is found.

### Algorithm

1.  DFS to find path `P_u` (Root -> ... -> u).
2.  DFS to find path `P_v` (Root -> ... -> v).
3.  Compare paths to find the divergence point (Standard LCA).
4.  Check LCA, then its parent, etc., until unblocked.

### Time Complexity

-   **O(N)**: DFS takes O(N). Path comparison takes O(H).

## Optimal Approach (Recursive LCA + Parent Map)

We can combine finding the LCA and tracking parents.

### Algorithm

1.  Run a traversal (DFS/BFS) to:
    -   Build a `parent` array/map.
    -   Locate `u` and `v` (verify they exist).
2.  Find Standard LCA:
    -   Use `parent` map to trace path of `u` to root. Store in a Set.
    -   Trace path of `v` to root. The first node found in the Set is the Standard LCA.
    -   *Alternatively*, use the recursive LCA function if you prefer, but `parent` map is needed for the "climb up" step anyway.
3.  From Standard LCA, loop up using `parent` array until `!blocked[curr]`.
4.  Return `values[curr]`.

### Time Complexity

-   **O(N)**: To build parent map and find LCA.

### Space Complexity

-   **O(N)**: Parent map and recursion stack.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int lcaBlocked(int n, int[] values, int[] blocked, int[] left, int[] right, int u, int v) {
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        
        // 1. Build Parent Map using BFS
        Queue<Integer> q = new LinkedList<>();
        q.offer(0);
        
        while (!q.isEmpty()) {
            int curr = q.poll();
            if (left[curr] != -1) {
                parent[left[curr]] = curr;
                q.offer(left[curr]);
            }
            if (right[curr] != -1) {
                parent[right[curr]] = curr;
                q.offer(right[curr]);
            }
        }
        
        // 2. Find Standard LCA using Ancestor Set
        Set<Integer> ancestors = new HashSet<>();
        int curr = u;
        while (curr != -1) {
            ancestors.add(curr);
            curr = parent[curr];
        }
        
        int lca = -1;
        curr = v;
        while (curr != -1) {
            if (ancestors.contains(curr)) {
                lca = curr;
                break;
            }
            curr = parent[curr];
        }
        
        if (lca == -1) return -1; // Should not happen if u, v in tree
        
        // 3. Climb up if blocked
        while (lca != -1 && blocked[lca] == 1) {
            lca = parent[lca];
        }
        
        return (lca != -1) ? values[lca] : -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] blocked = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            blocked[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        int u = sc.nextInt();
        int v = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.lcaBlocked(n, values, blocked, left, right, u, v));
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque

def lca_blocked(n: int, values: list[int], blocked: list[int], left: list[int], right: list[int], u: int, v: int) -> int:
    parent = [-1] * n
    
    # 1. Build Parent Map
    q = deque([0])
    while q:
        curr = q.popleft()
        if left[curr] != -1:
            parent[left[curr]] = curr
            q.append(left[curr])
        if right[curr] != -1:
            parent[right[curr]] = curr
            q.append(right[curr])
            
    # 2. Find Standard LCA
    ancestors = set()
    curr = u
    while curr != -1:
        ancestors.add(curr)
        curr = parent[curr]
        
    lca = -1
    curr = v
    while curr != -1:
        if curr in ancestors:
            lca = curr
            break
        curr = parent[curr]
        
    if lca == -1:
        return -1
        
    # 3. Climb up
    while lca != -1 and blocked[lca] == 1:
        lca = parent[lca]
        
    return values[lca] if lca != -1 else -1

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    blocked = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        blocked[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    u = int(data[idx]); idx += 1
    v = int(data[idx]); idx += 1
    
    print(lca_blocked(n, values, blocked, left, right, u, v))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lcaBlocked(int n, const vector<int>& values, const vector<int>& blocked,
                   const vector<int>& left, const vector<int>& right, int u, int v) {
        vector<int> parent(n, -1);
        
        // 1. Build Parent Map
        queue<int> q;
        q.push(0);
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            if (left[curr] != -1) {
                parent[left[curr]] = curr;
                q.push(left[curr]);
            }
            if (right[curr] != -1) {
                parent[right[curr]] = curr;
                q.push(right[curr]);
            }
        }
        
        // 2. Find Standard LCA
        unordered_set<int> ancestors;
        int curr = u;
        while (curr != -1) {
            ancestors.insert(curr);
            curr = parent[curr];
        }
        
        int lca = -1;
        curr = v;
        while (curr != -1) {
            if (ancestors.count(curr)) {
                lca = curr;
                break;
            }
            curr = parent[curr];
        }
        
        if (lca == -1) return -1;
        
        // 3. Climb up
        while (lca != -1 && blocked[lca] == 1) {
            lca = parent[lca];
        }
        
        return (lca != -1) ? values[lca] : -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), blocked(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> blocked[i] >> left[i] >> right[i];
    }
    int u, v;
    cin >> u >> v;

    Solution solution;
    cout << solution.lcaBlocked(n, values, blocked, left, right, u, v) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  lcaBlocked(n, values, blocked, left, right, u, v) {
    const parent = new Int32Array(n).fill(-1);
    
    // 1. Build Parent Map
    const q = [0];
    let head = 0;
    while (head < q.length) {
      const curr = q[head++];
      if (left[curr] !== -1) {
        parent[left[curr]] = curr;
        q.push(left[curr]);
      }
      if (right[curr] !== -1) {
        parent[right[curr]] = curr;
        q.push(right[curr]);
      }
    }
    
    // 2. Find Standard LCA
    const ancestors = new Set();
    let curr = u;
    while (curr !== -1) {
      ancestors.add(curr);
      curr = parent[curr];
    }
    
    let lca = -1;
    curr = v;
    while (curr !== -1) {
      if (ancestors.has(curr)) {
        lca = curr;
        break;
      }
      curr = parent[curr];
    }
    
    if (lca === -1) return -1;
    
    // 3. Climb up
    while (lca !== -1 && blocked[lca] === 1) {
      lca = parent[lca];
    }
    
    return lca !== -1 ? values[lca] : -1;
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
  const values = new Array(n);
  const blocked = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    blocked[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const u = parseInt(data[idx++], 10);
  const v = parseInt(data[idx++], 10);

  const solution = new Solution();
  console.log(solution.lcaBlocked(n, values, blocked, left, right, u, v).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
6 1 1 2
2 0 3 4
8 0 -1 -1
1 0 -1 -1
4 0 -1 -1
3 4
```
**Nodes:**
- 0(6, Blocked) -> L:1(2), R:2(8)
- 1(2, Unblocked) -> L:3(1), R:4(4)
- 2(8, Unblocked) -> Leaf
- 3(1, Unblocked) -> Leaf
- 4(4, Unblocked) -> Leaf
**Targets:** 3 and 4.

**Execution:**
1.  **Parents:** `1->0`, `2->0`, `3->1`, `4->1`.
2.  **Ancestors of 3:** `{3, 1, 0}`.
3.  **Trace 4:**
    -   4? No.
    -   Parent(4) = 1. In set? Yes.
    -   **Standard LCA:** 1.
4.  **Check Blocked:**
    -   Node 1 blocked? No (0).
    -   Return Value(1) = 2.

**Output:** `2`.

**Scenario 2 (If Node 1 was blocked):**
-   LCA = 1. Blocked.
-   Move to Parent(1) = 0.
-   Node 0 blocked? Yes (1).
-   Move to Parent(0) = -1.
-   Return -1.

## ✅ Proof of Correctness

The set of common ancestors of `u` and `v` forms a path from the Root to the Standard LCA.
Any unblocked common ancestor must lie on this path.
Since we want the "lowest" one (deepest), we start at the Standard LCA (the deepest possible common ancestor) and move upwards. The first unblocked node we encounter is the answer.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Multiple Targets**
    -   LCA of K nodes.
-   **Extension 2: Dynamic Updates**
    -   Block/Unblock nodes and query LCA (Heavy-Light Decomposition).
-   **Extension 3: Distance**
    -   Distance between u and v avoiding blocked nodes (Shortest Path on Tree).

## Common Mistakes to Avoid

1.  **Returning Index vs Value:**
    -   ❌ Returning `lca` index.
    -   ✅ Return `values[lca]`.
2.  **Root Blocked:**
    -   ❌ Infinite loop or crash.
    -   ✅ Handle `lca == -1`.

## Related Concepts

-   **LCA (Lowest Common Ancestor)**
-   **Parent Pointers**
-   **Path Tracing**
