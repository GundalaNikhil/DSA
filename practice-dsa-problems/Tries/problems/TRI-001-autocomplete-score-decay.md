# TRI-001: Autocomplete System with Score Decay

## Problem Statement

Build an autocomplete system that supports insertions and prefix queries. Each word has an integer score that changes over time.

You are given a decay percentage `D` (0 to 100). After every query, any word that is **not** returned as a suggestion has its score decayed as:

```
score = floor(score * (100 - D) / 100)
```

A query returns up to 5 suggestions that start with the given prefix, ordered by:

1. Higher current score
2. Lexicographically smaller word

Words returned in the suggestion list do not decay for that query. Words not returned (including words that do not match the prefix) do decay.

## Input Format

- First line: integers `n` and `D`
- Next `n` lines: `word score`
- Next line: integer `q`
- Next `q` lines: one of the following
  - `I word score` (insert or overwrite the score for `word`)
  - `Q prefix` (query)

## Output Format

- For each `Q` operation, output a line with up to 5 words separated by spaces
- If there are no matching words, output an empty line

## Constraints

- `1 <= n, q <= 200000`
- `1 <= word length <= 50`
- Words contain only lowercase English letters
- `0 <= D <= 100`
- `0 <= score <= 10^9`

## Clarifying Notes

- An insert with an existing word overwrites its current score.
- Decay is applied **after** producing the suggestions for a query.
- The trie must support prefix search; the decay mechanism is deterministic and global.

## Example Input

```
3 10
car 100
cat 80
dog 90
3
Q ca
Q d
Q ca
```

## Example Output

```
car cat
dog
car cat
```
