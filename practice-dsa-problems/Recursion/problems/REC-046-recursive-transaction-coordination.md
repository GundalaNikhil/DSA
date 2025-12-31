# REC-046: Recursive Transaction Coordination

## Problem Statement

You are given a rooted tree. Each node is a transaction with a tentative delta `d` applied to a global balance and a local allowed balance range `[L, R]`.

A transaction commits if, after including all committed children and its own delta, the balance is within `[L, R]`. If a transaction aborts, none of its subtree deltas apply.

Assume the global balance starts at `0`. Compute the final balance after evaluating the root transaction.

## Input Format

- First line: integer `n`
- Next `n` lines: `d L R parent` (parent is 0 for root)

## Output Format

- Single integer: final balance after the root transaction is evaluated

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= d <= 10^9`
- `-10^15 <= L <= R <= 10^15`

## Clarifying Notes

- Children are evaluated before their parent commits or aborts.
- If the root aborts, the final balance is `0`.

## Example Input

```
3
5 -10 10 0
4 0 20 1
-8 -5 5 1
```

## Example Output

```
1
```
