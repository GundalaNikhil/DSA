---
problem_id: BIT_TOGGLE_RANGES_MIN_FLIPS__8411
display_id: BIT-011
slug: toggle-ranges-min-flips
title: "Toggle Ranges Minimum Flips"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - Array
  - Greedy
  - Flipping
tags:
  - bitwise
  - array-transformation
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-011: Toggle Ranges Minimum Flips

## Problem Statement

You can flip all bits in any chosen subarray (0→1, 1→0). Find the minimum number of such flip operations needed to convert binary array `A` into array `B`.

## Input Format

- First line: Integer `n`
- Second line: `n` space-separated binary digits (array A)
- Third line: `n` space-separated binary digits (array B)

## Output Format

Single integer representing minimum flips needed

## Constraints

- `1 <= n <= 2 * 10^5`
- `A[i], B[i] ∈ {0, 1}`

## Example

**Input:**

```
4
0 1 1 0
1 0 1 0
```

**Output:**

```
1
```

**Explanation:**

A = [0,1,1,0]
B = [1,0,1,0]

**Step 1: Identify mismatches:**
- A[0]=0, B[0]=1 → mismatch
- A[1]=1, B[1]=0 → mismatch
- A[2]=1, B[2]=1 → match
- A[3]=0, B[3]=0 → match

**Step 2: Count contiguous mismatch runs:**
- Mismatch positions: [0, 1] form ONE contiguous run
- This requires exactly 1 flip operation

**Step 3: Apply flip:**
- Flip subarray [0,1]: A becomes [1,0,1,0] = B ✓

Answer: 1 flip is sufficient

## Notes

- Compare A and B element-wise
- Count runs of consecutive mismatches
- Each run needs one flip operation

## Related Topics

Array Transformation, Greedy Algorithm, Range Operations

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minFlips(int[] A, int[] B) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        int[] B = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            B[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.minFlips(A, B));
        sc.close();
    }
}
```

### Python

```python
def min_flips(A: list[int], B: list[int]) -> int:
    return 0

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(min_flips(A, B))

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
    int minFlips(vector<int>& A, vector<int>& B) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> A(n), B(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }
    Solution solution;
    cout << solution.minFlips(A, B) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minFlips(A, B) {
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
  const n = parseInt(data[0]);
  const A = data[1].split(" ").map(Number);
  const B = data[2].split(" ").map(Number);
  const solution = new Solution();
  console.log(solution.minFlips(A, B));
});
```
