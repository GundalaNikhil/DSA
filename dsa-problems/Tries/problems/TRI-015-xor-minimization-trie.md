---
problem_id: TRI_XOR_MINIMIZATION__9417
display_id: TRI-015
slug: xor-minimization-trie
title: "XOR Minimization With Trie"
difficulty: Medium
difficulty_score: 58
topics:
  - Trie
  - Binary Trie
  - XOR
  - Bit Manipulation
tags:
  - trie
  - xor
  - binary
  - prefix-xor
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-015: XOR Minimization With Trie

## Problem Statement

Given an array `a` of `n` non-negative integers and an integer `X`, find the minimum possible value of `(subarray_XOR) ⊕ X` over all subarrays, where `subarray_XOR` is the XOR of all elements in the subarray.

![Problem Illustration](../images/TRI-015/problem-illustration.png)

## Input Format

- First line: two integers `n` (array size) and `X` (target value)
- Second line: `n` space-separated integers representing array `a`

## Output Format

Return a single integer: the minimum value of `(subarray_XOR) ⊕ X`

## Constraints

- `1 <= n <= 2 × 10^5`
- `0 <= a[i], X <= 10^9`
- All array elements and X fit in 32-bit integers

## Example

**Input:**

```
3 3
4 1 2
```

**Output:**

```
0
```

**Explanation:**

Possible subarrays and their results:

- [4]: XOR=4, result=4⊕3=7
- [1]: XOR=1, result=1⊕3=2
- [2]: XOR=2, result=2⊕3=1
- [4,1]: XOR=4⊕1=5, result=5⊕3=6
- [1,2]: XOR=1⊕2=3, result=3⊕3=0 ← minimum!
- [4,1,2]: XOR=4⊕1⊕2=7, result=7⊕3=4

Minimum value: **0** (from subarray [1,2])

![Example Visualization](../images/TRI-015/example-1.png)

## Notes

- Use prefix XOR technique: `subarray[i,j] = prefix[j+1] ⊕ prefix[i]`
- Binary trie enables efficient XOR minimization queries
- Process prefixes sequentially, querying and inserting

## Related Topics

Binary Trie, XOR, Prefix XOR, Bit Manipulation

---

## Solution Template

### Java

```java
import java.util.*;

class TrieNode {
    TrieNode[] children = new TrieNode[2];  // 0 and 1
}

class Solution {
    public int minimizeXOR(int[] a, int X) {
        //Implement here
        return 0;
    }
    private void insert(int num) {
        //Implement here
    }
    private int query(int num) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int X = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.minimizeXOR(a, X);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    MAX_BITS = 30

    def __init__(self):
        self.root = TrieNode()

    def minimize_xor(self, a: List[int], X: int) -> int:
        # //Implement here
        return 0
    def _insert(self, num: int):
        # //Implement here
        return 0
    def _query(self, num: int) -> int:
        # //Implement here
        return 0
def main():
    import sys
    input_data = sys.stdin.read().strip().split()

    n = int(input_data[0])
    X = int(input_data[1])
    a = [int(input_data[i + 2]) for i in range(n)]

    solution = Solution()
    result = solution.minimize_xor(a, X)

    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

struct TrieNode {
    TrieNode* children[2] = {nullptr, nullptr};
};

class Solution {
public:
    void insert(int num) {
        //Implement here
    }
    int query(int num) {
        //Implement here
        return 0;
    }
    int minimizeXOR(vector<int>& a, int X) {
        //Implement here
        return 0;
    }
};

int main() {
    int n, X;
    cin >> n >> X;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution solution;
    int result = solution.minimizeXOR(a, X);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = [null, null];
  }
}

class Solution {
  insert(num) {
    //Implement here
    return 0;
  }
  query(num) {
    //Implement here
    return 0;
  }
  minimizeXOR(a, X) {
    //Implement here
    return 0;
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
  const [n, X] = lines[0].split(" ").map(Number);
  const a = lines[1].split(" ").map(Number);

  const solution = new Solution();
  const result = solution.minimizeXOR(a, X);

  console.log(result);
});
```
