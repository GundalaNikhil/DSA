# DP-045: DP with Hysteresis

## Problem Statement

A system has two modes: OFF and ON. It has a level `L` that changes with actions. You can turn ON only if `L >= A`, and can turn OFF only if `L <= B` (with `B < A`). Each step you choose an action that changes `L` by `delta` and yields reward `r`.

Start in OFF with `L = 0`. Maximize total reward in `n` steps.

## Input Format

- First line: integers `n`, `A`, `B`
- Second line: integer `a` (number of actions)
- Next `a` lines: `delta r`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `0 <= B < A <= 50`
- `-10 <= delta <= 10`
- `-10^9 <= r <= 10^9`
- Level is capped in `[0, 50]` for DP.

## Clarifying Notes

- Mode switching does not consume a step; it can occur after applying the action if thresholds allow.

## Example Input

```
3 3 1
2
2 5
-1 0
```

## Example Output

```
10
```
