---
title: Assembly Line Buffer Swap
slug: assembly-line-buffer-swap
difficulty: Easy
difficulty_score: 29
tags:
- Queue
- Simulation
- In-Place
problem_id: QUE_ASSEMBLY_LINE_BUFFER_SWAP__9053
display_id: QUE-016
topics:
- Queue
- Simulation
- In-Place
---
# Assembly Line Buffer Swap - Editorial

## Problem Summary

You are given two queues (buffers) of equal length `n`. Your task is to swap their contents completely. The first queue should end up containing the elements originally in the second queue, and vice-versa.

## Real-World Scenario

This problem models **Double Buffering** in computer graphics or **Assembly Line Switching** in manufacturing.
-   **Graphics**: While one buffer is being displayed on the screen, the GPU writes the next frame to a second buffer. Once the frame is ready, the pointers to the buffers are swapped instantly, so the new frame is displayed while the old one becomes the write target.
-   **Manufacturing**: Two parallel assembly lines might need to swap their entire set of active components due to a reconfiguration or a fault in one line's processing units.

## Problem Exploration

### 1. The Goal
We have:
-   Queue 1: `[A, B, C]`
-   Queue 2: `[X, Y, Z]`
We want:
-   Queue 1: `[X, Y, Z]`
-   Queue 2: `[A, B, C]`

### 2. Constraints
-   `n` up to `10^5`.
-   Operations should be efficient (`O(N)` or `O(1)`).

## Approaches

### Approach 1: Element-wise Swap (Simulation)

If we treat the inputs strictly as Queues (FIFO), we can use a temporary buffer or simply dequeue from one and enqueue to another.
Since we need to swap them, we can:
1.  Dequeue all elements from Q1 into a temporary list `Temp1`.
2.  Dequeue all elements from Q2 into a temporary list `Temp2`.
3.  Enqueue all elements from `Temp2` into Q1.
4.  Enqueue all elements from `Temp1` into Q2.

### Approach 2: Reference Swap (Optimal)

Since the queues are provided as arrays (or lists) in the input, and we just need to output the swapped result, the most efficient way is to simply swap the references to the arrays. In languages like C++, Java, or Python, swapping two variables pointing to large arrays is an `O(1)` operation. However, since we need to print the output which involves iterating through all elements, the overall complexity is dominated by I/O, which is `O(N)`.

For the purpose of the solution function which returns the swapped arrays:
-   We can just return `[q2, q1]`.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int[][] swapQueues(int[] q1, int[] q2) {
        return new int[][]{q2, q1};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[] q1, q2;

            // If we have exactly 2n values
            if (remaining.size() == 2 * n) {
                q1 = new int[n];
                q2 = new int[n];
                for (int i = 0; i < n; i++) {
                    q1[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    q2[i] = remaining.get(n + i);
                }
            } else if (remaining.size() == n) {
                // Only n values - use as q1, create default q2
                q1 = new int[n];
                q2 = new int[n];
                for (int i = 0; i < n; i++) {
                    q1[i] = remaining.get(i);
                    q2[i] = 0;
                }
            } else {
                // Fallback
                int q1Len = Math.min(n, remaining.size());
                q1 = new int[q1Len];
                q2 = new int[q1Len];

                for (int i = 0; i < q1Len; i++) {
                    q1[i] = remaining.get(i);
                    if (i < remaining.size() - n) {
                        q2[i] = remaining.get(n + i);
                    } else {
                        q2[i] = 0;
                    }
                }
            }

            Solution sol = new Solution();
            int[][] result = sol.swapQueues(q1, q2);
            for (int j = 0; j < 2; j++) {
                for (int i = 0; i < result[j].length; i++) {
                    if (i > 0) System.out.print(" ");
                    System.out.print(result[j][i]);
                }
                System.out.println();
            }
        }
    }
}
```

### Python
```python
from typing import List
import sys

def swap_queues(q1: List[int], q2: List[int]) -> List[List[int]]:
    return [q2, q1]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        remaining = list(iterator)

        # If we have exactly 2n values, split them in half
        if len(remaining) == 2 * n:
            q1 = [int(x) for x in remaining[:n]]
            q2 = [int(x) for x in remaining[n:]]
        # If we have exactly n values, use as q1, create q2
        elif len(remaining) == n:
            q1 = [int(x) for x in remaining]
            q2 = [0] * n  # Default second queue
        # Otherwise try to split as much as possible
        else:
            q1 = [int(x) for x in remaining[:n]]
            q2 = [int(x) for x in remaining[n:]] if len(remaining) > n else [0] * n

        result = swap_queues(q1, q2)
        for resArr in result:
            print(" ".join(map(str, resArr)))
    except (StopIteration, ValueError, IndexError):
        pass

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
    vector<vector<int>> swapQueues(const vector<int>& q1, const vector<int>& q2) {
        return {q2, q1};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<int> q1, q2;

        // If we have exactly 2n values
        if ((int)remaining.size() == 2 * n) {
            q1.assign(remaining.begin(), remaining.begin() + n);
            q2.assign(remaining.begin() + n, remaining.end());
        } else if ((int)remaining.size() == n) {
            // Only n values - use as q1, create default q2
            q1.assign(remaining.begin(), remaining.end());
            q2.assign(n, 0);
        } else {
            // Fallback
            q1.assign(remaining.begin(), remaining.begin() + min(n, (int)remaining.size()));
            if ((int)remaining.size() > n) {
                q2.assign(remaining.begin() + n, remaining.end());
            }
            // Pad q2 with 0s if needed
            while ((int)q2.size() < n) {
                q2.push_back(0);
            }
        }

        Solution sol;
        vector<vector<int>> result = sol.swapQueues(q1, q2);
        for (const auto& resArr : result) {
            for (int i = 0; i < (int)resArr.size(); i++) {
                cout << (i ? " " : "") << resArr[i];
            }
            cout << endl;
        }
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  swapQueues(q1, q2) {
    return [q2, q1];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let q1, q2;

  // If we have exactly 2n values
  if (remaining.length === 2 * n) {
    q1 = remaining.slice(0, n).map(x => parseInt(x, 10));
    q2 = remaining.slice(n, 2 * n).map(x => parseInt(x, 10));
  } else if (remaining.length === n) {
    // Only n values - use as q1, create default q2
    q1 = remaining.map(x => parseInt(x, 10));
    q2 = Array(n).fill(0);
  } else {
    // Fallback
    q1 = remaining.slice(0, n).map(x => parseInt(x, 10));
    q2 = remaining.length > n ? remaining.slice(n).map(x => parseInt(x, 10)) : Array(n).fill(0);
    // Pad q2 if needed
    while (q2.length < n) {
      q2.push(0);
    }
  }

  const solution = new Solution();
  const result = solution.swapQueues(q1, q2);
  result.forEach((resArr) => {
    console.log(resArr.join(" "));
  });
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2
4 5
7 8
```
`q1 = [4, 5]`, `q2 = [7, 8]`

**Execution:**
The function receives these two arrays. It returns a list/array where the first element is `q2` and the second is `q1`.

**Output:**
Line 1 (New Q1): `7 8`
Line 2 (New Q2): `4 5`

## Proof of Correctness

The operation is trivial. By definition, if we output the contents of the second queue where the first is expected, and vice-versa, we have achieved a swap. The data integrity is preserved because we are not modifying the individual elements, just the containers.

## Interview Extensions

1.  **What if you must use `std::queue` and cannot access the underlying container?**
    -   You would use `std::swap(q1, q2)`, which is an efficient `O(1)` operation for standard library containers in C++ (it swaps internal pointers). In Java/Python, you'd swap the variable references.

2.  **What if the queues are on different physical machines?**
    -   You cannot do a pointer swap. You would have to serialize the data and transmit it over the network, which is `O(N)` and limited by bandwidth.

3.  **What if the queues have different lengths?**
    -   The logic remains exactly the same: just swap the containers.

### Common Mistakes

-   **Overthinking**: Trying to implement a complex element-by-element swap logic when a simple container swap suffices.
-   **Deep Copying unnecessarily**: Creating new arrays and copying elements one by one is `O(N)` time and memory, whereas swapping references is `O(1)` (though printing is still `O(N)`).

## Related Concepts

-   **Pointers/References**: Understanding how variables refer to data in memory.
-   **Double Buffering**: A key system design concept.
-   **Swap**: Basic algorithmic primitive.
