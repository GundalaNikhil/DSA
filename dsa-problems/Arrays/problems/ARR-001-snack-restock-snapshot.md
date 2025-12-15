---
problem_id: ARR_PREFIX_AVG__4252
display_id: ARR-001
slug: snack-restock-snapshot
title: "Snack Restock Snapshot"
difficulty: Easy
difficulty_score: 25
topics:
  - Array
  - Prefix Sum
  - Mathematics
  - Running Sum
tags:
  - arrays
  - prefix-sum
  - mathematics
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Snack Restock Snapshot

## Problem Statement

Given daily deliveries `arr[i]`, output prefix averages rounded down for each day.

![Problem Illustration](../images/ARR-001/problem-illustration.png)

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 10^5) - size of array
- Second line: `n` space-separated integers representing `arr[i]` (0 ≤ arr[i] ≤ 10^9)

## Output Format

Print `n` space-separated integers representing the prefix average at each position (using floor division).

## Constraints

- 1 ≤ n ≤ 10^5
- 0 ≤ arr[i] ≤ 10^9

## Examples

### Example 1

**Input:**

```
4
4 6 6 0
```

**Output:**

```
4 5 5 4
```

**Explanation:**

- Position 0: (4) / 1 = 4
- Position 1: (4 + 6) / 2 = 5
- Position 2: (4 + 6 + 6) / 3 = 5
- Position 3: (4 + 6 + 6 + 0) / 4 = 4

![Example 1 Visualization](../images/ARR-001/example-1.png)

### Example 2

**Input:**

```
3
10 20 30
```

**Output:**

```
10 15 20
```

**Explanation:**

- Position 0: 10 / 1 = 10
- Position 1: (10 + 20) / 2 = 15
- Position 2: (10 + 20 + 30) / 3 = 20

## Notes

- Use floor division (integer division) for averages
- Prefix average at position i = sum of elements [0...i] divided by (i+1)

## Related Topics

Array, Prefix Sum, Mathematics, Running Sum

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] prefixAverages(int[] arr) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.prefixAverages(arr);

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
from typing import List

def prefix_averages(arr: List[int]) -> List[int]:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = prefix_averages(arr)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> prefixAverages(vector<int>& arr) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    vector<int> result = solution.prefixAverages(arr);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  prefixAverages(arr) {
    // Your implementation here
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
  if (lines.length === 2) {
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);

    const solution = new Solution();
    const result = solution.prefixAverages(arr);

    console.log(result.join(" "));
    rl.close();
  }
});
```
