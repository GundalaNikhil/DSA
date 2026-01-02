---
problem_id: BIT_PAIRWISE_XOR_BAND_PARITY__8404
display_id: BIT-004
slug: pairwise-xor-band-index-parity
title: "Pairwise XOR in Band With Index Parity"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Array
tags:
  - bitwise
  - xor
  - trie
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-004: Pairwise XOR in Band With Index Parity

## Problem Statement

Given an array and range `[L, U]`, count the number of index pairs `(i, j)` such that `i < j`, `i + j` is even, and the XOR sum `a[i] ^ a[j]` falls within `[L, U]`.

![Problem Illustration](../images/BIT-004/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integers L and U

## Output Format

Print the number of valid pairs.

## Constraints

- `1 <= n <= 100000`
- `0 <= a[i] <= 1000000000`
- `0 <= L <= U <= 1000000000`

## Example

**Input:**

```
4
2 3 1 7
1 4
```

**Output:**

```
2
```

**Explanation:**

Valid pairs are (0,2): 2 XOR 1 = 3 and (1,3): 3 XOR 7 = 4. Both have i + j even.

![Example Visualization](../images/BIT-004/example-1.png)

## Notes

- Indices are 0-based.
- Only pairs with i + j even are counted.

## Related Topics

Bitwise Operations, XOR, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class TrieNode {
        TrieNode[] children = new TrieNode[2];
        int count = 0;
    }

    private void insert(TrieNode root, int num) {
    }

    private int countLessEqual(TrieNode root, int num, int K) {
        return 0;
    }

    private long countPairsWithLimit(List<Integer> nums, int K) {
        return 0;
    }

    public long countPairwiseXorBandParity(int[] a, int L, int U) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int L = sc.nextInt();
        int U = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.countPairwiseXorBandParity(a, L, U));
        sc.close();
    }
}
```

### Python

```python
import sys

class TrieNode:
    def __init__(self):
        return 0
def insert(root, num):
    return 0
def count_less_equal(root, num, K):
    return 0
def solve_for_list(nums, L, U):
    return 0
def count_pairwise_xor_band_parity(a: list[int], L: int, U: int) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return

    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1

    L = int(data[ptr]); ptr += 1
    U = int(data[ptr]); ptr += 1

    result = count_pairwise_xor_band_parity(a, L, U)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct TrieNode {
    TrieNode* children[2];
    int count;

    TrieNode() {
        children[0] = children[1] = nullptr;
        count = 0;
    }
};

class Solution {
    void insert(TrieNode* root, int num) {
    }

    int countLessEqual(TrieNode* root, int num, int K) {
        return 0;
    }

    long long solve(const vector<int>& nums, int L, int U) {
        return 0;
    }

public:
    long long countPairwiseXorBandParity(vector<int>& a, int L, int U) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int L, U;
    cin >> L >> U;

    Solution solution;
    cout << solution.countPairwiseXorBandParity(a, L, U) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = [null, null];
    this.count = 0;
  }
}

class Solution {
  insert(root, num) {
    return 0;
  }

  countLessEqual(root, num, K) {
    return 0;
  }

  solve(nums, L, U) {
    return 0;
  }

  countPairwiseXorBandParity(a, L, U) {
    return 0;
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
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const a = [];
  for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
  const L = Number(tokens[ptr++]);
  const U = Number(tokens[ptr++]);

  const solution = new Solution();
  console.log(solution.countPairwiseXorBandParity(a, L, U).toString());
});
```

