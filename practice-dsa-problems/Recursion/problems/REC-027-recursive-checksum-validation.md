# REC-027: Recursive Checksum Validation

## Problem Statement

You are given a rooted tree. Each node has a value `v` and a coefficient `coef`. Define a checksum recursively:

- For a leaf: `chk = (v * coef) mod M`
- For an internal node: `chk = (v * coef + sum(child chk)) mod M`

You are given a target checksum `T`. Determine if the root checksum equals `T`.

## Input Format

- First line: integers `n`, `M`, `T`
- Next `n` lines: `v coef parent` (parent is 0 for root)

## Output Format

- Print `YES` if the root checksum equals `T`, otherwise `NO`.

## Constraints

- `1 <= n <= 200000`
- `2 <= M <= 10^9 + 7`
- `0 <= T < M`
- `-10^9 <= v <= 10^9`
- `-10^9 <= coef <= 10^9`

## Clarifying Notes

- Use modular arithmetic for every addition and multiplication.
- Negative values are allowed; apply modulo normalization.

## Example Input

```
3 100 42
5 3 0
2 7 1
1 11 1
```

## Example Output

```
YES
```
