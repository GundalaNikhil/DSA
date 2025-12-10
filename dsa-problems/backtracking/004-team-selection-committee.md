# Team Selection Committee

**Problem ID:** BACK-004
**Display ID:** 63
**Question Name:** Team Selection Committee
**Slug:** team-selection-committee
**Title:** Combinations
**Difficulty:** Medium
**Premium:** No
**Tags:** Backtracking, Array, Recursion

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

## A Simple Scenario (Daily Life Usage)

Imagine you're organizing a company hackathon and need to form teams. You have 5 volunteers and need to select 3 people for each team. How many different teams can you create? This problem helps you generate all possible team combinations. For example, from people numbered 1-5, choosing 3 gives you: [1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5], [1,4,5], [2,3,4], [2,3,5], [2,4,5], [3,4,5].

## Your Task

Write a function that generates all possible combinations of k numbers from 1 to n.

## Why is it Important?

This problem teaches you how to:

- Generate combinations using backtracking
- Understand the difference between permutations and combinations
- Avoid duplicate combinations by maintaining order
- Optimize with pruning techniques
- Calculate combinatorial mathematics programmatically

## Examples

### Example 1:

**Input:** `n = 4, k = 2`
**Output:** `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`
**Explanation:** All possible ways to choose 2 numbers from [1,2,3,4].

### Example 2:

**Input:** `n = 1, k = 1`
**Output:** `[[1]]`
**Explanation:** Only one way to choose 1 number from [1].

### Example 3:

**Input:** `n = 5, k = 3`
**Output:** `[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]`
**Explanation:** C(5,3) = 10 combinations.

### Example 4:

**Input:** `n = 3, k = 3`
**Output:** `[[1,2,3]]`
**Explanation:** Only one way to choose all 3 numbers.

## Constraints

- 1 ≤ n ≤ 20
- 1 ≤ k ≤ n

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Google
- Amazon
- Microsoft
- LinkedIn
- Facebook
- Apple

## Hints

1. Use backtracking with a start index to avoid duplicates
2. Only explore numbers greater than the last number added
3. When combination size equals k, add it to results
4. Prune early: if remaining numbers can't fill k slots, backtrack
5. The formula for combinations is C(n,k) = n! / (k! × (n-k)!)
6. Keep combinations in sorted order by always choosing increasing numbers

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
