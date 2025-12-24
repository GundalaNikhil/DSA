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
    public List<List<Integer>> traverseAll(int n, int[][] nodes) {
        // Your implementation here
        return new ArrayList<>();
    }

    public boolean structuralIdentical(int n1, int[][] t1, int n2, int[][] t2) {
        // Your implementation here
        return false;
    }

    public List<String> matchingTraversals(List<List<Integer>> t1, List<List<Integer>> t2) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n1 = sc.nextInt();
        int[][] t1 = new int[n1][3];
        for (int i = 0; i < n1; i++) {
            t1[i][0] = sc.nextInt();
            t1[i][1] = sc.nextInt();
            t1[i][2] = sc.nextInt();
        }
        int n2 = sc.nextInt();
        int[][] t2 = new int[n2][3];
        for (int i = 0; i < n2; i++) {
            t2[i][0] = sc.nextInt();
            t2[i][1] = sc.nextInt();
            t2[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<List<Integer>> trav1 = solution.traverseAll(n1, t1);
        List<List<Integer>> trav2 = solution.traverseAll(n2, t2);
        boolean same = solution.structuralIdentical(n1, t1, n2, t2);
        List<String> matches = solution.matchingTraversals(trav1, trav2);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            sb.append(join(trav1.get(i))).append('\n');
        }
        for (int i = 0; i < 3; i++) {
            sb.append(join(trav2.get(i))).append('\n');
        }
        sb.append(same ? "true" : "false").append('\n');
        if (matches.isEmpty()) {
            sb.append("NONE");
        } else {
            sb.append(String.join(" ", matches));
        }
        System.out.print(sb.toString());
        sc.close();
    }

    private static String join(List<Integer> list) {
        if (list.isEmpty()) return "";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < list.size(); i++) {
            sb.append(list.get(i));
            if (i + 1 < list.size()) sb.append(' ');
        }
        return sb.toString();
    }
}
```

### Python

```python
def traverse_all(n, nodes):
    # Your implementation here
    return [[], [], []]

def structural_identical(n1, t1, n2, t2):
    # Your implementation here
    return False

def matching_traversals(t1, t2):
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n1 = int(data[idx]); idx += 1
    t1 = []
    for _ in range(n1):
        v = int(data[idx]); l = int(data[idx + 1]); r = int(data[idx + 2])
        t1.append((v, l, r))
        idx += 3
    n2 = int(data[idx]); idx += 1
    t2 = []
    for _ in range(n2):
        v = int(data[idx]); l = int(data[idx + 1]); r = int(data[idx + 2])
        t2.append((v, l, r))
        idx += 3

    trav1 = traverse_all(n1, t1)
    trav2 = traverse_all(n2, t2)
    same = structural_identical(n1, t1, n2, t2)
    matches = matching_traversals(trav1, trav2)

    out = []
    for i in range(3):
        out.append(" ".join(str(x) for x in trav1[i]))
    for i in range(3):
        out.append(" ".join(str(x) for x in trav2[i]))
    out.append("true" if same else "false")
    out.append("NONE" if not matches else " ".join(matches))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<int>> traverseAll(int n, const vector<array<int, 3>>& nodes) {
        // Your implementation here
        return vector<vector<int>>(3);
    }

    bool structuralIdentical(int n1, const vector<array<int, 3>>& t1,
                             int n2, const vector<array<int, 3>>& t2) {
        // Your implementation here
        return false;
    }

    vector<string> matchingTraversals(const vector<vector<int>>& t1,
                                      const vector<vector<int>>& t2) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n1;
    if (!(cin >> n1)) return 0;
    vector<array<int, 3>> t1(n1);
    for (int i = 0; i < n1; i++) {
        cin >> t1[i][0] >> t1[i][1] >> t1[i][2];
    }
    int n2;
    cin >> n2;
    vector<array<int, 3>> t2(n2);
    for (int i = 0; i < n2; i++) {
        cin >> t2[i][0] >> t2[i][1] >> t2[i][2];
    }

    Solution solution;
    vector<vector<int>> trav1 = solution.traverseAll(n1, t1);
    vector<vector<int>> trav2 = solution.traverseAll(n2, t2);
    bool same = solution.structuralIdentical(n1, t1, n2, t2);
    vector<string> matches = solution.matchingTraversals(trav1, trav2);

    auto printList = [](const vector<int>& v) {
        for (int i = 0; i < (int)v.size(); i++) {
            if (i) cout << ' ';
            cout << v[i];
        }
        cout << "\n";
    };

    for (int i = 0; i < 3; i++) printList(trav1[i]);
    for (int i = 0; i < 3; i++) printList(trav2[i]);
    cout << (same ? "true" : "false") << "\n";
    if (matches.empty()) {
        cout << "NONE";
    } else {
        for (int i = 0; i < (int)matches.size(); i++) {
            if (i) cout << ' ';
            cout << matches[i];
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  traverseAll(n, nodes) {
    // Your implementation here
    return [[], [], []];
  }

  structuralIdentical(n1, t1, n2, t2) {
    // Your implementation here
    return false;
  }

  matchingTraversals(t1, t2) {
    // Your implementation here
    return [];
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
  const n1 = parseInt(data[idx++], 10);
  const t1 = [];
  for (let i = 0; i < n1; i++) {
    const v = parseInt(data[idx++], 10);
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    t1.push([v, l, r]);
  }
  const n2 = parseInt(data[idx++], 10);
  const t2 = [];
  for (let i = 0; i < n2; i++) {
    const v = parseInt(data[idx++], 10);
    const l = parseInt(data[idx++], 10);
    const r = parseInt(data[idx++], 10);
    t2.push([v, l, r]);
  }

  const solution = new Solution();
  const trav1 = solution.traverseAll(n1, t1);
  const trav2 = solution.traverseAll(n2, t2);
  const same = solution.structuralIdentical(n1, t1, n2, t2);
  const matches = solution.matchingTraversals(trav1, trav2);

  const out = [];
  for (let i = 0; i < 3; i++) out.push(trav1[i].join(" "));
  for (let i = 0; i < 3; i++) out.push(trav2[i].join(" "));
  out.push(same ? "true" : "false");
  out.push(matches.length === 0 ? "NONE" : matches.join(" "));
  console.log(out.join("\n"));
});
```
