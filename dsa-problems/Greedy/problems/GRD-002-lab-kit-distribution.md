---
problem_id: GRD_LAB_KIT_DISTRIBUTION__5291
display_id: GRD-002
slug: lab-kit-distribution
title: "Lab Kit Distribution"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
tags:
  - greedy
  - heap
  - priority-queue
  - distribution
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-002: Lab Kit Distribution

## Problem Statement

A lab has `k` different types of equipment kits, with `q[i]` units available for kit type `i`. There are `m` students who each need exactly one kit (any type is acceptable).

Your task is to distribute kits to students with two objectives:

1. **Primary**: Fulfill as many student requests as possible
2. **Secondary**: Among distributions that fulfill the maximum number of students, minimize the number of kit types that are completely depleted (reach zero quantity)

Return two integers: `(fulfilled, zeroedTypes)` where:

- `fulfilled` = number of students who received kits
- `zeroedTypes` = number of kit types that ended with zero quantity

![Problem Illustration](../images/GRD-002/problem-illustration.png)

## Input Format

- First line: two integers `k m` (number of kit types and number of students)
- Second line: `k` space-separated integers representing `q[0], q[1], ..., q[k-1]` (quantities of each kit type)

## Output Format

- Two space-separated integers: `fulfilled zeroedTypes`

## Constraints

- `1 <= k, m <= 10^5`
- `0 <= q[i] <= 10^9`
- Total kits available may be less than, equal to, or greater than `m`

## Example

**Input:**

```
3 4
3 1 2
```

**Output:**

```
4 2
```

**Explanation:**

Kit quantities: [3, 1, 2]
Students to serve: 4

Greedy strategy (always distribute from the largest pile):

- Student 1: Take from kit type 0 → quantities become [2, 1, 2]
- Student 2: Take from kit type 0 or 2 (both have 2) → take from type 0 → [1, 1, 2]
- Student 3: Take from kit type 2 → [1, 1, 1]
- Student 4: Take from any type → [0, 1, 1] or [1, 0, 1] or [1, 1, 0]

To minimize zeroed types, we take from type 0 again: [0, 1, 1]

Result:

- Fulfilled: 4 students
- Zeroed types: 1 (kit type 0)

The greedy approach repeatedly takes from the largest pile:

- Start: [3, 1, 2]
- Take from largest (type 0 with 3): [2, 1, 2]
- Take from largest (type 0 or 2, both have 2): [1, 1, 2]
- Take from largest (type 2 with 2): [1, 1, 1]
- Take from largest (all tied at 1): [0, 1, 1]

This results in 1 zeroed type, successfully minimizing the number of types that reach zero.

![Example Visualization](../images/GRD-002/example-1.png)

## Notes

- Use a max-heap to always distribute from the kit type with the most units
- This greedy strategy balances the distribution and minimizes the number of types that reach zero
- After fulfilling requests, count how many kit types have exactly 0 units remaining
- If total available kits < m, fulfill as many as possible
- Time complexity: O(m log k) for m heap operations

## Related Topics

Greedy Algorithms, Heap, Priority Queue, Resource Distribution, Load Balancing

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] distributeKits(int k, int m, int[] quantities) {
        // Implementation here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        int m = sc.nextInt();
        
        int[] quantities = new int[k];
        for (int i = 0; i < k; i++) {
            quantities[i] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        int[] result = solution.distributeKits(k, m, quantities);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
```

### Python

```python
import heapq
import sys

def distribute_kits(k: int, m: int, quantities: list) -> tuple:
    # Implementation here
    return ()

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    k = int(next(iterator))
    m = int(next(iterator))
    
    quantities = []
    for _ in range(k):
        quantities.append(int(next(iterator)))
        
    fulfilled, zeroed = distribute_kits(k, m, quantities)
    print(f"{fulfilled} {zeroed}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

class Solution {
public:
    pair<int,int> distributeKits(int k, int m, vector<int>& quantities) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, m;
    if (!(cin >> k >> m)) return 0;

    vector<int> quantities(k);
    for (int i = 0; i < k; i++) {
        cin >> quantities[i];
    }

    Solution solution;
    pair<int,int> result = solution.distributeKits(k, m, quantities);
    cout << result.first << " " << result.second << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  distributeKits(k, m, quantities) {
    // Implementation here
    return null;
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
  
  let ptr = 0;
  const [k, m] = data[ptr++].split(" ").map(Number);
  const quantities = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  const [fulfilled, zeroed] = solution.distributeKits(k, m, quantities);
  console.log(`${fulfilled} ${zeroed}`);
});
```
