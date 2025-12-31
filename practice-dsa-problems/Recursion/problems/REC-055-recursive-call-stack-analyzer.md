# REC-055: Recursive Call Stack Analyzer

## Problem Statement

You are given a call graph of functions. Each function has a frame size `f[i]`. Calls are either normal or tail calls. A tail call reuses the current frame size instead of pushing a new frame.

Starting from entry function `S`, compute the maximum stack usage possible along any call path.

## Input Format

- First line: integers `n`, `m`, and `S`
- Next `n` lines: `f[i]`
- Next `m` lines: `u v type` where `type` is `N` (normal) or `T` (tail)

## Output Format

- Single integer: maximum possible stack usage

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 300000`
- `0 <= f[i] <= 10^9`

## Clarifying Notes

- The call graph is a DAG.
- A tail call replaces the current frame size with the callee's frame size.

## Example Input

```
3 2 1
5
3
7
1 2 N
2 3 T
```

## Example Output

```
12
```
