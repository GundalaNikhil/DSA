# Original Greedy & Heap Practice Set (16 Questions)

## 1) Campus Shuttle Driver Swaps

- Slug: campus-shuttle-driver-swaps
- Difficulty: Easy
- Problem: You have `n` shuttle trips, each needing one driver. Two drivers A and B have availability intervals `[start, end]`. Assign trips to minimize the number of driver switches (A->B or B->A) while covering all trips. Return the minimum switches or -1 if impossible.
- Constraints: `1 <= n <= 10^5`, times are integers, trips are non-overlapping.
- Hint: Greedily extend the current driver as far as possible; switch only when a gap cannot be covered.
- Example:
  - Input: trips `[1-3, 4-6, 7-9]`, A available `[1-8]`, B `[3-10]`
  - Output: `1`

## 2) Lab Kit Distribution

- Slug: lab-kit-distribution
- Difficulty: Medium
- Problem: There are `k` kit types with quantities `q[i]` and `m` students each requesting one kit. Fulfill as many requests as possible while minimizing leftover kit types that become zero. Return `(fulfilled, zeroedTypes)`.
- Constraints: `1 <= k, m <= 10^5`, `0 <= q[i] <= 10^9`.
- Hint: Use a max-heap on quantities; always give from the largest pile to reduce zeroing.
- Example:
  - Input: `q = [3,1,2]`, `m = 4`
  - Output: `fulfilled=4, zeroedTypes=2`

## 3) Festival Stall Placement

- Slug: festival-stall-placement
- Difficulty: Medium
- Problem: Given `n` stall requests with start/end coordinates on a line, place the maximum number without two stalls being within distance `d` of each other. Return the max count.
- Constraints: `1 <= n <= 10^5`, positions are integers.
- Hint: Sort by end; greedy pick earliest end that’s at least `d` away from last chosen.
- Example:
  - Input: intervals `[(0,2),(1,4),(5,6)]`, `d=2`
  - Output: `2`

## 4) Library Power Backup

- Slug: library-power-backup
- Difficulty: Medium
- Problem: Backup batteries have capacities `c[i]`. You must power a server for `T` hours; each hour you may draw from one battery until empty. Choose batteries and ordering to minimize the number of battery swaps (times you change to a new battery). Return swaps or -1 if not enough total capacity.
- Constraints: `1 <= n <= 10^5`, `1 <= c[i] <= 10^9`, `1 <= T <= 10^9`.
- Hint: Greedy pick largest capacities first; swaps = chosen batteries - 1.
- Example:
  - Input: `c=[3,5,2], T=7`
  - Output: `1`

## 5) Shuttle Overtime Minimizer

- Slug: shuttle-overtime-minimizer
- Difficulty: Medium
- Problem: Each driver shift `i` has length `l[i]` and overtime cost per extra hour `p[i]`. You must cover `H` total hours; shifts can be partially used but overtime cost applies beyond `l[i]`. Minimize cost.
- Constraints: `1 <= n <= 10^5`, `0 <= l[i], p[i] <= 10^9`, `1 <= H <= 10^12`.
- Hint: Use a max-heap on `p[i]`; fill cheaper overtime last.
- Example:
  - Input: `l=[4,2], p=[3,1]`, `H=8`
  - Output: `14`

## 6) Robotics Component Bundling with Loss and Quality Score

- Slug: robotics-component-bundling-loss-quality
- Difficulty: Medium
- Problem: You can bundle two parts; the new part's weight is `w_big + w_small - floor(0.1 * w_small)` (10% of the smaller part is lost), and each part also has a quality score `q[i]`. When bundling, the new quality is `min(q[i], q[j]) - 1`. You must maintain quality >= T (threshold) for all intermediate bundles, or they become unusable. Choose the order to maximize the final weight among valid bundling sequences; return that weight or -1 if no valid sequence exists.
- Constraints: `1 <= n <= 2 * 10^5`, `1 <= w[i] <= 10^9`, `1 <= q[i] <= 100`, `1 <= T <= 100`.
- Hint: Loss depends on the smaller operand; to maximize final weight while maintaining quality threshold, use a max-heap to track (weight, quality) pairs and only merge when the resulting quality >= T.
- Example:
  - Input: `weights=[4, 3, 2]`, `quality=[10, 8, 6]`, `T=5`
  - Output: `9` (valid bundling sequence exists maintaining quality >= 5)

## 7) Campus Wi-Fi Expansion

- Slug: campus-wifi-expansion
- Difficulty: Medium
- Problem: You must connect `n` buildings. Some cables already exist; laying a new cable between buildings `i` and `j` costs `|h[i]-h[j]|` where `h` is building height. Find the min total cost to connect all buildings.
- Constraints: `1 <= n <= 10^5`.
- Hint: Build candidate edges only between adjacent buildings when sorted by height; then run Kruskal.
- Example:
  - Input: `h = [5, 1, 9]`
  - Output: `8`

## 8) Exam Proctor Allocation

- Slug: exam-proctor-allocation
- Difficulty: Medium
- Problem: Intervals of exams `[start,end]` need proctors. Each proctor can handle up to `r` overlapping exams at once. Find min number of proctors needed.
- Constraints: `1 <= n <= 10^5`, `1 <= r <= 10^9`.
- Hint: Sweep-line counts overlaps; proctors = ceil(maxOverlap / r).
- Example:
  - Input: `[(0,10),(5,7),(6,9)]`, `r=2`
  - Output: `2`

## 9) Shuttle Refuel with Refund

- Slug: shuttle-refuel-with-refund
- Difficulty: Medium
- Problem: A circular route with fuel at stops `gain[i]`, cost to next `cost[i]`, and a coupon that refunds the fuel you spend at exactly one segment. Find a start index to complete the loop using the refund optimally, or -1 if impossible.
- Constraints: `1 <= n <= 10^5`, `0 <= gain[i], cost[i] <= 10^9`.
- Hint: Track surplus and best refund opportunity; similar to gas-station but consider max `(cost - gain)` segment to refund.
- Example:
  - Input: `gain=[1,4,2], cost=[3,2,3]`
  - Output: `1`

## 10) Library Merge Queues

- Slug: library-merge-queues
- Difficulty: Medium
- Problem: Merge `k` sorted queues of book IDs into one stream but enforce that no ID appears more than twice in a row in the output; otherwise skip extra copies. Return the merged stream.
- Constraints: Total elements `<= 2 * 10^5`.
- Hint: Min-heap by value and source; track last two outputs to avoid triples.
- Example:
  - Input: `[[1,1,1],[1,2],[2]]`
  - Output: `[1,1,1,2,2]`

## 11) Campus Event Ticket Caps

- Slug: campus-event-ticket-caps
- Difficulty: Medium
- Problem: Ticket requests have quantities `q[i]` and deadlines `d[i]`. You can process at most one request per day; partially fulfill is allowed but counts as a day. Maximize total tickets sold.
- Constraints: `1 <= n <= 10^5`.
- Hint: Sort by deadline; use a min-heap of quantities kept to current day; if heap size exceeds days, drop smallest quantity.
- Example:
  - Input: `q=[3,5,2], d=[1,3,2]`
  - Output: `7`

## 12) Workshop Task Cooldown with Priority Interrupts

- Slug: workshop-task-cooldown-priority
- Difficulty: Medium
- Problem: Tasks A..Z have counts `c[i]` and priority `p[i]` in {1..3}. Between identical tasks, at least `k` different tasks must occur. A higher-priority task can preempt the cooldown queue: when scheduled, it resets the cooldown of any lower-priority tasks currently cooling down (they must wait an extra `k` slots). Idle slots cost 1. Minimize total slots.
- Constraints: `1 <= total tasks <= 10^5`, `0 <= k <= 10^5`.
- Hint: Max-heap by (priority, remaining count); cooldown queue carries readyTime and priority; when a high-priority task runs, push back lower-priority cooling tasks by k.
- Example:
  - Input: tasks `A:3,p=2`, `B:2,p=1`, `k=1`
  - Output: `7`

## 13) Auditorium Seat Refunds

- Slug: auditorium-seat-refunds
- Difficulty: Medium
- Problem: Seats sold in rows; refund requests list seat IDs. Process refunds to minimize the highest occupied row index after all refunds (lower rows fill first). Return that highest occupied row.
- Constraints: `1 <= rows <= 10^5`, initial occupancy full, requests `<= 10^5`.
- Hint: Use a max-heap of currently occupied rows; pop when emptied.
- Example:
  - Input: `rows=3`, requests remove seats in row order `[3,3,2]`
  - Output: `1`

## 14) Festival Bandwidth Split

- Slug: festival-bandwidth-split
- Difficulty: Medium
- Problem: `n` stages share a bandwidth pipe of size `B`. Each stage `i` needs at least `b[i]` to run; unused bandwidth is wasted. Allocate bandwidth to maximize the number of running stages; ties broken by minimizing unused bandwidth.
- Constraints: `1 <= n <= 10^5`, `1 <= B <= 10^12`.
- Hint: Sort `b` ascending; greedily take smallest until cannot; track waste.
- Example:
  - Input: `b=[5,2,4]`, `B=7`
  - Output: `2`

## 15) Robotics Median After Batches with Stale Filter

- Slug: robotics-median-after-batches-stale
- Difficulty: Medium
- Problem: Numbers arrive in batches. A value becomes “stale” once it has appeared more than `t` times overall and must be excluded from median computation. After each batch, report the median of all non-stale values seen so far (if none, report `"NA"`).
- Constraints: Total numbers `<= 2 * 10^5`, `1 <= t <= 10^5`.
- Hint: Two heaps plus a frequency map and lazy deletion; when a value exceeds `t`, purge it from heaps via lazy pops.
- Example:
  - Input: batches `[[5,5,1],[5,3],[8,9]]`, `t=2`
  - Output: `[5,3,6]`

## 16) Shuttle Schedule Delay Minimizer

- Slug: shuttle-schedule-delay-minimizer
- Difficulty: Medium
- Problem: Trips have planned start times and durations. If a trip starts late, its delay adds to all subsequent trips. Choose an execution order to minimize total accumulated delay.
- Constraints: `1 <= n <= 10^5`, durations and start times up to `10^9`.
- Hint: Sort by `(duration - start)` ascending (Smith-like rule for minimizing weighted completion with equal weights).
- Example:
  - Input: start `[0,1]`, dur `[3,2]`
  - Output: Order `[1,0]` (total delay smaller)
