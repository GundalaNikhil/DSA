# STR-007: Bounded Run Encoding

## Problem Statement

Compress a string by encoding each maximal run of identical characters as `<char><count>`, but split runs into chunks of at most 9. For example, a run of length 12 becomes `a9a3`.

## Input Format

- Single line: string `s`

## Output Format

- The encoded string

## Constraints

- `1 <= |s| <= 200000`
- `s` contains printable ASCII characters

## Clarifying Notes

- Every run is encoded with an explicit count, even when the count is 1.

## Example Input

```
aaaaaaaaaaaabbb
```

## Example Output

```
a9a3b3
```
