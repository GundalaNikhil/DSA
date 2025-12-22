---
problem_id: QUE_LAB_PRINTER_REVERSAL__6429
display_id: QUE-005
slug: lab-printer-reversal
title: "Lab Printer Reversal"
difficulty: Easy
difficulty_score: 26
topics:
  - Queue
  - Stack
  - Simulation
tags:
  - queue
  - stack
  - reversal
  - easy
premium: true
subscription_tier: basic
---

# QUE-005: Lab Printer Reversal

## 📋 Problem Summary

We are given a queue of $N$ jobs. We need to reverse the order of the first $K$ jobs while keeping the remaining $N-K$ jobs in their original relative order.

## 🌍 Real-World Scenario

**Scenario Title:** Stack of Papers

Imagine a printer tray.
- You put a stack of 50 papers in.
- You realize the first 10 papers were loaded upside down (last page first).
- You take out the top 10 papers, flip the entire small stack over, and put them back.
- The remaining 40 papers are untouched.
- This "flip" operation is exactly what reversing the first $K$ elements does.

**Why This Problem Matters:**

- **Packet Processing:** Reordering packets that arrived out of sequence.
- **Undo Operations:** Reversing a sequence of recent actions.
- **Data Transformation:** A building block for more complex permutations.

![Real-World Application](../images/QUE-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Reversal Process

Queue: `[2, 4, 6, 8, 10]`, $K=4$.

1. **Extract First K:**
   Queue: `[10]`
   Extracted: `2, 4, 6, 8`

2. **Reverse Extracted:**
   Using a Stack: Push `2`, `4`, `6`, `8`.
   Pop: `8, 6, 4, 2`.

3. **Re-insert:**
   Queue: `[10, 8, 6, 4, 2]` (Note: 10 is still at front!)

4. **Rotate Remaining:**
   Move `10` to back.
   Queue: `[8, 6, 4, 2, 10]`.

Result: `8 6 4 2 10`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** $N$, array of values, $K$.
- **Output:** Modified array.
- **Constraint:** $1 \le K \le N$.

## Naive Approach

### Intuition

Create a new array. Copy indices $K-1$ down to $0$. Then copy $K$ to $N-1$.

### Algorithm

1. Create `result` array.
2. Loop `i` from $K-1$ down to 0: Add `values[i]`.
3. Loop `i` from $K$ to $N-1$: Add `values[i]`.

### Limitations

- **Space Complexity:** $O(N)$ for new array.
- This is efficient for arrays but doesn't teach Queue mechanics.

## Optimal Approach (Queue-based)

### Key Insight

A **Stack** naturally reverses order (LIFO). A **Queue** preserves order (FIFO). Combining them allows partial reversal.

### Algorithm

1. Create an empty Stack.
2. Dequeue first $K$ elements and push them onto the Stack.
3. While Stack is not empty, pop and Enqueue back to the Queue.
   - Now the first $K$ are at the back, but reversed.
   - The remaining $N-K$ are at the front.
4. Rotate the Queue $N-K$ times (Dequeue and Enqueue immediately).
   - This moves the unreversed part to the back, bringing the reversed part to the front.

### Time Complexity

- **O(N)**. Each element is moved a constant number of times.

### Space Complexity

- **O(K)** for the stack.

![Algorithm Visualization](../images/QUE-005/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-005/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] reverseFirstK(int[] values, int k) {
        Queue<Integer> queue = new LinkedList<>();
        for (int v : values) queue.offer(v);
        
        Stack<Integer> stack = new Stack<>();
        
        // 1. Dequeue first K and push to stack
        for (int i = 0; i < k; i++) {
            stack.push(queue.poll());
        }
        
        // 2. Pop from stack and enqueue
        while (!stack.isEmpty()) {
            queue.offer(stack.pop());
        }
        
        // 3. Rotate remaining N-K elements
        int n = values.length;
        for (int i = 0; i < n - k; i++) {
            queue.offer(queue.poll());
        }
        
        // Convert back to array
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = queue.poll();
        }
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
            int k = sc.nextInt();
    
            Solution solution = new Solution();
            int[] result = solution.reverseFirstK(values, k);
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
from collections import deque
import sys

def reverse_first_k(values: List[int], k: int) -> List[int]:
    queue = deque(values)
    stack = []
    
    # 1. Dequeue first K and push to stack
    for _ in range(k):
        stack.append(queue.popleft())
        
    # 2. Pop from stack and enqueue
    while stack:
        queue.append(stack.pop())
        
    # 3. Rotate remaining N-K elements
    n = len(values)
    for _ in range(n - k):
        queue.append(queue.popleft())
        
    return list(queue)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        k = int(next(iterator))
        
        result = reverse_first_k(values, k)
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
#include <queue>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> reverseFirstK(const vector<int>& values, int k) {
        queue<int> q;
        for (int v : values) q.push(v);
        
        stack<int> s;
        
        // 1. Dequeue first K and push to stack
        for (int i = 0; i < k; i++) {
            s.push(q.front());
            q.pop();
        }
        
        // 2. Pop from stack and enqueue
        while (!s.empty()) {
            q.push(s.top());
            s.pop();
        }
        
        // 3. Rotate remaining N-K elements
        int n = values.size();
        for (int i = 0; i < n - k; i++) {
            q.push(q.front());
            q.pop();
        }
        
        vector<int> result;
        while (!q.empty()) {
            result.push_back(q.front());
            q.pop();
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
        int k;
        cin >> k;
    
        Solution solution;
        vector<int> result = solution.reverseFirstK(values, k);
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
  reverseFirstK(values, k) {
    // Using array methods to simulate Queue/Stack for clarity
    const queue = [...values]; // Copy
    const stack = [];
    
    // 1. Dequeue first K
    for (let i = 0; i < k; i++) {
      stack.push(queue.shift());
    }
    
    // 2. Pop and Enqueue
    while (stack.length > 0) {
      queue.push(stack.pop());
    }
    
    // 3. Rotate remaining N-K
    const n = values.length;
    for (let i = 0; i < n - k; i++) {
      queue.push(queue.shift());
    }
    
    return queue;
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
  const result = solution.reverseFirstK(values, k);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `2 4 6 8 10`, `k=4`
1. Queue: `[2, 4, 6, 8, 10]`.
2. Extract 4: Stack `[2, 4, 6, 8]` (Top is 8). Queue `[10]`.
3. Pop & Enqueue:
   - Pop 8 -> Q `[10, 8]`
   - Pop 6 -> Q `[10, 8, 6]`
   - Pop 4 -> Q `[10, 8, 6, 4]`
   - Pop 2 -> Q `[10, 8, 6, 4, 2]`
4. Rotate $N-K = 1$ time:
   - Dequeue 10, Enqueue 10.
   - Q `[8, 6, 4, 2, 10]`.

Output matches example.

![Example Visualization](../images/QUE-005/example-1.png)

## ✅ Proof of Correctness

### Invariant
The stack reverses the order of elements passed through it. The rotation step restores the relative position of the unreversed segment.

### Why the approach is correct
By processing the first $K$ elements through a LIFO structure and placing them at the back, then moving the remaining FIFO elements to the back, we achieve the desired permutation.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Reverse only the *last* K elements?
  - *Hint:* Rotate $N-K$ times first, then reverse first $K$, then rotate $K$ times. Or just use the logic: "Last K" is "First K" if we look from the back (Deque).
- **Extension 2:** Recursive Reversal?
  - *Hint:* You can reverse a queue using recursion (implicit stack) instead of an explicit stack.

### C++ommon Mistakes to Avoid

1. **Forgetting Rotation**
   - ❌ Wrong: Just reversing first $K$ and stopping. The reversed part is now at the *back* of the queue!
   - ✅ Correct: Must rotate the remaining elements to bring the reversed part to the front.
2. **Off-by-one**
   - ❌ Wrong: Looping $K-1$ or $K+1$ times.
   - ✅ Correct: Loop exactly $K$ times.

## Related Concepts

- **Stack:** LIFO.
- **Queue:** FIFO.
- **Deque:** Can be used to optimize rotations.
