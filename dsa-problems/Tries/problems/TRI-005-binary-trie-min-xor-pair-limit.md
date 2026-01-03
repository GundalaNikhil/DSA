---
problem_id: TRI_BIN_MIN_XOR__4256
display_id: TRI-005
slug: binary-trie-min-xor-pair-limit
title: "Binary Trie Min XOR Pair Under Limit"
difficulty: Medium
difficulty_score: 55
topics:
  - Trie
  - Binary Trie
  - Bit Manipulation
  - XOR
tags:
  - trie
  - binary-trie
  - bit-manipulation
  - xor
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Binary Trie Min XOR Pair Under Limit

## Problem Statement

Given an array of integers and a limit `L`, find the minimum XOR value of any pair of elements whose XOR is less than or equal to `L`. If no such pair exists, return -1.

![Problem Illustration](../images/TRI-005/problem-illustration.png)

## Input Format

- First line: Two integers `n` and `L` separated by space
- Second line: `n` space-separated integers representing the array

## Output Format

Print a single integer: the minimum XOR value ≤ L, or -1 if none exists.

## Constraints

- 1 ≤ n ≤ 2 × 10^5
- 0 ≤ a[i] ≤ 10^9
- 0 ≤ L ≤ 10^9

## Examples

### Example 1

**Input:**

```
4 8
3 10 5 25
```

**Output:**

```
6
```

**Explanation:**

Possible XOR pairs:

- 3 XOR 10 = 9 (> 8, excluded)
- 3 XOR 5 = 6 (≤ 8) ✓
- 3 XOR 25 = 26 (> 8, excluded)
- 10 XOR 5 = 15 (> 8, excluded)
- 10 XOR 25 = 19 (> 8, excluded)
- 5 XOR 25 = 28 (> 8, excluded)

Minimum valid XOR: 6

![Example 1 Visualization](../images/TRI-005/example-1.png)

## Notes

- Use binary trie for efficient XOR queries
- Store integers in binary representation
- For 32-bit integers, trie depth is 30-32 levels
- XOR(a, b) = a ^ b in most programming languages

## Related Topics

Trie, Binary Trie, Bit Manipulation, XOR Properties

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minXORPairUnderLimit(int[] arr, int L) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int L = sc.nextInt();
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        int result = solution.minXORPairUnderLimit(arr, L);
        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def min_xor_naive(arr, L):
    # //Implement here
    return 0
def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')

    n, L = map(int, input_data[0].split())
    arr = list(map(int, input_data[1].split()))
    result = min_xor_naive(arr, L)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int minXORPairUnderLimit(const vector<int>& arr, int L) {
        //Implement here
        return 0;
    }
};

int main() {
    int n, L;
    if (!(cin >> n >> L)) {
        return 0;
    }
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    int result = solution.minXORPairUnderLimit(arr, L);

    cout << result << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

function minXORPairUnderLimit(arr, L) {
  //Implement here
  return 0;
}

const lines = [];
rl.on('line', (line) => lines.push(line.trim()));
rl.on('close', () => {
    const [n, L] = lines[0].split(' ').map(Number);
    const arr = lines[1].split(' ').map(Number);
    
    const result = minXORPairUnderLimit(arr, L);
    console.log(result);
});
```
