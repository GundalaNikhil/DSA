# LNK-061: LRU Cache with Time-Decay

## Problem Statement

You maintain a cache of capacity `C`. Each item has a score:

```
score = last_access_time - decay * age
```

where `age = current_time - last_access_time`. On `PUT` when full, evict the item with lowest score (tie by oldest access time).

Operations:

- `GET key t`
- `PUT key value t`

Output the value for each `GET` or `-1` if missing.

## Input Format

- First line: integers `C` and `decay`
- Second line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output value or `-1`

## Constraints

- `1 <= C <= 200000`
- `0 <= decay <= 10^9`
- Timestamps are non-decreasing

## Clarifying Notes

- `GET` updates `last_access_time` if hit.
- `PUT` updates value if key exists.

## Example Input

```
2 1
4
PUT a 1 0
PUT b 2 1
GET a 2
PUT c 3 3
```

## Example Output

```
1
```
