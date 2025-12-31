# REC-021: Self-Modifying Recursion

## Problem Statement

You are given a set of symbols. Each symbol has two possible expansion lists and a toggle flag. A recursive evaluation starts from symbol `S` with mode `0` and depth `D`.

Define `Eval(symbol, depth, mode)` as follows:

- If `depth == 0` or the chosen expansion list is empty, return `weight[symbol]`.
- Otherwise choose the expansion list based on `mode` (`list0` if mode=0, `list1` if mode=1).
- Let `next_mode = mode XOR toggle[symbol]`.
- Return the sum of `Eval(child, depth-1, next_mode)` over all children in the chosen list.

Compute `Eval(S, D, 0)` modulo `1,000,000,007`.

## Input Format

- First line: integers `n` and `D`
- Second line: integer `S` (start symbol, 1-indexed)
- Next `n` lines: `weight toggle c0 list0... c1 list1...`
  - `weight`: integer value for this symbol
  - `toggle`: `0` or `1`
  - `c0`: number of children in `list0`, followed by `c0` integers
  - `c1`: number of children in `list1`, followed by `c1` integers

## Output Format

- Single integer: value of `Eval(S, D, 0)` modulo `1,000,000,007`

## Constraints

- `1 <= n <= 200000`
- `0 <= D <= 60`
- `1 <= S <= n`
- `0 <= weight <= 10^9`
- `0 <= c0, c1 <= 3`
- Children are in the range `[1, n]`

## Clarifying Notes

- The mode changes for the entire subtree of a symbol, not just a single child.
- The chosen expansion list is determined before the mode is toggled.
- The recursion is self-modifying because the rule selection depends on prior toggles along the path.

## Example Input

```
3 2
1
5 1 2 2 3 1 2
2 0 0 1 3
4 1 0 0
```

## Example Output

```
10
```
