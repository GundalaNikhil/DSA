---
problem_id: LNK_LINKED_LIST_NEURAL_NETWORK__9456
display_id: NTB-LNK-9456
slug: linked-list-neural-network
title: "Linked List as Neural Network"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-neural-network
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List as Neural Network

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

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long[] computeNeuralOutput(int n, long[] weights, long[] biases, long x, long y) {
        // Your code here
        return new long[2];
    }
}
```

```python
class Solution:
    def computeNeuralOutput(self, n: int, weights: list[int], biases: list[int], x: int, y: int) -> list[int]:
        # Your code here
        return [0, 0]
```

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> computeNeuralOutput(int n, vector<long long>& weights, vector<long long>& biases, long long x, long long y) {
        // Your code here
        return {0, 0};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number[]} weights
   * @param {number[]} biases
   * @param {number} x
   * @param {number} y
   * @returns {number[]}
   */
  computeNeuralOutput(n, weights, biases, x, y) {
    // Your code here
    return [0, 0];
  }
}
```
