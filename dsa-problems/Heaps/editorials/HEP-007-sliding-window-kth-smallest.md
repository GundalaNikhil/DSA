---
problem_id: HEP_SLIDING_WINDOW_KTH_SMALLEST__2665
display_id: HEP-007
slug: sliding-window-kth-smallest
title: "Sliding Window Kth Smallest"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Sliding Window
  - Order Statistics
tags:
  - heaps
  - sliding-window
  - order-statistics
  - medium
premium: true
subscription_tier: basic
---

# HEP-007: Sliding Window Kth Smallest

## 📋 Problem Summary

You have an array `arr` of size `n`.
Consider a sliding window of size `w`.
For each window position, find the `k`-th smallest element.
Return the list of `k`-th smallest elements.

## 🌍 Real-World Scenario

**Scenario Title:** Stock Market Volatility Analysis

Traders often look at the "median" or "25th percentile" price of a stock over the last `w` minutes to gauge trends without being affected by outliers.
- If `k = w/2`, you are finding the **Running Median**.
- If `k = 1`, you are finding the **Running Minimum**.
- If `k = w`, you are finding the **Running Maximum**.
This problem generalizes all these to the "Running K-th Percentile".

![Real-World Application](../images/HEP-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Two-Heap Strategy

Window: `[1, 5, 2, 8, 3]`, `k=3` (Median).
Sorted: `[1, 2, 3, 5, 8]`. 3rd smallest is 3.

We maintain two heaps (or balanced BSTs):
1. **Left Heap (Max-Heap):** Stores the smallest `k` elements.
2. **Right Heap (Min-Heap):** Stores the remaining `w-k` elements.

Invariant:
- Size of Left Heap = `k`.
- Size of Right Heap = `w-k`.
- `max(Left) <= min(Right)`.

The answer is always `Left.top()`.

**Sliding:**
- **Add** new element `x`.
- **Remove** old element `y`.

Steps:
1. Remove `y`:
   - If `y` was in Left, remove it. Left size decreases.
   - If `y` was in Right, remove it. Right size decreases.
2. Add `x`:
   - Insert into appropriate heap to maintain order.
3. Rebalance:
   - Ensure Left has exactly `k` elements.
   - Move elements between heaps if sizes are off.

### Key Concept: Lazy Deletion

Standard heaps don't support efficient removal of arbitrary elements ($O(N)$).
We use **Lazy Deletion**:
- Keep a `deleted` map (or hash table) of counts of elements to be removed.
- When `top()` of a heap is in `deleted`, pop it and decrement count.
- We also need to track the *logical* size of heaps, not just physical size.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n`, `w`, `k`, array `arr`.
- **Output:** Array of size `n-w+1`.
- **Constraints:** $N \le 2 \times 10^5$. $W \le N$.
- **Values:** Integers, can be negative.

## Naive Approach

### Intuition

For each window, copy elements, sort them, pick index `k-1`.

### Time Complexity

- **O(N * W log W)**: Too slow if $W$ is large.

## Optimal Approach

### Key Insight

Use **Two Heaps with Lazy Deletion**.
- **Max-Heap `L`**: Stores smallest `k` elements.
- **Min-Heap `R`**: Stores largest `w-k` elements.
- **Balance**: `L.size == k`.
- **Lazy Removal**: Use a hash map `to_remove` to mark elements that left the window but are still in heaps. Clean up tops lazily.

### Algorithm

1. Initialize `L` (Max-Heap), `R` (Min-Heap), `to_remove` map.
2. `balance` function:
   - While `L.size > k`: Move top of `L` to `R`.
   - While `L.size < k`: Move top of `R` to `L`.
   - While `L.top` > `R.top`: Swap tops (if heaps not empty).
   - *Wait, lazy deletion complicates size tracking.*
   - We must track `L_valid_size` and `R_valid_size` explicitly.
3. **Add(val)**:
   - If `L` empty or `val < L.top`: push to `L`, `L_valid++`.
   - Else: push to `R`, `R_valid++`.
   - Rebalance.
4. **Remove(val)**:
   - Increment `to_remove[val]`.
   - If `val` could be in `L` (i.e., `val <= L.top`): `L_valid--`.
   - Else: `R_valid--`.
   - Clean tops: `while L.top in to_remove: pop L`. Same for `R`.
   - Rebalance.
5. **Rebalance Logic**:
   - While `L_valid > k`:
     - Move `L.top` to `R`. (Pop L, Push R).
     - `L_valid--`, `R_valid++`.
     - Clean `L`.
   - While `L_valid < k`:
     - Move `R.top` to `L`.
     - `L_valid++`, `R_valid--`.
     - Clean `R`.
   - Note: We rely on `L.top` being the k-th smallest.

### Time Complexity

- **O(N log W)**.

### Space Complexity

- **O(N)** (due to lazy deletion, heap can grow up to N).

![Algorithm Visualization](../images/HEP-007/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] kthSmallestInWindows(int[] arr, int w, int k) {
        int n = arr.length;
        int[] result = new int[n - w + 1];
        
        // Max-Heap for smallest k elements
        PriorityQueue<Integer> left = new PriorityQueue<>(Collections.reverseOrder());
        // Min-Heap for largest w-k elements
        PriorityQueue<Integer> right = new PriorityQueue<>();
        
        Map<Integer, Integer> deleted = new HashMap<>();
        
        int leftSize = 0;
        int rightSize = 0;
        
        for (int i = 0; i < n; i++) {
            // Add new element
            int val = arr[i];
            if (leftSize < k) {
                left.offer(val);
                leftSize++;
            } else {
                if (val < left.peek()) {
                    right.offer(left.poll());
                    left.offer(val);
                    // Clean left top? No, we just swapped.
                    // But wait, lazy deletion means peek() might be garbage.
                    // We must clean before peeking.
                } else {
                    right.offer(val);
                }
                rightSize++; // Actually, logic is complex with lazy deletion.
            }
            
            // Let's restart logic with explicit balance function
        }
        
        // Reset and use cleaner approach
        left.clear(); right.clear(); deleted.clear();
        leftSize = 0; rightSize = 0;
        
        for (int i = 0; i < n; i++) {
            // ADD
            int val = arr[i];
            // Clean tops first? No, clean when needed.
            
            // Heuristic insert
            if (left.isEmpty() || val <= left.peek()) {
                left.offer(val);
                leftSize++;
            } else {
                right.offer(val);
                rightSize++;
            }
            
            // REMOVE (if window full)
            if (i >= w) {
                int out = arr[i - w];
                deleted.put(out, deleted.getOrDefault(out, 0) + 1);
                
                // Where was 'out'?
                // We can't know for sure without checking, but we know the invariant:
                // All in Left <= All in Right.
                // If out <= left.peek(), it must be in Left (or deleted from Left).
                // Wait, if out == left.peek(), it could be in Left.
                // But what if duplicates?
                // Standard logic: If out <= left.peek(), decrement leftSize. Else rightSize.
                // BUT, we must ensure left.peek() is valid first!
                
                clean(left, deleted);
                // Now left.peek() is valid (or null)
                
                if (!left.isEmpty() && out <= left.peek()) {
                    leftSize--;
                } else {
                    rightSize--;
                }
            }
            
            // REBALANCE
            // We want leftSize == k
            
            // 1. Clean tops
            clean(left, deleted);
            clean(right, deleted);
            
            // 2. Move R -> L if L needs more
            while (leftSize < k && !right.isEmpty()) {
                clean(right, deleted); // Ensure valid
                if (right.isEmpty()) break;
                left.offer(right.poll());
                leftSize++;
                rightSize--;
                clean(left, deleted); // Ensure valid top for next checks
            }
            
            // 3. Move L -> R if L has too many
            while (leftSize > k && !left.isEmpty()) {
                clean(left, deleted);
                if (left.isEmpty()) break;
                right.offer(left.poll());
                leftSize--;
                rightSize++;
                clean(right, deleted);
            }
            
            // 4. Ensure order (L.max <= R.min)
            // This is implicitly handled by insertion logic + rebalance?
            // If we insert to L but it belongs in R?
            // Example: L=[10], R=[5]. k=1.
            // L has 10. R has 5.
            // We need to swap.
            // Check: if !L.empty && !R.empty && L.peek > R.peek
            while (!left.isEmpty() && !right.isEmpty() && left.peek() > right.peek()) {
                int l = left.poll();
                int r = right.poll();
                left.offer(r);
                right.offer(l);
                clean(left, deleted);
                clean(right, deleted);
            }
            
            // Record result
            if (i >= w - 1) {
                clean(left, deleted);
                result[i - w + 1] = left.peek();
            }
        }
        
        return result;
    }
    
    private void clean(PriorityQueue<Integer> pq, Map<Integer, Integer> deleted) {
        while (!pq.isEmpty() && deleted.getOrDefault(pq.peek(), 0) > 0) {
            int val = pq.poll();
            deleted.put(val, deleted.get(val) - 1);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int w = sc.nextInt();
            int k = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            int[] result = solution.kthSmallestInWindows(arr, w, k);
            for (int i = 0; i < result.length; i++) {
                System.out.print(result[i]);
                if (i < result.length - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

class Solution:
    def kth_smallest_in_windows(self, arr: list, w: int, k: int) -> list:
        n = len(arr)
        result = []
        
        # Max-Heap (Left): stores negative values
        left = []
        # Min-Heap (Right)
        right = []
        
        deleted = {}
        
        left_size = 0
        right_size = 0
        
        def clean(heap, is_max=False):
            while heap:
                val = -heap[0] if is_max else heap[0]
                if deleted.get(val, 0) > 0:
                    heapq.heappop(heap)
                    deleted[val] -= 1
                    if deleted[val] == 0:
                        del deleted[val]
                else:
                    break
                    
        for i in range(n):
            val = arr[i]
            
            # ADD
            clean(left, True)
            if not left or val <= -left[0]:
                heapq.heappush(left, -val)
                left_size += 1
            else:
                heapq.heappush(right, val)
                right_size += 1
                
            # REMOVE
            if i >= w:
                out = arr[i - w]
                deleted[out] = deleted.get(out, 0) + 1
                
                clean(left, True)
                # Check if out was logically in left
                # If out <= left_max, it was in left.
                # Note: left might be empty after clean if k=0 (impossible) or w=0
                if left and out <= -left[0]:
                    left_size -= 1
                else:
                    right_size -= 1
            
            # REBALANCE
            # 1. Size balance
            while left_size < k:
                clean(right, False)
                if not right: break
                val = heapq.heappop(right)
                heapq.heappush(left, -val)
                left_size += 1
                right_size -= 1
                
            while left_size > k:
                clean(left, True)
                if not left: break
                val = -heapq.heappop(left)
                heapq.heappush(right, val)
                left_size -= 1
                right_size += 1
                
            # 2. Value balance (Swap if L.max > R.min)
            while True:
                clean(left, True)
                clean(right, False)
                if not left or not right:
                    break
                l_max = -left[0]
                r_min = right[0]
                if l_max > r_min:
                    heapq.heappop(left)
                    heapq.heappop(right)
                    heapq.heappush(left, -r_min)
                    heapq.heappush(right, l_max)
                else:
                    break
            
            if i >= w - 1:
                clean(left, True)
                result.append(-left[0])
                
        return result

def kth_smallest_in_windows(arr: list, w: int, k: int) -> list:
    solver = Solution()
    return solver.kth_smallest_in_windows(arr, w, k)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        w = int(next(it))
        k = int(next(it))
        arr = []
        for _ in range(n):
            arr.append(int(next(it)))
            
        result = kth_smallest_in_windows(arr, w, k)
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
#include <set>

using namespace std;

class Solution {
public:
    vector<int> kthSmallestInWindows(const vector<int>& arr, int w, int k) {
        // In C++, we can use multiset which supports deletion!
        // This simplifies things immensely compared to Java/Python heaps.
        // O(N log W)
        
        multiset<int> window;
        vector<int> result;
        
        // Optimization: Maintain an iterator to the k-th element?
        // Yes, "Moving Iterator" technique.
        // O(N) if we just move iterator, but insertion is O(log W).
        
        auto mid = window.begin(); // Points to k-th element (0-indexed k-1)
        
        for (int i = 0; i < arr.size(); i++) {
            window.insert(arr[i]);
            
            if (i < w) {
                // Initial build
                if (window.size() == k) {
                    mid = prev(window.end());
                } else if (window.size() > k) {
                    if (arr[i] < *mid) mid--;
                }
            } else {
                // Slide
                int out = arr[i - w];
                int in = arr[i];
                
                // Insert logic relative to mid
                if (in < *mid) mid--;
                
                // Remove logic
                // Be careful: mid might be invalidated if we erase it
                auto it = window.lower_bound(out); // Find ONE instance
                // If duplicates, any instance works, but we must be careful if it is mid
                
                if (it == mid) {
                    // We are removing the element mid points to.
                    // We need to shift mid.
                    // If we remove mid, the next element becomes the new k-th?
                    // Wait, if we remove k-th, the (k+1)-th becomes k-th.
                    // So mid should move to next.
                    auto next_it = next(mid);
                    window.erase(it);
                    mid = next_it;
                } else {
                    if (*it < *mid) {
                        // Removed from left of mid, mid shifts right (to larger)
                        window.erase(it);
                        mid++;
                    } else {
                        // Removed from right of mid, mid stays (relative index same)
                        window.erase(it);
                    }
                }
            }
            
            if (i >= w - 1) {
                // Adjust mid to be exactly k-th
                // Due to insert/remove, mid might be off by 1?
                // Let's rely on `advance` for safety in "Medium" solution?
                // No, O(K) is too slow.
                // Let's use two multisets L and R to be safe and match other langs.
                // L size = k. R size = w-k.
            }
        }
        
        // Re-implementation with Two Multisets for clarity and robustness
        multiset<int> L, R;
        result.clear();
        
        for (int i = 0; i < arr.size(); i++) {
            int val = arr[i];
            
            // ADD
            if (L.empty() || val <= *L.rbegin()) {
                L.insert(val);
            } else {
                R.insert(val);
            }
            
            // REMOVE
            if (i >= w) {
                int out = arr[i - w];
                auto itL = L.find(out);
                if (itL != L.end()) {
                    L.erase(itL);
                } else {
                    auto itR = R.find(out);
                    if (itR != R.end()) R.erase(itR);
                }
            }
            
            // BALANCE
            while (L.size() < k && !R.empty()) {
                L.insert(*R.begin());
                R.erase(R.begin());
            }
            while (L.size() > k) {
                R.insert(*L.rbegin());
                L.erase(prev(L.end()));
            }
            
            if (i >= w - 1) {
                result.push_back(*L.rbegin());
            }
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, w, k;
    if (cin >> n >> w >> k) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        
        Solution solution;
        vector<int> result = solution.kthSmallestInWindows(arr, w, k);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
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

class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.heap = [];
    this.compare = compare;
  }
  size() { return this.heap.length; }
  isEmpty() { return this.heap.length === 0; }
  peek() { return this.heap[0]; }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.size() > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.compare(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = null;
      if (left < this.size() && this.compare(this.heap[left], this.heap[idx]) < 0) swap = left;
      if (right < this.size() && this.compare(this.heap[right], swap === null ? this.heap[idx] : this.heap[swap]) < 0) swap = right;
      if (swap === null) break;
      [this.heap[idx], this.heap[swap]] = [this.heap[swap], this.heap[idx]];
      idx = swap;
    }
  }
}

class Solution {
  kthSmallestInWindows(arr, w, k) {
    const n = arr.length;
    const result = [];
    
    // Max-Heap (Left)
    const left = new PriorityQueue((a, b) => b - a);
    // Min-Heap (Right)
    const right = new PriorityQueue((a, b) => a - b);
    
    const deleted = new Map();
    let leftSize = 0;
    let rightSize = 0;
    
    const clean = (pq) => {
      while (!pq.isEmpty()) {
        const val = pq.peek();
        if (deleted.has(val) && deleted.get(val) > 0) {
          pq.pop();
          deleted.set(val, deleted.get(val) - 1);
          if (deleted.get(val) === 0) deleted.delete(val);
        } else {
          break;
        }
      }
    };
    
    for (let i = 0; i < n; i++) {
      const val = arr[i];
      
      // ADD
      clean(left);
      if (left.isEmpty() || val <= left.peek()) {
        left.push(val);
        leftSize++;
      } else {
        right.push(val);
        rightSize++;
      }
      
      // REMOVE
      if (i >= w) {
        const out = arr[i - w];
        deleted.set(out, (deleted.get(out) || 0) + 1);
        
        clean(left);
        if (!left.isEmpty() && out <= left.peek()) {
          leftSize--;
        } else {
          rightSize--;
        }
      }
      
      // REBALANCE
      while (leftSize < k) {
        clean(right);
        if (right.isEmpty()) break;
        const v = right.pop();
        left.push(v);
        leftSize++;
        rightSize--;
      }
      
      while (leftSize > k) {
        clean(left);
        if (left.isEmpty()) break;
        const v = left.pop();
        right.push(v);
        leftSize--;
        rightSize++;
      }
      
      while (true) {
        clean(left);
        clean(right);
        if (left.isEmpty() || right.isEmpty()) break;
        if (left.peek() > right.peek()) {
          const l = left.pop();
          const r = right.pop();
          left.push(r);
          right.push(l);
        } else {
          break;
        }
      }
      
      if (i >= w - 1) {
        clean(left);
        result.push(left.peek());
      }
    }
    
    return result;
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
  const n = parseInt(data[idx++]);
  const w = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  const result = solution.kthSmallestInWindows(arr, w, k);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `arr=[1, 3, 2, 6, 4]`, `w=3`, `k=2`.

1. `i=0, val=1`: L=[1], R=[]. Sizes: 1, 0. (Need k=2).
2. `i=1, val=3`: L=[1], R=[3]. Rebalance: Move 3 to L? No, L.max < R.min.
   - Wait, `leftSize < k` (1 < 2). Move R top to L.
   - L=[3, 1], R=[]. Sizes: 2, 0.
3. `i=2, val=2`: L=[3, 1]. `2 < 3`. Insert to L. L=[3, 2, 1]. Sizes: 3, 0.
   - `leftSize > k` (3 > 2). Move L top (3) to R.
   - L=[2, 1], R=[3]. Sizes: 2, 1.
   - Output: L.peek() = 2.
4. `i=3, val=6`: Remove `arr[0]=1`.
   - `1 <= 2`. Decrement `leftSize` -> 1. Mark 1 deleted.
   - Add 6. `6 > 2`. Insert R. R=[3, 6]. Sizes: 1, 2.
   - Rebalance: `leftSize < k` (1 < 2). Move R top (3) to L.
   - L=[3, 2, (1 del)], R=[6]. Sizes: 2, 1.
   - Output: L.peek() = 3.
5. `i=4, val=4`: Remove `arr[1]=3`.
   - `3 <= 3`. Decrement `leftSize` -> 1. Mark 3 deleted.
   - Add 4. `4 > 3` (old peek). Insert R. R=[6, 4]. Sizes: 1, 2.
   - Rebalance: `leftSize < k`. Move R top (4) to L.
   - L=[4, 2, (1 del), (3 del)], R=[6]. Sizes: 2, 1.
   - Output: L.peek() = 4.

Result: `2, 3, 4`. Correct.

## ✅ Proof of Correctness

### Invariant
- `L` contains `k` valid elements. `R` contains `w-k` valid elements.
- `max(L) <= min(R)`.
- `L.peek()` is the k-th smallest element.
- Lazy deletion ensures amortized efficiency.

## 💡 Interview Extensions

- **Extension 1:** Stream of numbers?
  - *Answer:* Same logic, just no removal (or infinite window).
- **Extension 2:** Fractional K (e.g., median)?
  - *Answer:* Same logic, set `k = w/2`.

## Common Mistakes to Avoid

1. **Size Tracking**
   - ❌ Wrong: Using `heap.size()` which includes deleted elements.
   - ✅ Correct: Maintain explicit `validSize` counters.
2. **Lazy Deletion**
   - ❌ Wrong: Forgetting to clean heaps before peeking/popping.
   - ✅ Correct: Always `clean()` before accessing top.

## Related Concepts

- **Median of Medians:** Selection algorithm.
- **Two Heaps Pattern:** Standard for median maintenance.
