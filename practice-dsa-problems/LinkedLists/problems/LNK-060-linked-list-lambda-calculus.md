# LNK-060: Linked List as Lambda Calculus

## Problem Statement

A lambda term is encoded as a list of tokens using:

- `Lx` for lambda `\x`
- `.` for separator
- variable names as single lowercase letters
- `(` and `)` for grouping

You must perform **exactly** `K` beta-reduction steps or stop earlier if no redex remains. Output the resulting token list.

Beta-reduction rule:

```
( Lx . body ) arg  => body with free x replaced by arg
```

## Input Format

- First line: integer `K`
- Second line: list of tokens separated by spaces

## Output Format

- One line: resulting tokens separated by spaces

## Constraints

- Number of tokens <= 200
- `0 <= K <= 100`

## Clarifying Notes

- Always reduce the leftmost-outermost redex.
- Variables are single lowercase letters.

## Example Input

```
1
( Lx . x ) y
```

## Example Output

```
y
```
