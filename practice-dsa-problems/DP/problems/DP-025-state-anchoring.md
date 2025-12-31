# DP-025: DP with State Anchoring

## Problem Statement

You have `n` steps and `s` states. Some states are anchors. You must not go more than `L` steps without visiting an anchor. Each step in state `j` yields reward `R[j]`.

Maximize total reward over `n` steps.

## Input Format

- First line: integers `n`, `s`, `L`
- Second line: `s` integers: rewards `R[1..s]`
- Third line: integer `a` (number of anchors)
- Fourth line: `a` integers: anchor state ids

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `1 <= s <= 20`
- `1 <= L <= n`

## Clarifying Notes

- State can change freely each step.
- Counter resets to 0 when an anchor is visited.

## Example Input

```
3 3 2
5 2 1
1
1
```

## Example Output

```
15
```
