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

## 3) Conveyor Weighted Deduplication

- Slug: conveyor-weighted-deduplication
- Difficulty: Easy-Medium
- Problem: Given a string and a weight array `w[]`, repeatedly remove adjacent equal characters, but only if their combined weight is even. When you remove a pair, the weight sum is added to a running total. Return both the reduced string and the total weight removed.
- Constraints: `1 <= len(s) <= 2 * 10^5`, `1 <= w[i] <= 1000`.
- Hint: Stack (char, weight) pairs; pop when incoming char matches top AND sum of weights is even; accumulate removed weights.
- Example 1:
  - Input: `s="xxyyz", w=[1,3,2,2,5]`
  - Output: `("xyz", 4)` (remove second y-y pair with weights 2+2=4)
- Example 2:
  - Input: `s="abbaac", w=[2,3,3,2,1,1]`
  - Output: `("c", 10)` (remove a-a with 2+2=4, b-b with 3+3=6)

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

## 5) Workshop Next Taller with Width

- Slug: workshop-next-taller-width
- Difficulty: Medium
- Problem: For each machine height, find the next taller height to its right within distance at most `w`; if none within `w`, output -1.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= h[i] <= 10^9`, `1 <= w <= n`.
- Hint: Monotonic stack storing indices; pop outdated (>w away).
- Example 1:
  - Input: `h=[1, 7, 3, 4, 2], w=2`
  - Output: `[7, -1, 4, -1, -1]`
    Example 2:
  - Input: `h=[9, 8, 8], w=1`
  - Output: `[-1, -1, -1]`

## 6) Assembly Previous Greater with Parity

- Slug: assembly-previous-greater-parity
- Difficulty: Medium
- Problem: For each element, find the nearest greater element to its left with opposite parity (one even, one odd); output -1 if none.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Maintain two stacks, one for even values and one for odd values.
- Example 1:
  - Input: `[2, 9, 5, 7, 3]`
  - Output: `[-1, 2, 9, 9, 9]`
    Example 2:
  - Input: `[2, 4, 6]`
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

## 11) Circuit Postfix Evaluator with Variables

- Slug: circuit-postfix-variables
- Difficulty: Medium
- Problem: Evaluate a postfix expression with integers, operators `+ - * / %`, and single-letter variables. You're given a variable map. Additionally, support `DUP` (duplicate top), `SWAP` (swap top two), and compute result modulo `10^9+7`.
- Constraints: `1 <= tokens <= 10^4`, `0 <= vars <= 26`, operands fit in 64-bit signed int.
- Hint: Push operands/variables; handle special stack operations; apply mod at each step to prevent overflow.
- Example 1:
  - Input: `tokens=["x", "5", "+", "y", "*"], vars={x:3, y:2}`
  - Output: `16` ((3+5)\*2)
- Example 2:
  - Input: `tokens=["10", "DUP", "*", "7", "+"]`
  - Output: `107` (10\*10+7)

## 12) Campus Expression Optimizer

- Slug: campus-expression-optimizer
- Difficulty: Medium
- Problem: Convert infix with `+ - * / ^ %` and parentheses to postfix. Additionally, detect syntax errors (mismatched parentheses, consecutive operators) and identify redundant parentheses. Return postfix or error message, plus count of redundant parenthesis pairs.
- Constraints: `1 <= len(expr) <= 10^4`, operands are single uppercase letters or digits.
- Hint: Use operator stack with precedence; track parenthesis depth for redundancy detection; validate operator sequences.
- Example 1:
  - Input: `"A*((B+C)/D)"`
  - Output: `("ABC+D/*", 1)` (1 redundant pair)
- Example 2:
  - Input: `"((A++B))"`
  - Output: `("ERROR: consecutive operators", 0)`

## 13) Auditorium Histogram With One Booster

- Slug: auditorium-histogram-one-booster
- Difficulty: Medium
- Problem: Given heights, you may increase exactly one bar by up to `b` units (non-negative) to maximize largest rectangle area. Compute maximal area.
- Constraints: `1 <= n <= 2 * 10^5`, `0 <= h[i], b <= 10^9`.
- Hint: Largest rectangle via monotonic stack; for each bar consider area with boost limited by neighbors’ mins.
- Example 1:
  - Input: `[2,4,2], b=3`
  - Output: `7` (boost middle bar to 7; best rectangle height 7 width 1)
- Example 2:
  - Input: `[1,3,2,2], b=2`
  - Output: `8` (boost bar of height 2 to 4 at index3; rectangle height 4 width 2)

## 14) Shuttle Validation with Time Windows

- Slug: shuttle-validation-time-windows
- Difficulty: Medium
- Problem: Given pushed and popped sequences with timestamps, plus time window constraints `W[]` for certain elements. Validate if: (1) pop sequence is valid, (2) each windowed element must be popped within `W[i]` time units of being pushed, and (3) elements with priority flag must be popped before any larger non-priority element.
- Constraints: `1 <= n <= 10^5`, `0 <= timestamps[i] <= 10^9`, `1 <= W[i] <= 10^6`.
- Hint: Simulate stack with timestamp tracking; check time windows during pop; maintain priority element positions.
- Example 1:
  - Input: pushed=[4,5,6], push_times=[0,2,4], popped=[5,6,4], pop_times=[3,5,10], W={5:2}, priority={4}
  - Output: false (element 5 popped at time 3, exceeds window 0+2)
- Example 2:
  - Input: pushed=[1,2,3], push_times=[0,1,2], popped=[2,1,3], pop_times=[2,3,4], W={}, priority={1}
  - Output: true

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
