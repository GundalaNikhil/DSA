---
problem_id: TRE_CAMPUS_DIRECTORY_MULTI_TREE__4813
display_id: TRE-001
slug: campus-directory-multi-tree
title: "Campus Directory Multi-Tree Comparison"
difficulty: Easy
difficulty_score: 28
topics:
  - Trees
  - Traversal
  - Comparison
tags:
  - trees
  - traversal
  - comparison
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-001: Campus Directory Multi-Tree Comparison

## Problem Statement

You are given two binary trees `T1` and `T2`. For each tree, output its preorder, inorder, and postorder traversals.

Then determine whether the two trees are structurally identical (ignoring node values). Also report which traversal types match exactly between the two trees.

![Problem Illustration](../images/TRE-001/problem-illustration.png)

## Input Format

- First line: integer `n1` (number of nodes in `T1`)
- Next `n1` lines: `value left right` for nodes `0..n1-1`
- Next line: integer `n2` (number of nodes in `T2`)
- Next `n2` lines: `value left right` for nodes `0..n2-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` in each tree. If `n=0`, the tree is empty.

## Output Format

- Line 1: preorder of `T1`
- Line 2: inorder of `T1`
- Line 3: postorder of `T1`
- Line 4: preorder of `T2`
- Line 5: inorder of `T2`
- Line 6: postorder of `T2`
- Line 7: `true` or `false` for structural identity
- Line 8: traversal names that match exactly (`preorder`, `inorder`, `postorder`) separated by spaces, or `NONE`

## Constraints

- `0 <= n1, n2 <= 100000`
- Node values fit in 32-bit signed integers
- Input trees are valid (no cycles)

## Example

**Input:**

```
3
2 1 2
1 -1 -1
3 -1 -1
3
1 -1 1
2 -1 2
3 -1 -1
```

**Output:**

```
2 1 3
1 2 3
1 3 2
1 2 3
1 2 3
3 2 1
false
inorder
```

**Explanation:**

Both trees have inorder traversal `1 2 3`, but their structures differ, so `structural_identity=false`.

![Example Visualization](../images/TRE-001/example-1.png)

## Notes

- Structural identity ignores values and checks only left/right child positions.
- Output a blank line for an empty traversal (tree with `n=0`).
- Traversal matching compares sequences of values for the same traversal type.

## Related Topics

Tree Traversals, Tree Comparison, Binary Trees

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> getPreorder(int n, int[] values, int[] left, int[] right) {
        // Implement here
        return new ArrayList<>();
    }

    public List<Integer> getInorder(int n, int[] values, int[] left, int[] right) {
        // Implement here
        return new ArrayList<>();
    }

    public List<Integer> getPostorder(int n, int[] values, int[] left, int[] right) {
        // Implement here
        return new ArrayList<>();
    }

    public boolean isStructurallyIdentical(int n1, int[] left1, int[] right1, int n2, int[] left2, int[] right2) {
        // Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Tree 1
        if (!sc.hasNextInt()) return;
        int n1 = sc.nextInt();
        int[] val1 = new int[n1];
        int[] left1 = new int[n1];
        int[] right1 = new int[n1];
        for (int i = 0; i < n1; i++) {
            val1[i] = sc.nextInt();
            left1[i] = sc.nextInt();
            right1[i] = sc.nextInt();
        }

        // Tree 2
        if (!sc.hasNextInt()) return;
        int n2 = sc.nextInt();
        int[] val2 = new int[n2];
        int[] left2 = new int[n2];
        int[] right2 = new int[n2];
        for (int i = 0; i < n2; i++) {
            val2[i] = sc.nextInt();
            left2[i] = sc.nextInt();
            right2[i] = sc.nextInt();
        }

        Solution sol = new Solution();

        // Output T1 Traversals
        printList(sol.getPreorder(n1, val1, left1, right1));
        printList(sol.getInorder(n1, val1, left1, right1));
        printList(sol.getPostorder(n1, val1, left1, right1));

        // Output T2 Traversals
        printList(sol.getPreorder(n2, val2, left2, right2));
        printList(sol.getInorder(n2, val2, left2, right2));
        printList(sol.getPostorder(n2, val2, left2, right2));

        // Identity
        System.out.println(sol.isStructurallyIdentical(n1, left1, right1, n2, left2, right2));

        
        System.out.println("NONE"); // Implement this part in your code
    }

    private static void printList(List<Integer> list) {
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i) + (i == list.size() - 1 ? "" : " "));
        }
        System.out.println();
    }
}
```

### Python

```python
import sys
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def get_preorder(self, n: int, values: List[int], left: List[int], right: List[int]) -> List[int]:
        # Implement here
        return []

    def get_inorder(self, n: int, values: List[int], left: List[int], right: List[int]) -> List[int]:
        # Implement here
        return []

    def get_postorder(self, n: int, values: List[int], left: List[int], right: List[int]) -> List[int]:
        # Implement here
        return []

    def is_structurally_identical(self, n1: int, left1: List[int], right1: List[int],
                                  n2: int, left2: List[int], right2: List[int]) -> bool:
        # Implement here
        return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    def parse_tree():
        try:
            n = int(next(iterator))
            vals, lefts, rights = [], [], []
            for _ in range(n):
                vals.append(int(next(iterator)))
                lefts.append(int(next(iterator)))
                rights.append(int(next(iterator)))
            return n, vals, lefts, rights
        except StopIteration:
            return 0, [], [], []

    n1, val1, left1, right1 = parse_tree()
    n2, val2, left2, right2 = parse_tree()

    sol = Solution()

    # traversals...
    print(*(sol.get_preorder(n1, val1, left1, right1)))
    print(*(sol.get_inorder(n1, val1, left1, right1)))
    print(*(sol.get_postorder(n1, val1, left1, right1)))
    print(*(sol.get_preorder(n2, val2, left2, right2)))
    print(*(sol.get_inorder(n2, val2, left2, right2)))
    print(*(sol.get_postorder(n2, val2, left2, right2)))

    # identity
    print(str(sol.is_structurally_identical(n1, left1, right1, n2, left2, right2)).lower())

    # matches
    print("NONE")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> getPreorder(int n, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        // Implement here
        return {};
    }

    vector<int> getInorder(int n, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        // Implement here
        return {};
    }

    vector<int> getPostorder(int n, const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        // Implement here
        return {};
    }

    bool isStructurallyIdentical(int n1, const vector<int>& left1, const vector<int>& right1,
                                 int n2, const vector<int>& left2, const vector<int>& right2) {
        // Implement here
        return false;
    }
};

void printVec(const vector<int>& v) {
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << (i == v.size() - 1 ? "" : " ");
    }
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n1;
    if (!(cin >> n1)) return 0;
    vector<int> val1(n1), left1(n1), right1(n1);
    for (int i = 0; i < n1; i++) cin >> val1[i] >> left1[i] >> right1[i];

    int n2;
    if (!(cin >> n2)) return 0;
    vector<int> val2(n2), left2(n2), right2(n2);
    for (int i = 0; i < n2; i++) cin >> val2[i] >> left2[i] >> right2[i];

    Solution sol;
    printVec(sol.getPreorder(n1, val1, left1, right1));
    printVec(sol.getInorder(n1, val1, left1, right1));
    printVec(sol.getPostorder(n1, val1, left1, right1));
    printVec(sol.getPreorder(n2, val2, left2, right2));
    printVec(sol.getInorder(n2, val2, left2, right2));
    printVec(sol.getPostorder(n2, val2, left2, right2));

    cout << (sol.isStructurallyIdentical(n1, left1, right1, n2, left2, right2) ? "true" : "false") << endl;
    cout << "NONE" << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  getPreorder(n, values, left, right) {
    // Implement here
    return [];
  }

  getInorder(n, values, left, right) {
    // Implement here
    return [];
  }

  getPostorder(n, values, left, right) {
    // Implement here
    return [];
  }

  isStructurallyIdentical(n1, left1, right1, n2, left2, right2) {
    // Implement here
    return false;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  let idx = 0;
  const parseTree = () => {
    const n = parseInt(tokens[idx++]);
    const vals = [],
      lefts = [],
      rights = [];
    for (let i = 0; i < n; i++) {
      vals.push(parseInt(tokens[idx++]));
      lefts.push(parseInt(tokens[idx++]));
      rights.push(parseInt(tokens[idx++]));
    }
    return { n, vals, lefts, rights };
  };

  const t1 = parseTree();
  const t2 = parseTree();

  const sol = new Solution();
  const printArr = (arr) => console.log(arr.join(" "));

  printArr(sol.getPreorder(t1.n, t1.vals, t1.lefts, t1.rights));
  printArr(sol.getInorder(t1.n, t1.vals, t1.lefts, t1.rights));
  printArr(sol.getPostorder(t1.n, t1.vals, t1.lefts, t1.rights));
  printArr(sol.getPreorder(t2.n, t2.vals, t2.lefts, t2.rights));
  printArr(sol.getInorder(t2.n, t2.vals, t2.lefts, t2.rights));
  printArr(sol.getPostorder(t2.n, t2.vals, t2.lefts, t2.rights));

  console.log(
    sol.isStructurallyIdentical(
      t1.n,
      t1.lefts,
      t1.rights,
      t2.n,
      t2.lefts,
      t2.rights
    )
  );
  console.log("NONE");
});
```
