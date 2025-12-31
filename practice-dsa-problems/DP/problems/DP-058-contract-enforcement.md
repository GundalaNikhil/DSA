# DP-058: DP with Contract Enforcement

## Problem Statement

Some actions create contracts that must be fulfilled within `D` steps. A contract requires you to take a specific action type within that window or pay penalty `P`.

Maximize total reward minus penalties.

## Input Format

- First line: integers `n`, `a`, `D`, `P`
- Next `a` lines: `reward_i creates_contract` (0/1)

## Output Format

- Single integer: maximum total score

## Constraints

- `1 <= n <= 50`
- `1 <= a <= 6`
- `0 <= reward_i <= 50`
- `0 <= D <= 5`
- `0 <= P <= 50`

## Clarifying Notes

- A contract requires taking the same action type that created it.
- Multiple contracts can overlap and are tracked separately.

## Example Input

```
3 2 2 4
5 1
2 0
```

## Example Output

```
11
```
