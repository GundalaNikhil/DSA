# Basic Queue & Deque Practice Set (15-18 Questions)

## 1) Campus Service Line

- Slug: campus-service-line
- Difficulty: Easy
- Problem: Implement a basic queue with `ENQUEUE x`, `DEQUEUE`, and `FRONT`. Return outputs for each non-enqueue command, using `"EMPTY"` for underflow.
- Constraints: `1 <= m <= 10^5`, `-10^9 <= x <= 10^9`.
- Hint: Use two indices on an array or two stacks for amortized O(1) operations.
- Example 1:
  - Input: `["ENQUEUE 12", "ENQUEUE -5", "FRONT", "DEQUEUE", "FRONT"]`
  - Output: `[12, -5]`
- Example 2:
  - Input: `["FRONT", "DEQUEUE"]`
  - Output: `["EMPTY", "EMPTY"]`

## 2) Circular Shuttle Buffer with Overwrite

- Slug: circular-shuttle-buffer-overwrite
- Difficulty: Easy-Medium
- Problem: Design a circular queue with fixed capacity `k` supporting enqueue, dequeue, front, rear, isEmpty/isFull, and `ENQ_OVR x` that overwrites the oldest element when full (returns the overwritten value). Normal `ENQ` should fail when full.
- Constraints: `1 <= k <= 10^5`, operations `<= 10^5`.
- Hint: Maintain head/tail indices modulo `k` and size; `ENQ_OVR` advances head when overwriting.
- Example 1:
  - Input: `k=2`, ops=`ENQ 5, ENQ 6, ENQ 7, ENQ_OVR 8, FRONT, REAR`
  - Output: `[false, 5, 6]` (ENQ 7 failed; ENQ_OVR overwrote 5)
- Example 2:
  - Input: `k=1`, ops=`ENQ 9, ENQ_OVR 4, FRONT`
  - Output: `[9, 4]`

## 3) Cafeteria Queue Rotation

- Slug: cafeteria-queue-rotation
- Difficulty: Easy
- Problem: Given a queue of student IDs, rotate it left by `k` positions (front elements move to back) and return the new order.
- Constraints: `1 <= n <= 10^5`, `0 <= k <= 10^9`.
- Hint: Normalize `k` with `k % n`; perform `k` dequeues and enqueues.
- Example 1:
  - Input: `queue = [4, 9, 1, 7], k = 3`
  - Output: `[7, 4, 9, 1]`
- Example 2:
  - Input: `queue = [2, 3], k = 1`
  - Output: `[3, 2]`

## 4) Hallway Interleave

- Slug: hallway-interleave
- Difficulty: Easy-Medium
- Problem: Given a queue with even length, interleave its first half with the second half (preserve relative order within each half).
- Constraints: `2 <= n <= 10^5`, `n` is even.
- Hint: Move first half into a stack or auxiliary queue, then alternately merge back.
- Example 1:
  - Input: `[11, 12, 13, 14]`
  - Output: `[11, 13, 12, 14]`
- Example 2:
  - Input: `[5, 6, 7, 8, 9, 10]`
  - Output: `[5, 8, 6, 9, 7, 10]`

## 5) Lab Printer Reversal

- Slug: lab-printer-reversal
- Difficulty: Easy
- Problem: Reverse the first `k` jobs in a print queue while keeping the rest in the same relative order.
- Constraints: `1 <= k <= n <= 10^5`.
- Hint: Use a stack for the first `k` items, then append the remainder.
- Example 1:
  - Input: `queue = [2, 4, 6, 8, 10], k = 4`
  - Output: `[8, 6, 4, 2, 10]`
- Example 2:
  - Input: `queue = [9, 1, 5], k = 1`
  - Output: `[9, 1, 5]`

## 6) Ticket Window Distinct Prefix

- Slug: ticket-window-distinct-prefix
- Difficulty: Easy-Medium
- Problem: Given a stream of lowercase letters, after each arrival output the shortest prefix of the stream that ends at the current character and contains all distinct letters seen so far. If no such prefix exists (a letter missing), output `"#"`.
- Constraints: `1 <= len(stream) <= 10^5`.
- Hint: Track first occurrence index of each character and the maximum of those indices among seen letters; output prefix length = current index - minIndex + 1 when all seen letters accounted for.
- Example 1:
  - Input: `"abac"`
  - Output: `"1,2,3,4"` (prefix lengths as strings)
- Example 2:
  - Input: `"aaaa"`
  - Output: `"1,1,1,1"`

## 7) Lab Window Instability

- Slug: lab-window-instability
- Difficulty: Medium
- Problem: For each window of size `k`, output `(max - min) / median` rounded down (median is lower median for even k). If median is 0, output 0.
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= k <= n`, readings are 32-bit ints.
- Hint: Deques for max/min plus two-heaps for median with lazy deletions.
- Example 1:
  - Input: `arr = [5, 1, 4, 6, 2], k = 3`
  - Output: `[ (5-1)/4=1, (6-1)/4=1, (6-2)/4=1 ]` -> `[1,1,1]`
    Example 2:
  - Input: `[9, 9, 9], k = 2`
  - Output: `[0,0]`

## 8) Corridor Window Second Minimum

- Slug: corridor-window-second-minimum
- Difficulty: Medium
- Problem: For each window of size `k`, output the second smallest element (or the smallest if window has size 1). Handle duplicates appropriately (second smallest may equal smallest if it occurs multiple times).
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= k <= n`.
- Hint: Use multiset (ordered map) sliding window; track counts to remove/insert.
- Example 1:
  - Input: `[6, 2, 5, 1, 7], k = 3`
  - Output: `[5,2,5]` (windows [6,2,5]->2nd=5, [2,5,1]->2nd=2, [5,1,7]->2nd=5)
    Example 2:
  - Input: `[8,6], k = 1`
  - Output: `[8,6]`

## 9) Battery Lab First Negative

- Slug: battery-lab-first-negative
- Difficulty: Easy-Medium
- Problem: For each window of size `k` in an array, report the first negative number; output 0 if none.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= n`.
- Hint: Maintain a queue of indices of negative numbers; drop indices leaving the window.
- Example 1:
  - Input: `[5, -2, -7, 3, 4], k = 2`
  - Output: `[-2, -7, -7, 3]`
- Example 2:
  - Input: `[1, 2, 3], k = 2`
  - Output: `[0, 0]`

## 10) Shuttle Seat Assignment

- Slug: shuttle-seat-assignment
- Difficulty: Medium
- Problem: Given arrival and departure times of shuttle seats, find the minimum number of seats required so no passenger waits. Use sorting plus a queue to track current departures.
- Constraints: `1 <= n <= 10^5`, times are integers in `[0, 10^9]`.
- Hint: Sort by arrival; push departures into a min-heap or queue sorted by time; pop while earliest departure <= current arrival.
- Example 1:
  - Input: `arrivals = [0, 4, 4], departures = [5, 5, 9]`
  - Output: `2`
- Example 2:
  - Input: `arrivals = [2], departures = [3]`
  - Output: `1`

## 11) Event Registration Merge

- Slug: event-registration-merge
- Difficulty: Easy
- Problem: Merge two already sorted queues of registration IDs into one sorted queue.
- Constraints: `0 <= n, m <= 10^5`.
- Hint: Use front comparisons; dequeue from the smaller front each step.
- Example 1:
  - Input: `Q1 = [3, 5, 9], Q2 = [1, 4, 10]`
  - Output: `[1, 3, 4, 5, 9, 10]`
- Example 2:
  - Input: `Q1 = [6], Q2 = []`
  - Output: `[6]`

## 12) Bus Loop With One Free Skip

- Slug: bus-loop-one-skip
- Difficulty: Medium
- Problem: A circular bus route lists fuel pickups `gain[i]` and costs `cost[i]` to reach the next stop. You are allowed to skip refueling at exactly one stop (fuel gained there is lost). Find a starting stop index to complete the loop with that single skip available; return -1 if impossible even with the skip.
- Constraints: `1 <= n <= 10^5`, `0 <= gain[i], cost[i] <= 10^9`.
- Hint: Track two running surpluses: without skip and with skip already used; reset start when both go negative; total gain must still be sufficient.
- Example 1:
  - Input: `gain = [1, 5, 1], cost = [3, 2, 2]`
  - Output: `1` (start at index 1 and skip refuel at index 2)
- Example 2:
  - Input: `gain = [1, 1], cost = [3, 3]`
  - Output: `-1`

## 13) Task Stream Rate Limit

- Slug: task-stream-rate-limit
- Difficulty: Easy-Medium
- Problem: Given timestamps of incoming requests and a window size `t`, return for each request whether it is allowed when at most `k` requests can occur in any window of length `t`.
- Constraints: `1 <= n <= 10^5`, `1 <= t <= 10^9`, `1 <= k <= n`.
- Hint: Maintain a queue of timestamps; drop those older than `current - t`; allow if queue size < k.
- Example 1:
  - Input: `times = [2, 4, 6, 9], t = 4, k = 1`
  - Output: `[true, false, false, true]`
- Example 2:
  - Input: `times = [0, 3, 3, 7], t = 3, k = 2`
  - Output: `[true, true, false, true]`

## 14) Deque Balance Rearrange

- Slug: deque-balance-rearrange
- Difficulty: Medium
- Problem: Given an array, rearrange it by alternately taking from the front and back into a new deque, then output the deque from front to back.
- Constraints: `1 <= n <= 10^5`.
- Hint: Use two indices (start/end) and push_front/push_back alternately.
- Example 1:
  - Input: `[2, 4, 6, 8]`
  - Output: `[2, 8, 4, 6]`
- Example 2:
  - Input: `[3, 7, 9, 1, 5]`
  - Output: `[3, 5, 7, 1, 9]`

## 15) Festival Lantern Spread

- Slug: festival-lantern-spread
- Difficulty: Medium
- Problem: In a grid of `0`s (empty) and `1`s (lit lanterns), each minute new lanterns light up adjacent empty cells (up, down, left, right). Compute minutes to light the whole grid or -1 if impossible. Use BFS with a queue.
- Constraints: `1 <= r, c <= 200`, grid size `<= 4 * 10^4`.
- Hint: Multi-source BFS from all `1`s; count remaining zeros; track layers by queue size.
- Example 1:
  - Input: `[[1,0,0],[0,0,1],[0,0,0]]`
  - Output: `3`
- Example 2:
  - Input: `[[1,1],[1,1]]`
  - Output: `0`

## 16) Assembly Line Buffer Swap

- Slug: assembly-line-buffer-swap
- Difficulty: Easy-Medium
- Problem: Swap the contents of two queues of equal length using only queue operations and O(1) extra variables.
- Constraints: `1 <= n <= 10^5`.
- Hint: Dequeue from both into the opposite queue in parallel, repeating twice to restore order.
- Example 1:
  - Input: `Q1 = [4,5], Q2 = [7,8]`
  - Output: `Q1 = [7,8], Q2 = [4,5]`
- Example 2:
  - Input: `Q1 = [3], Q2 = [1]`
  - Output: `Q1 = [1], Q2 = [3]`
