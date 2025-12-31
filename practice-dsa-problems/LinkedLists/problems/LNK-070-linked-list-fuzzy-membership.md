# LNK-070: Linked List with Fuzzy Membership

## Problem Statement

Each node belongs to the list with probability `p_i/1000`. The **confidence score** of a prefix of length `k` is the expected number of present nodes in that prefix.

For each query `k`, output the confidence score multiplied by 1000.

## Input Format

- First line: integer `n`
- Second line: `n` integers: `p_i` (0..1000)
- Third line: integer `q`
- Next `q` lines: `k`

## Output Format

- For each query, output the expected count * 1000

## Constraints

- `1 <= n, q <= 200000`
- `0 <= p_i <= 1000`

## Clarifying Notes

- Expectation is deterministic and additive.

## Example Input

```
3
500 1000 0
2
1
3
```

## Example Output

```
500
1500
```
