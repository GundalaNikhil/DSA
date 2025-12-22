---
title: Shuttle Validation with Time Windows
slug: shuttle-validation-time-windows
difficulty: Medium
difficulty_score: 61
tags:
- Stack
- Simulation
- Validation
problem_id: STK_SHUTTLE_VALIDATION_TIME_WINDOWS__2743
display_id: STK-014
topics:
- Stack
- Simulation
- Constraints
---
# Shuttle Validation with Time Windows - Editorial

## Problem Summary

Validate a stack push/pop sequence with two additional constraints:
1.  **Time Windows**: Certain elements must be popped within `W` time units of being pushed.
    -   "Each priority element is popped before any larger non-priority element".
    -   This phrasing is slightly ambiguous. Does it mean "If stack has Priority(5) and NonPriority(10), you cannot pop NonPriority(10) first"?
    -   Or does it mean "In the global pop sequence, all priority elements come before larger non-priority elements"?
    -   Given it's a stack problem, it likely refers to the state of the stack.
    -   "Each priority element is popped before any larger non-priority element".
    -   This implies: At the moment of popping a Non-Priority element `X`, there should be NO Priority element `P` in the stack such that `P < X`.
    -   If `P` is popped *before* `X`, that satisfies the condition.
    -   If `X` is popped *before* `P`, and `X > P`, then a larger non-priority was popped before a priority element. This violates the rule.
    -   So the rule is: **You cannot pop a Non-Priority element `X` if there exists a Priority element `P` in the stack such that `X > P`**.
    -   Basically, priority elements block larger non-priority elements from being popped.

## Real-World Scenario

Imagine a **Space Shuttle Cargo Bay**.
-   **Stack**: Cargo is loaded (pushed) and unloaded (popped) in LIFO order.
-   **Time Windows**: Some perishable items (e.g., food, biological samples) must be unloaded within `W` hours of loading, or they spoil.
-   **Priority**: Some items are "High Priority" (e.g., emergency medical supplies).
-   **Rule**: You shouldn't unload a large, low-priority crate if there's a small, high-priority box buried deeper?
    -   So if the top is Low-Priority Large, and below it is High-Priority Small, you *must* unload the top first to get to the bottom.
    -   This implies the *Push Sequence* itself must have been organized such that this situation doesn't arise, OR the Pop Sequence is invalid if it tries to pop the large one while the small one is waiting?
    -   It means the loading/unloading plan was flawed.

## Problem Exploration

### 1. Stack Simulation
-   Standard "Validate Stack Sequences" logic:
    -   Iterate through `pushed` array.
    -   Push `pushed[i]`.
    -   While `stack.top() == popped[j]`:
        -   Pop from stack.
        -   `j++`.
-   If stack is empty at the end, the sequence is valid (structurally).

### 2. Time Window Constraint
-   We are given `pushTimes` and `popTimes`.
-   When we push `x` at `pushT`, we store `(x, pushT)`.
-   When we pop `x` at `popT`, we check if `x` has a window `W`.
-   Condition: `popT - pushT <= W`.
-   If not, return `false`.

### 3. Priority Constraint
-   Rule: "Each priority element is popped before any larger non-priority element".
-   Equivalent to: At the time of popping a Non-Priority element `X`, there must be NO Priority element `P` currently in the stack such that `P < X`.
-   If there is such a `P`, then `X` is being popped *before* `P`, and `X > P`. Violation.
-   So, whenever we pop a Non-Priority element `X`, we must check the stack for any `P < X`.
-   Checking the entire stack is `O(N)` per pop -> `O(N^2)`. We need faster.
-   We need to know the **Minimum Priority Element** currently in the stack.
-   Let `min_priority` be the smallest value among all priority items currently in the stack.
-   If `X` is Non-Priority and `X > min_priority`, then Invalid.
-   We need to maintain `min_priority` efficiently.
-   Since it's a stack, we can use an auxiliary **Min-Stack** that tracks the minimum priority value.
-   Let `aux` stack store `min_priority_so_far`.
-   When pushing `val`:
    -   If `val` is Priority: `new_min = min(val, current_min)`.
    -   If `val` is Non-Priority: `new_min = current_min`.
    -   Push `new_min` to `aux`.
-   When popping:
    -   Pop from `aux`.
-   Check: If popping Non-Priority `X`, check `aux.peek()`.
    -   We need the min priority of the *remaining* elements?
    -   No, the rule applies "before any larger non-priority element".
    -   If `X` is the top, and `P` is below it. `X` is popped first.
    -   So we check if `X > min_priority_in_stack`.
    -   Does `min_priority_in_stack` include `X`?
    -   If `X` is Non-Priority, it doesn't affect the min priority set.
    -   So yes, `aux.peek()` (which tracks min priority of elements up to top) works.
    -   Since `X` is Non-Priority, `aux.peek()` is exactly the min priority of elements below `X` (and `X` itself is ignored by the min-tracker).
    -   Yes.
    -   So:
        -   `push(val)`:
            -   `prev_min = aux.isEmpty() ? infinity : aux.peek()`
            -   `curr_min = isPriority(val) ? min(val, prev_min) : prev_min`
            -   `aux.push(curr_min)`
        -   `pop(val)`:
            -   If `!isPriority(val)`:
                -   `min_p = aux.peek()`
                -   If `val > min_p`: return `false`.
            -   `aux.pop()`

## Approaches

### Approach 1: Simulation with Auxiliary Min-Stack
-   Use a main stack for simulation.
-   Use an auxiliary stack to track the minimum priority element currently in the stack.
-   Check time constraints on pop.
-   Check priority constraints on pop.
-   Complexity: `O(N)` time, `O(N)` space.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public boolean validate(int[] push, long[] pushT, int[] pop, long[] popT, Map<Integer, Long> windows, Set<Integer> priority) {
        int n = push.length;
        Stack<Integer> stack = new Stack<>();
        Stack<Long> timeStack = new Stack<>();
        Stack<Integer> minPriorityStack = new Stack<>();
        
        int j = 0;
        for (int i = 0; i < n; i++) {
            int val = push[i];
            long time = pushT[i];
            
            stack.push(val);
            timeStack.push(time);
            
            int currentMin = minPriorityStack.isEmpty() ? Integer.MAX_VALUE : minPriorityStack.peek();
            if (priority.contains(val)) {
                currentMin = Math.min(currentMin, val);
            }
            minPriorityStack.push(currentMin);
            
            while (!stack.isEmpty() && j < n && stack.peek() == pop[j]) {
                int poppedVal = stack.pop();
                long pushedTime = timeStack.pop();
                minPriorityStack.pop(); // Remove current state
                
                long poppedTime = popT[j];
                
                // Check 1: Time Window
                if (windows.containsKey(poppedVal)) {
                    if (poppedTime - pushedTime > windows.get(poppedVal)) {
                        return false;
                    }
                }
                
                // Check 2: Priority
                // If poppedVal is Non-Priority, it must not be larger than any existing Priority
                if (!priority.contains(poppedVal)) {
                    int minP = minPriorityStack.isEmpty() ? Integer.MAX_VALUE : minPriorityStack.peek();
                    if (poppedVal > minP) {
                        return false;
                    }
                }
                
                j++;
            }
        }
        
        return stack.isEmpty();
    }
}
```

### Python

```python
def validate(push, push_t, pop, pop_t, windows, priority) -> bool:
    stack = []
    time_stack = []
    min_priority_stack = []
    
    j = 0
    n = len(push)
    
    for i in range(n):
        val = push[i]
        t = push_t[i]
        
        stack.append(val)
        time_stack.append(t)
        
        current_min = min_priority_stack[-1] if min_priority_stack else float('inf')
        if val in priority:
            current_min = min(current_min, val)
        min_priority_stack.append(current_min)
        
        while stack and j < n and stack[-1] == pop[j]:
            popped_val = stack.pop()
            pushed_time = time_stack.pop()
            min_priority_stack.pop()
            
            popped_time = pop_t[j]
            
            # Check Time Window
            if popped_val in windows:
                if popped_time - pushed_time > windows[popped_val]:
                    return False
            
            # Check Priority
            if popped_val not in priority:
                min_p = min_priority_stack[-1] if min_priority_stack else float('inf')
                if popped_val > min_p:
                    return False
            
            j += 1
            
    return not stack
```

### C++

```cpp
#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    bool validate(const vector<int>& push, const vector<long long>& pushT, const vector<int>& pop, const vector<long long>& popT,
                  const unordered_map<int,long long>& windows, const unordered_set<int>& priority) {
        int n = push.size();
        stack<int> s;
        stack<long long> timeStack;
        stack<int> minPriorityStack;
        
        int j = 0;
        for (int i = 0; i < n; i++) {
            int val = push[i];
            long long time = pushT[i];
            
            s.push(val);
            timeStack.push(time);
            
            int currentMin = minPriorityStack.empty() ? INT_MAX : minPriorityStack.top();
            if (priority.count(val)) {
                currentMin = min(currentMin, val);
            }
            minPriorityStack.push(currentMin);
            
            while (!s.empty() && j < n && s.top() == pop[j]) {
                int poppedVal = s.top(); s.pop();
                long long pushedTime = timeStack.top(); timeStack.pop();
                minPriorityStack.pop();
                
                long long poppedTime = popT[j];
                
                // Check Time
                if (windows.count(poppedVal)) {
                    if (poppedTime - pushedTime > windows.at(poppedVal)) {
                        return false;
                    }
                }
                
                // Check Priority
                if (!priority.count(poppedVal)) {
                    int minP = minPriorityStack.empty() ? INT_MAX : minPriorityStack.top();
                    if (poppedVal > minP) {
                        return false;
                    }
                }
                
                j++;
            }
        }
        
        return s.empty();
    }
};
```

### JavaScript

```javascript
class Solution {
  validate(push, pushT, pop, popT, windows, priority) {
    const n = push.length;
    const stack = [];
    const timeStack = [];
    const minPriorityStack = [];
    
    let j = 0;
    
    for (let i = 0; i < n; i++) {
      const val = push[i];
      const time = pushT[i];
      
      stack.push(val);
      timeStack.push(time);
      
      let currentMin = minPriorityStack.length === 0 ? Infinity : minPriorityStack[minPriorityStack.length - 1];
      if (priority.has(val)) {
        currentMin = Math.min(currentMin, val);
      }
      minPriorityStack.push(currentMin);
      
      while (stack.length > 0 && j < n && stack[stack.length - 1] === pop[j]) {
        const poppedVal = stack.pop();
        const pushedTime = timeStack.pop();
        minPriorityStack.pop();
        
        const poppedTime = popT[j];
        
        // Check Time
        if (windows.has(poppedVal)) {
          if (poppedTime - pushedTime > windows.get(poppedVal)) {
            return false;
          }
        }
        
        // Check Priority
        if (!priority.has(poppedVal)) {
          const minP = minPriorityStack.length === 0 ? Infinity : minPriorityStack[minPriorityStack.length - 1];
          if (poppedVal > minP) {
            return false;
          }
        }
        
        j++;
      }
    }
    
    return stack.length === 0;
  }
}
```

## Test Case Walkthrough

**Input:**
-   Push: `4 5 6`, Times: `0 2 4`
-   Pop: `6 5 4`, Times: `5 6 10`
-   Window: `5` -> `2`
-   Priority: `4`

1.  Push `4` (t=0). Priority. MinP=`4`. Stack `[4]`.
2.  Push `5` (t=2). Non-P. MinP=`4`. Stack `[4, 5]`.
3.  Push `6` (t=4). Non-P. MinP=`4`. Stack `[4, 5, 6]`.
4.  Pop `6` (t=5).
    -   Window: None.
    -   Priority: `6` is Non-P. Check `MinP` below. Stack below has `[4, 5]`. MinP is `4`.
    -   `6 > 4`. **Violation!**
    -   Return `false`.

**Wait**, the example output says `false` due to **Time Window**.
"Value 5 must be popped within 2 time units... popped at time 6".
My trace found a Priority violation first.
Let's re-read the priority rule.
"Each priority element is popped before any larger non-priority element".
My interpretation: `6` (Non-P) popped. `4` (Priority) is in stack. `6 > 4`. So `4` is popped *after* `6`.
This violates "Priority popped before larger non-priority".
So my priority check is correct.
However, the example explanation focuses on the time window.
Maybe `4` is NOT priority?
Input: `1 \n 4`. Yes, `4` is priority.
Maybe `6` is not larger than `4`? `6 > 4`. Yes.
Why does the example explanation ignore the priority violation?
Maybe the check order matters? Or maybe my priority logic is too strict?
"Each priority element is popped before any larger non-priority element".
If `4` is in stack and `6` is popped. `4` is popped later. `4` is priority. `6` is larger non-priority.
So `4` is popped *after* larger non-priority.
This violates "popped before".
So yes, it fails priority check too.
The example explanation just picked the time window failure. Both are valid reasons for `false`.
Let's check the time window failure.
Pop `6`. Valid (no window).
Pop `5`. Window `2`. Push `2`. Pop `6`. Diff `4`. `4 > 2`. Fail.
So `5` fails time window.
My code would return `false` at `6` (priority) or `5` (time). Both correct.

## Proof of Correctness

-   **Structure**: Standard simulation ensures LIFO validity.
-   **Time**: Direct check `pop - push <= W`.
-   **Priority**: The Min-Stack invariant correctly tracks the minimum priority value *currently waiting* in the stack. If we pop a larger non-priority value, we confirm a priority value is still waiting, which violates the ordering rule.

## Interview Extensions

1.  **Multiple Priority Levels**: What if priority is 1-10?
    -   *Hint*: "Higher priority popped before lower priority". Similar logic, check `max_priority_below > current_priority`.
2.  **Online Validation**: Stream of operations.
    -   *Hint*: Same logic works online.

### Common Mistakes

-   **Min Stack Update**: Forgetting to pop from `minPriorityStack` when popping from main stack.
-   **Priority Logic**: Checking `val > minP` for *priority* elements too (only non-priority are restricted).
-   **Time Units**: Mixing up push/pop times.
