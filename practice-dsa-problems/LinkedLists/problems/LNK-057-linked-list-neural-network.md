# LNK-057: Linked List as Neural Network

## Problem Statement

A linked list represents a 1D neural network. Each node has a weight `w` and bias `b`. Given an input `x`, the forward value at node `i` is:

```
val_i = max(0, val_{i-1} * w_i + b_i)
```

with `val_0 = x`. You are given a target `y`. Compute the output `val_n` and the squared error `(val_n - y)^2`.

## Input Format

- First line: integer `n`
- Second line: `n` integers: weights `w_i`
- Third line: `n` integers: biases `b_i`
- Fourth line: integers `x` and `y`

## Output Format

- Two integers: `val_n` and squared error

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= w_i, b_i, x, y <= 10^9`

## Clarifying Notes

- ReLU is used: `max(0, z)`.

## Example Input

```
2
2 1
-1 0
3 5
```

## Example Output

```
5
0
```
