---
problem_id: REC_SUBSET_SUM_EXACT_COUNT__1854
display_id: REC-006
slug: subset-sum-exact-count
title: "Subset Sum Exact Count"
difficulty: Medium
difficulty_score: 43
topics:
  - Recursion
  - Backtracking
  - Subset Sum
tags:
  - recursion
  - subset-sum
  - backtracking
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-006: Subset Sum Exact Count

## Problem Statement

Given an array `arr`, determine whether there exists a subset of exactly `k` elements that sums to `target`. Return one such subset if it exists, otherwise output `NONE`.

![Problem Illustration](../images/REC-006/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `target`
- Second line: `n` space-separated integers `arr[i]`

## Output Format

- One line with a valid subset (space-separated), or `NONE` if no solution exists

## Constraints

- `1 <= n <= 20`
- `0 <= k <= n`
- `|arr[i]| <= 10000`
- `|target| <= 10^9`

## Example

**Input:**

```
4 2 7
4 1 6 2
```

**Output:**

```
1 6
```

**Explanation:**

The subset `{1, 6}` uses exactly two elements and sums to 7.

![Example Visualization](../images/REC-006/example-1.png)

## Notes

- Use recursion to choose or skip each element
- Track how many elements have been chosen
- Prune when remaining elements are insufficient to reach `k`
- Any valid subset is acceptable

## Related Topics

Backtracking, Subset Sum, Pruning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> findSubset(List<Integer> arr, int k, int target) {
        return null;
    }

    private boolean backtrack(int index, int count, int currentSum, List<Integer> arr, int k, int target, List<Integer> current) {
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int target = sc.nextInt();
        
        List<Integer> arr = new ArrayList<>();
        for(int i=0; i<n; i++) {
             if(sc.hasNextInt()) arr.add(sc.nextInt());
        }
        
        Solution sol = new Solution();
        List<Integer> res = sol.findSubset(arr, k, target);
        if(res.isEmpty()) {
            System.out.println("NONE");
        } else {
            for(int i=0; i<res.size(); i++) System.out.print(res.get(i) + (i==res.size()-1?"":" "));
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
def find_subset(arr: list[int], k: int, target: int) -> list[int]:
    return []
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    first_line = lines[0].split()
    n = int(first_line[0])
    k = int(first_line[1])
    target = int(first_line[2])

    arr = list(map(int, lines[1].split()))

    result = find_subset(arr, k, target)
    if result:
        print(' '.join(map(str, result)))
    else:
        print("NONE")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> findSubset(const vector<int>& arr, int k, int target) {
        return {};
    }

private:
    bool backtrack(int index, int count, int currentSum, const vector<int>& arr, int k, int target, vector<int>& current) {
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, k, target;
    if (!(cin >> n >> k >> target)) return 0;
    
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin >> arr[i];
    
    Solution sol;
    vector<int> res = sol.findSubset(arr, k, target);
    if(res.empty()) {
        cout << "NONE" << endl;
    } else {
        for(size_t i=0; i<res.size(); i++) cout << res[i] << (i==res.size()-1?"":" ");
        cout << endl;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    
    if(ptr >= tokens.length) return;
    const n = parseInt(tokens[ptr++]);
    const k = parseInt(tokens[ptr++]);
    const target = parseInt(tokens[ptr++]);
    
    const arr = [];
    for(let i=0; i<n; i++) {
        if(ptr < tokens.length) arr.push(parseInt(tokens[ptr++]));
    }
    
    const sol = new Solution();
    const res = sol.findSubset(arr, k, target);
    
    if(res.length === 0) {
        console.log("NONE");
    } else {
        console.log(res.join(' '));
    }
});

class Solution {
    findSubset(arr, k, target) {
    return 0;
  }

    backtrack(index, count, currentSum, arr, k, target, current) {
    return 0;
  }
}
```

