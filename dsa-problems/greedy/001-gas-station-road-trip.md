# Gas Station Circuit

**Problem ID:** GRDY-001
**Display ID:** 78
**Question Name:** Gas Station Road Trip
**Slug:** gas-station-road-trip
**Title:** Gas Station Circuit
**Difficulty:** Medium
**Premium:** No
**Tags:** Greedy, Array, Simulation

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are planning a circular road trip with n gas stations along the route. You have two arrays: `gas[i]` represents the amount of gas available at station i, and `cost[i]` represents the gas needed to travel from station i to station i+1. Your car starts with an empty tank, and you can only travel if you have enough gas. Find the starting gas station index from which you can complete the entire circular route. If no such starting point exists, return -1.

## A Simple Scenario (Daily Life Usage)

Imagine you're planning a cross-country road trip along a circular highway with several gas stations. Each station has different amounts of gas available, and the distance between stations varies (requiring different amounts of gas). You need to figure out which gas station to start from so you can complete the entire loop without running out of gas. If you start from the wrong station, you might get stranded halfway through!

## Your Task

Write a function that takes two arrays `gas` and `cost` and returns the index of the starting gas station that allows you to complete the circuit. If it's impossible to complete the circuit, return -1.

## Why is it Important?

This problem teaches you how to:

- Apply greedy algorithm thinking to optimization problems
- Recognize when a single pass solution exists
- Handle circular array traversal
- Understand cumulative sum patterns
- Optimize brute force approaches to linear time solutions

## Examples

### Example 1:

**Input:** `gas = [3, 5, 2, 6, 4]`, `cost = [4, 3, 7, 2, 3]`
**Output:** `1`
**Explanation:** Start at station 1 (0-indexed):
- Tank = 0 + 5 - 3 = 2 (station 1 to 2)
- Tank = 2 + 2 - 7 = -3 (fails if started here)
Starting from station 1 allows completing the circuit.

### Example 2:

**Input:** `gas = [1, 2, 3]`, `cost = [4, 5, 2]`
**Output:** `-1`
**Explanation:** Total gas available = 1+2+3 = 6. Total cost = 4+5+2 = 11. Since total gas < total cost, it's impossible to complete the circuit.

### Example 3:

**Input:** `gas = [6, 2, 3, 4, 5]`, `cost = [3, 6, 2, 7, 1]`
**Output:** `0`
**Explanation:** Starting at station 0 with 6 gallons allows completing the entire circuit without running out of gas.

## Constraints

- 1 ≤ gas.length == cost.length ≤ 10^4
- 0 ≤ gas[i], cost[i] ≤ 10^4

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Microsoft
- Tesla

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
