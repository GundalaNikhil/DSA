# REC-040: Recursive Partial Ordering

## Problem Statement

You are given a rooted tree. Each node has children with a partial order constraint: some child must be evaluated before another child. When a node evaluates its children, it chooses any order that respects all constraints.

The node's value is:

`v[node] + sum(orderIndex(child) * childValue)`

where `orderIndex(child)` is the 1-based position of that child in the chosen evaluation order, and `childValue` is the value returned by that child.

Compute the maximum possible value for the root, or report `IMPOSSIBLE` if any node's child constraints contain a cycle.

## Input Format

- First line: integer `n`
- Next `n` lines: `v parent` (parent is 0 for root)
- Next line: integer `c` (number of ordering constraints)
- Next `c` lines: `parent u v` meaning for `parent`, child `u` must be evaluated before child `v`

## Output Format

- Single integer: maximum root value, or `IMPOSSIBLE`

## Constraints

- `1 <= n <= 200000`
- Each node has at most `8` children
- `0 <= c <= 200000`
- `-10^9 <= v <= 10^9`

## Clarifying Notes

- Constraints are local to each parent; cycles at any parent make the result impossible.
- Child values are computed independently before ordering decisions at the parent.

## Example Input

```
5
1 0
2 1
3 1
4 1
5 1
2
1 2 3
1 3 4
```

## Example Output

```
29
```
