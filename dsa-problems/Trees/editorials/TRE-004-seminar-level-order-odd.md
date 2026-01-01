---
problem_id: TRE_SEMINAR_LEVEL_ORDER_ODD__5168
display_id: TRE-004
slug: seminar-level-order-odd
title: "Seminar Level Order Odd-Depth Only"
difficulty: Easy
difficulty_score: 26
topics:
  - Trees
  - BFS
  - Level Order
tags:
  - trees
  - bfs
  - traversal
  - easy
premium: true
subscription_tier: basic
---

# TRE-004: Seminar Level Order Odd-Depth Only

## 📋 Problem Summary

Perform a **level-order traversal** (BFS) of a binary tree, but only output the values of nodes located at **odd depths**. The root is considered to be at depth 0. For each odd depth, print the node values in a single line, from left to right.

## 🌍 Real-World Scenario

**Scenario Title:** University Course Prerequisites

Imagine a university curriculum structured as a tree.
-   **Depth 0 (Root):** "Intro to CS" (Freshman Fall).
-   **Depth 1:** "Data Structures", "Algorithms" (Freshman Spring).
-   **Depth 2:** "OS", "Networks" (Sophomore Fall).
-   **Depth 3:** "Distributed Systems", "AI" (Sophomore Spring).

The university wants to schedule seminars specifically for the Spring semester courses (which happen to be at odd depths 1, 3, etc.). By filtering the tree traversal to only odd depths, you can generate the list of courses that need seminar rooms for the Spring term.

![Real-World Application](../images/TRE-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      10 (Depth 0)
     /  \
    5    12 (Depth 1)
   /
  7 (Depth 2)
```
**Levels:**
-   **Depth 0:** [10] -> Even. Skip.
-   **Depth 1:** [5, 12] -> Odd. **Output**.
-   **Depth 2:** [7] -> Even. Skip.

**Output:**
```
5 12
```

### Algorithm Steps

1.  Use a **Queue** for Breadth-First Search (BFS).
2.  Start with the root at `depth = 0`.
3.  While the queue is not empty:
    -   Get the number of nodes at the current level (`size`).
    -   Initialize a list for the current level's values.
    -   Process `size` nodes:
        -   Add children to the queue.
        -   Add value to the list.
    -   If `depth % 2 != 0`, print/store the list.
    -   Increment `depth`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Root Depth:** 0 (Even).
-   **Empty Tree:** Output nothing (or a blank line depending on specific constraints, here blank line).
-   **Order:** Left-to-right is preserved by standard queue-based BFS.

## Naive Approach

### Intuition

We can traverse the tree using DFS (Preorder) and store nodes in a list of lists `levels[depth]`. After traversing the whole tree, we iterate through `levels` and print only those at odd indices.

### Algorithm

1.  `levels = []`.
2.  `dfs(node, depth)`:
    -   If `depth >= levels.size()`, add new list.
    -   `levels[depth].add(node.val)`.
    -   `dfs(left, depth + 1)`.
    -   `dfs(right, depth + 1)`.
3.  Print `levels[1], levels[3], ...`.

### Time Complexity

-   **O(N)**: Visit every node.

### Space Complexity

-   **O(N)**: To store all node values in the list of lists.

## Optimal Approach (BFS)

BFS is more natural for level-order problems. We can process level by level and discard the values immediately after printing, saving space compared to storing everything (though we still need the queue).

### Algorithm

1.  If `n=0`, return empty.
2.  Queue `q`, add `0`. `depth = 0`.
3.  Loop while `q` not empty:
    -   `count = q.size()`.
    -   `currentLevelNodes = []`.
    -   Loop `count` times:
        -   `u = q.poll()`.
        -   If `depth % 2 != 0`, add `values[u]` to `currentLevelNodes`.
        -   Add children of `u` to `q`.
    -   If `currentLevelNodes` is not empty, add to result.
    -   `depth++`.

### Time Complexity

-   **O(N)**: Each node processed once.

### Space Complexity

-   **O(W)**: Max width of tree (queue size).

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public List<List<Integer>> oddDepthLevels(int n, int[] left, int[] right, int[] values) {
        List<List<Integer>> result = new ArrayList<>();
        if (n == 0) return result;

        Queue<Integer> q = new LinkedList<>();
        q.offer(0);
        int depth = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> currentLevel = new ArrayList<>();
            boolean isOdd = (depth % 2 != 0);

            for (int i = 0; i < size; i++) {
                int u = q.poll();
                if (isOdd) {
                    currentLevel.add(values[u]);
                }
                
                if (left[u] != -1) q.offer(left[u]);
                if (right[u] != -1) q.offer(right[u]);
            }

            if (isOdd) {
                result.add(currentLevel);
            }
            depth++;
        }
        return result;
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
        List<List<Integer>> levels = solution.oddDepthLevels(n, left, right, values);
        if (levels.isEmpty()) {
            System.out.println();
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < levels.size(); i++) {
                List<Integer> lvl = levels.get(i);
                for (int j = 0; j < lvl.size(); j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(lvl.get(j));
                }
                if (i + 1 < levels.size()) sb.append('\n');
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python
```python
import sys
sys.setrecursionlimit(200000)
from collections import deque

def odd_depth_levels(n: int, left: list[int], right: list[int], values: list[int]) -> list[list[int]]:
    if n == 0:
        return []
        
    result = []
    q = deque([0])
    depth = 0
    
    while q:
        size = len(q)
        current_level = []
        is_odd = (depth % 2 != 0)
        
        for _ in range(size):
            u = q.popleft()
            if is_odd:
                current_level.append(values[u])
            
            if left[u] != -1:
                q.append(left[u])
            if right[u] != -1:
                q.append(right[u])
        
        if is_odd:
            result.append(current_level)
        depth += 1
        
    return result

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    if n == 0:
        print()
        return

    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    levels = odd_depth_levels(n, left, right, values)
    if not levels:
        print()
    else:
        print("\n".join(" ".join(str(x) for x in lvl) for lvl in levels))

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
    vector<vector<int>> oddDepthLevels(int n, const vector<int>& left,
                                       const vector<int>& right, const vector<int>& values) {
        vector<vector<int>> result;
        if (n == 0) return result;
        
        queue<int> q;
        q.push(0);
        int depth = 0;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> currentLevel;
            bool isOdd = (depth % 2 != 0);
            
            for (int i = 0; i < size; i++) {
                int u = q.front();
                q.pop();
                
                if (isOdd) {
                    currentLevel.push_back(values[u]);
                }
                
                if (left[u] != -1) q.push(left[u]);
                if (right[u] != -1) q.push(right[u]);
            }
            
            if (isOdd) {
                result.push_back(currentLevel);
            }
            depth++;
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    if (n == 0) {
        cout << "\n";
        return 0;
    }

    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<vector<int>> levels = solution.oddDepthLevels(n, left, right, values);
    if (levels.empty()) {
        cout << "\n";
    } else {
        for (int i = 0; i < (int)levels.size(); i++) {
            for (int j = 0; j < (int)levels[i].size(); j++) {
                if (j) cout << ' ';
                cout << levels[i][j];
            }
            if (i + 1 < (int)levels.size()) cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  oddDepthLevels(n, left, right, values) {
    if (n === 0) return [];
    
    const result = [];
    const q = [0];
    let depth = 0;
    
    while (q.length > 0) {
      const size = q.length;
      const currentLevel = [];
      const isOdd = (depth % 2 !== 0);
      
      for (let i = 0; i < size; i++) {
        const u = q.shift();
        
        if (isOdd) {
          currentLevel.push(values[u]);
        }
        
        if (left[u] !== -1) q.push(left[u]);
        if (right[u] !== -1) q.push(right[u]);
      }
      
      if (isOdd) {
        result.push(currentLevel);
      }
      depth++;
    }
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
  
  if (n === 0) {
      console.log("");
      return;
  }
  
  const values = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  const levels = solution.oddDepthLevels(n, left, right, values);
  if (levels.length === 0) {
    console.log("");
  } else {
    console.log(levels.map((lvl) => lvl.join(" ")).join("\n"));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
10 1 2
5 3 -1
12 -1 -1
7 -1 -1
```

**Execution:**
1.  `q = [0]`, `depth = 0`.
2.  **Level 0 (Even):**
    -   Pop 0 (10). Push 1 (5), 2 (12).
    -   `isOdd = false`. Do not add 10.
    -   `q = [1, 2]`.
3.  **Level 1 (Odd):**
    -   Pop 1 (5). Push 3 (7). Add 5 to list.
    -   Pop 2 (12). No children. Add 12 to list.
    -   `isOdd = true`. List: `[5, 12]`. Add to result.
    -   `q = [3]`.
4.  **Level 2 (Even):**
    -   Pop 3 (7). No children.
    -   `isOdd = false`. Do not add 7.
    -   `q = []`.
5.  End.

**Output:** `5 12`. Correct.

## ✅ Proof of Correctness

The BFS algorithm guarantees that nodes are visited level by level, and within each level, from left to right (assuming children are enqueued left then right).
By maintaining a `depth` counter and checking `depth % 2 != 0`, we strictly filter for odd levels.
The queue ensures that we process all nodes at depth `d` before any node at depth `d+1`.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Zigzag Traversal**
    -   Print odd levels left-to-right, even levels right-to-left.
-   **Extension 2: Average of Levels**
    -   Compute average value of nodes at each level.
-   **Extension 3: Connect Next Pointers**
    -   Populate a `next` pointer for each node pointing to its right neighbor in the same level.

### Common Mistakes to Avoid

1.  **Depth Indexing:**
    -   ❌ Assuming root is depth 1.
    -   ✅ Problem states root is depth 0.
2.  **Queue Size Loop:**
    -   ❌ `for (int i=0; i<q.size(); i++)` inside while loop. `q.size()` changes!
    -   ✅ Capture `size = q.size()` before the loop.

## Related Concepts

-   **BFS**
-   **Queue Data Structure**
-   **Tree Depth vs Height**
