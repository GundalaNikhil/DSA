# ARR-025: Duplicate Distance Minimization

## Problem Statement

You are given an array `a1..an`. You may remove **at most one** element from the array. After the removal, if a value appears at least twice, its distance is the absolute difference between the two indices of a chosen equal pair. Define the array's duplicate distance as the minimum distance among all equal pairs in the remaining array.

Your task is to minimize this duplicate distance by removing at most one element. If the array has no duplicates even after a removal, output `-1`.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: minimum possible duplicate distance, or `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- If no removal yields any duplicate pair, the answer is `-1`.
- Removal shifts indices after the removed position.

## Example Input

```
5
1 2 1 3 1
```

## Example Output

```
1
```
