---
problem_id: GRP_EXAM_SEATING_VIP__3928
display_id: GRP-012
slug: exam-seating-rooms-vip
title: "Exam Seating Rooms with VIP Isolation"
difficulty: Easy-Medium
difficulty_score: 40
topics:
  - Union-Find
  - Connected Components
  - Greedy
tags:
  - graph
  - union-find
  - dsu
  - greedy
  - medium
premium: true
subscription_tier: basic
---

# GRP-012: Exam Seating Rooms with VIP Isolation

## 📋 Problem Summary

You are given a graph of students and friendships. Some students are **VIPs**. You must remove the **minimum number of edges** such that no two VIPs belong to the same connected component. After doing so, return the **size of the largest remaining connected component**.

## 🌍 Real-World Scenario

**Scenario Title:** Secure Conference Zones

You are organizing a high-security summit.
-   **Nodes:** Delegates.
-   **Edges:** Professional connections (they want to network).
-   **VIPs:** Heads of State.

**Constraint:** For security, no two Heads of State can be in the same "networking zone" (connected component).
**Goal:** You want to keep as many connections as possible to facilitate networking, but you must cut connections to isolate the Heads of State from each other.
**Metric:** What is the size of the largest resulting networking zone?

## Detailed Explanation

### ASCII Diagram: Isolating VIPs

**Initial Graph:**
```
(VIP1) -- A -- B -- (VIP2)
          |
          C
```
**VIPs:** {VIP1, VIP2}

**Analysis:**
-   VIP1 and VIP2 are connected via A and B. We must cut this path.
-   We want to remove *minimum* edges. This implies we keep *maximum* edges.
-   We can keep `(VIP1, A)` and `(A, C)`.
-   We can keep `(B, VIP2)`.
-   We MUST cut `(A, B)` to separate the groups.
-   **Resulting Components:**
    1.  `{VIP1, A, C}` (Size 3)
    2.  `{VIP2, B}` (Size 2)
-   **Max Size:** 3.

Alternatively, if we gave `{A, B, C}` all to VIP2:
-   Components: `{VIP1}`, `{VIP2, A, B, C}` (Size 4).
-   This requires cutting `(VIP1, A)`.
-   Max Size: 4.

**Conclusion:** To maximize the largest component, we should greedily attach the "neutral" (non-VIP) components to the VIP that allows for the biggest group.

### Algorithm: DSU + Greedy

1.  **Identify Node Types:**
    -   **VIP Nodes:** Cannot be merged with each other.
    -   **Neutral Nodes:** Can be merged with each other freely.

2.  **Step 1: Process Neutral-Neutral Edges**
    -   Use Union-Find (DSU) to merge all connected neutral nodes.
    -   Ignore edges connected to VIPs for now.
    -   Result: A set of "Neutral Components" (blobs of non-VIP students).

3.  **Step 2: Connect Neutral Components to VIPs**
    -   Iterate through edges connecting a VIP to a Neutral Node.
    -   For each VIP, identify which Neutral Components it is directly connected to.
    -   Calculate the potential size of the component if this VIP "claims" all its neighboring Neutral Components.
    -   `Potential Size = 1 (the VIP itself) + sum(size of all adjacent Neutral Components)`.

4.  **Step 3: Find Maximum**
    -   The answer is the maximum of:
        -   The size of any purely Neutral Component (in case it's larger than any VIP group).
        -   The maximum "Potential Size" calculated for any VIP.

### Why this works?
Since we want to maximize the *single largest component*, we can imagine picking one "Winner VIP" and letting it keep ALL its adjacent neutral neighbors. For all other VIPs, it doesn't matter if they keep their neighbors or not, because we only care about the maximum size.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Input:** `n`, `m`, list of edges, list of VIPs.
-   **Output:** Integer (max component size).
-   **VIPs:** Can be 0 to n. If 0 VIPs, return size of largest component in original graph.
-   **Edges:** Undirected.

## Optimal Approach

### Time Complexity

-   **O(M * α(N))**: Processing edges with DSU.
-   **O(N + M)**: Calculating sizes and iterating adjacency.
-   **Total:** O(M * α(N)).

### Space Complexity

-   **O(N)**: DSU arrays and auxiliary storage.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
3
0 1
1 2
3 4
2 3
```
**VIPs:** {2, 3}

1.  **Edges:** (0,1), (1,2), (3,4).
2.  **Non-VIPs:** {0, 1, 4}.
3.  **Step 1 (Neutral-Neutral):**
    -   (0,1): Both non-VIP. Union(0,1). Comp {0,1}, size 2.
    -   (1,2): 2 is VIP. Skip.
    -   (3,4): 3 is VIP. Skip.
    -   (0,1): Union. {0,1} size 2.
            -   (1,2): Skip (2 is VIP).
            -   (3,4): Skip (3 is VIP).
        -   **Step 2 (VIP Neighbors):**
            -   VIP 2: Connected to 1 (root 0). Neighbors = {0}.
            -   VIP 3: Connected to 4 (root 4). Neighbors = {4}.
        -   **Step 3 (Max Size):**
            -   VIP 2: 1 + size({0,1}) = 1 + 2 = 3.
            -   VIP 3: 1 + size({4}) = 1 + 1 = 2.
            -   Max = 3.
    -   **Matches Example Output (3).**

## ✅ Proof of Correctness

-   **Separation:** We never merge two VIPs because we only merge Neutral-Neutral, and then attach Neutrals to *one* VIP.
-   **Maximality:** We greedily assign all available neutral neighbors to each VIP and take the maximum. Since neutral components are disjoint and can be assigned independently to any *one* VIP neighbor, checking the max potential size for each VIP covers the optimal case.

### Common Mistakes to Avoid

1.  **Merging VIPs:** Accidentally unioning a VIP with another node before checking.
2.  **Double Counting:** If a VIP connects to multiple nodes in the *same* neutral component, ensure you only add that component's size once (use a Set of roots).
3.  **Ignoring Pure Neutral:** If there are no VIPs, the answer is just the largest component.
