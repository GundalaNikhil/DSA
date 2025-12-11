# Original Heaps & Priority Queue Practice Set (16 Questions)

## 1) Running Median with Delete and Threshold
- Slug: running-median-with-delete-threshold
- Difficulty: Medium
- Problem: Support a stream with insert x and delete x (if present). Also given a threshold `T`; when reporting median (lower middle on even count), if the multiset size is below `T`, output `"NA"` instead of the median. If empty, output `"EMPTY"`.
- Constraints: `1 <= ops <= 10^5`, `-10^9 <= x <= 10^9`, `0 <= T <= 10^5`.
- Hint: Two heaps with lazy deletion; track size vs T.
- Example:
  - Input: ops [add 1, add 5, del 1, median], T=2
  - Output: "NA"

## 2) Merge K Streams with Rate Limit
- Slug: merge-k-streams-rate-limit
- Difficulty: Medium
- Problem: Merge k sorted streams but output at most `r` elements per stream per round. Return merged order.
- Constraints: total elements `<= 2 * 10^5`.
- Hint: Min-heap of (value, stream); track emitted counts per round.
- Example:
  - Input: streams [[1,4],[2,3,5]], r=1
  - Output: [1,2,4,3,5]

## 3) Top K Frequent with Decay
- Slug: top-k-frequent-decay
- Difficulty: Medium
- Problem: Elements arrive with timestamps; frequency decays every `d` seconds halving counts. Support query for top k by current decayed count.
- Constraints: `1 <= events <= 10^5`.
- Hint: Store last update time; apply decay lazily; max-heap by effective freq.
- Example:
  - Input: arrivals (a@0,a@5,b@5), d=5, query at t=10
  - Output: top1 = a

## 4) Rope Connection Maximize Strength
- Slug: rope-connect-maximize
- Difficulty: Medium
- Problem: Given rope strengths, you can connect two ropes into one; strength becomes min(s1,s2) - 1. Maximize the final rope strength.
- Constraints: `1 <= n <= 10^5`, strengths up to `10^9`.
- Hint: Max-heap; always connect two strongest to minimize loss.
- Example:
  - Input: [5,4,3]
  - Output: 2

## 5) Meeting Rooms Min Idle with Setup Time
- Slug: meeting-rooms-min-idle-setup
- Difficulty: Medium
- Problem: Meetings have (start,end) and require setup time `s` before each meeting in a room (cannot overlap). With `k` rooms, schedule to minimize total idle + setup slack (time between end+setup and next start). Return minimum slack.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= n`, `0 <= s <= 10^6`.
- Hint: Sort by start; min-heap by room available time (end + setup); assign greedily.
- Example:
  - Input: intervals [(0,30),(5,10),(15,20)], k=2, s=2
  - Output: 2 (slack between meetings in same room)

## 6) Task Scheduler with Energy
- Slug: task-scheduler-energy
- Difficulty: Medium
- Problem: Tasks have duration and energy gain. You have initial energy E; executing a task consumes 1 energy unit per time unit of its duration but gives a one-time gain. Pick order to maximize completed tasks.
- Constraints: `1 <= n <= 10^5`.
- Hint: Sort by start energy requirement; min-heap for durations when energy limited.
- Example:
  - Input: tasks [(dur=2,gain=3),(dur=3,gain=1)], E=3
  - Output: 2

## 7) Sliding Window Kth Smallest
- Slug: sliding-window-kth-smallest
- Difficulty: Medium
- Problem: Given array and window size k, output k-th smallest in each window.
- Constraints: `1 <= n <= 2 * 10^5`.
- Hint: Two heaps with lazy deletion; balance sizes.
- Example:
  - Input: [1,3,2,6,4], k=3, kth=2
  - Output: [2,3,4]

## 8) Huffman with Merge Limit
- Slug: huffman-merge-limit
- Difficulty: Medium
- Problem: Given frequencies, build a Huffman-like tree but you can merge at most `m` nodes at a time (2<=m<=5). Compute total cost.
- Constraints: `1 <= n <= 10^5`.
- Hint: Use min-heap; when size mod (m-1) != 1, pad with zeros; merge lowest m each step.
- Example:
  - Input: [5,7,10], m=3
  - Output: 34

## 9) Dynamic Median of Medians
- Slug: dynamic-median-of-medians
- Difficulty: Medium
- Problem: Maintain medians of disjoint groups; queries ask for median of current group medians after inserts and merges of groups.
- Constraints: groups <= 10^5.
- Hint: Heaps per group; global heap of medians.
- Example:
  - Input: create group A with [1,3], group B with [2]; merge A,B; query median-of-medians
  - Output: 2

## 10) Top K Products with Index Gap
- Slug: topk-products-index-gap
- Difficulty: Medium
- Problem: Two sorted arrays (desc). Find top k largest products `A[i]*B[j]` subject to |i-j| >= d (given). If fewer than k pairs satisfy, return all possible.
- Constraints: `1 <= n,m <= 10^5`, `1 <= k <= min(10^5, n*m)`, `0 <= d < max(n,m)`.
- Hint: Max-heap of candidate pairs respecting the gap; expand neighbors while maintaining gap constraint.
- Example:
  - Input: A=[9,7], B=[8,3], d=1, k=2
  - Output: [27,24]

## 11) K Closest Points to Origin (Stream) with Weight
- Slug: k-closest-stream-weight
- Difficulty: Medium
- Problem: Stream of points with positive weight w; distance metric is (squared distance)/w. Maintain k points with smallest weighted distance at any time.
- Constraints: `1 <= ops <= 10^5`.
- Hint: Max-heap of size k by weighted metric.
- Example:
  - Input: add (1,1,w=1), add (2,2,w=5), k=1
  - Output: current best is (1,1)

## 12) Merge Intervals With Max Payload
- Slug: merge-intervals-max-payload
- Difficulty: Medium
- Problem: Intervals have payload value. When intervals overlap, merged interval payload = max of overlapping payloads. Return merged list sorted.
- Constraints: `1 <= n <= 10^5`.
- Hint: Sort by start; merge tracking max payload; heap not strictly needed but allowed.
- Example:
  - Input: [(1,3,5),(2,4,7)]
  - Output: [(1,4,7)]

## 13) Project Selection with Risk Budget
- Slug: project-selection-risk-budget
- Difficulty: Medium
- Problem: Each project i has cost[i], profit[i], and risk[i]. Start with capital C and risk budget R. You may pick at most k projects, only if cost <= capital and cumulative risk + risk[i] <= R. Maximize final capital.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= n`, values up to 1e9.
- Hint: Min-heap by cost for affordability; among affordable within risk budget, pick max profit; decrement risk budget per choice.
- Example:
  - Input: cost=[1,2,3], profit=[1,2,3], risk=[1,2,2], C=1, R=3, k=2
  - Output: 5

## 14) Scheduler With Cooling and Priority
- Slug: scheduler-cooling-priority
- Difficulty: Medium
- Problem: Tasks A..Z with counts and priority weights. Cooling time k between identical tasks. Schedule to maximize total priority executed in given time T.
- Constraints: `1 <= T <= 10^5`.
- Hint: Max-heap by priority; cooldown queue with ready time.
- Example:
  - Input: tasks {A:2 (p=3), B:1 (p=5)}, k=1, T=3
  - Output: total priority 11

## 15) Median of Two Heaps After Merge
- Slug: median-two-heaps-merge
- Difficulty: Medium
- Problem: Two heaps (one max, one min) each contain some numbers. Merge them and report median without flattening all numbers.
- Constraints: total size <= 2 * 10^5.
- Hint: Transfer elements to balance counts; track medians.
- Example:
  - Input: heap1 [1,3] (max-heap), heap2 [2,4] (min-heap)
  - Output: 2.5

## 16) Priority Queue with Decrease-Key
- Slug: priority-queue-decrease-key
- Difficulty: Medium
- Problem: Implement a priority queue supporting insert, extract-min, and decrease-key by handle/id.
- Constraints: `1 <= ops <= 10^5`.
- Hint: Binary heap with position map or pairing heap.
- Example:
  - Input: insert(5,id1), insert(3,id2), dec(id1,1), extract -> ?
  - Output: 1 (id1), then next extract 3 (id2)
