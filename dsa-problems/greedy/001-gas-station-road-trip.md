# Gas Station Circuit

**Problem ID:** GRDY-001
**Display ID:** 78
**Question Name:** Gas Station Road Trip
**Slug:** gas-station-road-trip
**Title:** Gas Station Circuit
**Difficulty:** Medium
**Premium:** No
**Tags:** Greedy, Array, Simulation

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

**Input:** `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`
**Output:** `3`
**Explanation:** Start at station 3 (0-indexed):
- Tank = 0 + 4 - 1 = 3 (station 3 to 4)
- Tank = 3 + 5 - 2 = 6 (station 4 to 0)
- Tank = 6 + 1 - 3 = 4 (station 0 to 1)
- Tank = 4 + 2 - 4 = 2 (station 1 to 2)
- Tank = 2 + 3 - 5 = 0 (station 2 to 3)
Complete the circuit with tank = 0.

### Example 2:

**Input:** `gas = [2,3,4]`, `cost = [3,4,3]`
**Output:** `-1`
**Explanation:** Total gas available = 2+3+4 = 9. Total cost = 3+4+3 = 10. Since total gas < total cost, it's impossible to complete the circuit.

### Example 3:

**Input:** `gas = [5,1,2,3,4]`, `cost = [4,4,1,5,1]`
**Output:** `4`
**Explanation:** Starting at station 4 allows completing the entire circuit without running out of gas.

## Constraints

- 1 ≤ gas.length == cost.length ≤ 10^4
- 0 ≤ gas[i], cost[i] ≤ 10^4

## Asked by Companies

- Amazon
- Google
- Microsoft
- Tesla
