# LNK-047: Linked List Event Sourcing

## Problem Statement

You are given an event log of list operations. The list is empty at time 0. Each event has a time and is one of:

- `INS pos x`
- `DEL pos`

For each query time `t`, reconstruct the list after applying all events with time `<= t`, then output the value at position `pos` (or `-1`).

## Input Format

- First line: integer `e` (number of events)
- Next `e` lines: `time type pos [x]`
- Next line: integer `q`
- Next `q` lines: `t pos`

## Output Format

- For each query, output one integer

## Constraints

- `1 <= e, q <= 200000`
- `0 <= time <= 10^9`
- Event times are non-decreasing

## Clarifying Notes

- Positions are 1-based at the time of the event.

## Example Input

```
3
1 INS 1 5
2 INS 2 7
3 DEL 1
2
2 1
3 1
```

## Example Output

```
5
7
```
