# STR-038: Adversarial String Game

## Problem Statement

Two players play a game on a string `s`. On each turn, a player chooses a contiguous substring of identical characters with length between `L` and `R` (inclusive) and removes it. The remaining parts concatenate to form the new string. The player who cannot move loses.

Determine the winner assuming optimal play. Output `FIRST` if the first player wins, otherwise output `SECOND`.

## Input Format

- First line: string `s`
- Second line: integers `L` and `R`

## Output Format

- `FIRST` or `SECOND`

## Constraints

- `1 <= |s| <= 200000`
- `1 <= L <= R <= |s|`
- `s` contains only lowercase English letters

## Clarifying Notes

- Only substrings of identical characters are legal moves.

## Example Input

```
aaaab
2 3
```

## Example Output

```
FIRST
```
