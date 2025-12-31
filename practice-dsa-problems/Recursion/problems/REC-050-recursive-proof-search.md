# REC-050: Recursive Proof Search

## Problem Statement

You are given a set of inference rules. Each rule has a head symbol and a list of prerequisite symbols. A symbol is provable if there exists a rule whose prerequisites are all provable.

Given a start symbol `S`, compute the minimum number of rule applications needed to prove `S`. If `S` is not provable, output `IMPOSSIBLE`.

## Input Format

- First line: integers `R` and `S`
- Next `R` lines: `head k prereq1 prereq2 ... prereqk`

## Output Format

- Single integer: minimum number of rule applications, or `IMPOSSIBLE`

## Constraints

- `1 <= R <= 200000`
- `1 <= S <= 200000`
- `0 <= k <= 10`

## Clarifying Notes

- A rule with `k = 0` can be applied immediately and proves its head.
- Cycles do not imply provability; you must resolve them with base rules.

## Example Input

```
4 3
1 0
2 1 1
3 2 1 2
4 1 3
```

## Example Output

```
3
```
