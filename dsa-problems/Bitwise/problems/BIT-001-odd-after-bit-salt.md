---
problem_id: BIT_XOR_ODD_OCCURRENCE__8401
display_id: BIT-001
slug: odd-after-bit-salt
title: "Odd After Bit Salt"
difficulty: Easy
difficulty_score: 30
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Mathematics
tags:
  - bitwise
  - xor
  - array
  - mathematics
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Odd After Bit Salt

## Problem Statement

Each array element `x` is first transformed to `x' = x XOR salt`, where `salt` is a given integer. In the transformed multiset, exactly one value appears an odd number of times, while all other values appear an even number of times.

Your task is to find that odd-occurring transformed value **without explicitly building the transformed array**.

![Problem Illustration](../images/BIT-001/problem-illustration.png)

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 2 × 10^5) - size of array
- Second line: `n` space-separated integers representing the array elements (-10^9 ≤ arr[i] ≤ 10^9)
- Third line: Integer `salt` (-10^9 ≤ salt ≤ 10^9) - XOR transformation value

## Output Format

Print a single integer - the transformed value that appears an odd number of times.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- -10^9 ≤ arr[i] ≤ 10^9
- -10^9 ≤ salt ≤ 10^9

## Examples

### Example 1

**Input:**

```
7
4 1 2 1 2 4 7
3
```

**Output:**

```
4
```

**Explanation:**

- Original array: [4, 1, 2, 1, 2, 4, 7]
- After XOR with salt=3:
  - 4 ⊕ 3 = 7
  - 1 ⊕ 3 = 2
  - 2 ⊕ 3 = 1
  - 1 ⊕ 3 = 2
  - 2 ⊕ 3 = 1
  - 4 ⊕ 3 = 7
  - 7 ⊕ 3 = 4
- Transformed array: [7, 2, 1, 2, 1, 7, 4]
- Frequency count:
  - 7 appears 2 times (even)
  - 2 appears 2 times (even)
  - 1 appears 2 times (even)
  - 4 appears 1 time (odd) ✓

![Example 1 Visualization](../images/BIT-001/example-1.png)

### Example 2

**Input:**

```
5
5 5 3 3 8
0
```

**Output:**

```
8
```

**Explanation:**

- Original array: [5, 5, 3, 3, 8]
- Since salt = 0, XOR with 0 doesn't change values
- Transformed array: [5, 5, 3, 3, 8] (same as original)
- Frequency count:
  - 5 appears 2 times (even)
  - 3 appears 2 times (even)
  - 8 appears 1 time (odd) ✓

## Notes

- XOR (⊕) operation properties:
  - a ⊕ a = 0 (any number XORed with itself is 0)
  - a ⊕ 0 = a (any number XORed with 0 is itself)
  - XOR is commutative and associative
- Think about how to leverage XOR properties without creating the transformed array
- Consider the mathematical relationship between original and transformed arrays

## Related Topics

Bitwise Operations, XOR, Array, Mathematics, Bit Manipulation

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int oddAfterBitSalt(int[] arr, int salt) {
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
        int salt = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.oddAfterBitSalt(arr, salt);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def odd_after_bit_salt(arr: List[int], salt: int) -> int:
    # Your implementation here
    pass

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    salt = int(input())
    result = odd_after_bit_salt(arr, salt)
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
    int oddAfterBitSalt(vector<int>& arr, int salt) {
        // Your implementation here
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i] = cin >> arr[i];
    }
    int salt;
    cin >> salt;

    Solution solution;
    int result = solution.oddAfterBitSalt(arr, salt);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  oddAfterBitSalt(arr, salt) {
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
  if (lines.length === 3) {
    const n = parseInt(lines[0]);
    const arr = lines[1].split(" ").map(Number);
    const salt = parseInt(lines[2]);

    const solution = new Solution();
    const result = solution.oddAfterBitSalt(arr, salt);

    console.log(result);
    rl.close();
  }
});
```
