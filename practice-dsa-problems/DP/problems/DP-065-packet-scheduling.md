# DP-065: Network Packet Scheduling DP

## Problem Statement

You have `n` packets, each with deadline `d_i` and value `v_i`. Each packet takes 1 time unit and must be scheduled before or at its deadline. At most one packet can be sent per time unit.

Maximize total value.

## Input Format

- First line: integer `n`
- Next `n` lines: `d_i v_i`

## Output Format

- Single integer: maximum total value

## Constraints

- `1 <= n <= 2000`
- `1 <= d_i <= 2000`
- `0 <= v_i <= 10^9`

## Clarifying Notes

- This is a DP over time and packets.

## Example Input

```
3
1 5
2 6
2 4
```

## Example Output

```
11
```
