---
problem_id: TRE_HOSTEL_BOUNDARY_WALK_GAPS__3187
display_id: TRE-008
slug: hostel-boundary-walk-gaps
title: "Hostel Boundary Walk with Gaps"
difficulty: Medium
difficulty_score: 44
topics:
  - Trees
  - Boundary Traversal
  - DFS
tags:
  - trees
  - traversal
  - boundary
  - medium
premium: true
subscription_tier: basic
---

# TRE-008: Hostel Boundary Walk with Gaps

## 📋 Problem Summary

Perform a **boundary traversal** of a binary tree. The boundary includes:
1.  The **root** node.
2.  The **left boundary** (nodes on the leftmost path, excluding leaf nodes).
3.  All **leaf nodes** (from left to right).
4.  The **right boundary** (nodes on the rightmost path, excluding leaf nodes) in reverse order (bottom-up).

However, there is a twist: you must **skip** any node whose value is negative. The structural traversal remains the same (i.e., a negative node still defines the boundary path), but its value is not included in the output.

## 🌍 Real-World Scenario

**Scenario Title:** Perimeter Security Patrol

Imagine a security guard patrolling the perimeter (boundary) of a hostel complex.
-   **Root:** Main Gate.
-   **Left Boundary:** West Wall.
-   **Leaves:** Southern Fence (back of the complex).
-   **Right Boundary:** East Wall.

The guard has a checklist of checkpoints to log. Some checkpoints are marked "Inactive" (negative value) due to maintenance. The guard must walk the full perimeter path to ensure security but should only log the active checkpoints in the report.

![Real-World Application](../images/TRE-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
        1
       / \
      2   3
     / \   \
    4   5   6
       / \
      7   8
```
**Boundary Nodes:**
-   **Root:** 1
-   **Leaves:** 4, 7, 8, 6.
-   **Right Boundary:** 3 (6 is a leaf).

**Traversal Order:** 1 -> 2 -> 4 -> 7 -> 8 -> 6 -> 3.

**With Negative Values:**
If node 2 is `-5`:
Output: 1 -> 4 -> 7 -> 8 -> 6 -> 3. (Skip -5).

### Algorithm Steps

1.  **Root:** Add root value if non-negative.
2.  **Left Boundary:** Start from `root.left`.
    -   If node is a leaf, stop.
    -   Add value if non-negative.
    -   Move to `left` child if exists, else `right` child.
3.  **Leaves:** DFS traversal.
    -   If node is leaf, add value if non-negative.
4.  **Right Boundary:** Start from `root.right`.
    -   If node is a leaf, stop.
    -   Store values in a temporary list (or stack).
    -   Move to `right` child if exists, else `left` child.
    -   After collecting, add values in reverse order (if non-negative).

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Root as Leaf:** If root has no children, it's a leaf. Don't add it twice.
-   **Overlap:** Left boundary and leaves should not duplicate nodes. Right boundary and leaves should not duplicate nodes.
-   **Negative Values:** Only affects *output*, not the path logic. A negative node can still have children that are part of the boundary.

## Naive Approach

### Intuition

We can collect all boundary nodes into a list using the standard algorithm, and then filter out negative values at the very end.

### Algorithm

1.  `boundary = []`.
2.  Add Root.
3.  Traverse Left Boundary -> Add to `boundary`.
4.  Traverse Leaves -> Add to `boundary`.
5.  Traverse Right Boundary -> Add to `boundary` (reverse).
6.  Filter `boundary` for `val >= 0`.

### Time Complexity

-   **O(N)**: Visit boundary nodes and leaves.

## Optimal Approach (Standard Boundary Traversal)

The logic is identical to the naive approach, but we can filter "on the fly" to save memory (though O(N) memory is usually fine).

### Algorithm

1.  If `n=0`, return empty.
2.  If `root.val >= 0`, add to result.
3.  **Left Boundary:**
    -   `curr = root.left`.
    -   While `curr` is not leaf:
        -   If `curr.val >= 0`, add.
        -   `curr = curr.left ? curr.left : curr.right`.
4.  **Leaves:**
    -   `addLeaves(root)`. (Helper DFS).
    -   If leaf and `val >= 0`, add.
    -   Note: Root is technically a leaf if `n=1`. Handle carefully to avoid double counting. (Common trick: `addLeaves` skips root if it was already added, or Left Boundary logic handles root exclusion).
    -   *Better:* Left Boundary starts `root.left`. Leaves starts `root`. Right Boundary starts `root.right`.
    -   If `root` is leaf, Left/Right boundary loops won't run. `addLeaves` will add it. So don't add root in Step 1? Or exclude root from `addLeaves`?
    -   *Standard:* Add Root. Left Boundary (exclude root, exclude leaf). Leaves (exclude root? No, leaves are leaves). Right Boundary (exclude root, exclude leaf).
    -   If `n=1`, Root is added. Left/Right loops empty. `addLeaves` adds root. Double count!
    -   *Fix:* `addLeaves` should only add if `node != root`. Or simply:
        -   Add Root.
        -   `getLeft(root.left)`.
        -   `getLeaves(root.left)`.
        -   `getLeaves(root.right)`.
        -   `getRight(root.right)`.

### Time Complexity

-   **O(N)**.

### Space Complexity

-   **O(N)** output.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public List<Integer> boundaryWithGaps(int n, int[] values, int[] left, int[] right) {
        List<Integer> result = new ArrayList<>();
        if (n == 0) return result;

        // 1. Root
        if (values[0] >= 0) {
            result.add(values[0]);
        }

        if (left[0] == -1 && right[0] == -1) {
            return result; // Single node, already added
        }

        // 2. Left Boundary
        int curr = left[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break; // Is leaf
            if (values[curr] >= 0) result.add(values[curr]);
            if (left[curr] != -1) curr = left[curr];
            else curr = right[curr];
        }

        // 3. Leaves
        addLeaves(0, values, left, right, result);

        // 4. Right Boundary
        List<Integer> rightBound = new ArrayList<>();
        curr = right[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break; // Is leaf
            if (values[curr] >= 0) rightBound.add(values[curr]);
            if (right[curr] != -1) curr = right[curr];
            else curr = left[curr];
        }
        Collections.reverse(rightBound);
        result.addAll(rightBound);

        return result;
    }

    private void addLeaves(int u, int[] values, int[] left, int[] right, List<Integer> result) {
        if (u == -1) return;
        if (left[u] == -1 && right[u] == -1) {
            if (values[u] >= 0) result.add(values[u]);
            return;
        }
        addLeaves(left[u], values, left, right, result);
        addLeaves(right[u], values, left, right, result);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<Integer> ans = solution.boundaryWithGaps(n, values, left, right);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python
```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def boundary_with_gaps(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
    if n == 0:
        return []
        
    result = []
    
    # 1. Root
    if values[0] >= 0:
        result.append(values[0])
        
    if left[0] == -1 and right[0] == -1:
        return result

    # 2. Left Boundary
    curr = left[0]
    while curr != -1:
        if left[curr] == -1 and right[curr] == -1:
            break # Leaf
        if values[curr] >= 0:
            result.append(values[curr])
        if left[curr] != -1:
            curr = left[curr]
        else:
            curr = right[curr]
            
    # 3. Leaves
    def add_leaves(u):
        if u == -1:
            return
        if left[u] == -1 and right[u] == -1:
            if values[u] >= 0:
                result.append(values[u])
            return
        add_leaves(left[u])
        add_leaves(right[u])
        
    add_leaves(0)
    
    # 4. Right Boundary
    right_bound = []
    curr = right[0]
    while curr != -1:
        if left[curr] == -1 and right[curr] == -1:
            break # Leaf
        if values[curr] >= 0:
            right_bound.append(values[curr])
        if right[curr] != -1:
            curr = right[curr]
        else:
            curr = left[curr]
            
    result.extend(reversed(right_bound))
    return result

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    ans = boundary_with_gaps(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    void addLeaves(int u, const vector<int>& values, const vector<int>& left, const vector<int>& right, vector<int>& result) {
        if (u == -1) return;
        if (left[u] == -1 && right[u] == -1) {
            if (values[u] >= 0) result.push_back(values[u]);
            return;
        }
        addLeaves(left[u], values, left, right, result);
        addLeaves(right[u], values, left, right, result);
    }

public:
    vector<int> boundaryWithGaps(int n, const vector<int>& values,
                                 const vector<int>& left, const vector<int>& right) {
        vector<int> result;
        if (n == 0) return result;

        if (values[0] >= 0) result.push_back(values[0]);
        if (left[0] == -1 && right[0] == -1) return result;

        // Left Boundary
        int curr = left[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break;
            if (values[curr] >= 0) result.push_back(values[curr]);
            if (left[curr] != -1) curr = left[curr];
            else curr = right[curr];
        }

        // Leaves
        addLeaves(0, values, left, right, result);

        // Right Boundary
        vector<int> rightBound;
        curr = right[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break;
            if (values[curr] >= 0) rightBound.push_back(values[curr]);
            if (right[curr] != -1) curr = right[curr];
            else curr = left[curr];
        }
        reverse(rightBound.begin(), rightBound.end());
        result.insert(result.end(), rightBound.begin(), rightBound.end());

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<int> ans = solution.boundaryWithGaps(n, values, left, right);
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  boundaryWithGaps(n, values, left, right) {
    const result = [];
    if (n === 0) return result;

    if (values[0] >= 0) result.push(values[0]);
    if (left[0] === -1 && right[0] === -1) return result;

    // Left Boundary
    let curr = left[0];
    while (curr !== -1) {
      if (left[curr] === -1 && right[curr] === -1) break;
      if (values[curr] >= 0) result.push(values[curr]);
      if (left[curr] !== -1) curr = left[curr];
      else curr = right[curr];
    }

    // Leaves
    const addLeaves = (u) => {
      if (u === -1) return;
      if (left[u] === -1 && right[u] === -1) {
        if (values[u] >= 0) result.push(values[u]);
        return;
      }
      addLeaves(left[u]);
      addLeaves(right[u]);
    };
    addLeaves(0);

    // Right Boundary
    const rightBound = [];
    curr = right[0];
    while (curr !== -1) {
      if (left[curr] === -1 && right[curr] === -1) break;
      if (values[curr] >= 0) rightBound.push(values[curr]);
      if (right[curr] !== -1) curr = right[curr];
      else curr = left[curr];
    }
    rightBound.reverse();
    result.push(...rightBound);

    return result;
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
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  const ans = solution.boundaryWithGaps(n, values, left, right);
  console.log(ans.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
10 1 2
-5 3 -1
15 -1 -1
2 -1 -1
```
**Tree:**
- 0(10) -> L:1(-5), R:2(15)
- 1(-5) -> L:3(2), R:-1
- 2(15) -> Leaf
- 3(2) -> Leaf

**Execution:**
1.  **Root:** 10 >= 0. Add `10`.
2.  **Left Boundary:** Start at 1(-5).
    -   Not leaf.
    -   Val -5 < 0. Skip.
    -   Move to left child 3(2).
    -   3(2) is leaf. Stop.
3.  **Leaves:**
    -   DFS(0) -> DFS(1) -> DFS(3). 3(2) is leaf. Val 2 >= 0. Add `2`.
    -   DFS(2). 2(15) is leaf. Val 15 >= 0. Add `15`.
4.  **Right Boundary:** Start at 2(15).
    -   2(15) is leaf. Stop.

**Result:** `10 2 15`. Correct.

## ✅ Proof of Correctness

The algorithm decomposes the boundary into three disjoint sets (except for potential root/leaf overlaps which are handled):
1.  **Left Boundary:** Strictly follows the leftmost path.
2.  **Leaves:** Strictly follows DFS order (left-to-right).
3.  **Right Boundary:** Strictly follows the rightmost path.
By handling the root separately and ensuring boundary loops stop *before* leaves, we ensure no node is visited twice (except root if `n=1`, handled).
The negative check is a simple filter applied at the point of addition.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Anti-Clockwise vs Clockwise**
    -   Implement clockwise boundary traversal.
-   **Extension 2: Spiral Boundary**
    -   Complex variant.
-   **Extension 3: Sum of Boundary**
    -   Calculate sum instead of listing values.

### Common Mistakes to Avoid

1.  **Double Counting Leaves:**
    -   ❌ Adding a leaf in Left Boundary AND Leaves section.
    -   ✅ Stop Left/Right boundary loops when `isLeaf(curr)` is true.
2.  **Root Duplication:**
    -   ❌ Adding root in Left Boundary loop.
    -   ✅ Start Left Boundary loop from `root.left`.
3.  **Reverse Order:**
    -   ❌ Forgetting to reverse the Right Boundary.

## Related Concepts

-   **Tree Traversal**
-   **DFS**
