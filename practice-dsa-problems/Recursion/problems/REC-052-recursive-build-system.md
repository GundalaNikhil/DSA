# REC-052: Recursive Build System

## Problem Statement

You are given a dependency graph of build targets. Each target has a build time cost and a last built timestamp. Source files are modeled as targets with no dependencies.

A target must be rebuilt if any dependency's current timestamp is greater than its own timestamp. When rebuilt, its new timestamp becomes `max(dep timestamps) + 1` and its cost is added to the total build time.

Compute the total build time required to update the target `S` and return its final timestamp.

## Input Format

- First line: integers `n`, `m`, and `S`
- Next `n` lines: `cost time`
- Next `m` lines: directed edges `u v` meaning `u` depends on `v`

## Output Format

- Two integers: `total_cost` and `final_timestamp` for `S`

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `0 <= cost <= 10^9`
- `0 <= time <= 10^9`

## Clarifying Notes

- Dependencies are evaluated recursively; each target is considered once.
- Cycles do not occur in the dependency graph.

## Example Input

```
3 2 1
5 10
3 12
2 9
1 2
1 3
```

## Example Output

```
5 13
```
