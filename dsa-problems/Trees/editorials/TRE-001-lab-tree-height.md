---
problem_id: TRE_LAB_TREE_HEIGHT__2847
display_id: TRE-001
slug: lab-tree-height
title: "Lab Tree Height"
difficulty: Easy
difficulty_score: 15
topics:
  - Trees
  - Binary Tree
  - Recursion
tags:
  - trees
  - binary-tree
  - recursion
  - tree-height
  - dfs
premium: true
subscription_tier: basic
---

# TRE-001: Lab Tree Height

## �� Problem Summary

Given the root of a binary tree, compute its height (the number of edges on the longest path from root to any leaf). This is a fundamental tree property that measures the depth of the tree structure. An empty tree has height -1, and a single-node tree has height 0.

## 🌍 Real-World Scenario

**Scenario Title:** University Lab Access Control System

Imagine you're designing an access control system for a university's computer science lab. The lab has a hierarchical permission structure represented as a tree where:

- The **root** represents the Lab Director
- **Internal nodes** represent Team Leads, Project Managers, and Supervisors  
- **Leaf nodes** represent individual students and researchers

When a security incident occurs, the system needs to determine the **maximum chain of command depth** to understand how many approval levels might be required for emergency access override. For example, if a critical server needs emergency maintenance, the system must know: "How many management levels deep is our organizational structure?" This helps determine response time and escalation procedures.

In practice, the height of this tree tells administrators:
- **Emergency response time**: Each level adds ~30 minutes to decision-making
- **Communication overhead**: More levels mean more coordination complexity
- **Organizational efficiency**: Very deep trees (height > 5) might indicate over-management
- **Access audit trails**: Height determines the maximum audit log chain length

This problem applies to any hierarchical system: corporate org charts, file system directory depths, network topology analysis, and database query plan optimization where tree depth impacts performance.

**Why This Problem Matters:**

- **System Design**: Understanding tree depth helps optimize cache sizes and memory allocation
- **Performance Analysis**: Tree height correlates with worst-case operation time in many data structures (BST, heap, etc.)
- **Resource Planning**: Network administrators use tree height to calculate maximum latency in routing hierarchies

![Real-World Application](../images/TRE-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Tree Height Visualization

```
Example 1: Height = 2
       5
      / \
     3   9
    /
   1

Depth 0: [5]        (root level)
Depth 1: [3, 9]     (1 edge from root)
Depth 2: [1]        (2 edges from root) ← maximum depth

Height = max edges = 2

Legend:
  / \ = parent-child relationship
  [x] = node at depth x
  Height = maximum depth (in edges)

Example 2: Height = 0
   42
   
Only root, no edges → Height = 0

Example 3: Height = -1
   (empty)
   
No nodes → Height = -1 (by convention)

Example 4: Height = 3
         1
        / \
       2   3
      /   / \
     4   5   6
    /
   7

Path 1→2→4→7: 3 edges (longest)
Height = 3
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Height vs Depth**: Height is measured from root downward (max edges to leaf), depth is measured from a specific node upward to root
- **Edge-based, not node-based**: A tree with 3 nodes in a chain has height 2 (two edges), not 3
- **Empty tree convention**: Returns -1 (some definitions use 0, but we use -1)
- **Single node**: A tree with only a root has height 0 (zero edges)

Common interpretation mistakes:

- ❌ **Wrong**: Counting nodes instead of edges (height = number of nodes on longest path)
- ✅ **Correct**: Counting edges (height = number of edges on longest path)

- ❌ **Wrong**: Returning 0 for an empty tree
- ✅ **Correct**: Returning -1 for an empty tree (as specified)

### Understanding Tree Height

The height of a binary tree is the length of the longest path from the root to any leaf node, measured in edges. This is different from the number of nodes on the path.

### Why Naive Iteration is Complicated

A naive iterative approach would require:
1. Level-order traversal (BFS)  
2. Tracking depth at each node
3. Maintaining a queue with (node, depth) pairs
4. Updating maximum depth seen

While this works, it requires O(N) space for the queue and more complex bookkeeping.

## Optimal Approach (Recursive DFS)

### Key Insight

The height of a tree can be computed recursively:
- If the tree is empty (null), return -1
- Otherwise, the height is: `1 + max(height of left subtree, height of right subtree)`

This elegant recursive formula breaks down the problem:
1. Base case: null node → height = -1
2. Recursive case: height = 1 (current edge) + max(left height, right height)

### Algorithm

1. **Base Case**: If `root == null`, return `-1`
2. **Recursive Step**:
   - Recursively compute `leftHeight = height(root.left)`
   - Recursively compute `rightHeight = height(root.right)`
   - Return `1 + max(leftHeight, rightHeight)`
3. The function naturally explores all paths and finds the maximum

### Time Complexity

- **O(N)** where N is the number of nodes
- We visit each node exactly once in post-order fashion
- At each node, we do O(1) work (comparison and addition)

### Space Complexity

- **O(H)** where H is the height of the tree
- Space is used for the recursive call stack
- In the worst case (skewed tree), H = N, so O(N)
- In the best case (balanced tree), H = log(N), so O(log N)

### Why This Is Optimal

We must visit every node at least once to determine which is the deepest, so O(N) time is optimal. The recursive approach is clean, easy to implement, and directly matches the problem definition.

![Algorithm Visualization](../images/TRE-001/algorithm-visualization.png)
![Algorithm Steps](../images/TRE-001/algorithm-steps.png)

## Implementations

### Java

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    /**
     * Computes the height of a binary tree.
     * Height = number of edges on the longest path from root to leaf.
     * 
     * @param root The root node of the binary tree
     * @return The height of the tree (-1 for empty, 0 for single node)
     */
    public int height(TreeNode root) {
        // Base case: empty tree has height -1
        if (root == null) {
            return -1;
        }
        
        // Recursive case: compute height of left and right subtrees
        int leftHeight = height(root.left);
        int rightHeight = height(root.right);
        
        // Height is 1 (current edge) + max of subtree heights
        return 1 + Math.max(leftHeight, rightHeight);
    }
}

// Main class with input parsing (already provided in problem template)
```

### Python

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root: TreeNode) -> int:
    """
    Computes the height of a binary tree.
    Height = number of edges on the longest path from root to leaf.
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        The height of the tree (-1 for empty, 0 for single node)
    """
    # Base case: empty tree has height -1
    if root is None:
        return -1
    
    # Recursive case: compute height of left and right subtrees
    left_height = height(root.left)
    right_height = height(root.right)
    
    # Height is 1 (current edge) + max of subtree heights
    return 1 + max(left_height, right_height)

# Main function with input parsing (already provided in problem template)
```

### C++

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    /**
     * Computes the height of a binary tree.
     * Height = number of edges on the longest path from root to leaf.
     * 
     * @param root The root node of the binary tree
     * @return The height of the tree (-1 for empty, 0 for single node)
     */
    int height(TreeNode* root) {
        // Base case: empty tree has height -1
        if (root == nullptr) {
            return -1;
        }
        
        // Recursive case: compute height of left and right subtrees
        int leftHeight = height(root->left);
        int rightHeight = height(root->right);
        
        // Height is 1 (current edge) + max of subtree heights
        return 1 + max(leftHeight, rightHeight);
    }
};

// Main function with input parsing (already provided in problem template)
```

### JavaScript

```javascript
class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    /**
     * Computes the height of a binary tree.
     * Height = number of edges on the longest path from root to leaf.
     * 
     * @param {TreeNode} root - The root node of the binary tree
     * @return {number} The height of the tree (-1 for empty, 0 for single node)
     */
    height(root) {
        // Base case: empty tree has height -1
        if (root === null) {
            return -1;
        }
        
        // Recursive case: compute height of left and right subtrees
        const leftHeight = this.height(root.left);
        const rightHeight = this.height(root.right);
        
        // Height is 1 (current edge) + max of subtree heights
        return 1 + Math.max(leftHeight, rightHeight);
    }
}

// Main function with input parsing (already provided in problem template)
```

## 🧪 Test Case Walkthrough (Dry Run)

Use the sample:
- Tree with 5 nodes: values [5, 3, 9, 1, -1], parents [-1, 0, 0, 1, -1]
- This builds the tree:
```
       5
      / \
     3   9
    /
   1
```

We maintain:
- Current recursion depth
- Height computed at each node

Call `height(node_5)` (root):

| Call Stack | Node | Left Height | Right Height | Calculation | Returns |
|-----------:|:----:|------------:|-------------:|-------------|--------:|
| 1 | 5 | ? | ? | Recurse left and right | ? |
| 2 | 3 | ? | ? | Recurse left and right | ? |
| 3 | 1 | -1 | -1 | 1 + max(-1, -1) = 0 | 0 |
| (back to 2) | 3 | 0 | -1 | 1 + max(0, -1) = 1 | 1 |
| 4 | 9 | -1 | -1 | 1 + max(-1, -1) = 0 | 0 |
| (back to 1) | 5 | 1 | 0 | 1 + max(1, 0) = 2 | 2 |

**Step-by-step execution:**

1. `height(5)` calls `height(3)` and `height(9)`
2. `height(3)` calls `height(1)` and `height(null)`
3. `height(1)` calls `height(null)` and `height(null)` → both return -1
4. `height(1)` returns `1 + max(-1, -1) = 0`
5. `height(3)` gets left = 0, right = -1 → returns `1 + max(0, -1) = 1`
6. `height(9)` calls `height(null)` twice → both return -1 → returns `1 + max(-1, -1) = 0`
7. `height(5)` gets left = 1, right = 0 → returns `1 + max(1, 0) = 2`

**Observations:**
- Leaf node (1): Has no children, returns 0 (zero edges to itself)
- Node 3: One child at distance 1, returns 1
- Node 9: Leaf node, returns 0
- Root 5: Max child height is 1, so returns 1 + 1 = 2

Answer is `2`.

![Example Visualization](../images/TRE-001/example-1.png)

## ✅ Proof of Correctness

### Invariant

At each node, the height returned is the maximum number of edges from that node to any leaf in its subtree.

### Why the approach is correct

**Base Case**: When `root == null`, there are no nodes, hence no edges. By definition, height = -1. This is correct.

**Inductive Step**: Assume the function correctly computes height for all subtrees of size < N. For a tree of size N:
- By the inductive hypothesis, `height(root.left)` returns the correct height h_L of the left subtree
- Similarly, `height(root.right)` returns the correct height h_R of the right subtree
- The longest path from root to any leaf goes through either the left or right child
- This path has length = 1 (edge to the child) + max(h_L, h_R)
- Therefore, `1 + max(h_L, h_R)` is correct

By induction, the algorithm is correct for all tree sizes.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Diameter of Tree** - Find the longest path between any two nodes (not necessarily through root). Solution: At each node, update answer with leftHeight + rightHeight + 2.

- **Extension 2: Check if Balanced** - Determine if the tree is height-balanced (height difference of left and right subtrees ≤ 1 at every node). Solution: Return both height and balance flag from each recursive call.

- **Extension 3: Level with Maximum Nodes** - Find which level has the most nodes. Solution: Use BFS with level tracking, count nodes at each level.

- **Extension 4: K-ary Tree Height** - Generalize to trees where each node can have up to K children. Solution: Return `1 + max(height of all children)`.

- **Extension 5: Height of Forest** - Given multiple disconnected trees (forest), find the maximum height among all trees. Solution: Call height() on each root and return the maximum.

## Common Mistakes to Avoid

1. **Counting Nodes Instead of Edges**
   - Description: Returning the number of nodes on the longest path instead of edges
   - ❌ Wrong: `return 1 + max(leftHeight, rightHeight)` where leaf returns 1
   - ✅ Correct: Leaf returns 0 (no edges below it)

2. **Empty Tree Returns 0**
   - Description: Returning 0 for null input when the problem expects -1
   - ❌ Wrong: `if (root == null) return 0;`
   - ✅ Correct: `if (root == null) return -1;`

3. **Forgetting the +1**
   - Description: Not counting the edge from current node to child
   - ❌ Wrong: `return max(leftHeight, rightHeight);`
   - ✅ Correct: `return 1 + max(leftHeight, rightHeight);`

4. **Stack Overflow on Large Trees**
   - Description: Not considering iterative approach for very deep trees
   - Impact: Recursion depth > 10^5 can cause stack overflow
   - Prevention: For extremely deep trees, use iterative BFS with explicit queue

5. **Confusing Height with Depth**
   - Description: Height is measured from a node downward; depth is measured upward to root
   - Impact: Getting off-by-one errors or wrong base cases
   - Prevention: Clearly define: "height = max edges from this node to any leaf below it"

## Related Concepts

- **Tree Depth**: Distance from root to a specific node
- **Tree Diameter**: Longest path between any two nodes
- **Balanced Trees**: Height difference between subtrees ≤ 1
- **Level-Order Traversal**: BFS approach to compute height iteratively
- **Post-Order Traversal**: The recursive solution follows post-order (left-right-root)
- **AVL Trees**: Self-balancing trees that maintain height balance property
- **Recursion Tree Analysis**: Understanding time complexity through recursion trees
