---
problem_id: BIT_DISTINCT_SUBARRAY_XORS__8412
display_id: BIT-012
slug: distinct-subarray-xors
title: "Distinct Subarray XORs"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - Prefix XOR
  - Set
tags:
  - bitwise
  - prefix-xor
  - medium
premium: true
subscription_tier: basic
---


# Distinct Subarray XORs

## Problem Summary

Compute the number of distinct XOR values that appear among all possible subarrays.

## Real-World Scenario: Network Packet Checksum Diversity Analysis

In network security, analyzing the diversity of checksums (computed via XOR) across data packet subsequences helps identify patterns, detect anomalies, and assess error detection coverage. Computing distinct XOR values across all contiguous packet sequences measures the robustness of the checksum space.

---

## Problem Analysis

### Understanding the Problem

Given an array of `n` integers, find how many distinct XOR values exist among all possible contiguous subarrays.

**Key Observations:**

1. There are exactly `n(n+1)/2` subarrays total
2. XOR of subarray `[L, R]` = `prefix[R] XOR prefix[L-1]`
3. Using prefix XOR simplifies computation
4. We need to track unique XOR values (use Set)

### Visual Example

```
Array: [1, 2, 3]

All Subarrays and Their XORs:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subarray    | Elements | Calculation   | XOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[0, 0]      | [1]      | 1             |  1
[1, 1]      | [2]      | 2             |  2
[2, 2]      | [3]      | 3             |  3
[0, 1]      | [1,2]    | 1 ^ 2         |  3
[1, 2]      | [2,3]    | 2 ^ 3         |  1
[0, 2]      | [1,2,3]  | 1 ^ 2 ^ 3     |  0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

XOR values: [1, 2, 3, 3, 1, 0]
Distinct XOR values: {0, 1, 2, 3}
Count = 4

Note: Problem statement shows answer as 6, which might be:
- Total subarrays (6) - but that's not distinct XORs
- Or there's a different test case
```

### Prefix XOR Technique

```
Prefix XOR Array:
═══════════════════════════════════════
Index:    -1   0   1   2
Array:         1   2   3
Prefix:    0   1   3   0

prefix[i] = a[0] ^ a[1] ^ ... ^ a[i]

Subarray XOR [L, R] = prefix[R] ^ prefix[L-1]

Example:
  XOR[1,2] = prefix[2] ^ prefix[0]
           = 0 ^ 1 = 1

prefix[-1] = 0
prefix[0] = 1
prefix[1] = 1 ^ 2 = 3
prefix[2] = 1 ^ 2 ^ 3 = 0

XOR[0,0] = prefix[0] ^ prefix[-1] = 1 ^ 0 = 1 ✓
XOR[1,1] = prefix[1] ^ prefix[0] = 3 ^ 1 = 2 ✓
XOR[2,2] = prefix[2] ^ prefix[1] = 0 ^ 3 = 3 ✓
XOR[0,1] = prefix[1] ^ prefix[-1] = 3 ^ 0 = 3 ✓
XOR[1,2] = prefix[2] ^ prefix[0] = 0 ^ 1 = 1 ✓
XOR[0,2] = prefix[2] ^ prefix[-1] = 0 ^ 0 = 0 ✓
```

---

## Approach 1: Brute Force - Compute All Subarray XORs

### Algorithm

1. Generate all subarrays [L, R]
2. Compute XOR for each subarray
3. Store in a set to track unique values
4. Return set size

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int distinctSubarrayXORs(int[] a) {
        int n = a.length;
        Set<Integer> distinctXORs = new HashSet<>();

        // Generate all subarrays
        for (int L = 0; L < n; L++) {
            int xorValue = 0;
            for (int R = L; R < n; R++) {
                xorValue ^= a[R];
                distinctXORs.add(xorValue);
            }
        }

        return distinctXORs.size();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.distinctSubarrayXORs(a));
        sc.close();
    }
}
```

**Python:**

```python
def distinct_subarray_xors(a):
    n = len(a)
    distinct_xors = set()

    # Generate all subarrays
    for L in range(n):
        xor_value = 0
        for R in range(L, n):
            xor_value ^= a[R]
            distinct_xors.add(xor_value)

    return len(distinct_xors)

# Main
n = int(input())
a = list(map(int, input().split()))
print(distinct_subarray_xors(a))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int distinctSubarrayXORs(vector<int>& a) {
    int n = a.size();
    unordered_set<int> distinctXORs;

    // Generate all subarrays
    for (int L = 0; L < n; L++) {
        int xorValue = 0;
        for (int R = L; R < n; R++) {
            xorValue ^= a[R];
            distinctXORs.insert(xorValue);
        }
    }

    return distinctXORs.size();
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << distinctSubarrayXORs(a) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function distinctSubarrayXORs(a) {
  const n = a.length;
  const distinctXORs = new Set();

  // Generate all subarrays
  for (let L = 0; L < n; L++) {
    let xorValue = 0;
    for (let R = L; R < n; R++) {
      xorValue ^= a[R];
      distinctXORs.add(xorValue);
    }
  }

  return distinctXORs.size;
}

// Main
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const n = parseInt(lines[0]);
  const a = lines[1].split(" ").map(Number);
  console.log(distinctSubarrayXORs(a));
});
```

### Detailed Trace

```
Array: [1, 2, 3]

L=0:
  R=0: xor = 1, set = {1}
  R=1: xor = 1^2 = 3, set = {1, 3}
  R=2: xor = 3^3 = 0, set = {0, 1, 3}

L=1:
  R=1: xor = 2, set = {0, 1, 2, 3}
  R=2: xor = 2^3 = 1, set = {0, 1, 2, 3} (1 already exists)

L=2:
  R=2: xor = 3, set = {0, 1, 2, 3} (3 already exists)

Final set: {0, 1, 2, 3}
Count: 4
```

### Complexity Analysis

- **Time Complexity:** O(n²)
  - Two nested loops to generate all subarrays
  - Set operations are O(1) average
- **Space Complexity:** O(min(n², MAX_XOR))
  - Storing distinct XOR values
  - At most n² distinct values, but typically much fewer

---

## Approach 2: Prefix XOR with Set (Optimal)

### Core Insight

**Prefix XOR Properties:**

- `prefix[i] = a[0] ^ a[1] ^ ... ^ a[i]`
- XOR of subarray `[L, R] = prefix[R] ^ prefix[L-1]`
- We can compute all subarray XORs by XORing pairs of prefix values

### Algorithm

```
Optimized Using Prefix XOR:
══════════════════════════════════════════
1. Compute prefix XOR array
2. For each pair (i, j) where i <= j:
   - Subarray XOR = prefix[j] ^ prefix[i-1]
3. Store in set for uniqueness
4. Return set size

Note: This is still O(n²) but uses prefix XOR elegantly
```

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int distinctSubarrayXORs(int[] a) {
        int n = a.length;
        Set<Integer> distinctXORs = new HashSet<>();

        // Compute prefix XOR
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] ^ a[i];
        }

        // Generate all subarray XORs using prefix
        for (int L = 0; L < n; L++) {
            for (int R = L; R < n; R++) {
                int xorValue = prefix[R + 1] ^ prefix[L];
                distinctXORs.add(xorValue);
            }
        }

        return distinctXORs.size();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.distinctSubarrayXORs(a));
        sc.close();
    }
}
```

**Python:**

```python
def distinct_subarray_xors_prefix(a):
    n = len(a)
    distinct_xors = set()

    # Compute prefix XOR
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] ^ a[i]

    # Generate all subarray XORs
    for L in range(n):
        for R in range(L, n):
            xor_value = prefix[R + 1] ^ prefix[L]
            distinct_xors.add(xor_value)

    return len(distinct_xors)

# Main
n = int(input())
a = list(map(int, input().split()))
print(distinct_subarray_xors_prefix(a))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int distinctSubarrayXORs(vector<int>& a) {
    int n = a.size();
    unordered_set<int> distinctXORs;

    // Compute prefix XOR
    vector<int> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] ^ a[i];
    }

    // Generate all subarray XORs
    for (int L = 0; L < n; L++) {
        for (int R = L; R < n; R++) {
            int xorValue = prefix[R + 1] ^ prefix[L];
            distinctXORs.insert(xorValue);
        }
    }

    return distinctXORs.size();
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << distinctSubarrayXORs(a) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function distinctSubarrayXORs(a) {
  const n = a.length;
  const distinctXORs = new Set();

  // Compute prefix XOR
  const prefix = new Array(n + 1).fill(0);
  for (let i = 0; i < n; i++) {
    prefix[i + 1] = prefix[i] ^ a[i];
  }

  // Generate all subarray XORs
  for (let L = 0; L < n; L++) {
    for (let R = L; R < n; R++) {
      const xorValue = prefix[R + 1] ^ prefix[L];
      distinctXORs.add(xorValue);
    }
  }

  return distinctXORs.size;
}

// Main
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const n = parseInt(lines[0]);
  const a = lines[1].split(" ").map(Number);
  console.log(distinctSubarrayXORs(a));
});
```

### Detailed Trace

```
Array: [1, 2, 3]

Prefix XOR:
━━━━━━━━━━━━━━━━━━━━━━━━
Index | -1  0  1  2
Value |  0  1  3  0
━━━━━━━━━━━━━━━━━━━━━━━━

Subarray XORs:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
L | R | prefix[R+1] | prefix[L] | XOR | Set
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0 | 0 |      1      |     0     |  1  | {1}
0 | 1 |      3      |     0     |  3  | {1,3}
0 | 2 |      0      |     0     |  0  | {0,1,3}
1 | 1 |      3      |     1     |  2  | {0,1,2,3}
1 | 2 |      0      |     1     |  1  | {0,1,2,3}
2 | 2 |      0      |     3     |  3  | {0,1,2,3}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Final count: 4
```

### Complexity Analysis

- **Time Complexity:** O(n²)
  - O(n) for prefix computation
  - O(n²) for double loop
- **Space Complexity:** O(n + U)
  - O(n) for prefix array
  - O(U) for set, where U = number of unique XORs

---

## Approach 3: Incremental XOR (Most Efficient for Implementation)

### Core Insight

**Avoid Recomputation:**

- When extending subarray from [L, R-1] to [L, R], just XOR with a[R]
- No need to store prefix array explicitly
- Same complexity but cleaner code

This is Approach 1, and it is the cleanest solution here.

### Implementation

Already covered in Approach 1.

### Complexity Analysis

- **Time Complexity:** O(n²)
- **Space Complexity:** O(U) where U = distinct XOR count

---

## Edge Cases

### Case 1: Single Element

```
Array: [5]
Subarrays: [5]
XOR values: {5}
Count: 1
```

### Case 2: All Zeros

```
Array: [0, 0, 0]
All subarray XORs = 0
Distinct: {0}
Count: 1
```

### Case 3: All Same Non-Zero

```
Array: [7, 7, 7]
Subarrays:
  [7] → 7
  [7,7] → 0
  [7,7,7] → 7
Distinct: {0, 7}
Count: 2
```

### Case 4: Powers of 2

```
Array: [1, 2, 4]
Subarrays: [1]=1, [2]=2, [4]=4, [1,2]=3, [2,4]=6, [1,2,4]=7
Distinct: {1, 2, 3, 4, 6, 7}
Count: 6
```

---

### Common Mistakes

### Mistake 1: Double Counting

```java
// Wrong: counting duplicates
int count = 0;
for (int L = 0; L < n; L++) {
    for (int R = L; R < n; R++) {
        count++;  // Counts all, not distinct!
    }
}
```

### Mistake 2: Incorrect Prefix XOR

```python
# Wrong: off-by-one error
for i in range(n):
    prefix[i] = prefix[i-1] ^ a[i]  # Wrong index for i=0!
```

### Mistake 3: Not Using Set

```cpp
// Wrong: using array instead of set
vector<int> xors;
// ... compute xors
return xors.size();  // Includes duplicates!
```

---

## Interview Extensions

### Extension 1: K-Length Subarrays Only

Count distinct XORs of subarrays with length exactly K.

**Approach:** Sliding window with Set.

### Extension 2: Maximum XOR Subarray

Find the maximum XOR value among all subarrays.

**Approach:** Use Trie for efficient maximum XOR finding.

### Extension 3: Count Subarrays with XOR = X

Count how many subarrays have XOR equal to target X.

**Approach:** Use prefix XOR with HashMap.

---

## Practice Problems

1. **Count Triplets with XOR = 0** - Extend to triplets
2. **Maximum XOR of Two Numbers** - Trie-based XOR maximum
3. **Subarray XOR to K** - Count subarrays with XOR = K
4. **XOR Queries of Subarray** - Handle Q range queries
5. **Minimum XOR Subarray** - Find minimum instead of distinct count

---

## Summary Table

| Approach    | Time  | Space    | Best For                    |
| ----------- | ----- | -------- | --------------------------- |
| Brute Force | O(n²) | O(U)     | Clean implementation        |
| Prefix XOR  | O(n²) | O(n + U) | Explicit prefix usage       |
| Incremental | O(n²) | O(U)     | Most efficient (Approach 1) |

---

## Key Takeaways

1. **Prefix XOR simplifies** subarray XOR computation
2. **Set data structure** handles uniqueness automatically
3. **O(n²) is optimal** for this problem (must check all subarrays)
4. **XOR properties** enable elegant solutions
5. **Space-time tradeoff** between storing prefix vs recomputing

This problem teaches:

- Prefix XOR technique
- Set operations for uniqueness
- Subarray enumeration
- XOR properties

Essential for competitive programming and technical interviews!
