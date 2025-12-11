# Advanced Range Data Structures Practice Set (14 Questions)

## 1) Persistent Range Sum with Version Diff
- Slug: persistent-range-sum-version-diff
- Difficulty: Medium
- Problem: Build persistent segment tree supporting point updates creating new versions and queries asking sum over [l,r] in version v. Also support diff queries: sum_v1 - sum_v2 over [l,r].
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Example:
  - Input: arr=[1,2,3], update v0 pos1->5 => v1; query diff(v1,v0,0,2)
  - Output: 3

## 2) Persistent Kth in Range Between Versions
- Slug: persistent-kth-between-versions
- Difficulty: Medium
- Problem: Given versions v1, v2 (v2 newer), find k-th smallest in subarray [l,r] when applying differences between v2 and v1 (i.e., multiset of elements added minus removed). Return value or -1 if k out of bounds.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Example:
  - Input: arr=[5,1,3], v1=base, v2 after update pos0->2; query l=0 r=2 k=1
  - Output: 2

## 3) Range Assign and Range Sum with Rollbacks
- Slug: range-assign-sum-rollback
- Difficulty: Medium
- Problem: Support operations: assign value x to all in [l,r], query sum [l,r], and rollback to any previous state (indexed). Use segment tree with persistent lazy nodes.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Example:
  - Input: arr=[1,1,1]; assign(0,2,5) -> v1; query v1 [0,1]
  - Output: 10

## 4) DSU on Tree Subtree Mode Query
- Slug: dsu-on-tree-mode
- Difficulty: Medium
- Problem: For a rooted tree with node colors, for every node output the color with highest frequency in its subtree (smallest color on tie). Use DSU on tree (small-to-large).
- Constraints: `1 <= n <= 2 * 10^5`, colors <= 10^9.
- Example:
  - Input: tree 1-2,1-3, colors [1,2,2]
  - Output: node1->2, node2->2, node3->2

## 5) DSU on Tree With Updates
- Slug: dsu-on-tree-with-updates
- Difficulty: Hard
- Problem: Tree with color updates on nodes and queries asking distinct color count in subtree at that time. Offline process with Mo’s on tree + updates or Euler + sqrt-decomp.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Example:
  - Input: colors [1,2], edge(1,2); update node2 to 1; query subtree of 1
  - Output: before update 2, after update 1

## 6) Segment Tree Beats (Range Chmin/Chmax/Add/Sum)
- Slug: segment-tree-beats
- Difficulty: Hard
- Problem: Support range chmin, chmax, add, and sum queries.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Example:
  - Input: arr=[5,1,4]; chmin(0,2,3); query sum(0,2)
  - Output: 8

## 7) 2D BIT for Points
- Slug: bit-2d-points
- Difficulty: Medium
- Problem: Support point add and rectangle sum queries on grid coords up to 1e5 using compressed 2D Fenwick.
- Constraints: `1 <= ops <= 2 * 10^5`.
- Example:
  - Input: add (1,1,5), add (2,3,2), query (1,1)-(2,3)
  - Output: 7

## 8) Mergeable Segment Trees (Multiset Union)
- Slug: mergeable-segtrees
- Difficulty: Medium
- Problem: Maintain disjoint sets each with a segment tree of frequencies over values. Support merge of two sets and query k-th smallest in a set.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Example:
  - Input: sets A:[1,4], B:[2]; merge A,B; query kth=2
  - Output: 2

## 9) Range Convolution Updates
- Slug: range-convolution-updates
- Difficulty: Hard
- Problem: Maintain array a; support point updates and queries asking convolution sum over window: sum_{i=l..r} a[i]*b[i-l] for fixed kernel b length <= 500.
- Constraints: `1 <= n <= 2 * 10^5`, `q <= 2 * 10^5`.
- Hint: Segment tree storing dot-product with kernel prefix; or sqrt decomp.
- Example:
  - Input: a=[1,2,3], b=[2,1], query l=0 r=1 => 1*2+2*1=4
  - Output: 4

## 10) Range Minimum Query on Dynamic Array
- Slug: rmq-dynamic-array
- Difficulty: Medium
- Problem: Support insert at end, delete from end, and RMQ on current array.
- Constraints: `1 <= ops <= 2 * 10^5`.
- Hint: Segment tree over max size; maintain size pointer.
- Example:
  - Input: push 3, push 1, min(0,1), pop, min(0,0)
  - Output: [1,3]

## 11) Offline Range Distinct Count with Mo
- Slug: offline-range-distinct-mo
- Difficulty: Medium
- Problem: Answer queries for number of distinct values in [l,r] offline using Mo’s algorithm.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Example:
  - Input: a=[1,2,1,3], query [1,3]
  - Output: 3

## 12) Mo’s on Tree for Path Queries
- Slug: mos-on-tree-path
- Difficulty: Hard
- Problem: Given a tree with colors, offline answer queries asking distinct colors on path (u,v). Use Euler + Mo on tree.
- Constraints: `1 <= n,q <= 2 * 10^5`.
- Example:
  - Input: path 1-2-3, colors [1,2,1], query (1,3)
  - Output: 2

## 13) Dynamic Segment Tree for Sparse Coordinates
- Slug: dynamic-segtree-sparse
- Difficulty: Medium
- Problem: Support point updates and range sum queries on coordinate range up to 1e18 using dynamic nodes.
- Constraints: `1 <= q <= 2 * 10^5`.
- Example:
  - Input: update(1e12,5), update(2e12,3), query(0,3e12)
  - Output: 8

## 14) Interval Stabbing Count with Fenwick Offline
- Slug: interval-stabbing-count
- Difficulty: Medium
- Problem: Given intervals and points, count how many intervals stab each point. Offline sweep with Fenwick.
- Constraints: `1 <= intervals, points <= 2 * 10^5`.
- Example:
  - Input: intervals [1,3],[2,4]; points [2,5]
  - Output: [2,0]
