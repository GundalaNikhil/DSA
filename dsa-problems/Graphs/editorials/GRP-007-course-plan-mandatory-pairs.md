---
problem_id: GRP_COURSE_PLAN_MANDATORY__5183
display_id: GRP-007
slug: course-plan-mandatory-pairs
title: "Course Plan with Mandatory Pairs"
difficulty: Medium
difficulty_score: 55
topics:
  - Topological Sort
  - Directed Acyclic Graph
  - Graph Contraction
tags:
  - graph
  - topological-sort
  - dag
  - scheduling
  - medium
premium: true
subscription_tier: basic
---

# GRP-007: Course Plan with Mandatory Pairs

## 📋 Problem Summary

Produce a topological ordering of courses that respects both prerequisite constraints and mandatory adjacency pairs. This combines standard topological sort with the constraint that certain course pairs must appear adjacent in the final schedule.

## 🌍 Real-World Scenario

**Scenario Title:** University Course Scheduling with Lab Pairs

Imagine scheduling university courses where some courses have prerequisites (must be taken before others) and some courses have mandatory lab components that must be scheduled in consecutive time slots. For example, "Chemistry Theory" and "Chemistry Lab" must be adjacent, and "Physics 1" must come before "Physics 2".

The challenge is to create a valid semester schedule that satisfies both types of constraints. This is common in academic planning where theory-lab pairs, lecture-tutorial pairs, or related courses need to be consecutive for pedagogical or logistical reasons.

**Why This Problem Matters:**

- **Academic Scheduling:** Course timetabling with paired sessions
- **Task Scheduling:** Jobs with setup/cleanup phases that must be adjacent
- **Manufacturing:** Processes with mandatory consecutive steps
- **Project Planning:** Tasks with hard adjacency requirements

![Real-World Application](../images/GRP-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Topological Sort with Pairs

```
Prerequisites: 0→2, 1→2
Mandatory pair: (2,3) must be adjacent

Graph:
    0 ↘
         2 → 3
    1 ↗

Valid orderings:
[0, 1, 2, 3] ✓ (2 and 3 adjacent)
[1, 0, 2, 3] ✓ (2 and 3 adjacent)

Invalid:
[0, 2, 1, 3] ✗ (2 and 3 not adjacent)

Approach: Contract (2,3) into super-node,
run topological sort, then expand.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Prerequisite edges:** Directed edges representing "must come before"
- **Adjacency pairs:** Undirected pairs that must be consecutive in output
- **Valid ordering:** Satisfies all prerequisites AND all adjacency constraints
- **Multiple solutions:** Any valid ordering is acceptable

Common interpretation mistake:

- ❌ **Wrong:** Treating adjacency pairs as prerequisite edges
- ✅ **Correct:** Adjacency means consecutive in final ordering, not dependency

### Core Concept

**Graph Contraction:** Merge each adjacency pair into a single super-node, perform topological sort on the contracted graph, then expand super-nodes back to individual courses maintaining the pair adjacency.

## Optimal Approach

### Algorithm

```
course_schedule(n, prerequisites, pairs):
    # Step 1: Create super-nodes for adjacency pairs
    parent = [i for i in range(n)]  # Union-Find
    
    for (a, b) in pairs:
        union(a, b, parent)
    
    # Step 2: Build contracted graph
    contracted_adj = build_contracted_graph(prerequisites, parent)
    
    # Step 3: Topological sort on contracted graph
    topo_order = topological_sort(contracted_adj)
    
    if topo_order is empty:
        return []  # Cycle detected or impossible
    
    # Step 4: Expand super-nodes
    result = []
    for super_node in topo_order:
        members = get_members(super_node, parent)
        # Order members respecting internal prerequisites
        result.extend(order_members(members, prerequisites))
    
    return result
```

### Time Complexity

- **O(n + m + p)** where n=courses, m=prerequisites, p=pairs
- Union-Find: O(p × α(n))
- Topological sort: O(n + m)

### Space Complexity

- **O(n + m)** for graph and auxiliary structures

![Algorithm Visualization](../images/GRP-007/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: n=4, prerequisites=[(0,2), (1,2)], pairs=[(2,3)]

1. Union pairs: {2,3} become super-node
2. Contracted graph: 0→{2,3}, 1→{2,3}
3. Topological sort: [0, 1, {2,3}] or [1, 0, {2,3}]
4. Expand: [0, 1, 2, 3] or [1, 0, 2, 3]

Both satisfy: 0 before 2, 1 before 2, and 2 adjacent to 3 ✓

![Example Visualization](../images/GRP-007/example-1.png)

## ✅ Proof of Correctness

**Theorem:** If a valid ordering exists, graph contraction + topological sort finds it.

**Proof:**
- Contraction preserves prerequisite relationships between super-nodes
- Topological sort ensures prerequisite order
- Expansion maintains adjacency within super-nodes

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Handle multiple adjacency pairs per course
- **Extension 2:** Minimize total schedule length with time constraints
- **Extension 3:** Find all valid orderings
- **Extension 4:** Handle conflicts (impossible to satisfy all constraints)

### Common Mistakes to Avoid

1. **Treating Pairs as Prerequisites**
   - ❌ Wrong: Adding directed edges for pairs
   - ✅ Correct: Using Union-Find to group pairs
   - **Impact:** Incorrect ordering

2. **Not Checking for Cycles**
   - ❌ Wrong: Assuming topological sort always succeeds
   - ✅ Correct: Validate topo_order.size() == num_super_nodes
   - **Description:** Prerequisites might form a cycle

3. **Incorrect Super-Node Expansion**
   - ❌ Wrong: Random order within super-nodes
   - ✅ Correct: Respect internal prerequisites when expanding
   - **Prevention:** Check prerequisites within super-nodes

4. **Forgetting Self-Loops**
   - ❌ Wrong: Not checking if from_root == to_root
   - ✅ Correct: Skip edges within same super-node
   - **Description:** Contracted edges to same node create issues

5. **Not Handling Disconnected Components**
   - ❌ Wrong: Only processing one component
   - ✅ Correct: Ensure all super-nodes are in topological order
   - **Description:** Missing courses in output

## Related Concepts

- **Standard Topological Sort:** Kahn's algorithm, DFS-based
- **Graph Contraction:** Merging nodes while preserving structure
- **Union-Find (DSU):** Efficient set operations for grouping
- **Constraint Satisfaction:** CSP with ordering constraints
- **Job Scheduling:** Real-world application of topological sort
