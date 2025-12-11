# Original Linked List Practice Set (16 Questions)

## 1) Lab Roster Append
- Slug: lab-roster-append
- Difficulty: Easy
- Problem: Implement a singly linked list supporting `push_back(value)` and `to_array()` that returns all elements in order.
- Constraints: Up to `10^5` operations; values fit in 32-bit int.
- Hint: Track both head and tail for O(1) append.
- Example:
  - Input: `push_back 3, push_back 7, push_back -2`
  - Output: `[3, 7, -2]`

## 2) Campus Badge Search
- Slug: campus-badge-search
- Difficulty: Easy
- Problem: Given the head of a singly linked list and a target value, return the 0-based index of its first occurrence, or -1 if absent.
- Constraints: `1 <= n <= 10^5`.
- Hint: Linear scan with a position counter.
- Example:
  - Input: `list = 5 -> 1 -> 5 -> 9`, target `9`
  - Output: `3`

## 3) Lab Swap Neighbors with Skip
- Slug: lab-swap-neighbors-with-skip
- Difficulty: Easy-Medium
- Problem: Swap nodes in pairs except skip any node whose value is negative (leave it and its neighbor in place). Return new head.
- Constraints: `0 <= n <= 10^5`.
- Hint: Dummy head; when a negative appears, advance without swapping.
- Example:
  - Input: `1 -> -2 -> 3 -> 4`
  - Output: `1 -> -2 -> 4 -> 3`

## 4) Hostel Cleanup Deduplicate (At Most Two)
- Slug: hostel-cleanup-deduplicate-two
- Difficulty: Easy-Medium
- Problem: Given a sorted singly linked list, reduce duplicates so each value appears at most twice.
- Constraints: `0 <= n <= 10^5`.
- Hint: Keep a counter as you iterate; unlink extras beyond two.
- Example:
  - Input: `1 -> 1 -> 1 -> 2 -> 2 -> 3`
  - Output: `1 -> 1 -> 2 -> 2 -> 3`

## 5) Shuttle Route Alternating Reverse
- Slug: shuttle-route-alternating-reverse
- Difficulty: Medium
- Problem: Starting at position `l`, reverse every other contiguous segment of length `k` (reverse k, skip k, reverse k, ...). The last segment may be shorter; still reverse it if it’s a “reverse” turn. Return the head.
- Constraints: `1 <= l <= n <= 10^5`, `1 <= k <= 10^5`.
- Hint: Traverse to position `l`, then alternately reverse and skip blocks of size `k`.
- Example:
  - Input: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`, `l=2`, `k=2`
  - Output: `1 -> 3 -> 2 -> 4 -> 5 -> 7 -> 6`

## 6) Lab Loop Detector with Length
- Slug: lab-loop-detector-length
- Difficulty: Medium
- Problem: Detect if a singly linked list has a cycle; if yes, return its length, else return 0.
- Constraints: `0 <= n <= 10^5`.
- Hint: Floyd’s pointers; count cycle length upon meeting.
- Example:
  - Input: `1 -> 2 -> 3 -> 4 -> (back to 2)`
  - Output: `3`

## 7) Seminar Middle Seat (First Middle)
- Slug: seminar-middle-seat-first
- Difficulty: Easy
- Problem: Return the first middle node (for even length, return the left middle).
- Constraints: `1 <= n <= 10^5`.
- Hint: Slow/fast with fast starting at head.next.
- Example:
  - Input: `1 -> 2 -> 3 -> 4`
  - Output: `2`

## 8) Lab Playlist Merge by Parity
- Slug: lab-playlist-merge-parity
- Difficulty: Easy-Medium
- Problem: Merge two sorted lists into one, but place even-valued nodes ahead of odd-valued nodes while keeping relative order among evens and among odds.
- Constraints: `0 <= n, m <= 10^5`.
- Hint: Two-pass merge: first collect evens from both, then odds.
- Example:
  - Input: `1 -> 4 -> 7` and `2 -> 3 -> 10`
  - Output: `4 -> 2 -> 10 -> 1 -> 7 -> 3`

## 9) Robotics Chunk Reverse with Remainder
- Slug: robotics-chunk-reverse-remainder
- Difficulty: Medium
- Problem: Reverse nodes in groups of size `k`, but leave any trailing group of size `< k` reversed as well (not left in place). Return new head.
- Constraints: `0 <= n <= 10^5`, `1 <= k <= n`.
- Hint: Same as k-group reverse, but always reverse the last chunk regardless of size.
- Example:
  - Input: `1 -> 2 -> 3 -> 4 -> 5`, `k = 2`
  - Output: `2 -> 1 -> 4 -> 3 -> 5`

## 10) Shuttle ID Stable Partition
- Slug: shuttle-id-stable-partition
- Difficulty: Medium
- Problem: Stable-partition the list so that nodes with value < `x` appear first, then nodes equal to `x`, then > `x`, preserving relative order within each group.
- Constraints: `0 <= n <= 10^5`.
- Hint: Build three lists and concatenate.
- Example:
  - Input: `5 -> 1 -> 4 -> 2 -> 5`, `x = 4`
  - Output: `1 -> 2 -> 4 -> 5 -> 5`

## 11) Exam Seating Intersection Distance
- Slug: exam-seating-intersection-distance
- Difficulty: Medium
- Problem: Given two singly linked lists that may intersect, return the number of nodes shared (common suffix length), else 0.
- Constraints: `0 <= n <= 10^5`.
- Hint: Advance the longer list by length diff; then walk together counting matches until diverge.
- Example:
  - Input: A `1->2->3->4`, B `9->3->4` (nodes 3,4 shared)
  - Output: `2`

## 12) Hostel Number Remove Mth from Start
- Slug: hostel-number-remove-mth
- Difficulty: Easy-Medium
- Problem: Remove the M-th node from the start (1-indexed) and return head; if M > length, return original list.
- Constraints: `1 <= n <= 10^5`.
- Hint: Handle head removal carefully; single pass with counter.
- Example:
  - Input: `9 -> 8 -> 7 -> 6`, `M = 2`
  - Output: `9 -> 7 -> 6`

## 13) Shuttle Ticket Rotate by Blocks
- Slug: shuttle-ticket-rotate-blocks
- Difficulty: Easy-Medium
- Problem: Rotate the list to the right by `k` places but only within blocks of size `b` (last block may be smaller). Concatenate rotated blocks.
- Constraints: `0 <= n <= 10^5`, `1 <= b <= n`, `0 <= k <= 10^9`.
- Hint: For each block, compute `k % blockSize` and rotate that block.
- Example:
  - Input: `1 -> 2 -> 3 -> 4 -> 5 -> 6`, `b=3`, `k=1`
  - Output: `3 -> 1 -> 2 -> 6 -> 4 -> 5`

## 14) Robotics Palindrome with One Skip
- Slug: robotics-palindrome-one-skip
- Difficulty: Medium
- Problem: Determine if the list can become a palindrome after deleting at most one node.
- Constraints: `1 <= n <= 10^5`.
- Hint: Use two-pointer technique on array copy or reverse-second-half with one mismatch allowed.
- Example:
  - Input: `1 -> 2 -> 3 -> 2 -> 1`
  - Output: `true`
  - Input: `1 -> 2 -> 4 -> 2`
  - Output: `true` (remove 4)

## 15) Workshop Odd Even Grouping Stable
- Slug: workshop-odd-even-grouping-stable
- Difficulty: Medium
- Problem: Reorder nodes so values with odd parity appear first, then even parity, preserving original order within each group.
- Constraints: `0 <= n <= 10^5`.
- Hint: Build two lists and join; do not confuse with positional parity.
- Example:
  - Input: `2 -> 5 -> 4 -> 7`
  - Output: `5 -> 7 -> 2 -> 4`

## 16) Lecture Notes Subtract Two Numbers (Forward Order)
- Slug: lecture-notes-subtract-forward
- Difficulty: Medium
- Problem: Two linked lists represent non-negative integers in forward order. Subtract the smaller number from the larger and return the result in forward order, along with a sign bit indicating if the result is zero (sign=0) or positive (sign=1). Do not use big integers.
- Constraints: Length up to `10^5`, digits 0-9, no leading zeros except zero itself.
- Hint: Compare lengths and lexicographic order to pick minuend; use stacks to subtract with borrow; drop leading zeros in result.
- Example:
  - Input: `7 -> 1 -> 6` (716) and `2 -> 9 -> 5` (295)
  - Output: `sign=1`, list `4 -> 2 -> 1` (421)
  - Input: `9 -> 0` (90) and `9 -> 0` (90)
  - Output: `sign=0`, list `0`
