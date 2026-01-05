---
problem_id: GRD_LAB_KIT_DISTRIBUTION__5291
display_id: GRD-002
slug: lab-kit-distribution
title: "Lab Kit Distribution"
difficulty: Medium
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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/dsa/greedy/GRD-002.jpg)

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
import java.io.*;

class Solution {
    public int[] distributeKits(int k, int m, long[] q) {
        // Implement here
        return new int[]{0, 0};
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String kmLine = br.readLine();
        if (kmLine == null) return;
        String[] km = kmLine.trim().split("\\s+");
        int k = Integer.parseInt(km[0]);
        int m = Integer.parseInt(km[1]);

        long[] q = new long[k];
        String[] qLine = br.readLine().trim().split("\\s+");
        for (int i = 0; i < k; i++) {
            q[i] = Long.parseLong(qLine[i]);
        }

        Solution sol = new Solution();
        int[] result = sol.distributeKits(k, m, q);
        System.out.println(result[0] + " " + result[1]);
    }
}
```

### Python

```python
import sys

class Solution:
    def distribute_kits(self, k, m, q):
        # Implement here
        return [0, 0]

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    m = int(input_data[1])
    q = list(map(int, input_data[2:2+k]))

    sol = Solution()
    result = sol.distribute_kits(k, m, q)
    print(f"{result[0]} {result[1]}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> distributeKits(int k, int m, vector<long long>& q) {
        // Implement here
        return {0, 0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int k, m;
    if (!(cin >> k >> m)) return 0;

    vector<long long> q(k);
    for (int i = 0; i < k; i++) {
        cin >> q[i];
    }

    Solution sol;
    vector<int> result = sol.distributeKits(k, m, q);
    cout << result[0] << " " << result[1] << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  distributeKits(k, m, q) {
    // Implement here
    return [0, 0];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const k = parseInt(input[idx++]);
  const m = parseInt(input[idx++]);
  const q = [];
  for (let i = 0; i < k; i++) {
    q.push(BigInt(input[idx++]));
  }

  const sol = new Solution();
  const result = sol.distributeKits(k, m, q);
  console.log(`${result[0]} ${result[1]}`);
}

solve();
```
