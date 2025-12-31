# ARR-021: Range Update with Saturation

## Problem Statement

You are given an array `a1..an`, a saturation cap `C`, and `q` range increment operations. Each operation is:

```
L R delta
```

which adds `delta` to all elements in indices `[L, R]` (1-based). After all operations, each element is capped at `C`:

```
final_i = min(C, a_i + total_increment_i)
```

Output the final array.

## Input Format

- First line: integers `n`, `q`, and `C`
- Second line: `n` integers `a1 a2 ... an`
- Next `q` lines: integers `L R delta`

## Output Format

- `n` integers: the final array values

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a_i, delta <= 10^9`
- `-10^9 <= C <= 10^9`
- `1 <= L <= R <= n`

## Clarifying Notes

- Saturation is applied only after all updates are combined.
- `C` can be less than initial values.

## Example Input

```
3 2 5
1 4 2
1 2 3
2 3 2
```

## Example Output

```
4 5 4
```
