# AGR-002: Minimum Spanning Tree with Post-Processing Penalties

## Problem Statement

You are given a connected, undirected graph with `n` nodes and `m` edges. Each edge has a base weight `w` and a penalty `p`.

Build a minimum spanning tree using **only the base weights** (standard Kruskal on `w`). After the MST is selected, the final cost is:

```
(sum of base weights in the MST) + (sum of penalties of the selected edges)
```

If the graph is not connected, output `-1`.

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w p`

## Output Format

- Single integer: final cost after adding penalties, or `-1` if no spanning tree exists

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `1 <= u, v <= n`
- `-10^9 <= w, p <= 10^9`

## Clarifying Notes

- Edge selection is based **only** on base weight `w` (penalties do not affect the choice).
- If multiple edges have the same base weight, any tie-breaking order consistent with Kruskal is valid.

## Example Input

```
4 5
1 2 1 5
2 3 2 0
3 4 1 1
1 4 3 0
2 4 4 10
```

## Example Output

```
10
```
