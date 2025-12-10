# Candy Distribution Problem

**Problem ID:** GRDY-005
**Display ID:** 82
**Question Name:** Candy Distribution
**Slug:** candy-distribution
**Title:** Candy Distribution Problem
**Difficulty:** Hard
**Premium:** Yes
**Tags:** Greedy, Array, Two Pass

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

There are n children standing in a line. Each child is assigned a rating value given in the integer array `ratings`. You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy
2. Children with a higher rating get more candies than their neighbors

Return the minimum number of candies you need to distribute.

## A Simple Scenario (Daily Life Usage)

Imagine you're a teacher distributing candy rewards to students based on their test scores. Each student must get at least one candy, but students with higher scores than their neighbors should get more candy to be fair. You want to minimize the total number of candies used while maintaining fairness. For example, if three students scored 1, 2, and 1 respectively, you'd give them 1, 2, and 1 candies (total 4), not 1, 3, 1 or higher.

## Your Task

Write a function that takes an array of ratings and returns the minimum total number of candies needed to satisfy the distribution rules.

## Why is it Important?

This problem teaches you how to:

- Apply greedy algorithms to constraint satisfaction problems
- Use two-pass algorithms for bidirectional dependencies
- Optimize resource distribution with competing constraints
- Handle local vs. global optimization challenges
- Recognize when multiple passes are necessary for correctness

## Examples

### Example 1:

**Input:** `ratings = [1,0,2]`
**Output:** `5`
**Explanation:**
- Child 0: rating 1, gets 2 candies (higher than neighbor with rating 0)
- Child 1: rating 0, gets 1 candy (minimum)
- Child 2: rating 2, gets 2 candies (higher than neighbor with rating 0)
Total = 2 + 1 + 2 = 5 candies

### Example 2:

**Input:** `ratings = [1,2,2]`
**Output:** `4`
**Explanation:**
- Child 0: rating 1, gets 1 candy
- Child 1: rating 2, gets 2 candies (higher than left neighbor)
- Child 2: rating 2, gets 1 candy (same rating as neighbor, no constraint)
Total = 1 + 2 + 1 = 4 candies

### Example 3:

**Input:** `ratings = [1,3,2,2,1]`
**Output:** `7`
**Explanation:** Optimal distribution is [1,2,1,2,1] = 7 candies total.

## Constraints

- 1 ≤ ratings.length ≤ 2 * 10^4
- 0 ≤ ratings[i] ≤ 2 * 10^4

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Facebook
- Microsoft

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
