# STR-013: Word Family Clustering with Overflow

## Problem Statement

You are given `n` words. Words belong to the same family if they are anagrams (same multiset of characters). For each family, keep words in their original input order and split them into groups of size `K`. If a family has leftover words fewer than `K`, concatenate those leftovers (in order) into a single word to form the final group.

Output all groups in the order of the families' first appearance in the input.

## Input Format

- First line: integers `n` and `K`
- Next `n` lines: one word per line

## Output Format

- First line: integer `g`, number of groups
- Next `g` lines: one group per line with its words separated by spaces

## Constraints

- `1 <= n <= 200000`
- `1 <= K <= n`
- Total length of all words <= 200000
- Words contain only lowercase English letters

## Clarifying Notes

- The leftover concatenation is done without separators.
- Groups within a family are output in input order.

## Example Input

```
6 2
eat
tea
tan
ate
nat
bat
```

## Example Output

```
4
eat tea
ate
tan nat
bat
```
