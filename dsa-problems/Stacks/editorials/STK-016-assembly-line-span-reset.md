---
title: Assembly Line Span Reset
slug: assembly-line-span-reset
difficulty: Medium
difficulty_score: 45
tags:
- Stack
- Monotonic Stack
- Spans
problem_id: STK_ASSEMBLY_LINE_SPAN_RESET__3846
display_id: STK-016
topics:
- Stack
- Spans
- Arrays
---
# Assembly Line Span Reset - Editorial

## Problem Summary

For each day `i`, calculate the "span" of production counts. The span is the number of consecutive days ending at `i` (including `i` itself) where the production count was **strictly less** than `count[i]`.
"compute for each day the span of consecutive prior days with counts strictly less than today's count. The span includes today as 1."
Example: `2 1 3 2 5`.
-   Day 0 (2): Span 1 (itself).
-   Day 1 (1): Span 1 (itself).
-   Day 2 (3): Prior days `1` (<3), `2` (<3). Span 3 (itself + 1 + 2).
-   Day 3 (2): Prior day `3` (not < 2). Span 1 (itself).
-   Day 4 (5): Prior `2` (<5), `3` (<5), `1` (<5), `2` (<5). Span 5.
-   For Day 3 (2): Prior is `3`. `3` is not `< 2`. So span stops. Correct.
-   For Day 4 (5): Prior `2` (<5). Before that `3` (<5). Before that `1` (<5). Before that `2` (<5). All consecutive prior days are `< 5`. Correct.


## Constraints

- `1 <= n <= 100000`
- `0 <= count[i] <= 10^9`
## Real-World Scenario

Imagine an **Assembly Line Performance Tracker**.
-   You track daily output.
-   You want to know "How long has it been since we performed *at least as well* as today?"
-   If today is a record high relative to the last `k` days, then `k+1` is your span.
-   This helps identify local peaks in performance. "Today is the best day in the last 5 days!"

## Problem Exploration

### 1. Stock Span Problem
-   This is exactly the **Stock Span Problem**.
-   Standard definition: Span of day `i` is max number of consecutive days ending at `i` such that `price[day] <= price[i]`.
-   Our Problem: `count[day] < count[i]`.
-   Difference: Strictly less vs Less than or equal.
-   Logic remains identical, just the comparison operator changes.

### 2. Monotonic Stack
-   We need to find the nearest previous day `j` such that `count[j] >= count[i]`.
-   The span is then `i - j`.
-   If no such day exists, `j = -1`. Span `i - (-1) = i + 1`.
-   We maintain a stack of indices `j` such that `count[j]` is decreasing (or non-increasing).
-   So the stack will store indices of elements that are `>=` the current element (candidates for future blocking).
-   Example: `2 1 3`.
    -   `2`: Stack `[0]`.
    -   `1`: `1 < 2`. Push 1. Stack `[0, 1]`.
    -   `3`: `3 > 1` (pop 1). `3 > 2` (pop 0). Stack empty. Push 2. Stack `[2]`.
-   Yes, this maintains a decreasing stack.

### 3. Algorithm
-   Initialize `stack` (indices).
-   Iterate `i` from `0` to `n-1`.
-   While `stack` not empty and `count[stack.peek()] < count[i]`:
    -   `stack.pop()`
-   If `stack` empty: `span = i + 1`.
-   Else: `span = i - stack.peek()`.
-   `stack.push(i)`.

## Approaches

### Approach 1: Monotonic Stack
-   Standard solution.
-   Complexity: `O(N)` time, `O(N)` space.

## Implementations

### Java
```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] spans(int[] counts) {
        int n = counts.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && counts[stack.peek()] < counts[i]) {
                stack.pop();
            }
            
            if (stack.isEmpty()) {
                result[i] = i + 1;
            } else {
                result[i] = i - stack.peek();
            }
            stack.push(i);
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        
        int n = Integer.parseInt(line.trim());
        
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        while (list.size() < n) {
            while (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (!st.hasMoreTokens()) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] counts = new int[list.size()];
        for(int i=0; i<list.size(); i++) counts[i] = list.get(i);
        
        Solution sol = new Solution();
        int[] res = sol.spans(counts);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
```

### Python
```python
def spans(counts: list[int]) -> list[int]:
    n = len(counts)
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and counts[stack[-1]] < counts[i]:
            stack.pop()
            
        if not stack:
            result[i] = i + 1
        else:
            result[i] = i - stack[-1]
            
        stack.append(i)
        
    return result


def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    counts = list(map(int, lines[1].split()))
    result = spans(counts)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> spans(vector<int>& counts) {
        int n = counts.size();
        vector<int> result(n);
        stack<int> stack;
        
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && counts[stack.top()] < counts[i]) {
                stack.pop();
            }
            
            if (stack.empty()) {
                result[i] = i + 1;
            } else {
                result[i] = i - stack.top();
            }
            stack.push(i);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> counts(n);
    for (int i = 0; i < n; i++) {
        cin >> counts[i];
    }
    
    Solution sol;
    vector<int> res = sol.spans(counts);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
```

### JavaScript
```javascript
class Solution {
  spans(counts) {
    const n = counts.length;
    const result = new Int32Array(n);
    const stack = [];
    
    for (let i = 0; i < n; i++) {
      while (stack.length > 0 && counts[stack[stack.length - 1]] < counts[i]) {
        stack.pop();
      }
      
      if (stack.length === 0) {
        result[i] = i + 1;
      } else {
        result[i] = i - stack[stack.length - 1];
      }
      stack.push(i);
    }
    return Array.from(result);
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const counts = [];
  for (let i = 0; i < n; i++) {
    counts.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.spans(counts);
  console.log(res.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `2 1 3 2 5`

1.  `i=0 (2)`: Stack empty. `res=1`. Push 0. Stack `[0]`.
2.  `i=1 (1)`: `1 < 2`. `res=1-0=1`. Push 1. Stack `[0, 1]`.
3.  `i=2 (3)`: `3 > 1` (pop 1). `3 > 2` (pop 0). Empty. `res=3`. Push 2. Stack `[2]`.
4.  `i=3 (2)`: `2 < 3`. `res=3-2=1`. Push 3. Stack `[2, 3]`.
5.  `i=4 (5)`: `5 > 2` (pop 3). `5 > 3` (pop 2). Empty. `res=5`. Push 4. Stack `[4]`.

**Result:** `1 1 3 1 5`. Matches example.

## Proof of Correctness

-   **Invariant**: Stack stores indices of elements that are strictly greater than or equal to the current element's predecessors.
-   **Nearest Greater or Equal**: By popping smaller elements, we find the nearest element to the left that is `>=` current. This bounds the span of strictly smaller elements.

## Interview Extensions

1.  **Online Stock Span**: Implement `next(price)` class.
    -   *Hint*: Store `(price, span)` pairs in stack. If `price >= top.price`, pop and add `top.span` to current span.
2.  **Daily Temperatures**: Find days until warmer.
    -   *Hint*: Same logic, but look forward (or iterate backwards).

### Common Mistakes

-   **Comparison**: Using `<=` instead of `<` (or vice versa) depending on problem statement. Here "strictly less" means we stop at `>=`.
-   **Index Math**: `i - stack.peek()` vs `i - stack.peek() - 1`. Since span includes today, `i - prev_index` is correct. (e.g., indices 2 and 3. Span is 1. `3-2=1`).
