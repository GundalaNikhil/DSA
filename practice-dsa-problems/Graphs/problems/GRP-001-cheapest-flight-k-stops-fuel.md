---
problem_id: GRP_CHEAPEST_FLIGHT_K_STOPS_FUEL__4796
display_id: NTB-GRP-4796
slug: cheapest-flight-k-stops-fuel
title: "Cheapest Flight Within K Stops with Fuel State"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - cheapest-flight-k-stops-fuel
  - coding-interviews
  - data-structures
  - graphs
  - search
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Cheapest Flight Within K Stops with Fuel State

## Problem Statement

You are given a directed graph of flights. Each flight `(u, v)` consumes a fixed amount of fuel. At each node, you can buy fuel at a per-unit cost specific to that node. You start at node `s` with 0 fuel and want to reach node `t` using at most `K` flights.

Your task is to compute the minimum total fuel cost to reach `t`. If it is impossible within `K` flights, output `-1`.

## Input Format

- First line: integers `n`, `m`, `s`, `t`, `K`, `C`
  - `C` is the maximum fuel capacity
- Second line: `n` integers `cost_1 ... cost_n` (fuel cost per unit at each node)
- Next `m` lines: `u v fuel` describing a directed edge that consumes `fuel` units

## Output Format

- Single integer: minimum total cost, or `-1` if unreachable within `K` flights

## Constraints

- `1 <= n, m <= 1000`
- `1 <= s, t <= n`
- `0 <= K <= 100`
- `1 <= C <= 100`
- `0 <= cost_i <= 10^9`
- `1 <= fuel <= C`

## Clarifying Notes

- You can buy fuel in any non-negative integer amount as long as current fuel does not exceed `C`.
- Each flight consumes exactly its fuel requirement and increases the stop count by 1.
- The intended solution uses Dijkstra on state `(node, stops_used, fuel)`.

## Example Input

```
3 3 1 3 2 5
5 2 4
1 2 3
2 3 3
1 3 5
```

## Example Output

```
21
```
