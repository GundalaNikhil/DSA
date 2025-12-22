---
problem_id: QUE_CAFETERIA_QUEUE_ROTATION__9067
display_id: QUE-003
slug: cafeteria-queue-rotation
title: "Cafeteria Queue Rotation"
difficulty: Easy
difficulty_score: 20
topics:
  - Queue
  - Array Manipulation
  - Simulation
tags:
  - queue
  - rotation
  - easy
  - arrays
premium: true
subscription_tier: basic
---

# QUE-003: Cafeteria Queue Rotation

## 📋 Problem Summary

We are given a queue of $N$ students. We need to perform a "left rotation" $K$ times.
- A single left rotation means taking the person at the front and moving them to the back.
- We need to output the final order of the queue.

## 🌍 Real-World Scenario

**Scenario Title:** Playlist Looping

Imagine a music playlist on "Repeat All" mode.
- You have a list of songs: `[A, B, C, D]`.
- You press "Next" 3 times.
- 1st Next: A plays and goes to back. `[B, C, D, A]`.
- 2nd Next: B plays and goes to back. `[C, D, A, B]`.
- 3rd Next: C plays and goes to back. `[D, A, B, C]`.
- The "Queue Rotation" problem asks: "What does the playlist look like after skipping $K$ songs?"

**Why This Problem Matters:**

- **Load Balancing:** Round-robin scheduling often involves rotating a list of servers.
- **Cryptography:** Bitwise rotation (circular shift) is a core operation in hashing algorithms like MD5/SHA.
- **UI Carousels:** Rotating images in a slider.

![Real-World Application](../images/QUE-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Rotation Logic

Queue: `[4, 9, 1, 7]`, $K=3$.

1. **Initial:**
   Front -> `4, 9, 1, 7` <- Back

2. **Rotate 1:** Move 4 to back.
   Front -> `9, 1, 7, 4` <- Back

3. **Rotate 2:** Move 9 to back.
   Front -> `1, 7, 4, 9` <- Back

4. **Rotate 3:** Move 1 to back.
   Front -> `7, 4, 9, 1` <- Back

Result: `7 4 9 1`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** $N$, array of values, $K$.
- **Output:** Space-separated values.
- **Edge Case:** $K$ can be very large ($10^9$). Rotating $N$ times brings us back to the start. So we only need to rotate $K \pmod N$ times.
- **Edge Case:** $N=0$ (empty queue).

## Naive Approach

### Intuition

Simulate the process literally using a Queue data structure.

### Algorithm

1. Load all elements into a Queue.
2. Loop $K$ times:
   - `val = queue.dequeue()`
   - `queue.enqueue(val)`
3. Print queue contents.

### Limitations

- **Time Complexity:** $O(K)$. If $K = 10^9$, this will Time Limit Exceed (TLE).
- We must optimize using modulo arithmetic.

## Optimal Approach

### Key Insight

1. **Modulo Reduction:** Rotating $N$ times is a no-op. Effective rotations $K_{eff} = K \pmod N$.
2. **Array Slicing:** The element at index $K_{eff}$ becomes the new head. The elements from $0$ to $K_{eff}-1$ move to the back.
   - New order: `arr[K:] + arr[:K]` (Python syntax).

### Algorithm

1. If $N=0$, return empty.
2. $K = K \pmod N$.
3. Create a new array `result` of size $N$.
4. Copy `values[K...N-1]` to the start of `result`.
5. Copy `values[0...K-1]` to the end of `result`.
6. Return `result`.

### Time Complexity

- **O(N)** to copy elements.
- Independent of $K$ (after modulo).

### Space Complexity

- **O(N)** for the result array.

![Algorithm Visualization](../images/QUE-003/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-003/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] rotateQueue(int[] values, long k) {
        int n = values.length;
        if (n == 0) return new int[0];
        
        int rotations = (int)(k % n);
        if (rotations == 0) return values;
        
        int[] result = new int[n];
        // Copy from rotations to end -> start of result
        // System.arraycopy(src, srcPos, dest, destPos, length)
        
        // Part 1: values[rotations...n-1] -> result[0...]
        System.arraycopy(values, rotations, result, 0, n - rotations);
        
        // Part 2: values[0...rotations-1] -> result[n-rotations...]
        System.arraycopy(values, 0, result, n - rotations, rotations);
        
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] values = new int[n];
            for (int i = 0; i < n; i++) {
                values[i] = sc.nextInt();
            }
            long k = sc.nextLong();
    
            Solution solution = new Solution();
            int[] result = solution.rotateQueue(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

def rotate_queue(values: List[int], k: int) -> List[int]:
    n = len(values)
    if n == 0:
        return []
    
    k = k % n
    # Slicing is O(N)
    return values[k:] + values[:k]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        k = int(next(iterator))
        
        result = rotate_queue(values, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> rotateQueue(const vector<int>& values, long long k) {
        int n = values.size();
        if (n == 0) return {};
        
        int rotations = k % n;
        if (rotations == 0) return values;
        
        vector<int> result;
        result.reserve(n);
        
        // Append second part
        for (int i = rotations; i < n; i++) {
            result.push_back(values[i]);
        }
        // Append first part
        for (int i = 0; i < rotations; i++) {
            result.push_back(values[i]);
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> values(n);
        for (int i = 0; i < n; i++) {
            cin >> values[i];
        }
        long long k;
        cin >> k;
    
        Solution solution;
        vector<int> result = solution.rotateQueue(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  rotateQueue(values, k) {
    const n = values.length;
    if (n === 0) return [];
    
    // In JS, k can be larger than Number.MAX_SAFE_INTEGER if not careful,
    // but constraints say 10^9 which fits.
    const rotations = k % n;
    
    if (rotations === 0) return values;
    
    // Slice and concat
    const part1 = values.slice(rotations);
    const part2 = values.slice(0, rotations);
    return part1.concat(part2);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }
  const k = parseInt(data[idx++], 10);

  const solution = new Solution();
  const result = solution.rotateQueue(values, k);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `4 9 1 7`, `k=3`
1. $N=4$.
2. $K_{eff} = 3 \pmod 4 = 3$.
3. New Head Index = 3. Value is `7`.
4. Part 1 (from index 3 to end): `[7]`.
5. Part 2 (from index 0 to 3): `[4, 9, 1]`.
6. Concat: `[7, 4, 9, 1]`.

Output matches example.

![Example Visualization](../images/QUE-003/example-1.png)

## ✅ Proof of Correctness

### Invariant
Rotating left by 1 is equivalent to shifting indices $i \to (i-1) \pmod N$. Rotating by $K$ shifts indices by $-K \pmod N$.

### Why the approach is correct
The element at original index $K$ moves to index $0$. The element at index $K+1$ moves to index $1$, etc. Our slicing logic perfectly reconstructs this.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Rotate in-place with $O(1)$ extra space?
  - *Hint:* "Reversal Algorithm". Reverse `0..K-1`, reverse `K..N-1`, then reverse `0..N-1`.
- **Extension 2:** Right Rotation?
  - *Hint:* Right rotate by $K$ is same as Left rotate by $N - (K \pmod N)$.

### Common Mistakes to Avoid

1. **Large K**
   - ❌ Wrong: Looping $K$ times when $K=10^9$.
   - ✅ Correct: Use modulo $N$.
2. **Empty Array**
   - ❌ Wrong: `k % n` when `n=0` causes division by zero.
   - ✅ Correct: Check `n == 0` first.

## Related Concepts

- **Circular Buffer:** Naturally supports rotation by moving head pointer.
- **String Rotation:** Checking if string A is a rotation of B (check if A is substring of B+B).
