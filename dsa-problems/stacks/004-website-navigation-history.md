# Website Navigation History

**Problem ID:** STK-004
**Display ID:** 21
**Question Name:** Website Navigation History
**Slug:** website-navigation-history
**Title:** Min Stack Implementation
**Difficulty:** Medium
**Premium:** No
**Tags:** Stack, Design, Data Structure

## Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time O(1).

Implement the MinStack class:
- `MinStack()` initializes the stack object
- `void push(int val)` pushes the element val onto the stack
- `void pop()` removes the element on top of the stack
- `int top()` gets the top element of the stack
- `int getMin()` retrieves the minimum element in the stack

All operations must run in O(1) time complexity.

## A Simple Scenario (Daily Life Usage)

You're building a shopping app like Amazon. As users browse products, you need to track which item they viewed and also keep track of the cheapest item they've seen so far - all in real-time. When they use the back button (pop), you still need to instantly know what the current cheapest item is. The getMin() operation helps recommend "You've seen cheaper options!" messages.

## Your Task

Design and implement a stack with an additional method to get the minimum value in constant time.

## Why is it Important?

This problem teaches you:

- Advanced stack design patterns
- Space-time tradeoff decisions
- Maintaining auxiliary information efficiently
- System design for real-time applications

## Examples

### Example 1:

**Input:**
```
["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[[], [-2], [0], [-3], [], [], [], []]
```

**Output:**
```
[null, null, null, null, -3, null, 0, -2]
```

**Explanation:**
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

### Example 2:

**Input:**
```
["MinStack", "push", "push", "getMin", "getMin", "push", "getMin"]
[[], [5], [3], [], [], [1], []]
```

**Output:**
```
[null, null, null, 3, 3, 1]
```

**Explanation:**
```
MinStack minStack = new MinStack();
minStack.push(5);    // stack: [5]
minStack.push(3);    // stack: [5, 3]
minStack.getMin();   // return 3
minStack.getMin();   // return 3 (calling multiple times)
minStack.push(1);    // stack: [5, 3, 1]
minStack.getMin();   // return 1
```

## Constraints

- -2^31 ≤ val ≤ 2^31 - 1
- Methods pop, top, and getMin will always be called on non-empty stacks
- At most 30,000 calls will be made to push, pop, top, and getMin

## Asked by Companies

- Amazon
- Microsoft
- Bloomberg
- Adobe
