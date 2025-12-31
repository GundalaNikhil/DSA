# AGR-001: Offline Dynamic Connectivity with Rollback DSU

## Problem Statement

You are given an undirected graph with `n` nodes and a sequence of `q` operations. The graph changes over time by adding and removing edges. For each query, determine whether two nodes are connected at that time.

Operations:

- `ADD u v`: add the edge `(u, v)`.
- `REM u v`: remove the edge `(u, v)`.
- `ASK u v`: output whether `u` and `v` are connected in the current graph.

Edges are identified by unordered pairs. An edge will not be added twice without being removed in between, and every `REM` refers to an active edge.

You must answer the queries in order using a rollback DSU with stack-based undo (offline dynamic connectivity).

## Input Format

- First line: integers `n` and `q`
- Next `q` lines: operations in the format above

## Output Format

- For each `ASK` operation, output `YES` or `NO` on its own line

## Constraints

- `1 <= n, q <= 200000`
- `1 <= u, v <= n`

## Clarifying Notes

- The problem is offline: you can read all operations before producing outputs.
- A correct solution uses a segment tree over time with rollback DSU.
- Edge endpoints can be given in any order; treat `(u, v)` the same as `(v, u)`.

## Example Input

```
4 7
ADD 1 2
ADD 2 3
ASK 1 3
REM 2 3
ASK 1 3
ADD 3 4
ASK 1 4
```

## Example Output

```
YES
NO
NO
```
