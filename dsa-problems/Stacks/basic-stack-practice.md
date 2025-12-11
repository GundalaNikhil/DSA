# Basic Stack Practice Set (15-18 Questions)

## 1) Notebook Undo Simulator
- Slug: notebook-undo-simulator
- Difficulty: Easy
- Problem: Implement a simple stack that supports `PUSH x`, `POP`, and `TOP` commands for a text editor undo buffer. Return the top element after each command that is not `PUSH`.
- Constraints: `1 <= m <= 10^5` commands, `-10^9 <= x <= 10^9`.
- Hint: Use an array-backed stack; check for empty before `POP`/`TOP`.
- Example 1:
  - Input: `["PUSH 10", "PUSH -1", "TOP", "POP", "TOP"]`
  - Output: `[-1, 10]`
- Example 2:
  - Input: `["POP", "TOP"]`
  - Output: `["EMPTY", "EMPTY"]`

## 2) Lab Mixed Bracket Repair
- Slug: lab-mixed-bracket-repair
- Difficulty: Easy-Medium
- Problem: The string contains characters from `()[]{}` and wildcard `?`. You may replace each `?` with any single bracket character. Decide if it is possible to replace all `?` so the final string is balanced and well-nested.
- Constraints: `1 <= len(s) <= 10^5`, number of `?` <= `10^5`.
- Hint: Use a stack for structure plus a greedy check on available `?` to balance closings; track unmatched openings and remaining wildcards.
- Example 1:
  - Input: `"(?[?])?"`
  - Output: `true` (replace with `"([][])")
- Example 2:
  - Input: `")?(("`
  - Output: `false`

## 3) Conveyor Deduplication
- Slug: conveyor-deduplication
- Difficulty: Easy
- Problem: Given a string, repeatedly remove adjacent equal characters until no such pair remains. Return the reduced string.
- Constraints: `1 <= len(s) <= 2 * 10^5`.
- Hint: Stack characters; pop when the incoming char matches the top.
- Example 1:
  - Input: `"xxyyz"`
  - Output: `"z"`
- Example 2:
  - Input: `"abbaac"`
  - Output: `"c"`

## 4) Rooftop Sunset Count
- Slug: rooftop-sunset-count
- Difficulty: Easy-Medium
- Problem: Given building heights from west to east, count how many buildings can see the sunset looking west (no taller building to their left).
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= h[i] <= 10^9`.
- Hint: Monotonic decreasing stack of heights; pop while current is taller.
- Example 1:
  - Input: `[5, 4, 3, 2]`
  - Output: `4`
- Example 2:
  - Input: `[2, 5, 2, 6, 1]`
  - Output: `3`

## 5) Workshop Next Taller
- Slug: workshop-next-taller
- Difficulty: Easy-Medium
- Problem: For each machine height, find the next taller height to its right; output -1 if none exists.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= h[i] <= 10^9`.
- Hint: Traverse from right; maintain monotonic decreasing stack.
- Example 1:
  - Input: `[1, 7, 3, 4, 2]`
  - Output: `[7, -1, 4, -1, -1]`
- Example 2:
  - Input: `[9, 8, 8]`
  - Output: `[-1, -1, -1]`

## 6) Assembly Previous Greater
- Slug: assembly-previous-greater
- Difficulty: Easy-Medium
- Problem: For each element, find the nearest greater element to its left; output -1 if none.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Sweep left to right with a decreasing stack of values.
- Example 1:
  - Input: `[2, 9, 5, 7, 3]`
  - Output: `[-1, -1, 9, 9, 7]`
- Example 2:
  - Input: `[1, 1, 1]`
  - Output: `[-1, -1, -1]`

## 7) Trading Desk Threshold Jump
- Slug: trading-desk-threshold-jump
- Difficulty: Medium
- Problem: Given intraday prices and a threshold `t`, for each price find how many steps forward until you see a price at least `t` units higher; output 0 if none exists.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= price[i], t <= 10^9`.
- Hint: Monotonic stack but compare `price[next] - price[i] >= t`; pop while current price is too small to help prior items.
- Example 1:
  - Input: `prices = [3, 1, 4, 6, 5], t = 2`
  - Output: `[2, 1, 1, 0, 0]`
- Example 2:
  - Input: `prices = [10, 9, 8], t = 1`
  - Output: `[0, 0, 0]`

## 8) Canteen Token Climb Span
- Slug: canteen-token-climb-span
- Difficulty: Medium
- Problem: For each day's canteen demand, compute how many consecutive prior days (not including today) had demand strictly lower than today; if any of those prior days equals today’s demand, the span resets to zero. Return the span count (not including today).
- Constraints: `1 <= n <= 10^5`, `0 <= demand[i] <= 10^9`.
- Hint: Use a strictly increasing monotonic stack of (value, index); pop while lower, reset to 0 if equal encountered.
- Example 1:
  - Input: `[3, 1, 2, 2, 5]`
  - Output: `[0, 0, 1, 0, 4]`
- Example 2:
  - Input: `[1, 3, 3, 2]`
  - Output: `[0, 1, 0, 0]`

## 9) Lab Sliding-Min Stack
- Slug: lab-sliding-min-stack
- Difficulty: Medium
- Problem: Support `PUSH x`, `POP`, and queries `MIN k` that ask for the minimum among the top `k` elements currently in the stack (counting the top as 1). If the stack has fewer than `k` elements, return `"NA"`.
- Constraints: `1 <= m <= 10^5` operations, `1 <= k <= 10^5`, values are 32-bit signed ints.
- Hint: Maintain a stack of values and an auxiliary stack of monotonic mins with counts so you can roll back pops and handle window size `k`.
- Example 1:
  - Input: `["PUSH 5","PUSH 1","PUSH 3","MIN 2","POP","MIN 2"]`
  - Output: `[1, 1]`
- Example 2:
  - Input: `["PUSH 7","MIN 3","POP","MIN 1"]`
  - Output: `["NA", 7]`

## 10) Stadium Max Tracker
- Slug: stadium-max-tracker
- Difficulty: Medium
- Problem: Design a stack supporting `push`, `pop`, `top`, and `getMax` in O(1) time.
- Constraints: `1 <= m <= 10^5` operations.
- Hint: Mirror the min-stack idea but store running maximums.
- Example 1:
  - Input: `push 2, push 9, push 5, getMax, pop, getMax`
  - Output: `[9, 9]`
- Example 2:
  - Input: `push -1, pop, getMax`
  - Output: `["EMPTY"]`

## 11) Circuit Postfix Evaluator
- Slug: circuit-postfix-evaluator
- Difficulty: Easy-Medium
- Problem: Evaluate a postfix arithmetic expression containing non-negative integers and operators `+ - * /`. Division is integer floor toward zero.
- Constraints: `1 <= tokens <= 10^4`, operands fit in 32-bit signed int.
- Hint: Push operands; on operator, pop two, compute, push result.
- Example 1:
  - Input: `["4", "13", "5", "/", "+"]`
  - Output: `6`
- Example 2:
  - Input: `["10", "6", "9", "+", "*"]`
  - Output: `150`

## 12) Campus Infix to Postfix
- Slug: campus-infix-to-postfix
- Difficulty: Easy-Medium
- Problem: Convert an infix expression with `+ - * /` and parentheses into postfix form.
- Constraints: `1 <= len(expr) <= 10^4`, operands are single uppercase letters.
- Hint: Use operator stack with precedence; output operands immediately.
- Example 1:
  - Input: `"A*(B+C/D)"` 
  - Output: `"ABCD/+*"`
- Example 2:
  - Input: `"((A+B)-C)"`
  - Output: `"AB+C-"`

## 13) Auditorium Histogram After One Skip
- Slug: auditorium-histogram-after-one-skip
- Difficulty: Medium
- Problem: Given heights of adjacent stands, you may remove at most one bar entirely. Compute the largest rectangular area achievable under the histogram after optionally deleting one bar.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= h[i] <= 10^9`.
- Hint: Precompute previous smaller and next smaller; also compute best area with one deletion by considering spans that skip a single bar.
- Example 1:
  - Input: `[2, 1, 5, 6, 2, 3]`
  - Output: `12` (delete the `1` to use `[5,6,2,3]` with area 12)
- Example 2:
  - Input: `[3, 3, 3]`
  - Output: `9`

## 14) Shuttle Validation
- Slug: shuttle-validation
- Difficulty: Easy-Medium
- Problem: Given pushed and popped sequences for a single stack, determine if the popped order is valid.
- Constraints: `1 <= n <= 10^5`, elements are distinct ints.
- Hint: Simulate pushing; while top matches pop pointer, pop.
- Example 1:
  - Input: `pushed=[4,5,6], popped=[5,6,4]`
  - Output: `true`
- Example 2:
  - Input: `pushed=[1,2,3,4], popped=[2,1,4,3]`
  - Output: `false`

## 15) Bike Repair Plates
- Slug: bike-repair-plates
- Difficulty: Medium
- Problem: You have a stack of metal plates with diameters. Remove plates one by one; if a plate is smaller than a plate beneath it, that lower plate is unsafe. Count how many plates become unsafe after the entire pop process when plates are removed in the given order.
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= d[i] <= 10^9`.
- Hint: Use a monotonic stack to track non-increasing diameters; increment when a pop reveals a larger plate beneath.
- Example 1:
  - Input: `[5, 2, 4]`
  - Output: `1`
- Example 2:
  - Input: `[4, 4, 4]`
  - Output: `0`

## 16) Assembly Line Span Reset
- Slug: assembly-line-span-reset
- Difficulty: Medium
- Problem: Given daily production counts, for each day find the span of consecutive prior days with counts strictly less than today. When you pop strictly smaller counts, reset the span accordingly.
- Constraints: `1 <= n <= 10^5`, `0 <= count[i] <= 10^9`.
- Hint: Variation of span using a stack of (value, span) but with strict inequality.
- Example 1:
  - Input: `[2, 1, 3, 2, 5]`
  - Output: `[1, 1, 3, 1, 5]`
- Example 2:
  - Input: `[2, 2, 2]`
  - Output: `[1, 1, 1]`
