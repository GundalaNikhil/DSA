# MAT-016: Dynamic Submatrix Ownership

## Problem Statement

A grid starts with no owners (owner id 0). You receive `q` ownership claims. Each claim specifies a rectangle and metadata:

- Higher priority wins.
- If priorities tie, earlier timestamp wins.
- If both tie, larger area wins.
- If all tie, smaller claim id wins.

A claim replaces ownership of any covered cell if it wins by the rules above.

For each claim, report how many cells become owned by this claim after resolution. After all claims, output the final ownership grid.

## Input Format

- First line: integers `n`, `m`, `q`
- Next `q` lines: `r1 c1 r2 c2 priority timestamp`

## Output Format

- For each claim: one line with the number of newly owned cells
- After all claims: `n` lines with `m` integers (owner ids)

## Constraints

- `1 <= n, m <= 200`
- `1 <= q <= 200000`
- `1 <= r1 <= r2 <= n`, `1 <= c1 <= c2 <= m`
- `0 <= priority, timestamp <= 10^9`

## Clarifying Notes

- Claim ids are 1-based in input order.
- Area is `(r2 - r1 + 1) * (c2 - c1 + 1)`.

## Example Input

```
2 2 2
1 1 2 2 5 10
1 2 2 2 7 8
```

## Example Output

```
4
1
1 2
1 2
```
