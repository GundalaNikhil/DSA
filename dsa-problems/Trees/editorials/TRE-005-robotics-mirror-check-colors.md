---
problem_id: TRE_ROBOTICS_MIRROR_CHECK_COLORS__6729
display_id: TRE-005
slug: robotics-mirror-check-colors
title: "Robotics Mirror Check with Colors"
difficulty: Easy
difficulty_score: 32
topics:
  - Trees
  - Symmetry
  - BFS
tags:
  - trees
  - symmetry
  - bfs
  - easy
premium: true
subscription_tier: basic
---

# TRE-005: Robotics Mirror Check with Colors

## 📋 Problem Summary

You are given a binary tree where each node has a **value** and a **color** (0 or 1). You need to determine if the tree satisfies two conditions:
1.  **Structural & Value Symmetry:** The tree is a mirror image of itself in terms of structure and node values (standard "Symmetric Tree" problem).
2.  **Color Balance:** For every level of the tree, the collection (multiset) of colors in the left subtree must exactly match the collection of colors in the right subtree. Note that colors do *not* need to be in symmetric positions; only their counts at each level must match.

## 🌍 Real-World Scenario

**Scenario Title:** Robot Assembly Quality Control

Imagine a robot built with a left arm and a right arm.
-   **Symmetry:** The mechanical structure (joints, lengths) and component types (values) must be identical mirrors for the robot to be balanced.
-   **Color Balance:** The wiring or aesthetic panels (colors) might be distributed differently, but the *total inventory* of parts used on the left side must match the right side at each vertical level to ensure equal weight distribution or material usage.

![Real-World Application](../images/TRE-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
        1 (Root)
      /   \
     2     2
    / \   / \
   3   4 4   3
```
**Values:** Symmetric. (2==2, 3==3, 4==4).
**Colors:**
-   Root: Irrelevant (center).
-   Level 1: Left Node (Color 0), Right Node (Color 0). Match? Yes.
-   Level 2:
    -   Left Subtree Nodes: [Color 1, Color 0]
    -   Right Subtree Nodes: [Color 0, Color 1]
    -   Multisets: {0, 1} vs {0, 1}. Match? Yes.

**Result:** True.

### Algorithm Steps

1.  **Symmetry Check:**
    -   Use a recursive helper `isMirror(node1, node2)`.
    -   Check if `node1.val == node2.val`.
    -   Recurse: `isMirror(node1.left, node2.right)` AND `isMirror(node1.right, node2.left)`.
2.  **Color Balance Check:**
    -   Perform a traversal (BFS is easiest) on the Left Subtree and Right Subtree separately.
    -   For each level, count the number of 0s and 1s in the Left Subtree.
    -   Compare with the counts in the Right Subtree.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Empty Tree:** Returns `true`.
-   **Color Constraint:** Colors are only 0 or 1. This simplifies the multiset check to just counting sums.
-   **Symmetry:** `left.left` matches `right.right`, `left.right` matches `right.left`.

## Naive Approach

### Intuition

Run two completely separate checks. First, run the standard `isSymmetric` algorithm. If it passes, run a Level Order Traversal on the left child and right child separately, storing colors level-by-level, and compare them.

### Algorithm

1.  If `!isSymmetric(root)`, return `false`.
2.  `leftColors = getLevelColors(root.left)`.
3.  `rightColors = getLevelColors(root.right)`.
4.  Compare `leftColors` and `rightColors`.

### Time Complexity

-   **O(N)**: Both checks visit all nodes.

### Space Complexity

-   **O(N)**: To store levels.

## Optimal Approach (Single Pass / Combined)

We can combine logic, but keeping them separate is cleaner and has the same asymptotic complexity. Since we need to check level-wise properties for colors, BFS is very natural. We can run a BFS that processes the left and right subtrees in parallel (or just level-by-level for the whole tree) but distinguishing left-side nodes from right-side nodes is tricky in a single queue unless we track it.

Actually, the simplest robust way is:
1.  **Check Symmetry (DFS):** Standard recursive check.
2.  **Check Colors (BFS):**
    -   Queue `qLeft` for root.left, `qRight` for root.right.
    -   At each step, process full level of `qLeft` and `qRight`.
    -   Sum colors in `qLeft` batch. Sum colors in `qRight` batch.
    -   If sums differ (or counts differ), return `false`.

### Time Complexity

-   **O(N)**.

### Space Complexity

-   **O(W)**: Width of tree.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public boolean mirrorCheck(int n, int[] values, int[] colors, int[] left, int[] right) {
        if (n == 0) return true;
        
        // 1. Check Structural & Value Symmetry
        if (!isSymmetric(0, values, left, right)) return false;
        
        // 2. Check Color Balance Level-by-Level
        if (left[0] == -1 && right[0] == -1) return true; // Single node
        if (left[0] == -1 || right[0] == -1) return false; // Should be caught by symmetry, but safe check
        
        return checkColorBalance(left[0], right[0], colors, left, right);
    }
    
    private boolean isSymmetric(int root, int[] values, int[] left, int[] right) {
        if (root == -1) return true;
        return checkMirror(left[root], right[root], values, left, right);
    }
    
    private boolean checkMirror(int u, int v, int[] values, int[] left, int[] right) {
        if (u == -1 && v == -1) return true;
        if (u == -1 || v == -1) return false;
        if (values[u] != values[v]) return false;
        return checkMirror(left[u], right[v], values, left, right) &&
               checkMirror(right[u], left[v], values, left, right);
    }
    
    private boolean checkColorBalance(int rootLeft, int rootRight, int[] colors, int[] left, int[] right) {
        Queue<Integer> qL = new LinkedList<>();
        Queue<Integer> qR = new LinkedList<>();
        qL.add(rootLeft);
        qR.add(rootRight);
        
        while (!qL.isEmpty() && !qR.isEmpty()) {
            int sizeL = qL.size();
            int sizeR = qR.size();
            if (sizeL != sizeR) return false; // Should be caught by symmetry
            
            int sumL = 0;
            int sumR = 0;
            
            for (int i = 0; i < sizeL; i++) {
                int u = qL.poll();
                sumL += colors[u];
                if (left[u] != -1) qL.add(left[u]);
                if (right[u] != -1) qL.add(right[u]);
            }
            
            for (int i = 0; i < sizeR; i++) {
                int v = qR.poll();
                sumR += colors[v];
                if (left[v] != -1) qR.add(left[v]);
                if (right[v] != -1) qR.add(right[v]);
            }
            
            if (sumL != sumR) return false;
        }
        
        return qL.isEmpty() && qR.isEmpty();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] colors = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            colors[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque

# Increase recursion depth
sys.setrecursionlimit(200000)

def mirror_check(n: int, values: list[int], colors: list[int], left: list[int], right: list[int]) -> bool:
    if n == 0:
        return True
        
    # 1. Check Symmetry
    def is_mirror(u, v):
        if u == -1 and v == -1:
            return True
        if u == -1 or v == -1:
            return False
        if values[u] != values[v]:
            return False
        return is_mirror(left[u], right[v]) and is_mirror(right[u], left[v])
        
    if left[0] == -1 and right[0] == -1:
        return True
    if not is_mirror(left[0], right[0]):
        return False
        
    # 2. Check Color Balance
    qL = deque([left[0]])
    qR = deque([right[0]])
    
    while qL and qR:
        if len(qL) != len(qR):
            return False
            
        sumL = 0
        size = len(qL)
        for _ in range(size):
            u = qL.popleft()
            sumL += colors[u]
            if left[u] != -1: qL.append(left[u])
            if right[u] != -1: qL.append(right[u])
            
        sumR = 0
        for _ in range(size):
            v = qR.popleft()
            sumR += colors[v]
            if left[v] != -1: qR.append(left[v])
            if right[v] != -1: qR.append(right[v])
            
        if sumL != sumR:
            return False
            
    return not qL and not qR

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    values = [0] * n
    colors = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        colors[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    print("true" if mirror_check(n, values, colors, left, right) else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

class Solution {
    bool checkMirror(int u, int v, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        if (u == -1 && v == -1) return true;
        if (u == -1 || v == -1) return false;
        if (values[u] != values[v]) return false;
        return checkMirror(left[u], right[v], values, left, right) &&
               checkMirror(right[u], left[v], values, left, right);
    }

public:
    bool mirrorCheck(int n, const vector<int>& values, const vector<int>& colors,
                     const vector<int>& left, const vector<int>& right) {
        if (n == 0) return true;
        
        if (left[0] == -1 && right[0] == -1) return true;
        if (!checkMirror(left[0], right[0], values, left, right)) return false;
        
        // Color Check
        queue<int> qL, qR;
        qL.push(left[0]);
        qR.push(right[0]);
        
        while (!qL.empty() && !qR.empty()) {
            if (qL.size() != qR.size()) return false;
            
            int size = qL.size();
            long long sumL = 0;
            for (int i = 0; i < size; i++) {
                int u = qL.front(); qL.pop();
                sumL += colors[u];
                if (left[u] != -1) qL.push(left[u]);
                if (right[u] != -1) qL.push(right[u]);
            }
            
            long long sumR = 0;
            for (int i = 0; i < size; i++) {
                int v = qR.front(); qR.pop();
                sumR += colors[v];
                if (left[v] != -1) qR.push(left[v]);
                if (right[v] != -1) qR.push(right[v]);
            }
            
            if (sumL != sumR) return false;
        }
        
        return qL.empty() && qR.empty();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), colors(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> colors[i] >> left[i] >> right[i];
    }

    Solution solution;
    cout << (solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  mirrorCheck(n, values, colors, left, right) {
    if (n === 0) return true;
    
    // Helper for symmetry
    const isMirror = (u, v) => {
      if (u === -1 && v === -1) return true;
      if (u === -1 || v === -1) return false;
      if (values[u] !== values[v]) return false;
      return isMirror(left[u], right[v]) && isMirror(right[u], left[v]);
    };
    
    if (left[0] === -1 && right[0] === -1) return true;
    if (!isMirror(left[0], right[0])) return false;
    
    // Helper for color balance
    const qL = [left[0]];
    const qR = [right[0]];
    
    while (qL.length > 0 && qR.length > 0) {
      if (qL.length !== qR.length) return false;
      
      const size = qL.length;
      let sumL = 0;
      for (let i = 0; i < size; i++) {
        const u = qL.shift();
        sumL += colors[u];
        if (left[u] !== -1) qL.push(left[u]);
        if (right[u] !== -1) qL.push(right[u]);
      }
      
      let sumR = 0;
      for (let i = 0; i < size; i++) {
        const v = qR.shift();
        sumR += colors[v];
        if (left[v] !== -1) qR.push(left[v]);
        if (right[v] !== -1) qR.push(right[v]);
      }
      
      if (sumL !== sumR) return false;
    }
    
    return qL.length === 0 && qR.length === 0;
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
  const colors = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    colors[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false");
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
7
4 0 1 2
2 1 3 4
2 1 5 6
1 0 -1 -1
3 1 -1 -1
3 1 -1 -1
1 0 -1 -1
```

**Structure:**
- Root(4,0) -> L(2,1), R(2,1)
- L -> L(1,0), R(3,1)
- R -> L(3,1), R(1,0)

**Symmetry Check:**
- `val(L) == val(R)` (2==2). OK.
- `L.left(1)` vs `R.right(1)`. Values 1==1. OK.
- `L.right(3)` vs `R.left(3)`. Values 3==3. OK.
- Symmetry Passed.

**Color Check:**
- **Level 1:** `qL=[1]`, `qR=[2]`.
  - `sumL = color[1] = 1`.
  - `sumR = color[2] = 1`.
  - Match.
  - `qL` adds children of 1: 3, 4.
  - `qR` adds children of 2: 5, 6.
- **Level 2:** `qL=[3, 4]`, `qR=[5, 6]`.
  - `sumL = color[3] + color[4] = 0 + 1 = 1`.
  - `sumR = color[5] + color[6] = 1 + 0 = 1`.
  - Match.
- **Level 3:** Empty.

**Result:** `true`.

## ✅ Proof of Correctness

1.  **Symmetry:** Standard recursive check ensures structural and value mirroring.
2.  **Color Balance:** BFS ensures we process nodes level by level. By summing colors (since they are 0/1) or using a frequency map (for general colors), we verify the multiset condition. Since we check every level, the condition is fully verified.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: General Colors**
    -   If colors were 0-100, use a `HashMap` or frequency array instead of `sum`.
-   **Extension 2: Foldable Tree**
    -   Check structure symmetry only (ignore values).
-   **Extension 3: Iterative Symmetry**
    -   Implement `isSymmetric` using a Queue/Stack instead of recursion.

## Common Mistakes to Avoid

1.  **Checking Colors in Symmetry Function:**
    -   ❌ `if (color[u] != color[v]) return false;`
    -   ✅ Problem says colors don't need to match node-for-node, only level-multiset.
2.  **Queue Sync:**
    -   ❌ Processing `qL` and `qR` at different rates.
    -   ✅ Must process exactly `size` nodes for both queues at each step.

## Related Concepts

-   **Symmetric Tree (LeetCode 101)**
-   **BFS Level Order**
-   **Multiset Equality**
