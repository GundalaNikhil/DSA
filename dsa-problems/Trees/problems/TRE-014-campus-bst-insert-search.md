---
problem_id: TRE_CAMPUS_BST_INSERT_SEARCH__2824
display_id: TRE-014
slug: campus-bst-insert-search
title: "Campus BST Insert & Search"
difficulty: Easy
difficulty_score: 30
topics:
  - Trees
  - BST
  - Traversal
tags:
  - trees
  - bst
  - insertion
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRE-014: Campus BST Insert & Search

## Problem Statement

Build a binary search tree (BST) by inserting values in the given order. Then search for a target value.

Output the inorder traversal of the final BST and the result of the search.

![Problem Illustration](../images/TRE-014/problem-illustration.png)

## Input Format

- First line: integer `n`, number of values to insert
- Second line: `n` integers, the insertion order
- Third line: integer `x`, the value to search

Duplicates, if any, must be inserted into the right subtree.

## Output Format

- Line 1: inorder traversal of the BST (space-separated)
- Line 2: `true` if `x` exists in the BST, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- Values fit in 32-bit signed integers

## Example

**Input:**

```
5
4 2 6 1 3
5
```

**Output:**

```
1 2 3 4 6
false
```

**Explanation:**

After insertion, the BST inorder traversal is sorted. The value `5` is not present.

![Example Visualization](../images/TRE-014/example-1.png)

## Notes

- If `n=0`, the inorder traversal is empty and search is `false`.
- Inorder traversal of a BST is non-decreasing.
- Insertion uses standard BST rules with duplicates to the right.

## Related Topics

Binary Search Trees, Insertion, Traversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> buildInorder(int[] values) {
        // Implement here
        return new ArrayList<>();
    }

    public boolean searchValue(int[] values, int x) {
        // Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
        }
        int x = sc.hasNextInt() ? sc.nextInt() : 0;

        Solution solution = new Solution();
        List<Integer> inorder = solution.buildInorder(values);
        for (int i = 0; i < inorder.size(); i++) {
            System.out.print(inorder.get(i) + (i == inorder.size() - 1 ? "" : " "));
        }
        System.out.println();
        System.out.println(solution.searchValue(values, x));
        sc.close();
    }
}
```

### Python

```python
import sys
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def build_inorder(self, values: List[int]) -> List[int]:
        # Implement here
        return []

    def search_value(self, values: List[int], x: int) -> bool:
        # Implement here
        return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = []
        for _ in range(n):
            values.append(int(next(iterator)))

        x = 0
        try:
            x = int(next(iterator))
        except StopIteration:
            pass

        solution = Solution()
        inorder = solution.build_inorder(values)
        print(*(inorder))
        print(str(solution.search_value(values, x)).lower())
    except StopIteration:
        pass

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
public:
    vector<int> buildInorder(const vector<int>& values) {
        // Implement here
        return {};
    }

    bool searchValue(const vector<int>& values, int x) {
        // Implement here
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }
    int x;
    cin >> x;

    Solution solution;
    vector<int> inorder = solution.buildInorder(values);
    for (int i = 0; i < inorder.size(); i++) {
        cout << inorder[i] << (i == inorder.size() - 1 ? "" : " ");
    }
    cout << "\n";
    cout << (solution.searchValue(values, x) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  buildInorder(values) {
    // Implement here
    return [];
  }

  searchValue(values, x) {
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
  const n = parseInt(tokens[idx++]);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(tokens[idx++]));
  }
  let x = 0;
  if (idx < tokens.length) x = parseInt(tokens[idx++]);

  const solution = new Solution();
  console.log(solution.buildInorder(values).join(" "));
  console.log(solution.searchValue(values, x));
});
```
