---
title: Range XOR Basis
slug: range-xor-basis
difficulty: Medium
difficulty_score: 56
tags:
- Segment Tree
- Linear Basis
- Bitwise
problem_id: SEG_RANGE_XOR_BASIS__8820
display_id: SEG-007
topics:
- Segment Tree
- Bitwise
- Linear Basis
---
# Range XOR Basis - Editorial

## Problem Summary

You are given an array `a` and need to support two operations:
1.  **SET i x**: Update `a[i] = x`.
2.  **MAXXOR l r**: Find the maximum XOR sum of any subset of elements in the range `a[l..r]`.


## Constraints

- `1 <= n, q <= 100000`
- `0 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Digital Signal Processing** system where you have a stream of signals. You want to combine a subset of signals (using XOR, which corresponds to addition in GF(2)) to produce the strongest possible signal (maximum value) within a specific time window. As new signals arrive or old ones are corrected, you need to re-evaluate the maximum potential signal strength.

## Problem Exploration

### 1. Linear Basis
The "Maximum Subset XOR" problem is classically solved using a **Linear Basis**.
A Linear Basis for a set of numbers is a minimal set of numbers such that any XOR sum achievable from the original set is also achievable from the basis.
-   Size of basis is at most `log(max(A_i)) ~= 30`.
-   We can merge two bases `B_1` and `B_2` by inserting every element of `B_2` into `B_1`. Size remains `<= 30`.
-   Merging takes `O(B^2)` or `O(B)` depending on implementation. Since `B` is small (30), this is efficient.

### 2. Segment Tree with Linear Basis
We can build a Segment Tree where each node stores the Linear Basis of the numbers in its range.
-   **Leaf Node**: Basis contains just `a[i]`.
-   **Internal Node**: Merge bases of left and right children.
-   **Update**: Update leaf, then re-merge up the tree. `O(B^2 log N)`.
-   **Query**: Query range `[l, r]`, merge bases of `O(log N)` segments, then compute max XOR. `O(B^2 log N)`.

With `B=30`, `B^2 ~= 900`. `N, Q = 100,000`.
`10^5 x 900 x 17 ~= 1.5 x 10^9`. This is a bit slow for 2 seconds.
We need to optimize the merge or be careful with constants.
Can we do better?
Standard merge is: take all elements of one basis and insert into other.
Since basis size is small, this is acceptable if implemented efficiently.

## Approaches

### Approach 1: Segment Tree with Linear Basis
-   **Node**: `vector<int> basis`.
-   **Merge**: Insert elements of `right` into `left`.
-   **Query**: Accumulate basis from relevant nodes.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 1`
`1 2 3`
`MAXXOR 0 2`

1.  **Build**:
    -   Leaf `[0]`: Basis `{1}`.
    -   Leaf `[1]`: Basis `{2}`.
    -   Leaf `[2]`: Basis `{3}`.
    -   Root `[0, 2]`: Merge `{1}`, `{2}`, `{3}`.
        -   Insert 1: B=`{1}`.
        -   Insert 2: B=`{1, 2}`.
        -   Insert 3: `3 oplus 2 = 1`, `1 oplus 1 = 0`. 3 is linearly dependent. B remains `{1, 2}`.
2.  **Query**: `MAXXOR 0 2`.
    -   Returns basis `{1, 2}`.
    -   `maxXor`:
        -   Start 0.
        -   Bit 1 (val 2): `0 ^ 2 = 2 > 0`. Res=2.
        -   Bit 0 (val 1): `2 ^ 1 = 3 > 2`. Res=3.
3.  **Result**: 3.

## Proof of Correctness

-   **Linear Basis Property**: The basis of a union of sets is the merge of their bases.
-   **Segment Tree**: Correctly decomposes range into `O(log N)` canonical sub-ranges. Merging their bases gives the basis for the full range.

## Interview Extensions

1.  **Persistent Basis?**
    -   If we need to query past versions, use Persistent Segment Tree.
2.  **Greedy Basis Construction**:
    -   Standard algorithm is greedy (Gaussian elimination). It always finds *a* basis.
3.  **Basis Intersection**:
    -   Much harder. Intersection of vector spaces.

### Common Mistakes

-   **Basis Size**: 30 bits is enough for `10^9`. Don't use 64 unless needed.
-   **Merge Logic**: Don't just copy arrays. You must `insert` elements to maintain the triangular basis property.
