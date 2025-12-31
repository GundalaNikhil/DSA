# STR-042: Suffix Automaton with Frequency

## Problem Statement

You are given a string `s` and must answer `q` queries about its substrings:

- `EXISTS p`: output `true` if `p` is a substring of `s`, otherwise `false`.
- `COUNT p`: output the number of occurrences of `p` in `s`.
- `KTH p k`: output the starting index (1-based) of the `k`-th occurrence of `p` in `s`, ordered by starting index. If `p` occurs fewer than `k` times, output `-1`.

## Input Format

- First line: string `s`
- Second line: integer `q`
- Next `q` lines: one query as described

## Output Format

- For each query, output the required answer on its own line

## Constraints

- `1 <= |s| <= 200000`
- `1 <= q <= 200000`
- `1 <= |p| <= 200000`
- Total length of all patterns <= 200000
- `s` and `p` contain only lowercase English letters

## Clarifying Notes

- Occurrences can overlap.
- The intended solution uses a suffix automaton augmented with occurrence counts and position tracking.

## Example Input

```
abracadabra
3
EXISTS abra
COUNT abra
KTH abra 2
```

## Example Output

```
true
2
8
```
