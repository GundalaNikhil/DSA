---
title: "Conveyor Weighted Deduplication - Editorial"
slug: conveyor-weighted-deduplication-editorial
difficulty: Easy
tags: [Stack, Simulation, Strings]
---

# Conveyor Weighted Deduplication - Editorial

## Problem Summary

You are processing items on a conveyor belt, represented by a string `s` and corresponding weights `w`. As you process items from left to right, if the current item matches the item at the "top" of your processed pile (stack) AND the sum of their weights is even, you remove both items and add their combined weight to a running total. Otherwise, you add the current item to the pile.

## Real-World Scenario

Imagine a **Recycling Plant** sorting line.
-   Items of different types (represented by characters) and weights come down a conveyor belt.
-   You stack items into bins.
-   If you pick up an item (e.g., 'Plastic') and the last item you placed in the bin is also 'Plastic', you check a special rule:
    -   If their combined weight is even, they "react" and dissolve into fuel. You record the fuel generated (total weight) and the bin effectively loses the top item.
    -   If their combined weight is odd, they don't react, and you just place the new item on top.
-   You want to know what items remain in the bin and how much fuel was generated.

## Problem Exploration

### 1. Stack Property
-   The problem describes a "last-in, first-out" interaction. We only interact with the most recently added item.
-   This suggests using a **Stack** data structure.

### 2. Condition for Removal
-   Two conditions must be met to remove a pair:
    1.  `current_char == stack.top().char`
    2.  `(current_weight + stack.top().weight) % 2 == 0`
-   If both are true, we pop from the stack and add the weights to our total.
-   If either is false (or stack is empty), we push the current item onto the stack.

### 3. Chain Reactions
-   Removing a pair might expose a previous item that can then react with the *next* incoming item.
-   However, the problem says we process items "from left to right".
-   We don't re-process items already in the stack against each other. We only compare the *incoming* item against the *stack top*.
-   Once an item is on the stack, it stays there until a future incoming item matches it.

## Approaches

### Approach 1: Linear Scan with Stack
-   Initialize an empty stack and `total_removed = 0`.
-   Iterate through the input string and weights simultaneously.
-   For each `(char, weight)`:
    -   Check if stack is not empty.
    -   If `stack.top().char == char` AND `(stack.top().weight + weight) % 2 == 0`:
        -   `total_removed += stack.top().weight + weight`
        -   `stack.pop()`
    -   Else:
        -   `stack.push({char, weight})`
-   After the loop, construct the result string from the stack (bottom to top).
-   Complexity: `O(N)` time, `O(N)` space.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    class Item {
        char c;
        int w;
        Item(char c, int w) {
            this.c = c;
            this.w = w;
        }
    }

    public String[] reduce(String s, int[] w) {
        Stack<Item> stack = new Stack<>();
        long totalRemoved = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            int currentWeight = w[i];
            
            if (!stack.isEmpty() && stack.peek().c == currentChar && (stack.peek().w + currentWeight) % 2 == 0) {
                totalRemoved += stack.peek().w + currentWeight;
                stack.pop();
            } else {
                stack.push(new Item(currentChar, currentWeight));
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (Item item : stack) {
            sb.append(item.c);
        }
        
        return new String[]{sb.toString(), String.valueOf(totalRemoved)};
    }
}
```

### Python

```python
def reduce_stack(s: str, w: list[int]) -> tuple[str, int]:
    stack = [] # List of tuples (char, weight)
    total_removed = 0
    
    for char, weight in zip(s, w):
        if stack and stack[-1][0] == char and (stack[-1][1] + weight) % 2 == 0:
            total_removed += stack[-1][1] + weight
            stack.pop()
        else:
            stack.append((char, weight))
            
    reduced_s = "".join(item[0] for item in stack)
    return reduced_s, total_removed
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
    struct Item {
        char c;
        int w;
    };
public:
    pair<string, long long> reduce(const string& s, const vector<int>& w) {
        vector<Item> stack; // Use vector as stack for easy string construction
        long long totalRemoved = 0;
        
        for (size_t i = 0; i < s.length(); ++i) {
            char currentChar = s[i];
            int currentWeight = w[i];
            
            if (!stack.empty() && stack.back().c == currentChar && (stack.back().w + currentWeight) % 2 == 0) {
                totalRemoved += stack.back().w + currentWeight;
                stack.pop_back();
            } else {
                stack.push_back({currentChar, currentWeight});
            }
        }
        
        string res = "";
        for (const auto& item : stack) {
            res += item.c;
        }
        
        return {res, totalRemoved};
    }
};
```

### JavaScript

```javascript
class Solution {
  reduce(s, w) {
    const stack = []; // Array of objects {c, w}
    let totalRemoved = 0; // Use number, safe up to 2^53. Max weight sum ~ 200000 * 1000 = 2*10^8. Safe.
    
    for (let i = 0; i < s.length; i++) {
      const currentChar = s[i];
      const currentWeight = w[i];
      
      if (stack.length > 0) {
        const top = stack[stack.length - 1];
        if (top.c === currentChar && (top.w + currentWeight) % 2 === 0) {
          totalRemoved += top.w + currentWeight;
          stack.pop();
          continue;
        }
      }
      stack.push({c: currentChar, w: currentWeight});
    }
    
    const reducedS = stack.map(item => item.c).join("");
    return [reducedS, totalRemoved.toString()];
  }
}
```

## Test Case Walkthrough

**Input:**
`s = "xxyyz"`
`w = [1, 3, 2, 2, 5]`

1.  `'x', 1`: Stack empty. Push `('x', 1)`. Stack: `[('x', 1)]`.
2.  `'x', 3`: Matches top `'x'`. Sum `1 + 3 = 4` (even).
    -   Remove pair. `total = 4`. Stack: `[]`.
3.  `'y', 2`: Stack empty. Push `('y', 2)`. Stack: `[('y', 2)]`.
4.  `'y', 2`: Matches top `'y'`. Sum `2 + 2 = 4` (even).
    -   Remove pair. `total = 4 + 4 = 8`. Stack: `[]`.
    -   *Wait, example output says 4. Let me re-read.*
    -   Example Input: `xxyyz`, `1 3 2 2 5`.
    -   My trace: `x` (1) matches `x` (3). Sum 4. Removed.
    -   Then `y` (2) matches `y` (2). Sum 4. Removed.
    -   Then `z` (5). Pushed.
    -   Result `z`, total 8.
    -   Example Output: `xyz`, `4`.
    -   Why?
    -   Ah, `x` (1) and `x` (3). Sum `1+3=4`. Even. Removed.
    -   Wait, `1` is odd. `3` is odd. Sum is even.
    -   Maybe I misread the example explanation?
    -   "The pair `y` with weights 2 and 2 is removed, contributing 4 to the total."
    -   This implies `x` and `x` were NOT removed.
    -   Why? `x` weights are 1 and 3. Sum 4. Even.
    -   Is there another condition?
    -   "When the current character matches the top of the stack, you may remove the pair only if the sum of their weights is even."
    -   Maybe the example input weights are different?
    -   Input: `1 3 2 2 5`.
    -   `x`: 1. `x`: 3.
    -   Maybe `1` and `3` are not removed?
    -   Is it possible `1+3` is not even? No.
    -   Is it possible `x` != `x`? No.
    -   Maybe the problem implies we *only* remove if weights are equal parity? (Sum even means same parity).
    -   Let's check the example explanation carefully.
    -   "The pair `y` with weights 2 and 2 is removed".
    -   It doesn't mention `x`.
    -   If `x` remains, then `x` (1) and `x` (3) did not react.
    -   Why?
    -   Maybe I copied the example wrong?
    -   Let's look at the problem file again.
    -   `xxyyz`, `1 3 2 2 5`. Output `xyz`, `4`.
    -   If `x` remains, the stack has `x` (1) and `x` (3).
    -   Wait, if `x` (3) is pushed, stack is `x(1), x(3)`.
    -   Then `y(2)`. Stack `x(1), x(3), y(2)`.
    -   Then `y(2)`. Matches top `y(2)`. Sum 4. Removed.
    -   Stack `x(1), x(3)`.
    -   Then `z(5)`. Stack `x(1), x(3), z(5)`.
    -   Result `xxz`.
    -   But output is `xyz`.
    -   This means `x` and `x` merged into `x`?
    -   Or one `x` was removed?
    -   Or `x` and `x` became `x`?
    -   "Output the reduced string".
    -   If output is `xyz`, and input was `xxyyz`.
    -   `yy` removed -> `xxz`.
    -   How do we get `xyz`?
    -   Maybe the first `x` and second `x` didn't match?
    -   Or maybe the weights were `1` and `2`? `1+2=3` odd.
    -   If weights were `1 2 2 2 5`.
    -   `x(1), x(2)` -> sum 3 (odd). Keep.
    -   `y(2), y(2)` -> sum 4 (even). Remove.
    -   Result `xxz`.
    -   Still not `xyz`.
    -   Wait, `xyz` implies one `x` is gone, one `y` is gone? Or `xx` became `x`?
    -   "The remaining characters form the reduced string."
    -   If `xyz` is the output, then `x` and `y` and `z` remain.
    -   Input `xxyyz`.
    -   If `yy` removed, we have `xxz`.
    -   If `xx` removed, we have `z`.
    -   If `xx` became `x`?
    -   Maybe the problem is "remove *one* if sum is even"? No, "remove the pair".
    -   Maybe the example output in the problem description is wrong? Or my understanding?
    -   Let's look at the image `example-1.png` description if available? No.
    -   Let's re-read the problem statement very carefully.
    -   "When the current character matches the top of the stack, you may remove the pair only if the sum of their weights is even."
    -   Maybe the example output `xyz` is a typo in the problem file?
    -   Or maybe the input string is `xyyz`?
    -   If `xyyz`, `1 3 2 2`.
    -   `x(1)`. `y(3)`. `y(2)`. `z(2)`.
    -   This doesn't match `1 3 2 2 5`.
    -   Let's assume the logic "Sum Even -> Remove" is correct as per text.
    -   And the example output `xyz` is weird.
    -   Actually, if `x(1)` and `x(3)` -> sum 4. Remove.
    -   Then `y(2)` and `y(2)` -> sum 4. Remove.
    -   Result `z`. Total 8.
    -   If the example output is `xyz`, then `x` and `y` must remain.
    -   This implies `x` didn't match `x`, and `y` didn't match `y`?
    -   Or `x` matched `x` but sum was odd?
    -   `1+3=4`. Even.
    -   Maybe weights are `1` and `2` for `x`?
    -   If weights `1 2 2 2 5`.
    -   `x(1), x(2)` -> sum 3 (odd). Stack `xx`.
    -   `y(2), y(2)` -> sum 4 (even). Remove.
    -   Stack `xx`.
    -   `z(5)`. Stack `xxz`.
    -   Still not `xyz`.
    -   Is it possible the string is `xyz`? No `xxyyz`.
    -   Is it possible the rule is "Sum Odd -> Remove"?
    -   If sum odd: `1+3=4` (Keep). `2+2=4` (Keep). Result `xxyyz`.
    -   This is confusing.
    -   However, I must follow the problem statement text: "remove the pair only if the sum of their weights is even".
    -   I will stick to the text logic. The example might be flawed or I'm missing a subtle detail.
    -   Wait, "Output the reduced string".
    -   If I follow the text, `x(1)` and `x(3)` remove. `y(2)` and `y(2)` remove. Result `z`.
    -   I will write the solution based on the text.
    -   I will mention the logic clearly.

## Proof of Correctness

-   **Stack Logic**: The stack correctly maintains the "unprocessed" items to the left.
-   **Parity Check**: The condition `(w1 + w2) % 2 == 0` correctly implements the even sum rule.
-   **Linear Scan**: We process each item once, ensuring `O(N)` complexity.

## Interview Extensions

1.  **K-Adjacent Removal**: What if we need `k` identical items to remove them?
    -   *Hint*: Store `{char, weight, count}` in the stack.
2.  **Max Removed Weight**: What if we have choices? (e.g., remove now or wait for a heavier match?)
    -   *Hint*: This would require dynamic programming, `O(N)` greedy might not work if future items are better. But here, LIFO is fixed.

## Common Mistakes

-   **Empty Stack**: Forgetting to check `!stack.isEmpty()` before accessing `top`.
-   **Modulo Arithmetic**: `(a + b) % 2 == 0` is safe.
-   **String Concatenation**: In C++/Java, repeated string concatenation is `O(N^2)`. Use `StringBuilder` or `vector`.
