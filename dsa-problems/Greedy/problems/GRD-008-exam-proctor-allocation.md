---
problem_id: GRD_EXAM_PROCTOR_ALLOCATION__3517
display_id: GRD-008
slug: exam-proctor-allocation
title: "Exam Proctor Allocation"
difficulty: Easy-Medium
difficulty_score: 40
topics:
  - Greedy Algorithms
  - Sweep Line
  - Intervals
tags:
  - greedy
  - sweep-line
  - intervals
  - scheduling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-008: Exam Proctor Allocation

## Problem Statement

You have `n` exam sessions, where each session `i` occurs during time interval `[start[i], end[i]]`. Each proctor can supervise up to `r` simultaneously occurring exams.

Your task is to find the minimum number of proctors needed to cover all exam sessions.

![Problem Illustration](../images/GRD-008/problem-illustration.png)

## Input Format

- First line: two integers `n r` (number of exams and max exams per proctor)
- Next `n` lines: two integers `start end` representing each exam's time interval

## Output Format

- Single integer: minimum number of proctors needed

## Constraints

- `1 <= n <= 10^5`
- `1 <= r <= 10^9`
- `0 <= start < end <= 10^9`

## Example

**Input:**
```
3 2
0 10
5 7
6 9
```

**Output:**
```
2
```

**Explanation:**

Exams:
- Exam 1: [0, 10]
- Exam 2: [5, 7]  
- Exam 3: [6, 9]

Each proctor can handle up to r = 2 exams simultaneously.

Timeline analysis:
- At time 5: Exams 1 and 2 are active (2 exams)
- At time 6: Exams 1, 2, and 3 are active (3 exams)
- Maximum overlap: 3 exams

Proctors needed: ceil(3 / 2) = ceil(1.5) = 2

![Example Visualization](../images/GRD-008/example-1.png)

## Notes

- Use sweep line algorithm to track overlapping intervals
- Track maximum number of simultaneously active exams
- Answer = ceil(max_overlap / r)
- Create events for exam start (+1) and exam end (-1)
- Sort events by time and process in order
- Time complexity: O(n log n) for sorting

## Related Topics

Greedy Algorithms, Sweep Line, Interval Scheduling, Resource Allocation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minProctors(int n, int r, int[][] exams) {
        // exams[i] = [start, end]
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int r = sc.nextInt();
        
        int[][] exams = new int[n][2];
        for (int i = 0; i < n; i++) {
            exams[i][0] = sc.nextInt();
            exams[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.minProctors(n, r, exams));
        sc.close();
    }
}
```

### Python

```python
from typing import List
import math

def min_proctors(n: int, r: int, exams: List[List[int]]) -> int:
    # Your implementation here
    return 0

def main():
    n, r = map(int, input().split())
    exams = []
    for _ in range(n):
        start, end = map(int, input().split())
        exams.append([start, end])
    
    result = min_proctors(n, r, exams)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

class Solution {
public:
    int minProctors(int n, int r, vector<pair<int,int>>& exams) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, r;
    cin >> n >> r;
    
    vector<pair<int,int>> exams(n);
    for (int i = 0; i < n; i++) {
        cin >> exams[i].first >> exams[i].second;
    }
    
    Solution solution;
    cout << solution.minProctors(n, r, exams) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minProctors(n, r, exams) {
    // Your implementation here
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
  let ptr = 0;
  const [n, r] = data[ptr++].split(" ").map(Number);
  
  const exams = [];
  for (let i = 0; i < n; i++) {
    const [start, end] = data[ptr++].split(" ").map(Number);
    exams.push([start, end]);
  }
  
  const solution = new Solution();
  console.log(solution.minProctors(n, r, exams));
});
```