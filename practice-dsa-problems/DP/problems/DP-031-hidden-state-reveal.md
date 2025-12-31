# DP-031: DP with Hidden State Reveal

## Problem Statement

There are `m` modules, each with a fixed bonus `b_i` that is revealed only when you activate it. You are given all bonuses in input, but a module's bonus only starts contributing after it is activated.

You have `n` steps. At each step, you either activate one inactive module or perform a task. A task yields reward equal to the sum of bonuses of all activated modules.

Maximize total reward.

## Input Format

- First line: integers `n` and `m`
- Second line: `m` integers: bonuses `b_1..b_m`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 30`
- `1 <= m <= 15`
- `0 <= b_i <= 100`

## Clarifying Notes

- Activation consumes the whole step and yields no immediate reward.
- State includes the set of activated modules.

## Example Input

```
3 2
5 2
```

## Example Output

```
7
```
