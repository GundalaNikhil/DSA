# LNK-062: Git-Like Linked List

## Problem Statement

You manage branches of a linked list. Version `0` is the initial list on branch `main`.

Operations:

- `BRANCH name from_version`
- `COMMIT name pos x`: insert value `x` at position `pos` on the branch, creating a new version
- `MERGE target source base_version`: three-way merge using base version; conflicts resolved by choosing smaller value
- `GET version pos`: output value at `pos`

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list
- Third line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output one integer
- For each `MERGE`, output conflict count

## Constraints

- `1 <= n, q <= 200000`

## Clarifying Notes

- Versions are global and increment with each `COMMIT` or `MERGE`.

## Example Input

```
2
1 2
4
BRANCH dev 0
COMMIT dev 2 9
MERGE main dev 0
GET 3 2
```

## Example Output

```
1
9
```
