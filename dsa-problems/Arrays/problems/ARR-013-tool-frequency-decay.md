---
problem_id: ARR_FREQ_DECAY__E31B
display_id: ARR-013
slug: tool-frequency-decay
title: "Tool Frequency Top K with Recency Decay"
difficulty: Medium
difficulty_score: 50
topics:
  - Array
  - Hash Map
  - Sorting
  - Mathematics
  - Exponential Decay
tags:
  - arrays
  - hashmap
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Tool Frequency Top K with Recency Decay

## Problem Statement

You are given an array of events where each event is a pair `(value, timestamp)`. Timestamps are non-decreasing. The decayed score of a value `v` at current time `now` with decay factor `D` is:

```
score(v) = Σ exp(-(now - t_i) / D)   for every occurrence t_i of value v
```

Return the `k` values with the highest decayed scores. If two values have the same score, the smaller value appears earlier in the result.

![Problem Illustration](../images/ARR-013/problem-illustration.png)


## Input Format

- First line: Integer `n` — number of events (1 ≤ n ≤ 2 × 10^5)
- Next `n` lines: Two integers `value` and `timestamp` for each event
- Next line: Integer `now`
- Next line: Integer `D`
- Next line: Integer `k`

## Output Format

Print `k` space-separated integers representing the values with the largest decayed scores in order of rank.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- 0 ≤ value ≤ 10^9
- Timestamps are non-decreasing, 0 ≤ timestamp ≤ 10^9
- 1 ≤ D ≤ 10^6
- 1 ≤ k ≤ n

## Examples

### Example 1

**Input:**

```
5
3 0
1 0
3 5
2 6
1 9
10
5
2
```

**Output:**

```
1 3
```

**Explanation:**

- Score(3) = e^(-10/5) + e^(-5/5) ≈ 0.503
- Score(1) = e^(-10/5) + e^(-1/5) ≈ 0.954
- Score(2) = e^(-4/5) ≈ 0.449
- Top 2 scores belong to values 1 and 3. Output in score order with tie broken by smaller value.

![Example 1 Visualization](../images/ARR-013/example-1.png)

### Example 2

**Input:**

```
3
5 0
5 1
3 2
5
2
1
```

**Output:**

```
3
```

**Explanation:**

- Score(5) = e^(-5/2) + e^(-4/2) ≈ 0.217
- Score(3) = e^(-3/2) ≈ 0.223
- Highest score is for value 3, so it is the only element in the result.

## Notes

- Maintain a hash map of scores per value and track the top `k` using a min-heap (`O(n log k)`).

## Related Topics

Array, Hash Map, Sorting, Mathematics, Exponential Decay

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] topKWithDecay(int[][] values, int now, int D, int k) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] values = new int[n][2];
        for (int i = 0; i < n; i++) {
            values[i][0] = sc.nextInt();
            values[i][1] = sc.nextInt();
        }
        int now = sc.nextInt();
        int D = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.topKWithDecay(values, now, D, k);

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

def top_k_with_decay(values: List[List[int]], now: int, D: int, k: int) -> List[int]:
    # Your implementation here
    pass

def main():
    n = int(input())
    values = []
    for _ in range(n):
        val, timestamp = map(int, input().split())
        values.append([val, timestamp])
    now = int(input())
    D = int(input())
    k = int(input())
    result = top_k_with_decay(values, now, D, k)
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
    vector<int> topKWithDecay(vector<vector<int>>& values, int now, int D, int k) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<vector<int>> values(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> values[i][0] >> values[i][1];
    }
    int now, D, k;
    cin >> now >> D >> k;

    Solution solution;
    vector<int> result = solution.topKWithDecay(values, now, D, k);

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
const readline = require('readline');

class Solution {
    topKWithDecay(values, now, D, k) {
        // Your implementation here
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];
let n = 0;
let lineCount = 0;

rl.on('line', (line) => {
    lines.push(line);
    if (lineCount === 0) {
        n = parseInt(lines[0]);
    }
    lineCount++;
    if (lineCount === n + 4) {
        const values = [];
        for (let i = 1; i <= n; i++) {
            const parts = lines[i].split(' ').map(Number);
            values.push(parts);
        }
        const now = parseInt(lines[n + 1]);
        const D = parseInt(lines[n + 2]);
        const k = parseInt(lines[n + 3]);

        const solution = new Solution();
        const result = solution.topKWithDecay(values, now, D, k);

        console.log(result.join(' '));
        rl.close();
    }
});
```
