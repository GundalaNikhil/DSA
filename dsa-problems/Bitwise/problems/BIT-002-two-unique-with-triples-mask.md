---
problem_id: BIT_TWO_UNIQUE_TRIPLES__8402
display_id: BIT-002
slug: two-unique-with-triples-mask
title: "Two Unique With Triple Others Under Mask"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - bit-manipulation
  - array
  - medium
premium: true
subscription_tier: basic
---

# BIT-002: Two Unique With Triple Others Under Mask

## Problem Statement

Given an array where every number appears exactly three times except two distinct numbers that appear once, find the two unique numbers. Return them in sorted order.

![Problem Illustration](../images/BIT-002/problem-illustration.png)

## Input Format

- First line: Two integers `n` and `M` - size of array and mask value
- Second line: `n` space-separated integers representing the array

## Output Format

Two space-separated integers representing the two unique numbers in sorted order.

## Constraints

- 2 ≤ n ≤ 2 × 10⁵
- 0 ≤ M ≤ 10⁹
- 0 ≤ nums[i] ≤ 10⁹
- Exactly two numbers appear once; all others appear exactly three times

## Example

**Input:**

```
5 1
7 7 7 2 4
```

**Output:**

```
2 4
```

**Explanation:**

- Number 7 appears 3 times
- Numbers 2 and 4 each appear once
- Use bit counting modulo 3 to identify uniques
- Partition array using differentiating bit to extract both numbers

![Example Visualization](../images/BIT-002/example-1.png)

## Notes

- Use O(1) extra space (not counting input array)
- Algorithm should run in O(n) time
- Do not use hash maps or sorting

## Related Topics

Bitwise Operations, XOR, Array, Bit Counting, Mathematics

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] twoUniqueWithTriples(int[] nums, int M) {
        // Your implementation here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int M = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.twoUniqueWithTriples(nums, M);

        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def two_unique_with_triples(nums: List[int], M: int) -> List[int]:
    # Your implementation here
    pass

def main():
    n, M = map(int, input().split())
    nums = list(map(int, input().split()))
    result = two_unique_with_triples(nums, M)
    print(result[0], result[1])

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
    vector<int> twoUniqueWithTriples(vector<int>& nums, int M) {
        // Your implementation here
    }
};

int main() {
    int n, M;
    cin >> n >> M;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    Solution solution;
    vector<int> result = solution.twoUniqueWithTriples(nums, M);

    cout << result[0] << " " << result[1] << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  twoUniqueWithTriples(nums, M) {
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
    const [n, M] = lines[0].split(" ").map(Number);
    const nums = lines[1].split(" ").map(Number);

    const solution = new Solution();
    const result = solution.twoUniqueWithTriples(nums, M);

    console.log(result[0] + " " + result[1]);
    rl.close();
  }
});
```
