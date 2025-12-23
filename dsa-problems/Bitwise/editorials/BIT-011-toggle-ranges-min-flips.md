---
problem_id: BIT_TOGGLE_RANGES_MIN_FLIPS__8411
display_id: BIT-011
slug: toggle-ranges-min-flips
title: "Toggle Ranges Minimum Flips"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - Greedy
  - Array
tags:
  - bitwise
  - greedy
  - medium
premium: true
subscription_tier: basic
---


# Toggle Ranges Minimum Flips

## Problem Summary

You can flip all bits in any chosen subarray (0→1, 1→0). Find the minimum number of such flip operations needed to convert binary array `A` into array `B`.

## Real-World Scenario: LED Display State Transformation

In digital signage and LED matrix displays, states are represented as binary arrays (on/off). Converting one display configuration to another using range toggle operations (flipping all LEDs in a segment) is a common task. Finding the minimum number of toggle operations optimizes power consumption and transition time.

---

## Problem Analysis

### Understanding the Problem

Given two binary arrays `A` and `B` of length `n`, find the minimum number of range flip operations needed to transform `A` into `B`. A range flip toggles all bits in a subarray (0→1, 1→0).

**Key Observations:**

1. We need to identify positions where `A[i] ≠ B[i]` (mismatches)
2. Consecutive mismatches can be fixed with a single range flip
3. Each contiguous group of mismatches requires exactly one flip operation
4. Order of flips doesn't matter (flips are independent when non-overlapping)

### Visual Example

```
Array A: [0, 1, 1, 0, 1, 0]
Array B: [1, 0, 1, 0, 0, 1]

Step 1: Identify Mismatches
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Index:     0  1  2  3  4  5
A[i]:      0  1  1  0  1  0
B[i]:      1  0  1  0  0  1
Match?     X  X  ✓  ✓  X  X
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 2: Group Consecutive Mismatches
Group 1: indices [0, 1] (2 consecutive mismatches)
Group 2: indices [4, 5] (2 consecutive mismatches)

Step 3: Count Groups
Number of mismatch runs = 2

Answer: 2 flips needed
  - Flip range [0, 1]: [1, 0, 1, 0, 1, 0]
  - Flip range [4, 5]: [1, 0, 1, 0, 0, 1] = B ✓
```

### Key Insight: Run-Length Encoding

```
Difference Array D: D[i] = A[i] XOR B[i]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Index:  0  1  2  3  4  5
D[i]:   1  1  0  0  1  1
Runs:   [   1    ][   1    ]
           ↑            ↑
        Run 1        Run 2

Count transitions 0→1 in D = Number of runs of 1s
Answer = 2
```

---

## Approach 1: Brute Force - Count Mismatch Runs

### Algorithm

1. Compare `A` and `B` element-wise
2. Mark positions where they differ
3. Count contiguous groups of mismatches
4. Each group needs one flip

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int minFlips(int[] A, int[] B) {
        int n = A.length;
        int flips = 0;
        boolean inMismatchRun = false;

        for (int i = 0; i < n; i++) {
            if (A[i] != B[i]) {
                // Found a mismatch
                if (!inMismatchRun) {
                    // Start of new mismatch run
                    flips++;
                    inMismatchRun = true;
                }
            } else {
                // Match - end any ongoing mismatch run
                inMismatchRun = false;
            }
        }

        return flips;
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

**Python:**

```python
def min_flips(A, B):
    n = len(A)
    flips = 0
    in_mismatch_run = False

    for i in range(n):
        if A[i] != B[i]:
            if not in_mismatch_run:
                # Start of new mismatch run
                flips += 1
                in_mismatch_run = True
        else:
            # Match - end mismatch run
            in_mismatch_run = False

    return flips

# Main
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(min_flips(A, B))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int minFlips(vector<int>& A, vector<int>& B) {
    int n = A.size();
    int flips = 0;
    bool inMismatchRun = false;

    for (int i = 0; i < n; i++) {
        if (A[i] != B[i]) {
            if (!inMismatchRun) {
                flips++;
                inMismatchRun = true;
            }
        } else {
            inMismatchRun = false;
        }
    }

    return flips;
}

int main() {
    int n;
    cin >> n;
    vector<int> A(n), B(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < n; i++) cin >> B[i];
    cout << minFlips(A, B) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function minFlips(A, B) {
  const n = A.length;
  let flips = 0;
  let inMismatchRun = false;

  for (let i = 0; i < n; i++) {
    if (A[i] !== B[i]) {
      if (!inMismatchRun) {
        flips++;
        inMismatchRun = true;
      }
    } else {
      inMismatchRun = false;
    }
  }

  return flips;
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
  const A = lines[1].split(" ").map(Number);
  const B = lines[2].split(" ").map(Number);
  console.log(minFlips(A, B));
});
```

### Detailed Trace

```
A = [0, 1, 1, 0, 1, 0]
B = [1, 0, 1, 0, 0, 1]

Iteration:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
i | A[i] | B[i] | Match? | inMismatchRun | flips
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0 |  0   |  1   |   No   | false → true  |   1
1 |  1   |  0   |   No   |     true      |   1
2 |  1   |  1   |   Yes  | true → false  |   1
3 |  0   |  0   |   Yes  |     false     |   1
4 |  1   |  0   |   No   | false → true  |   2
5 |  0   |  1   |   No   |     true      |   2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Final Answer: 2
```

### Complexity Analysis

- **Time Complexity:** O(n)
  - Single pass through arrays
- **Space Complexity:** O(1)
  - Only using constant extra space

---

## Approach 2: XOR and Transition Counting

### Core Insight

**Using XOR to Find Differences:**

- `D[i] = A[i] XOR B[i]` marks mismatches as 1
- Count "runs of 1s" in D
- Number of runs = number of transitions from 0→1

### Algorithm

```
Transition Counting Method:
════════════════════════════════════════════
D[i] = A[i] XOR B[i]

Count positions where D[i-1] = 0 and D[i] = 1
(Start of new mismatch run)

Special case: If D[0] = 1, count it
```

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int minFlips(int[] A, int[] B) {
        int n = A.length;
        int flips = 0;

        // Count transitions to mismatch state
        int prevDiff = 0; // Initially not in mismatch

        for (int i = 0; i < n; i++) {
            int curDiff = (A[i] == B[i]) ? 0 : 1;

            // Transition from match (0) to mismatch (1)
            if (prevDiff == 0 && curDiff == 1) {
                flips++;
            }

            prevDiff = curDiff;
        }

        return flips;
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

**Python:**

```python
def min_flips_xor(A, B):
    n = len(A)
    flips = 0
    prev_diff = 0  # Initially not in mismatch

    for i in range(n):
        cur_diff = 1 if A[i] != B[i] else 0

        # Transition from 0 to 1
        if prev_diff == 0 and cur_diff == 1:
            flips += 1

        prev_diff = cur_diff

    return flips

# Main
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(min_flips_xor(A, B))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int minFlips(vector<int>& A, vector<int>& B) {
    int n = A.size();
    int flips = 0;
    int prevDiff = 0;

    for (int i = 0; i < n; i++) {
        int curDiff = (A[i] != B[i]) ? 1 : 0;

        if (prevDiff == 0 && curDiff == 1) {
            flips++;
        }

        prevDiff = curDiff;
    }

    return flips;
}

int main() {
    int n;
    cin >> n;
    vector<int> A(n), B(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < n; i++) cin >> B[i];
    cout << minFlips(A, B) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function minFlips(A, B) {
  const n = A.length;
  let flips = 0;
  let prevDiff = 0;

  for (let i = 0; i < n; i++) {
    const curDiff = A[i] !== B[i] ? 1 : 0;

    if (prevDiff === 0 && curDiff === 1) {
      flips++;
    }

    prevDiff = curDiff;
  }

  return flips;
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
  const A = lines[1].split(" ").map(Number);
  const B = lines[2].split(" ").map(Number);
  console.log(minFlips(A, B));
});
```

### Visual Trace

```
A = [0, 1, 1, 0, 1, 0]
B = [1, 0, 1, 0, 0, 1]

Difference Array D:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
i     | 0  1  2  3  4  5
A[i]  | 0  1  1  0  1  0
B[i]  | 1  0  1  0  0  1
D[i]  | 1  1  0  0  1  1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Transitions (0→1):
prev=0, cur=1 at i=0 → flips=1
prev=1, cur=1 at i=1 → no change
prev=1, cur=0 at i=2 → no change
prev=0, cur=0 at i=3 → no change
prev=0, cur=1 at i=4 → flips=2
prev=1, cur=1 at i=5 → no change

Answer: 2
```

### Complexity Analysis

- **Time Complexity:** O(n)
  - Single pass with XOR comparison
- **Space Complexity:** O(1)
  - Only tracking previous difference state

---

## Approach 3: Difference Array Technique

### Core Insight

**Difference Tracking:**

- Create explicit difference array `D`
- Use two-pointer or scanning to count runs of 1s
- More explicit visualization

### Implementation

**Java:**

```java
import java.util.*;

class Solution {
    public int minFlips(int[] A, int[] B) {
        int n = A.length;

        // Create difference array
        int[] D = new int[n];
        for (int i = 0; i < n; i++) {
            D[i] = (A[i] == B[i]) ? 0 : 1;
        }

        // Count runs of 1s
        int flips = 0;
        for (int i = 0; i < n; i++) {
            if (D[i] == 1 && (i == 0 || D[i-1] == 0)) {
                flips++;
            }
        }

        return flips;
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

**Python:**

```python
def min_flips_diff_array(A, B):
    n = len(A)

    # Create difference array
    D = [1 if A[i] != B[i] else 0 for i in range(n)]

    # Count runs of 1s
    flips = 0
    for i in range(n):
        if D[i] == 1 and (i == 0 or D[i-1] == 0):
            flips += 1

    return flips

# Main
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(min_flips_diff_array(A, B))
```

**C++:**

```cpp
#include <bits/stdc++.h>
using namespace std;

int minFlips(vector<int>& A, vector<int>& B) {
    int n = A.size();

    // Create difference array
    vector<int> D(n);
    for (int i = 0; i < n; i++) {
        D[i] = (A[i] != B[i]) ? 1 : 0;
    }

    // Count runs of 1s
    int flips = 0;
    for (int i = 0; i < n; i++) {
        if (D[i] == 1 && (i == 0 || D[i-1] == 0)) {
            flips++;
        }
    }

    return flips;
}

int main() {
    int n;
    cin >> n;
    vector<int> A(n), B(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < n; i++) cin >> B[i];
    cout << minFlips(A, B) << endl;
    return 0;
}
```

**JavaScript:**

```javascript
function minFlips(A, B) {
  const n = A.length;

  // Create difference array
  const D = A.map((val, i) => (val !== B[i] ? 1 : 0));

  // Count runs of 1s
  let flips = 0;
  for (let i = 0; i < n; i++) {
    if (D[i] === 1 && (i === 0 || D[i - 1] === 0)) {
      flips++;
    }
  }

  return flips;
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
  const A = lines[1].split(" ").map(Number);
  const B = lines[2].split(" ").map(Number);
  console.log(minFlips(A, B));
});
```

### Complexity Analysis

- **Time Complexity:** O(n)
  - Two passes: one to create D, one to count
- **Space Complexity:** O(n)
  - Storing difference array D

---

## Edge Cases

### Case 1: Identical Arrays

```
A = [1, 0, 1, 0]
B = [1, 0, 1, 0]

D = [0, 0, 0, 0]
No mismatches → flips = 0
```

### Case 2: Completely Different

```
A = [0, 0, 0, 0]
B = [1, 1, 1, 1]

D = [1, 1, 1, 1]
One continuous mismatch run → flips = 1
```

### Case 3: Alternating Mismatches

```
A = [0, 1, 0, 1]
B = [1, 1, 1, 1]

D = [1, 0, 1, 0]
Each mismatch is isolated → flips = 2
```

### Case 4: Single Element

```
A = [0], B = [1] → flips = 1
A = [1], B = [1] → flips = 0
```

---

### Common Mistakes

### Mistake 1: Counting Individual Mismatches

```java
// Wrong: counts each mismatch separately
int flips = 0;
for (int i = 0; i < n; i++) {
    if (A[i] != B[i]) flips++;  // Wrong!
}
```

**Fix:** Count runs, not individual mismatches.

### Mistake 2: Not Handling Edge Cases

```python
# Wrong: accessing D[i-1] without checking i > 0
if D[i] == 1 and D[i-1] == 0:  # IndexError when i=0!
    flips += 1
```

### Mistake 3: Overlapping Flips

```
Thinking: Can we optimize by overlapping flips?
Answer: No! Each non-overlapping run needs exactly one flip.
```

---

## Interview Extensions

### Extension 1: Minimize Cost with Weighted Flips

Different range lengths have different costs. Find minimum cost.

**Approach:** Dynamic programming where `dp[i]` = minimum cost to fix A[0..i-1].

### Extension 2: Circular Array

Array wraps around (A[0] follows A[n-1]). Handle wraparound mismatches.

### Extension 3: K-Limited Flips

What if we can perform at most K flips? Check if transformation is possible.

---

## Practice Problems

1. **Minimum Flips to Make Binary String Alternating** - LeetCode 1888
2. **Flip Columns For Maximum Equal Rows** - Matrix version
3. **Range Toggle Queries** - Handle Q queries with toggles
4. **Minimum Swaps to Group All 1s** - Related sliding window problem
5. **Bit Flip Queries** - Dynamic updates with flip operations

---

## Summary Table

| Approach                | Time | Space | Best For                     |
| ----------------------- | ---- | ----- | ---------------------------- |
| Count Mismatch Runs     | O(n) | O(1)  | Clean, efficient             |
| XOR Transition Counting | O(n) | O(1)  | Explicit difference tracking |
| Difference Array        | O(n) | O(n)  | Visualization, debugging     |

---

## Key Takeaways

1. **Problem reduces to counting runs** - consecutive mismatches form groups
2. **Single pass solution exists** - O(n) time, O(1) space
3. **XOR identifies mismatches** - fundamental bitwise operation
4. **Greedy is optimal** - each run needs exactly one flip
5. **Order doesn't matter** - independent non-overlapping flips

This problem teaches:

- Run-length encoding
- Greedy algorithms
- Bitwise XOR applications
- Array transformation techniques

Perfect for interviews testing array manipulation and optimization skills!
