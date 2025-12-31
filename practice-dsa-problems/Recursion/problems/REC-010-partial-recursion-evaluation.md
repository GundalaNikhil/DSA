# REC-010: Partial Recursion Evaluation

## Problem Statement

You are given a rooted tree. Each node has two values: `exact` and `estimate`. A recursive evaluation returns:

- If depth <= `D`: `exact + sum(child results)`
- If depth > `D`: `estimate` (children are not evaluated)

Compute the value returned from the root.

## Input Format

- First line: integers `n` and `D`
- Next `n` lines: `exact estimate parent` (parent is 0 for root)

## Output Format

- Single integer: root value

## Constraints

- `1 <= n <= 200000`
- `0 <= D <= 200000`
- `-10^9 <= exact, estimate <= 10^9`

## Clarifying Notes

- Depth of root is 0.

## Example Input

```
3 0
5 1 0
2 10 1
3 10 1
```

## Example Output

```
1
```
