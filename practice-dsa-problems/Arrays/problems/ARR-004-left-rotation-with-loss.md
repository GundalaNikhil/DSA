# ARR-004: Left Rotation with Loss

## Problem Statement

Given an array `a1..an` and an integer `K`, rotate the array left by `K` positions. Elements that wrap from the front to the back lose 1 value each, but do not go below 0.

Formally, let `K = K mod n`. After left rotation, any element originally in positions `1..K` is decreased by 1 with floor at 0.

## Input Format

- First line: integers `n` and `K`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n` integers: the rotated array after loss adjustment

## Constraints

- `1 <= n <= 200000`
- `0 <= K <= 10^9`
- `0 <= a_i <= 10^9`

## Clarifying Notes

- If `K = 0`, the array is unchanged.
- Loss is applied after rotation to the elements that wrapped from the front.

## Example Input

```
5 2
3 0 2 5 1
```

## Example Output

```
2 5 1 2 0
```
