# LNK-059: Linked List with Self-Healing

## Problem Statement

Each node stores `value` and a checksum `cs = value XOR prev_value XOR next_value` (where missing neighbors are treated as 0). Some checksums are corrupted.

Repair the list by recomputing any node whose checksum does not match, setting its `value` to the **majority** of its neighbors' values (tie -> smaller value). After one full pass, output the repaired list.

## Input Format

- First line: integer `n`
- Second line: `n` integers: values
- Third line: `n` integers: checksums

## Output Format

- One line: repaired values

## Constraints

- `1 <= n <= 200000`
- Values are 32-bit signed integers

## Clarifying Notes

- Use original neighbor values from the start of the pass.
- For endpoints, missing neighbor value is 0.

## Example Input

```
3
5 7 5
2 0 2
```

## Example Output

```
5 5 5
```
