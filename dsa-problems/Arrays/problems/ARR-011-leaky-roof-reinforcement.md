---
problem_id: ARR_DP_COST__1FA6
display_id: ARR-011
slug: leaky-roof-reinforcement
title: "Leaky Roof Reinforcement"
difficulty: Hard
difficulty_score: 70
topics:
  - Array
  - Dynamic Programming
  - Optimization
  - Peak Finding
tags:
  - arrays
  - dynamic-programming
  - hard
premium: true
subscription_tier: pro
time_limit: 2000
memory_limit: 256
---

# Leaky Roof Reinforcement

## Problem Statement

Given roof heights, you can add planks on top of any positions (increase height) so that water will not spill off either end when raining (heights become non-decreasing from left to peak and non-increasing to right). Find the minimum total plank height to add to achieve a single-peak non-leaking profile; peak can be any index.

![Problem Illustration](../images/ARR-011/problem-illustration.png)


## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5) - size of array
- Second line: `n` space-separated integers representing heights

## Output Format

Print the minimum total plank height needed to create a valid peak profile.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- 0 ≤ height[i] ≤ 10^9
- Can only add planks (increase height), not remove

## Examples

### Example 1

**Input:**

```
5
4 1 3 1 5
```

**Output:**

```
7
```

**Explanation:**

- Choose peak at index 4 (height 5)
- Left must be non-decreasing to peak: [4,4,4,4,5] adds 0+3+1+3=7
- Right already non-increasing from peak
- Total planks = 7

![Example 1 Visualization](../images/ARR-011/example-1.png)

### Example 2

**Input:**

```
5
1 2 3 2 1
```

**Output:**

```
0
```

**Explanation:**

- Already forms a peak at index 2, no planks needed
- Heights are non-decreasing to peak (1,2,3) and non-increasing after (3,2,1)

## Notes

- Precompute non-decreasing prefix maxima and suffix maxima
- For each peak, cost = sum of additions needed - take minimum across all peaks

## Related Topics

Array, Dynamic Programming, Optimization, Peak Finding

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minAdditionsForPeak(int[] height) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] height = new int[n];
        for (int i = 0; i < n; i++) {
            height[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.minAdditionsForPeak(height);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def min_additions_for_peak(height: List[int]) -> int:
    # Your implementation here
    pass

def main():
    n = int(input())
    height = list(map(int, input().split()))
    result = min_additions_for_peak(height)
    print(result)

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
    int minAdditionsForPeak(vector<int>& height) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }

    Solution solution;
    int result = solution.minAdditionsForPeak(height);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    minAdditionsForPeak(height) {
        // Your implementation here
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];
rl.on('line', (line) => {
    lines.push(line);
    if (lines.length === 2) {
        const n = parseInt(lines[0]);
        const height = lines[1].split(' ').map(Number);

        const solution = new Solution();
        const result = solution.minAdditionsForPeak(height);

        console.log(result);
        rl.close();
    }
});
```
