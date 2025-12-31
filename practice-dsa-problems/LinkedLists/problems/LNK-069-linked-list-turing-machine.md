# LNK-069: Linked List as Turing Machine

## Problem Statement

A linked list represents a tape of symbols `0` and `1`. A head points to a node. You are given a set of state transitions:

```
(state, symbol) -> (new_symbol, move, new_state)
```

where `move` is `L` or `R`. Simulate exactly `T` steps or stop early if no transition exists. Output the final tape and head position.

## Input Format

- First line: integers `n`, `S`, `T`
- Second line: string of length `n` (tape)
- Third line: integer `h` (head position, 1-based)
- Next line: integer `m` (number of transitions)
- Next `m` lines: `state symbol new_symbol move new_state`

## Output Format

- First line: final head position
- Second line: final tape string

## Constraints

- `1 <= n <= 200000`
- `1 <= S <= 20`
- `0 <= T <= 200000`

## Clarifying Notes

- Head cannot move beyond tape ends; if move would go out of bounds, halt.

## Example Input

```
3 2 2
010
2
2
0 1 1 R 1
1 0 1 L 0
```

## Example Output

```
2
110
```
